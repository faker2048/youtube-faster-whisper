from faster_whisper import WhisperModel


def main():
    model = WhisperModel("large-v2", device="cuda", compute_type="float16")
    segments, info = model.transcribe("data/jfk.flac", "en", beam_size=5)

    for segment in segments:
        print("[%.2fs -> %.2fs] %s" % (segment.start, segment.end, segment.text))


if __name__ == "__main__":
    main()
