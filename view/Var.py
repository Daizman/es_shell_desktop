from PyQt5.QtWidgets import QErrorMessage, QDialog

from utils.Observer import Observer
from utils.ObserverMeta import ObserverMeta

from view.windows.VarWindow import UIVarWindow
from model.types.VarType import VarType

from model.Domain import Domain as DomainModel
from controller.Domain import Domain as DomainController

from copy import deepcopy


class Var(QDialog, Observer, metaclass=ObserverMeta):
    def __init__(self, controller, model, parent=None):
        super(QDialog, self).__init__(parent)

        self.__controller = controller
        self.__model = model

        if model.name:
            self.__old = deepcopy(model)
            self.notify_model_is_changed()
        else:
            self.refresh_domain_combo()

        self.ui = UIVarWindow()
        self.ui.setup_ui(self)

        self.__model.add_observer(self)
        self.connect_buttons()
        self.connect_events()

    def add_domain(self):
        new_domain = DomainModel('')
        new_domain_controller = DomainController(new_domain)
        if new_domain.name:
            self.__controller.add_domain(new_domain)
            self.__controller.set_domain(new_domain.name)

    def restore_var(self):
        if self.__old:
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

    def refresh_domain_combo(self):
        self.ui.domain_combo.clear()
        self.ui.domain_combo.addItems(map(str, self.__controller.domains))

    def notify_model_is_changed(self):
        self.ui.var_name_text.setText(self.__model.name)
        self.refresh_domain_combo()
        self.ui.domain_combo.setCurrentText(str(self.__model.domain.name))
        if self.__model.var_type == VarType.REQUESTED:
            self.ui.var_type_radio1.setChecked()
        elif self.__model.var_type == VarType.INFERRED:
            self.ui.var_type_radio2.setChecked()
        else:
            self.ui.var_type_radio3.setChecked()
        self.ui.question_text.setText(self.__model.question)
