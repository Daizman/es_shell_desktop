import sys
from PyQt5.QtWidgets import QApplication

from model.Shell import Shell as ShellModel
from controller.Shell import Shell as ShellController


def main():
    app = QApplication(sys.argv)

    controller = ShellController(ShellModel(''))
    controller.show()
    app.exec_()


if __name__ == '__main__':
    sys.exit(main())
