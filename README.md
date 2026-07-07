# 🎙️ Audio Voice Extractor

> Python tool for automatic speech detection and voice extraction using WebRTC VAD, FFmpeg and pydub.

---

## 📖 Overview

Audio Voice Extractor automatically detects speech in long audio recordings, removes silence, extracts voice segments and generates clean MP3 and WAV files ready for AI transcription, archiving or further audio processing.

The project is designed as a preprocessing step for speech-to-text workflows using Faster-Whisper and similar transcription engines.

---

![Python](https://img.shields.io/badge/Python-3.10+-3776AB?style=for-the-badge&logo=python&logoColor=white)
![WebRTC VAD](https://img.shields.io/badge/WebRTC-VAD-success?style=for-the-badge)
![FFmpeg](https://img.shields.io/badge/FFmpeg-007808?style=for-the-badge&logo=ffmpeg&logoColor=white)
![Status](https://img.shields.io/badge/Status-Stable-success?style=for-the-badge)
![License](https://img.shields.io/badge/License-MIT-green?style=for-the-badge)
---

## ✨ Features

- 🎤 Speech detection using WebRTC VAD
- ✂ Automatic silence removal
- 🔊 Audio denoising (FFmpeg afftdn)
- 📂 Batch processing of WAV files
- 📦 Separate speech segments export
- 🎵 Clean MP3 generation
- 🎧 Clean WAV generation
- ⚡ Optimized for Faster-Whisper preprocessing
- 🤖 Ready for Faster-Whisper transcription workflows

---
## 🔄 Workflow

```text
Long WAV Recordings
        │
        ▼
Noise Reduction
        │
        ▼
Voice Activity Detection
        │
        ▼
Merge Speech Segments
        │
        ▼
Export Individual Segments
        │
        ▼
voice_only.wav
voice_only.mp3
```

---

## 🛠 Technologies

![Python](https://img.shields.io/badge/Python-3776AB?style=for-the-badge&logo=python&logoColor=white)
![WebRTC VAD](https://img.shields.io/badge/WebRTC-VAD-success?style=for-the-badge)
![FFmpeg](https://img.shields.io/badge/FFmpeg-007808?style=for-the-badge&logo=ffmpeg&logoColor=white)
![pydub](https://img.shields.io/badge/pydub-Audio-orange?style=for-the-badge)
![Batch Processing](https://img.shields.io/badge/Batch%20Processing-Enabled-blue?style=for-the-badge)
![AI Ready](https://img.shields.io/badge/AI-Ready-purple?style=for-the-badge)

---

## 📁 Folder Structure

```text
processed_audio/
│
├── meeting_001/
│   ├── segments/
│   │   ├── part_001.wav
│   │   ├── part_002.wav
│   │   └── ...
│   ├── meeting_001_voice_only.wav
│   └── meeting_001_voice_only.mp3
│
└── meeting_002/
```
---

## ▶ Installation

Install Python dependencies:

```bash
pip install -r requirements.txt
```

Install FFmpeg and make sure it is available in your system PATH.

Then run:

```bash
python voice_vad_ready.py
```

---

## ▶ Usage

Place your WAV recordings into the project folder.

Run:

```bash
python voice_vad_ready.py
```

Processed files will be generated inside:

```text
processed_audio/
```

---

## 💡 Why this project?

Long audio recordings often contain hours of silence.

Instead of forcing AI transcription models to process everything,
this tool removes non-speech parts first.

The result is faster transcription,
lower processing cost,
and cleaner output.

---

## Future roadmap

- [ ] GUI
- [ ] Multithreading
- [ ] Speaker separation
- [ ] Spectrogram visualization
- [ ] Command-line arguments
- [ ] Docker support

---

## 📸 Screenshots

### Processing audio recordings

![terminal screenshot](Screenshots/screenshot%202026-07-07%20113752.png)

### Generated output

![processed_audio folder](Screenshots/screenshot%202026-07-07%20093331.png)

### Voice segments

![segments folder](Screenshots/screenshot%202026-07-07%20114004.png)

---

## 🚀 Release

**v1.0.0 — Initial Public Release**

Released: **07 July 2026**

---

## 📜 License

This project is licensed under the MIT License.

---

## 👤 Author

**Denys Ostroushko**

GitHub:
https://github.com/DorianGray-web

---

⭐ If you find this project useful, consider giving it a star!