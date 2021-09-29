from PyQt5 import QtCore, QtWidgets


class UIRuleWindow(object):
    def setup_ui(self, rule_view):
        rule_view.setObjectName('rule_view')
        rule_view.resize(650, 380)

        rule_view.setWindowTitle('Правило')

        grid = QtWidgets.QGridLayout()
        rule_view.setLayout(grid)

        grid.setSpacing(5)

        name_l = QtWidgets.QLabel('Имя переменной:')

        self.name_le = QtWidgets.QLineEdit()
        self.name_le.setObjectName('name')

        requisite_gb = QtWidgets.QGroupBox('Посылка:', rule_view)

        self.requisite_tw = QtWidgets.QTableWidget(requisite_gb)
        self.requisite_tw.setObjectName('requisite_tw')
        self.requisite_tw.setColumnCount(2)
        self.requisite_tw.setHorizontalHeaderLabels(['Переменная', 'Значение'])
        self.requisite_tw.horizontalHeader().setSectionResizeMode(1, QtWidgets.QHeaderView.Stretch)
        self.requisite_tw.setSelectionBehavior(QtWidgets.QAbstractItemView.SelectRows)

        self.add_requisite_button = QtWidgets.QPushButton(requisite_gb)
        self.add_requisite_button.setObjectName('add_requisite_button')

        self.edit_requisite_button = QtWidgets.QPushButton(requisite_gb)
        self.edit_requisite_button.setObjectName('edit_requisite_button')

        self.remove_requisite_button = QtWidgets.QPushButton(requisite_gb)
        self.remove_requisite_button.setObjectName('remove_requisite_button')

        conclusion_gb = QtWidgets.QGroupBox('Заключение:', rule_view)

        self.conclusion_tw = QtWidgets.QTableWidget(conclusion_gb)
        self.conclusion_tw.setObjectName('conclusion_tw')
        self.conclusion_tw.setColumnCount(2)
        self.conclusion_tw.setHorizontalHeaderLabels(['Переменная', 'Значение'])
        self.conclusion_tw.horizontalHeader().setSectionResizeMode(1, QtWidgets.QHeaderView.Stretch)
        self.conclusion_tw.setSelectionBehavior(QtWidgets.QAbstractItemView.SelectRows)

        self.add_conclusion_button = QtWidgets.QPushButton(conclusion_gb)
        self.add_conclusion_button.setObjectName('add_conclusion_button')

        self.edit_conclusion_button = QtWidgets.QPushButton(conclusion_gb)
        self.edit_conclusion_button.setObjectName('edit_conclusion_button')

        self.remove_conclusion_button = QtWidgets.QPushButton(conclusion_gb)
        self.remove_conclusion_button.setObjectName('remove_conclusion_button')

        description_l = QtWidgets.QLabel('Пояснение:')

        self.description_le = QtWidgets.QTextEdit()
        self.description_le.setObjectName('description_le')

        buttons = QtWidgets.QDialogButtonBox.Ok | QtWidgets.QDialogButtonBox.Cancel
        self.button_box = QtWidgets.QDialogButtonBox(buttons)

        grid.addWidget(name_l, 1, 0)
        grid.addWidget(self.name_le, 1, 1, 1, 10)

        grid.addWidget(requisite_gb, 2, 0, 5, 5)
        grid.addWidget(conclusion_gb, 2, 6, 5, 5)

        grid.addWidget(self.requisite_tw, 5, 0, 1, 5)
        grid.addWidget(self.conclusion_tw, 5, 6, 1, 5)

        grid.addWidget(self.add_requisite_button, 6, 0)
        grid.addWidget(self.edit_requisite_button, 6, 2)
        grid.addWidget(self.remove_requisite_button, 6, 4)

        grid.addWidget(self.add_conclusion_button, 6, 6)
        grid.addWidget(self.edit_conclusion_button, 6, 8)
        grid.addWidget(self.remove_conclusion_button, 6, 10)

        grid.addWidget(description_l, 7, 0)
        grid.addWidget(self.description_le, 8, 0, 1, 11)

        grid.addWidget(self.button_box.buttons()[0], 9, 8)
        grid.addWidget(self.button_box.buttons()[1], 9, 10)

        self.retranslate_ui(rule_view)

    def retranslate_ui(self, rule_view):
        _translate = QtCore.QCoreApplication.translate
        rule_view.setWindowTitle(_translate('rule_view', 'Редактирование правила'))
        self.add_requisite_button.setText(_translate('EditRuleWindow', 'Добавить'))
        self.edit_requisite_button.setText(_translate('EditRuleWindow', 'Изменить'))
        self.remove_requisite_button.setText(_translate('EditRuleWindow', 'Удалить'))
        self.add_conclusion_button.setText(_translate('EditRuleWindow', 'Добавить'))
        self.edit_conclusion_button.setText(_translate('EditRuleWindow', 'Изменить'))
        self.remove_conclusion_button.setText(_translate('EditRuleWindow', 'Удалить'))
