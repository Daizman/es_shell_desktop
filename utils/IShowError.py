from PyQt5.QtWidgets import QWidget, QDialog, QErrorMessage


class IShowError(QWidget):
    def show_error(self, e):
        error_dialog = QErrorMessage(self)
        error_dialog.setWindowTitle('Ошибка!')
        error_dialog.showMessage(str(e))


class IShowErrorDialog(QDialog, IShowError):
    pass
