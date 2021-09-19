from PyQt5 import QtCore, QtWidgets
from view.pyqt5_exten.TableWidgetDragRows import TableWidgetDragRows


class UIDomainWindow(object):
    def setup_ui(self, domain_view):
        domain_view.setObjectName('domain_view')
        domain_view.resize(350, 375)

        self.central_widget = QtWidgets.QWidget(domain_view)
        self.central_widget.setObjectName('central_widget')

        self.domain_name_label = QtWidgets.QLabel(self.central_widget)
        self.domain_name_label.setGeometry(QtCore.QRect(10, 0, 90, 15))
        self.domain_name_label.setObjectName('domain_name_label')

        self.domain_name_text = QtWidgets.QLineEdit(self.central_widget)
        self.domain_name_text.setGeometry(QtCore.QRect(10, 20, 330, 20))
        self.domain_name_text.setObjectName('domain_name_text')

        self.domain_val_label = QtWidgets.QLabel(self.central_widget)
        self.domain_val_label.setGeometry(QtCore.QRect(10, 50, 60, 15))
        self.domain_val_label.setObjectName('domain_val_label')

        self.domain_val_view = TableWidgetDragRows(self.central_widget)
        self.domain_val_view.setGeometry(QtCore.QRect(10, 70, 330, 140))
        self.domain_val_view.setObjectName('domain_val_view')
        self.domain_val_view.setColumnCount(1)
        self.domain_val_view.setHorizontalHeaderLabels(['Значения'])
        self.domain_val_view.horizontalHeader().setSectionResizeMode(0, QtWidgets.QHeaderView.Stretch)

        self.domain_val_text = QtWidgets.QLineEdit(self.central_widget)
        self.domain_val_text.setGeometry(QtCore.QRect(10, 230, 290, 20))
        self.domain_val_text.setObjectName('domain_val_text')

        self.domain_val_inp_label = QtWidgets.QLabel(self.central_widget)
        self.domain_val_inp_label.setGeometry(QtCore.QRect(10, 210, 60, 15))
        self.domain_val_inp_label.setObjectName('domain_val_inp_label')

        self.domain_add_button = QtWidgets.QPushButton(self.central_widget)
        self.domain_add_button.setGeometry(QtCore.QRect(300, 230, 20, 20))
        self.domain_add_button.setObjectName('domain_add_button')

        self.remove_domain_val_button = QtWidgets.QPushButton(self.central_widget)
        self.remove_domain_val_button.setGeometry(QtCore.QRect(10, 260, 330, 25))
        self.remove_domain_val_button.setObjectName('remove_domain_val_button')

        self.line = QtWidgets.QFrame(self.central_widget)
        self.line.setGeometry(QtCore.QRect(10, 290, 330, 15))
        self.line.setFrameShape(QtWidgets.QFrame.HLine)
        self.line.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line.setObjectName('line')

        self.cancel_button = QtWidgets.QPushButton(self.central_widget)
        self.cancel_button.setGeometry(QtCore.QRect(260, 310, 75, 25))
        self.cancel_button.setObjectName('cancel_button')

        self.ok_button = QtWidgets.QPushButton(self.central_widget)
        self.ok_button.setGeometry(QtCore.QRect(180, 310, 75, 25))
        self.ok_button.setObjectName('ok_button')

        domain_view.setCentralWidget(self.central_widget)

        self.menu_bar = QtWidgets.QMenuBar(domain_view)
        self.menu_bar.setGeometry(QtCore.QRect(0, 0, 350, 20))
        self.menu_bar.setObjectName('menu_bar')
        domain_view.setMenuBar(self.menu_bar)

        self.status_bar = QtWidgets.QStatusBar(domain_view)
        self.status_bar.setObjectName('status_bar')
        domain_view.setStatusBar(self.status_bar)

        self.retranslate_ui(domain_view)

        QtCore.QMetaObject.connectSlotsByName(domain_view)

    def retranslate_ui(self, domain_view):
        _translate = QtCore.QCoreApplication.translate
        domain_view.setWindowTitle(_translate('domain_view', 'Редактирование домена'))
        self.domain_name_label.setText(_translate('domain_view', 'Имя домена:'))
        self.domain_val_label.setText(_translate('domain_view', 'Значения:'))
        self.domain_val_inp_label.setText(_translate('domain_view', 'Значение:'))
        self.domain_add_button.setToolTip(_translate('domain_view', 'Добавить'))
        self.domain_add_button.setText(_translate('domain_view', '+'))
        self.remove_domain_val_button.setText(_translate('domain_view', 'Удалить'))
        self.cancel_button.setText(_translate('domain_view', 'Отмена'))
        self.ok_button.setText(_translate('domain_view', 'OK'))
