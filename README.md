# 🎥 YTWS: YouTube Download and Subtitle Generation Tool 🔥

YTWS is a command-line tool designed to download videos from YouTube and generate subtitles, all with the power of the efficient `faster-whisper`.

## 💽 Installation
You can easily install YTWS using the following commands:
```bash
git clone https://github.com/faker2048/youtube-whisper
cd youtube-whisper
pip install .
```

### Preparations Before Running

_Principle: Simplicity is key, and there should be no side effects._

#### ffmpeg
If you don't have ffmpeg installed, you can use the standard method to install ffmpeg in your computer's global environment (not detailed here), or you can use conda to install it in your Python virtual environment (recommended):
```
conda install ffmpeg
```
#### GPU Acceleration
Should you need to install the CUDA and cudnn suite, the following methods provide a simple solution:
- For Linux:
```
conda install cudnn
```
- For Windows:
```
pip3 install torch --index-url https://download.pytorch.org/whl/cu118

# While utilizing additional torch libraries may not be ideal, it's one of the most 
# straightforward approaches I've discovered for Windows (relative to Nvidia's official CUDA 
# installation). If you're aware of alternative methods or suggestions, your insight would be 
# graciously appreciated!
```

These steps aim to make the installation process as seamless as possible. Feel free to reach out if you have any questions or concerns!

## 🪄 Available Model

Visit https://huggingface.co/guillaumekln for more details.

## 🚀 Quick Start
You can begin downloading YouTube videos and generating subtitles right away. Here's a simple example of how to use YTWS:

```bash
# To download videos from YouTube and generate subtitles.
ytws -m large-v2 -u https://www.youtube.com/watch?v=nWvCd8lC4_Q 
```

```bash
# To generate .srt subtitles only. (This will download only the audio and delete it after transcribing)
ytws -m large-v2 -u https://www.youtube.com/watch?v=nWvCd8lC4_Q --srt_only
```

```bash
# Runs on cpu
ytws -u https://www.youtube.com/watch?v=nWvCd8lC4_Q --cpu
```

Please replace `https://www.youtube.com/watch?v=nWvCd8lC4_Q` with the URL of the YouTube video you wish to download.

For more customized options like downloading only the video or generating only the subtitles, you can use the `--video_only` or `--srt_only` options.

## 🎛️ Custom Settings
For further details and customization options, please refer to the help information:

```bash
ytws --help
```

## 🌟 Contributing to ytws

We welcome your support for ytws! Your contributions make a difference.

### How to Contribute
- **Fork, Clone, Branch**: Start by forking and cloning the repository, then work in separate branches.
- **Commit**: Follow the project's standards, and commit your changes.
- **Pull Request**: Submit a brief pull request (PR) to the main branch.

### Using Pre-Commit
To ensure code format:

```bash
pip install pre-commit
pre-commit install
```

Pre-commit will guide you through necessary checks and adjustments.
