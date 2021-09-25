from PyQt5.QtWidgets import QWidget, QErrorMessage


class IShowError(QWidget):
    def show_error(self, e):
        error_dialog = QErrorMessage(self)
        error_dialog.setWindowTitle('Ошибка!')
        error_dialog.showMessage(e)
