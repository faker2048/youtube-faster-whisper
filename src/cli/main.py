from threading import Thread

import click
import yt_dlp
from loguru import logger
import os
from src.whisper.subtitles import write_srt
from src.whisper.transcribe import initialize_whisper_model
from src.youtube.download import download, download_audio


@click.group()
def main():
    pass


@main.command()
@click.option("--url", "-u", required=True, help="Youtube URL.")
@click.option(
    "--threads",
    "-n",
    default=8,
    help="Number of threads to use",
)
@click.option(
    "--format",
    "-f",
    default="bestvideo+bestaudio/best",
    help="Download format. See: https://github.com/yt-dlp/yt-dlp#format-selection-examples",
)
def video(url: str, threads: int, format: str) -> None:
    """Download video from Youtube."""
    download(url, threads, format)


@main.command()
@click.option("--url", "-u", required=True, help="Youtube URL.")
@click.option("--threads", "-n", default=8, help="Number of threads to use.")
def audio(url: str, threads: int) -> None:
    """Download video from Youtube."""
    download_audio(url, threads)


@main.command()
@click.option("--url", "-u", required=True, help="Youtube URL.")
@click.option("--threads", "-n", default=8, help="Number of threads to use.")
@click.option(
    "--format",
    "-f",
    default="bestvideo+bestaudio/best",
    help="Download format. See: https://github.com/yt-dlp/yt-dlp#format-selection-examples",
)
@click.option(
    "--model_name",
    "-m",
    default="tiny.en",
    help="Name of the model to use. e.g.  (tiny, tiny.en, base, base.en, small, small.en,\
          medium, medium.en, large-v1, or large-v2), recommended: (large-v2)",
)
@click.option(
    "--model_root",
    "-r",
    default=None,
    help="Root directory for the models.",
)
def full(
    url: str, threads: int, format: str, model_name: str, model_root: str | None
) -> None:
    """Download video from Youtube and generate subtitles."""
    try:
        yt_dlp.YoutubeDL().extract_info(
            url, download=False
        )  # This will throw exception if URL is not valid.
    except Exception:
        click.echo("Invalid URL. Please provide a valid YouTube URL.")
        return

    logger.info(f"Downloading video from {url}.")
    audio_file_name = download_audio(url, threads)
    srt_file_name = audio_file_name.split(".")[0] + ".srt"

    # Download video in parallel
    download_thread = Thread(target=download, args=(url, threads, format))
    download_thread.start()

    # Transcribe audio
    if not os.path.exists(srt_file_name):
        logger.info(f"Transcribing audio from {audio_file_name}.")
        model = initialize_whisper_model(model_name=model_name, model_root=model_root)
        segs, info = model.transcribe(audio=audio_file_name, vad_filter=True)
        write_srt(segments=segs, file=srt_file_name)
        if os.path.exists(audio_file_name):
            os.remove(audio_file_name)
    else:
        logger.info(f"File {srt_file_name} already exists. Skipping transcription.")

    download_thread.join()


if __name__ == "__main__":
    main()
