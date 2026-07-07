import os
import wave
from pathlib import Path

import webrtcvad
from pydub import AudioSegment


FRAME_MS = 30
VAD_MODE = 3
PADDING_MS = 400
MIN_VOICE_MS = 1500
TEMP_FILE = "temp.wav"
OUTPUT_ROOT = Path("processed_audio")


def convert_audio(input_file, temp_file):
    audio = AudioSegment.from_file(input_file)

    audio = audio.high_pass_filter(180)
    audio = audio.set_channels(1)
    audio = audio.set_frame_rate(16000)
    audio = audio.set_sample_width(2)

    audio.export(
        temp_file,
        format="wav",
        parameters=["-af", "afftdn"],
    )


def read_wave(path):
    with wave.open(path, "rb") as wf:
        sample_rate = wf.getframerate()
        pcm_data = wf.readframes(wf.getnframes())

    return pcm_data, sample_rate


def detect_voice(pcm_data, sample_rate):
    vad = webrtcvad.Vad(VAD_MODE)
    frame_size = int(sample_rate * FRAME_MS / 1000) * 2

    segments = []
    triggered = False
    start_time = 0
    silence = 0

    total_frames = len(pcm_data) // frame_size

    for i in range(total_frames):
        frame = pcm_data[i * frame_size:(i + 1) * frame_size]

        if len(frame) < frame_size:
            continue

        is_speech = vad.is_speech(frame, sample_rate)
        current_ms = i * FRAME_MS

        if is_speech:
            if not triggered:
                start_time = max(0, current_ms - PADDING_MS)
                triggered = True

            silence = 0
        elif triggered:
            silence += FRAME_MS

            if silence >= PADDING_MS:
                end_time = current_ms

                if end_time - start_time > MIN_VOICE_MS:
                    segments.append((start_time, end_time))

                triggered = False
                silence = 0

    return segments


def merge_close_segments(segments, max_gap_ms=2000):
    if not segments:
        return []

    merged = [segments[0]]

    for start, end in segments[1:]:
        last_start, last_end = merged[-1]

        if start - last_end <= max_gap_ms:
            merged[-1] = (last_start, end)
        else:
            merged.append((start, end))

    return merged


def save_segments(input_file, segments):
    audio = AudioSegment.from_file(input_file)
    base_name = Path(input_file).stem

    output_folder = OUTPUT_ROOT / base_name
    output_folder.mkdir(parents=True, exist_ok=True)

    segments_folder = output_folder / "segments"
    segments_folder.mkdir(exist_ok=True)

    result = AudioSegment.silent(duration=0)

    for idx, (start, end) in enumerate(segments):
        piece = audio[start:end]

        piece.export(
            segments_folder / f"part_{idx + 1:03d}.wav",
            format="wav",
        )

        result += piece
        result += AudioSegment.silent(duration=300)

    result.export(
        output_folder / f"{base_name}_voice_only.wav",
        format="wav",
    )

    result.export(
        output_folder / f"{base_name}_voice_only.mp3",
        format="mp3",
        bitrate="64k",
    )


def process_file(input_file):
    base_name = Path(input_file).stem
    output_folder = OUTPUT_ROOT / base_name
    output_mp3 = output_folder / f"{base_name}_voice_only.mp3"

    if output_mp3.exists():
        print(f"Skipping: {input_file} has already been processed")
        return

    print(f"\nProcessing: {input_file}")

    convert_audio(input_file, TEMP_FILE)

    pcm_data, sample_rate = read_wave(TEMP_FILE)
    segments = detect_voice(pcm_data, sample_rate)
    segments = merge_close_segments(
        segments,
        max_gap_ms=3000,
    )

    print(f"Detected segments: {len(segments)}")

    save_segments(input_file, segments)

    if os.path.exists(TEMP_FILE):
        os.remove(TEMP_FILE)

    print("Done")


def main():
    wav_files = sorted([
        f for f in Path(".").glob("*.WAV")
        if f.is_file()
    ])

    if not wav_files:
        print("No WAV files found")
        return

    print(f"Found files: {len(wav_files)}")

    for wav_file in wav_files:
        process_file(str(wav_file))

    print("\nAll files have been processed!")


if __name__ == "__main__":
    main()
