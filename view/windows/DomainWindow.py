from PyQt5 import QtCore, QtWidgets
from view.pyqt5_exten.TableWidgetDragRows import TableWidgetDragRows


class UIDomainWindow(object):
    def setup_ui(self, domain_view):
        domain_view.setObjectName('domain_view')
        domain_view.resize(350, 375)

        grid = QtWidgets.QGridLayout()
        domain_view.setLayout(grid)

        grid.setSpacing(5)

        domain_name_label = QtWidgets.QLabel('Имя домена:')

        self.domain_name_text = QtWidgets.QLineEdit()
        self.domain_name_text.setObjectName('domain_name_text')

        domain_val_label = QtWidgets.QLabel('Значения:')

        self.domain_val_view = TableWidgetDragRows()
        self.domain_val_view.setObjectName('domain_val_view')
        self.domain_val_view.setColumnCount(1)
        self.domain_val_view.setHorizontalHeaderLabels(['Значения'])
        self.domain_val_view.horizontalHeader().setSectionResizeMode(0, QtWidgets.QHeaderView.Stretch)

        self.domain_val_text = QtWidgets.QLineEdit()
        self.domain_val_text.setObjectName('domain_val_text')

        domain_val_inp_label = QtWidgets.QLabel('Значение:')

        self.domain_add_button = QtWidgets.QPushButton()
        self.domain_add_button.setObjectName('domain_add_button')

        self.remove_domain_val_button = QtWidgets.QPushButton()
        self.remove_domain_val_button.setObjectName('remove_domain_val_button')

        buttons = QtWidgets.QDialogButtonBox.Ok | QtWidgets.QDialogButtonBox.Cancel
        self.button_box = QtWidgets.QDialogButtonBox(buttons)

        grid.addWidget(domain_name_label, 1, 0)
        grid.addWidget(self.domain_name_text, 1, 1, 1, 2)

        grid.addWidget(domain_val_label, 2, 0)
        grid.addWidget(self.domain_val_view, 3, 0, 1, 3)

        grid.addWidget(domain_val_inp_label, 4, 0)
        grid.addWidget(self.domain_val_text, 4, 1)
        grid.addWidget(self.domain_add_button, 4, 2)

        grid.addWidget(self.remove_domain_val_button, 5, 0, 1, 3)

        grid.addWidget(self.button_box.buttons()[0], 6, 0)
        grid.addWidget(self.button_box.buttons()[1], 6, 2)

        self.retranslate_ui(domain_view)

    def retranslate_ui(self, domain_view):
        _translate = QtCore.QCoreApplication.translate
        domain_view.setWindowTitle(_translate('domain_view', 'Редактирование домена'))
        self.domain_add_button.setToolTip(_translate('domain_view', 'Добавить'))
        self.domain_add_button.setText(_translate('domain_view', '+'))
        self.remove_domain_val_button.setText(_translate('domain_view', 'Удалить'))
