# 🎥 YTWS: YouTube Download and Faster-Whisper Subtitle Generation Tool 🔥

YTWS is a command-line tool that allows you to download videos from YouTube and generate subtitles, all powered by the efficient `faster-whisper`.

## ⭐ Features

- **Easy to Use**: Start without any hassle.
- **Fast Subtitle Generation**: Harness the speed of `faster-whisper`.
- **GPU Acceleration**: A simple guide for harnessing GPU power.
- **Cross-Platform Compatibility**: Runs on Windows and Linux. (Mac OS compatibility is likely but not tested.)

These features make YTWS an efficient and user-friendly choice for downloading YouTube videos and generating subtitles.

## ⚙ Requirements

_Principle: Keep it simple, with no side effects._

#### ffmpeg
For Python virtual environment (recommended):
```bash
conda install ffmpeg
```
For Windows scoop users:
```bash
scoop install ffmpeg
```

## 💽 Installation

Install YTWS easily with these commands:

```bash
pip install ytws
```
or
```bash
git clone https://github.com/faker2048/youtube-whisper
cd youtube-whisper
pip install .
```

## 🚀 Usage

Start downloading YouTube videos and generating subtitles right away:

```bash
# To download videos and generate subtitles.
ytws -m large-v2 -u https://www.youtube.com/watch?v=nWvCd8lC4_Q 
```

```bash
# To generate .srt subtitles only (this downloads only audio, deleting it after transcription).
ytws -m large-v2 -u https://www.youtube.com/watch?v=nWvCd8lC4_Q --srt_only
```

```bash
# Runs on CPU.
ytws -u https://www.youtube.com/watch?v=nWvCd8lC4_Q --cpu
```

Replace the URL with the YouTube video you wish to download.

For more customization options, use the `--video_only` or `--srt_only` flags.

- Custom Settings  
For further details, consult the help section:

```bash
ytws --help
```

## 🛫 GPU Acceleration

For easy CUDA and cuDNN installation:
- Linux:
```bash
conda install cudnn
```

- Windows:

_Although using additional torch libraries may not be ideal, it's a straightforward approach for Windows (compared to Nvidia's official CUDA installation). Any alternative methods or suggestions are welcome!_
```bash
pip3 install torch --index-url https://download.pytorch.org/whl/cu118
```

After these settings, YTWS should work with a GPU.

## 🪄 Available Models

Visit [here](https://huggingface.co/guillaumekln) for more details.

## 🌟 Contributing to YTWS

We welcome contributions to YTWS! Your support makes a difference.

### How to Contribute
- **Fork, Clone, Branch**: Start by forking and cloning the repository, then work in separate branches.
- **Commit**: Follow the project standards and commit your changes.
- **Pull Request**: Submit a concise pull request (PR) to the main branch.

### Using Pre-Commit
To maintain code format:

```bash
pip install pre-commit
pre-commit install
```

Pre-commit will guide you through necessary checks and corrections. Feel free to reach out if you have any questions or suggestions!