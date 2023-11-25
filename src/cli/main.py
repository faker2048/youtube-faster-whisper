import os
import time
from threading import Thread

import click
import yt_dlp
from loguru import logger

from src.whisper.subtitles import write_srt
from src.whisper.transcribe import initialize_whisper_model
from src.youtube.download import download, download_audio


@click.group()
def main():
    """Main command group for handling YouTube video downloading and transcription."""
    pass


@main.command()
@click.option("--url", "-u", required=True, help="Youtube URL.")
@click.option("--threads", "-n", default=16, help="Number of threads to use.")
@click.option(
    "--format",
    "-f",
    default="bestvideo+bestaudio/best",
    help="Download format. See: https://github.com/yt-dlp/yt-dlp#format-selection-examples",
)
@click.option(
    "--translate",
    "-t",
    is_flag=True,
    default=False,
    help="Translate the subtitles to English.",
)
@click.option(
    "--model_name",
    "-m",
    default="tiny.en",
    help="Name of the model to use. e.g.  (tiny, tiny.en, base, base.en, small, small.en,\
          medium, medium.en, large-v1, or large-v2 or large-v3), recommended: (large-v3)",
)
@click.option(
    "--model_root",
    "-r",
    default=None,
    help="Root directory for the models.",
)
@click.option(
    "--cpu",
    is_flag=True,
    default=False,
    help="Use CPU instead of GPU. This is useful if you do not have a GPU.",
)
@click.option(
    "--srt_only",
    "-s",
    is_flag=True,
    default=False,
    help="Only generate subtitles. Do not download video.",
)
@click.option(
    "--video_only",
    "-v",
    is_flag=True,
    default=False,
    help="Only download video. Do not generate subtitles.",
)
def dt(
    url: str,
    threads: int,
    format: str,
    translate: bool,
    model_name: str,
    model_root: str | None,
    cpu: bool,
    srt_only: bool,
    video_only: bool,
) -> None:
    """Download video/audio from Youtube and generate subtitles."""

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
        # download_thread should exit when main thread exits
        # (i.e. when the user presses Ctrl+C)
        download_thread.daemon = True 
        download_thread.start()
    else:
        logger.info("Skipping video download due to --srt_only flag.")

    # Transcribe audio
    logger.info(f"Downloading video from {url}.")

    if not video_only:
        audio_file_name = download_audio(url, threads)
        srt_file_name = audio_file_name + ".srt"
        if not os.path.exists(srt_file_name):
            logger.info(f"Transcribing audio from {audio_file_name}.")
            model = initialize_whisper_model(
                model_name=model_name, model_root=model_root, cpu=cpu
            )
            logger.info("Model initialized successfully.")

            begin_transcription = time.time()
            segs, info = model.transcribe(
                audio=audio_file_name,
                vad_filter=True,
                task="transcribe" if not translate else "translate",
            )
            write_srt(segments=segs, file=srt_file_name)
            logger.info(
                f"Transcription completed in {time.time() - begin_transcription:.2f} \
                    seconds. Audio duration: {info.duration:.2f} seconds."
            )

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


@main.command()
@click.option(
    "--url",
    "-u",
    required=True,
    help="The URL of the YouTube video or the filename to be downloaded.",
)
@click.option(
    "--threads",
    "-n",
    default=16,
    help="The number of threads to use for downloading. Default is 16.",
)
@click.option(
    "--format",
    "-f",
    default="bestvideo+bestaudio/best",
    help=(
        "The download format. Options include: "
        "'worstaudio[tbr>100]/bestaudio/best' for audio only, "
        "'bestvideo[height>=1080]/bestvideo' for video only, "
        "'bestvideo+bestaudio/best' for both video and audio (default). "
        "Use 'best' for the best quality or specify particular formats."
    ),
)
def d(url: str, threads: int, format: str):
    """Download a video/audio from YouTube."""
    file_name: str = download(url, threads, format)
    click.echo(file_name)


@main.command()
@click.option(
    "--file",
    "-f",
    required=True,
    help="The media file to be transcribed.",
)
@click.option(
    "--translate",
    "-t",
    is_flag=True,
    default=False,
    help="Translate the subtitles to English.",
)
@click.option(
    "--model_name",
    "-m",
    default="tiny.en",
    help="Name of the model to use. e.g.  (tiny, tiny.en, base, base.en, small, small.en,\
          medium, medium.en, large-v1, or large-v2 or large-v3), recommended: (large-v3)",
)
@click.option(
    "--model_root",
    "-r",
    default=None,
    help="Root directory for the models.",
)
@click.option(
    "--cpu",
    is_flag=True,
    default=False,
    help="Use CPU instead of GPU. This is useful if you do not have a GPU.",
)
def t(file: str, translate: bool, model_name: str, model_root: str | None, cpu: bool):
    """Transcribe a video/audio file."""
    if os.path.isfile(file):
        logger.info(f"Transcribing file from {file}.")
        model = initialize_whisper_model(
            model_name=model_name, model_root=model_root, cpu=cpu
        )
        logger.info("Model initialized successfully.")

        begin_transcription = time.time()
        segs, info = model.transcribe(
            audio=file,
            vad_filter=True,
            task="transcribe" if not translate else "translate",
        )
        write_srt(segments=segs, file=file + ".srt")
        logger.info(
            f"Transcription completed in {time.time() - begin_transcription:.2f} \
                seconds. Audio duration: {info.duration:.2f} seconds."
        )


if __name__ == "__main__":
    main()
