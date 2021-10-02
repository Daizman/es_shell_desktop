from PyQt5.QtWidgets import QAction, QTableWidgetItem, QAbstractItemView

from PyQt5.QtCore import pyqtSignal

from functools import partial

from view.windows.RuleWindow import UIRuleWindow

from model.types.FactType import FactType
from model.Fact import Fact as FactModel
from controller.Fact import Fact as FactController

from utils.Mixins import *


class Rule(IValidateMyFields, IShowError):
    change_signal = pyqtSignal()

    def __init__(self, rule, variants, domains, parent=None):
        super(Rule, self).__init__(parent)

        self.ui_name = rule.name
        self.ui_description = rule.description
        self.ui_rule = rule
        self.ui_variants = variants
        self.ui_domains = domains

        self.fields_validators = {
            'ui_name': IValidateMyFields.empty_string_validator,
            'ui_description': IValidateMyFields.empty_string_validator,
            'ui_rule': lambda field: (
                    IValidateMyFields.empty_array_validator(field.reasons) and
                    IValidateMyFields.empty_array_validator(field.conclusions)
            )
        }

        self.ui = UIRuleWindow()
        self.ui.setup_ui(self)

        self.refresh_requisite()
        self.refresh_conclusion()

        self.setup_buttons()
        self.setup_events()

    def setup_buttons(self):
        self.ui.button_box.accepted.connect(self.accept_changes)
        self.ui.button_box.rejected.connect(self.reject)

        self.ui.add_requisite_button.clicked.connect(self.add_fact)
        self.ui.edit_requisite_button.clicked.connect(self.edit_fact)
        self.ui.remove_requisite_button.clicked.connect(self.remove_fact)

        self.ui.add_conclusion_button.clicked.connect(self.add_fact)
        self.ui.edit_conclusion_button.clicked.connect(self.edit_fact)
        self.ui.remove_conclusion_button.clicked.connect(self.remove_fact)

    def setup_events(self):
        self.edit_action = QAction(self)
        self.edit_action.setShortcut('Return')
        self.edit_action.triggered.connect(self.edit_fact)

        self.remove_action = QAction(self)
        self.remove_action.setShortcut('Delete')
        self.remove_action.triggered.connect(self.remove_fact)

        self.addAction(self.edit_action)
        self.addAction(self.remove_action)

        self.ui.name_le.textChanged.connect(partial(setattr, self, 'ui_name'))
        self.ui.description_le.textChanged.connect(self.description_text_change)

    def refresh_requisite(self):
        self.ui.requisite_tw.clearContents()
        self.ui.requisite_tw.setRowCount(len(self.ui_rule.reasons))
        for i, reason in enumerate(self.ui_rule.reasons):
            self.ui.requisite_tw.setItem(i, 0, QTableWidgetItem(reason.var.name))
            self.ui.requisite_tw.setItem(i, 1, QTableWidgetItem(reason.value))
        self.ui.requisite_tw.setEditTriggers(QAbstractItemView.NoEditTriggers)

    def refresh_conclusion(self):
        self.ui.conclusion_tw.clearContents()
        self.ui.conclusion_tw.setRowCount(len(self.ui_rule.conclusions))
        for i, conclusion in enumerate(self.ui_rule.conclusions):
            self.ui.conclusion_tw.setItem(i, 0, QTableWidgetItem(conclusion.var.name))
            self.ui.conclusion_tw.setItem(i, 1, QTableWidgetItem(conclusion.value))
        self.ui.conclusion_tw.setEditTriggers(QAbstractItemView.NoEditTriggers)

    def description_text_change(self):
        self.ui_description = self.ui.description_le.toPlainText()

    def add_fact(self):
        source = self.sender()
        new_fact = FactModel()
        new_fact_controller = FactController(new_fact, self.ui_variants, self.ui_domains, self)
        if source == self.ui.add_requisite_button:
            new_fact_controller.set_title('Добавление факта посылки')
        else:
            new_fact_controller.set_title('Добавление факта заключения')
        if new_fact_controller.get_fact():
            if source == self.ui.add_requisite_button:
                self.ui_rule.add_reason(new_fact)
                self.refresh_requisite()
            else:
                self.ui_rule.add_conclusion(new_fact)
                self.refresh_conclusion()

    def edit_fact(self):
        source = self.sender()
        sel_reasons = self.ui.requisite_tw.selectedIndexes()
        sel_conclusions = self.ui.conclusion_tw.selectedIndexes()

        fact_type = None
        new_fact_controller = None

        if source == self.ui.edit_requisite_button and len(sel_reasons) > 0:
            reason_idx = sel_reasons[0].row()
            reason = self.ui_rule.reasons[reason_idx]
            new_fact_controller = FactController(reason, self.ui_variants, self.ui_domains, self)
            new_fact_controller.set_title('Изменение факта посылки')
            fact_type = FactType.REASON

        elif source == self.edit_action and (len(sel_reasons) > 0 or len(sel_conclusions) > 0):
            reason_idx = sel_reasons[0].row() if len(sel_reasons) > 0 else -1
            conclusion_idx = sel_conclusions[0].row() if len(sel_conclusions) > 0 else -1
            reason = self.ui_rule.reasons[reason_idx] if reason_idx != -1 else None
            conclusion = self.ui_rule.conclusions[conclusion_idx] if conclusion_idx != -1 else None

            if reason:
                new_fact_controller = FactController(reason, self.ui_variants, self.ui_domains, self)
                new_fact_controller.set_title('Изменение факта посылки')
                fact_type = FactType.REASON
            elif conclusion:
                new_fact_controller = FactController(conclusion, self.ui_variants, self.ui_domains, self)
                new_fact_controller.set_title('Изменение факта заключения')
                fact_type = FactType.CONCLUSION

        elif source == self.ui.edit_conclusion_button and len(sel_conclusions) > 0:
            conclusion_idx = sel_conclusions[0].row()
            conclusion = self.ui_rule.conclusions[conclusion_idx]
            new_fact_controller = FactController(conclusion, self.ui_variants, self.ui_domains, self)
            new_fact_controller.set_title('Изменение факта заключения')
            fact_type = FactType.CONCLUSION

        if new_fact_controller and new_fact_controller.get_fact():
            if fact_type == FactType.REASON:
                self.refresh_requisite()
            else:
                self.refresh_conclusion()

    def remove_fact(self):
        source = self.sender()
        sel_reasons = self.ui.requisite_tw.selectedIndexes()
        sel_conclusions = self.ui.conclusion_tw.selectedIndexes()

        if source == self.ui.remove_requisite_button and len(sel_reasons) > 0:
            reason_idx = sel_reasons[0].row()
            reason = self.ui_rule.reasons[reason_idx]
            self.ui_rule.remove_reason(reason)
            self.refresh_requisite()
        elif source == self.remove_action and (len(sel_reasons) > 0 or len(sel_conclusions) > 0):
            reason_idx = sel_reasons[0].row() if len(sel_reasons) > 0 else -1
            conclusion_idx = sel_conclusions[0].row() if len(sel_conclusions) > 0 else -1
            reason = self.ui_rule.reasons[reason_idx] if reason_idx != -1 else None
            conclusion = self.ui_rule.conclusions[conclusion_idx] if conclusion_idx != -1 else None
            if reason:
                self.ui_rule.remove_reason(reason)
                self.refresh_requisite()
            elif conclusion:
                self.ui_rule.remove_conclusion(conclusion)
                self.refresh_conclusion()
        elif source == self.ui.edit_conclusion_button and len(sel_conclusions) > 0:
            conclusion_idx = sel_conclusions[0].row()
            conclusion = self.ui_rule.conclusions[conclusion_idx]
            self.ui_rule.remove_conclusion(conclusion)
            self.refresh_conclusion()
