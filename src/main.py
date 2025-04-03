import sys
from view.CrisperWhisperInterface import CrisperWhisperInterface
from view.WhisperInterface import WhisperInterface
from controller.Controller import Controller
import logging.config
import argparse

def main() -> None: 
    logging.config.fileConfig("config/logging.conf")
    
    parser = argparse.ArgumentParser(
        description="PACOIA project"
    )
    parser.add_argument("--model", required=True, type=str)

    args = parser.parse_args()
    model = args.model
    controller = Controller(model)

    if model == "CrisperWhisper":
        CrisperWhisperInterface(controller.generate_outputs_crisper_whisper).blocks.launch(debug=True)
    elif model == "Whisper":
        WhisperInterface(controller.generate_outputs_whisper).blocks.launch(debug=True)
    else:
        print(f"Model '{model}' is not currently supported", file=sys.stderr)
        sys.exit(1)

if __name__ == "__main__":
    main()