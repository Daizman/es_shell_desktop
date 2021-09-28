from PyQt5.QtWidgets import QDialog, QErrorMessage


class IShowError(QDialog):
    def show_error(self, e):
        error_dialog = QErrorMessage(self)
        error_dialog.setWindowTitle('Ошибка!')
        error_dialog.showMessage(e)
