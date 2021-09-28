from PyQt5 import QtCore, QtGui, QtWidgets


class UIFactWindow(object):
    def setup_ui(self, requisite_view):
        requisite_view.setObjectName('requisite_view')
        requisite_view.resize(355, 100)

        requisite_view.setWindowTitle('Факт')

        grid = QtWidgets.QGridLayout()
        requisite_view.setLayout(grid)

        grid.setSpacing(5)

        self.combo = QtWidgets.QComboBox(requisite_view)
        self.combo.setObjectName('combo')

        self.value_combo = QtWidgets.QComboBox(requisite_view)
        self.value_combo.setObjectName('value_combo')

        self.add_button = QtWidgets.QPushButton()
        self.add_button.setObjectName('add_button')

        eq_label = QtWidgets.QLabel('=')
        eq_label.setGeometry(QtCore.QRect(180, 40, 15, 15))

        font = QtGui.QFont()
        font.setPointSize(16)

        eq_label.setFont(font)
        eq_label.setObjectName('eq_label')

        buttons = QtWidgets.QDialogButtonBox.Ok | QtWidgets.QDialogButtonBox.Cancel
        self.button_box = QtWidgets.QDialogButtonBox(buttons)

        grid.addWidget(self.combo, 1, 0, 1, 5)
        grid.addWidget(self.add_button, 1, 5, 1, 1)

        grid.addWidget(eq_label, 2, 3)

        grid.addWidget(self.value_combo, 3, 0, 1, 6)

        grid.addWidget(self.button_box.buttons()[0], 12, 0)
        grid.addWidget(self.button_box.buttons()[1], 12, 5)

        self.retranslate_ui(requisite_view)

    def retranslate_ui(self, requisite_view):
        _translate = QtCore.QCoreApplication.translate
        requisite_view.setWindowTitle(_translate('requisite_view', 'Факт посылки'))
        self.add_button.setText(_translate('requisite_view', '+'))
