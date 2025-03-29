from view.Interface import Interface
from controller.Controller import Controller


def main():  
    Interface(Controller().generate_outputs).blocks.launch(debug=True)

if __name__ == "__main__":
    main()