from view.Interface import Interface
from controller.Controller import Controller
import logging.config


def main() -> None:  
    logging.config.fileConfig("config/logging.conf")
    controller = Controller()
    Interface(controller.generate_outputs).blocks.launch(debug=True)

if __name__ == "__main__":
    main()