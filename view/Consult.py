from PyQt5.QtCore import pyqtSignal
from PyQt5.QtWidgets import QInputDialog, QMessageBox

from view.windows.ConsultWindow import UIConsultWindow

from utils.Mixins import *


class Consult(IShowErrorDialog):
    change_signal = pyqtSignal()

    def __init__(self, controller, parent=None):
        super(Consult, self).__init__(parent)

        self.controller = controller

        self.ui = UIConsultWindow()
        self.ui.setup_ui(self)

        self.setup_buttons()
        self.refresh()

    def setup_buttons(self):
        self.ui.exit_b.clicked.connect(self.reject)
        self.ui.answer_b.clicked.connect(self.consult)

    def refresh(self):
        self.ui.answer_cb.clear()
        for i in filter(lambda var: var.can_be_goal, self.controller.get_vars()):
            self.ui.answer_cb.addItem(i.name, i)

    def consult(self):
        var = self.ui.answer_cb.currentData()
        answer = self.controller.consult(var)
        if answer:
            self.show_answer(answer)

    def ask_var(self, var):
        dlg = QInputDialog(self)
        dlg.resize(500, 500)
        dlg.setWindowTitle(var.question)
        dlg.setComboBoxItems(var.domain.values)
        dlg.setComboBoxEditable(False)
        dlg.setLabelText(var.question)
        if dlg.exec_():
            return dlg.textValue()
        return False

    def show_answer(self, answer_text):
        answer = QMessageBox(self)
        answer.setWindowTitle('Результат консультации!')
        answer.setText(answer_text)
        answer.exec_()
