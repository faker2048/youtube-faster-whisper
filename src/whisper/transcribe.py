from loguru import logger
from faster_whisper import WhisperModel


def initialize_whisper_model(
    model_name: str = "tiny.en", model_root: str | None = None, cpu: bool = False
):
    logger.info(f"Initializing WhisperModel with model {model_name}.")
    device = "cpu" if cpu else "cuda"
    compute_type = "float32" if cpu else "float16"
    try:
        return WhisperModel(
            model_name,
            device=device,
            compute_type=compute_type,
            download_root=model_root,
        )
    except RuntimeError:
        if cpu:
            raise RuntimeError(
                "WhisperModel could not be initialized even with CPU device."
            )
        else:
            logger.info(
                "WhisperModel could not be initialized with CUDA device.\
                      Falling back to CPU device."
            )
            return WhisperModel(
                model_name,
                device="cpu",
                compute_type="float32",
                download_root=model_root,
            )
