from setuptools import setup, find_packages

with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()

setup(
    name="ytws",
    version="0.4.2",
    description="YouTube Whisper - A YouTube Downloader with Transcription",
    long_description=long_description,
    long_description_content_type="text/markdown",
    author="faker2048",
    author_email="nspyia2002@gmail.com",
    url="https://github.com/faker2048/youtube-whisper",
    packages=find_packages(include=["src", "src.*"]),
    install_requires=[
        "click==8.1.6",
        "faster_whisper==0.10.0",
        "loguru==0.7.0",
        "yt_dlp==2023.10.13",
    ],
    entry_points="""
        [console_scripts]
        ytws=src.cli.main:main
    """,
    classifiers=[
        "Development Status :: 3 - Alpha",
        "Intended Audience :: Developers",
        "License :: OSI Approved :: MIT License",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.10",
    ],
)
