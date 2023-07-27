from faster_whisper import WhisperModel


class YoutubeWhisper:
    def __init__(self, model: str = "tiny.en") -> None:
        try:
            self.model = WhisperModel(model, device="cuda", compute_type="float16")
        except RuntimeError:
            self.model = WhisperModel(model, device="cpu")
