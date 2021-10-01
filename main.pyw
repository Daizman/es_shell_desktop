import sys
from PyQt5.QtWidgets import QApplication

import model.Shell as ShellModel
import controller.Shell as ShellController


def main():
    app = QApplication(sys.argv)

    model = ShellModel.Shell()
    controller = ShellController.Shell(model)

    app.exec_()


if __name__ == '__main__':
    sys.exit(main())
