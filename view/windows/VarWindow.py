from PyQt5 import QtCore, QtWidgets


class UIVarWindow(object):
    def setup_ui(self, var_view):
        var_view.setObjectName('var_view')
        var_view.resize(380, 350)

        var_view.setWindowTitle('Переменная')

        grid = QtWidgets.QGridLayout()
        var_view.setLayout(grid)

        grid.setSpacing(5)

        var_name_label = QtWidgets.QLabel('Имя переменной:')

        self.var_name_text = QtWidgets.QLineEdit()
        self.var_name_text.setObjectName('var_name_text')

        domain_label = QtWidgets.QLabel('Домен:')

        self.domain_combo = QtWidgets.QComboBox(var_view)
        self.domain_combo.setObjectName('domain_combo')

        self.domain_add_button = QtWidgets.QPushButton()
        self.domain_add_button.setObjectName('domain_add_button')

        self.can_be_goal = QtWidgets.QCheckBox('Может быть целью', var_view)

        var_type_label = QtWidgets.QLabel('Тип переменной:')

        self.var_type_radio_inferred = QtWidgets.QRadioButton()
        self.var_type_radio_inferred.setObjectName('var_type_radio_inferred')
        self.var_type_radio_inferred.setChecked(True)

        self.var_type_radio_requested = QtWidgets.QRadioButton()
        self.var_type_radio_requested.setObjectName('var_type_radio_requested')

        self.var_type_radio_out_requested = QtWidgets.QRadioButton()
        self.var_type_radio_out_requested.setObjectName('var_type_radio_out_requested')

        question_text_label = QtWidgets.QLabel('Текст вопроса(если не указать, будет: {имя_переменной}?)')

        self.question_text = QtWidgets.QTextEdit()
        self.question_text.setObjectName('question_text')

        buttons = QtWidgets.QDialogButtonBox.Ok | QtWidgets.QDialogButtonBox.Cancel
        self.button_box = QtWidgets.QDialogButtonBox(buttons)

        grid.addWidget(var_name_label, 1, 0)
        grid.addWidget(self.var_name_text, 1, 1, 1, 5)

        grid.addWidget(domain_label, 2, 0)
        grid.addWidget(self.domain_combo, 2, 1, 1, 4)
        grid.addWidget(self.domain_add_button, 2, 5)

        grid.addWidget(self.can_be_goal, 3, 0, 1, 5)

        grid.addWidget(var_type_label, 4, 0)
        grid.addWidget(self.var_type_radio_inferred, 4, 1, 1, 5)
        grid.addWidget(self.var_type_radio_requested, 5, 1, 1, 5)
        grid.addWidget(self.var_type_radio_out_requested, 6, 1, 1, 5)

        grid.addWidget(question_text_label, 7, 0, 1, 6)

        grid.addWidget(self.question_text, 8, 0, 4, 6)

        grid.addWidget(self.button_box.buttons()[0], 12, 0)
        grid.addWidget(self.button_box.buttons()[1], 12, 5)

        self.retranslate_ui(var_view)

    def retranslate_ui(self, var_view):
        _translate = QtCore.QCoreApplication.translate
        var_view.setWindowTitle(_translate('var_view', 'Редактирование переменной'))
        self.domain_add_button.setText(_translate('var_view', '+'))
        self.var_type_radio_inferred.setText(_translate('var_view', 'Запрашиваемая'))
        self.var_type_radio_requested.setText(_translate('var_view', 'Выводимая'))
        self.var_type_radio_out_requested.setText(_translate('var_view', 'Запрашиваемо-выводимая'))
