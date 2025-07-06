import logging.config
import sys

from src.controller.Controller import Controller
from src.model.llm.LLMPeer import LLMPeer
from src.utils import Utils
from src.view.Interface import Interface
from src.view.WhisperInterface import WhisperInterface

logger = logging.getLogger(__name__)


def main() -> None:
    config = Utils.read_config()

    logging.config.fileConfig("config/logging.conf")

    model = config["model"]
    local = config["local"]

    controller = Controller(model, local, LLMPeer())

    if model == "CrisperWhisper":
        Interface(controller.generate_outputs_crisper_whisper).blocks.launch(debug=True)
    elif model == "Whisper":
        WhisperInterface(controller.generate_outputs_whisper).blocks.launch(debug=True)
    else:
        logger.error("Model '{model}' is not currently supported")
        sys.exit(1)


if __name__ == "__main__":
    main()
