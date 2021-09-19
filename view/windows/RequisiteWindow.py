from PyQt5 import QtCore, QtGui, QtWidgets


class UIRequisiteWindow(object):
    def setup_ui(self, requisite_view):
        requisite_view.setObjectName('requisite_view')
        requisite_view.resize(355, 180)

        self.central_widget = QtWidgets.QWidget(requisite_view)
        self.central_widget.setObjectName('central_widget')

        self.combo = QtWidgets.QComboBox(self.central_widget)
        self.combo.setGeometry(QtCore.QRect(10, 10, 300, 20))
        self.combo.setObjectName('combo')

        self.value_combo = QtWidgets.QComboBox(self.central_widget)
        self.value_combo.setGeometry(QtCore.QRect(10, 60, 340, 20))
        self.value_combo.setObjectName('value_combo')

        self.line = QtWidgets.QFrame(self.central_widget)
        self.line.setGeometry(QtCore.QRect(10, 90, 340, 15))
        self.line.setFrameShape(QtWidgets.QFrame.HLine)
        self.line.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line.setObjectName('line')

        self.add_button = QtWidgets.QPushButton(self.central_widget)
        self.add_button.setGeometry(QtCore.QRect(310, 10, 40, 25))
        self.add_button.setObjectName('add_button')

        self.eq_label = QtWidgets.QLabel(self.central_widget)
        self.eq_label.setGeometry(QtCore.QRect(180, 40, 15, 15))

        font = QtGui.QFont()
        font.setPointSize(16)

        self.eq_label.setFont(font)
        self.eq_label.setObjectName('eq_label')

        self.cancel_button = QtWidgets.QPushButton(self.central_widget)
        self.cancel_button.setGeometry(QtCore.QRect(270, 110, 75, 25))
        self.cancel_button.setObjectName('cancel_button')

        self.ok_button = QtWidgets.QPushButton(self.central_widget)
        self.ok_button.setGeometry(QtCore.QRect(190, 110, 75, 25))
        self.ok_button.setObjectName('ok_button')

        requisite_view.setCentralWidget(self.central_widget)

        self.menu_bar = QtWidgets.QMenuBar(requisite_view)
        self.menu_bar.setGeometry(QtCore.QRect(0, 0, 355, 20))
        self.menu_bar.setObjectName('menu_bar')

        requisite_view.setMenuBar(self.menu_bar)

        self.status_bar = QtWidgets.QStatusBar(requisite_view)
        self.status_bar.setObjectName('status_bar')

        requisite_view.setStatusBar(self.status_bar)

        self.retranslate_ui(requisite_view)
        QtCore.QMetaObject.connectSlotsByName(requisite_view)

    def retranslate_ui(self, requisite_view):
        _translate = QtCore.QCoreApplication.translate
        requisite_view.setWindowTitle(_translate('requisite_view', 'Факт посылки'))
        self.add_button.setText(_translate('requisite_view', '+'))
        self.eq_label.setText(_translate('requisite_view', '='))
        self.cancel_button.setText(_translate('requisite_view', 'Отмена'))
        self.ok_button.setText(_translate('requisite_view', 'OK'))

    def connect_buttons(self):
        self.ok_button.clicked.connect(self.ok)
        self.add_button.clicked.connect(self.add_var)
        self.combo.currentTextChanged.connect(self.on_select_var)
        self.cancel_button.clicked.connect(lambda: self.requisite_editor_window.close())

    def fill_requisite(self):
        var_index = self.combo.findText(self.requisite.getVar().getName())
        self.combo.setCurrentIndex(var_index)
        val_idx = self.value_combo.findText(self.requisite.getVal())
        self.value_combo.setCurrentIndex(val_idx)

    def add_var(self):
        self.add_var_window.prevWindow = self
        self.add_var_ui.setup_ui(self.add_var_window)
        self.add_var_window.show()

    def on_select_var(self):
        self.fill_values()

    def on_vars_change(self):
        self.requisite_editor_window.prevWindow.editRuleWindow.prevWindow.on_vars_change()
        self.fill_vars()
        self.combo.setCurrentIndex(self.combo.count() - 1)

    def on_domains_change(self):
        self.requisite_editor_window.prevWindow.editRuleWindow.prevWindow.on_domains_change()
        self.fill_vars()
        self.combo.setCurrentIndex(self.combo.count() - 1)

    def fill_vars(self):
        self.combo.clear()
        es_vars = self.es_main_window.expertSystem.getVariables()
        for var in es_vars:
            self.combo.addItem(var.getName())

    def fill_values(self):
        self.value_combo.clear()
        var = self.combo.currentText()
        if var == '':
            return False
        values = self.es_main_window.expertSystem.getVariableByName(var).getdomain().getValues()
        for val in values:
            self.value_combo.addItem(val)

    def ok(self):
        exp_sys = self.requisite_editor_window.prevWindow.es_main_window.expertSystem
        if self.combo.currentText() == '':
            error = QtWidgets.QErrorMessage(self.requisite_editor_window)
            error.setWindowTitle('Ошибка!')
            error.showMessage('Необходимо указать переменную')
            return False
        var = exp_sys.getVariableByName(self.combo.currentText())
        val = self.value_combo.currentText()
        if self.requisite is not None:
            self.requisite.setVar(var)
            self.requisite.setVal(val)
        else:
            self.requisite_editor_window.prevWindow.requisiteFacts.append(Fact(var, val))
        self.requisite_editor_window.prevWindow.onRequisiteChanged()
        self.requisite_editor_window.close()
