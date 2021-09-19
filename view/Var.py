from PyQt5.QtWidgets import QErrorMessage,\
    QShortcut, \
    QDialog, \
    QTableWidgetItem

from PyQt5.QtGui import QKeySequence

from utils.Observer import Observer
from utils.ObserverMeta import ObserverMeta

from view.windows.VarWindow import UIVarWindow

from copy import deepcopy


class Var(QDialog, Observer, metaclass=ObserverMeta):
    def __init__(self, controller, model, parent=None):
        super(QDialog, self).__init__(parent)

        self.__controller = controller
        self.__model = model

        self.__old = deepcopy(model)

        self.ui = UIVarWindow()
        self.ui.setup_ui(self)

        self.__model.add_observer(self)
        self.connect_buttons()
        self.connect_events()

    def add_domain(self):
        pass

    def change_domain(self):
        pass

    def fill_domains(self):
        pass

    def fill_var(self):
        pass

    def restore_var(self):
        self.__model.remove_observer(self)
        self.__model.name = self.__old.name
        self.__model.question = self.__old.question
        self.__model.var_type = self.__old.var_type
        self.__model.may_be_goal = self.__old.may_be_goal
        self.__model.domain = self.__old.domain
        self.close()

    def connect_buttons(self):
        self.ui.domain_add_button.clicked.connect(self.add_domain)
        self.ui.ok_button.clicked.connect(lambda: self.close())
        self.ui.cancel_button.clicked.connect(self.restore_var)

    def connect_events(self):
        self.ui.var_name_text.textChanged.connect(self.__controller.set_name)
        self.ui.domain_combo.currentTextChanged.connect(self.__controller.set_domain)
        self.ui.var_type_radio1.setChecked.connect(self.__controller.set_var_type)
        self.ui.var_type_radio2.setChecked.connect(self.__controller.set_var_type)
        self.ui.var_type_radio3.setChecked.connect(self.__controller.set_var_type)
        self.ui.question_text.textChanged.connect(self.__controller.set_question)

    def show_error(self, e):
        error_dialog = QErrorMessage(self)
        error_dialog.setWindowTitle('Ошибка!')
        error_dialog.showMessage(e)

    def notify_model_is_changed(self):
        pass
