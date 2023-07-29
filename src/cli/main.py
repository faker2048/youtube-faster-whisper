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
@click.option(
    "--srt_only",
    "-s",
    default=False,
    help="Only generate subtitles. Do not download video.",
)
@click.option(
    "--video_only",
    "-v",
    default=False,
    help="Only download video. Do not generate subtitles.",
)
def full(
    url: str,
    threads: int,
    format: str,
    model_name: str,
    model_root: str | None,
    srt_only: bool,
    video_only: bool,
) -> None:
    """Download video from Youtube and generate subtitles."""

    # Check if URL is valid
    try:
        yt_dlp.YoutubeDL().extract_info(
            url, download=False
        )  # This will throw exception if URL is not valid.
    except Exception:
        click.echo("Invalid URL. Please provide a valid YouTube URL.")
        return

    # Download video in parallel
    download_thread = None
    if not srt_only:
        # Download video in parallel
        download_thread = Thread(target=download, args=(url, threads, format))
        download_thread.start()
    else:
        logger.info("Skipping video download due to --srt_only flag.")

    # Transcribe audio
    logger.info(f"Downloading video from {url}.")

    if not video_only:
        audio_file_name = download_audio(url, threads)
        srt_file_name = audio_file_name.split(".")[0] + ".srt"
        if not os.path.exists(srt_file_name):
            logger.info(f"Transcribing audio from {audio_file_name}.")
            model = initialize_whisper_model(
                model_name=model_name, model_root=model_root
            )
            segs, info = model.transcribe(audio=audio_file_name, vad_filter=True)
            write_srt(segments=segs, file=srt_file_name)
            if os.path.exists(audio_file_name):
                os.remove(audio_file_name)
        else:
            logger.info(
                f"Skipping audio transcription due to {srt_file_name} already exists."
            )
    else:
        logger.info("Skipping audio transcription due to --video_only flag.")

    if download_thread is not None:
        download_thread.join()


if __name__ == "__main__":
    main()
