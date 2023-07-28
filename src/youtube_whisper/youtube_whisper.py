from faster_whisper import WhisperModel
from loguru import logger


class WhisperWrapper:
    def __init__(self, model: str = "tiny.en") -> None:
        try:
            self.model = WhisperModel(model, device="cuda", compute_type="float16")
        except RuntimeError:
            logger.info(
                "WhisperModel could not be initialized with CUDA device. Falling back to CPU device."
            )
            self.model = WhisperModel(model, device="cpu")


class YoutubeWrapper:
    def __init__(self) -> None:
        pass
