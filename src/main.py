from view.CrisperWhisperInterface import CrisperWhisperInterface
from view.WhisperInterface import WhisperInterface
from controller.Controller import Controller
import logging.config


def main() -> None:  
    logging.config.fileConfig("config/logging.conf")
    controller = Controller()
    WhisperInterface(controller.generate_outputs_whisper).blocks.launch(debug=True)
    # CrisperWhisperInterface(controller.generate_outputs_crisper_whisper).blocks.launch(debug=True)

if __name__ == "__main__":
    main()