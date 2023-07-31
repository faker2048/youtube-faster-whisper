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
pip install git+https://github.com/faker2048/youtube-whisper.git
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
❯ ytws --help
Usage: ytws [OPTIONS]

  Download video from Youtube and generate subtitles.

Options:
  -u, --url TEXT         Youtube URL.  [required]
  -n, --threads INTEGER  Number of threads to use.
  -f, --format TEXT      Download format. See: https://github.com/yt-dlp/yt-
                         dlp#format-selection-examples
  -t, --translate        Translate the subtitles to English.
  -m, --model_name TEXT  Name of the model to use. e.g.  (tiny, tiny.en, base,
                         base.en, small, small.en,          medium, medium.en,
                         large-v1, or large-v2), recommended: (large-v2)
  -r, --model_root TEXT  Root directory for the models.
  --cpu                  Use CPU instead of GPU. This is useful if you do not
                         have a GPU.
  -s, --srt_only         Only generate subtitles. Do not download video.
  -v, --video_only       Only download video. Do not generate subtitles.
  --help                 Show this message and exit.
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
