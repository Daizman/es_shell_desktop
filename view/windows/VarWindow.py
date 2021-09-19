from PyQt5 import QtCore, QtWidgets


class UIVarWindow(object):
    def setup_ui(self, var_view):
        var_view.setObjectName('var_view')
        var_view.resize(380, 380)

        self.central_widget = QtWidgets.QWidget(var_view)
        self.central_widget.setObjectName('central_widget')

        self.var_name_label = QtWidgets.QLabel(self.central_widget)
        self.var_name_label.setGeometry(QtCore.QRect(10, 10, 90, 15))
        self.var_name_label.setObjectName('var_name_label')

        self.var_name_text = QtWidgets.QLineEdit(self.central_widget)
        self.var_name_text.setGeometry(QtCore.QRect(10, 30, 360, 20))
        self.var_name_text.setObjectName('var_name_text')

        self.domain_label = QtWidgets.QLabel(self.central_widget)
        self.domain_label.setGeometry(QtCore.QRect(10, 60, 45, 15))
        self.domain_label.setObjectName('domain_label')

        self.domain_combo = QtWidgets.QComboBox(self.central_widget)
        self.domain_combo.setGeometry(QtCore.QRect(10, 80, 340, 20))
        self.domain_combo.setObjectName('domain_combo')

        self.domain_add_button = QtWidgets.QPushButton(self.central_widget)
        self.domain_add_button.setGeometry(QtCore.QRect(350, 80, 25, 25))
        self.domain_add_button.setObjectName('domain_add_button')

        self.var_type_label = QtWidgets.QLabel(self.central_widget)
        self.var_type_label.setGeometry(QtCore.QRect(10, 110, 90, 15))
        self.var_type_label.setObjectName('var_type_label')

        self.var_type_radio1 = QtWidgets.QRadioButton(self.central_widget)
        self.var_type_radio1.setGeometry(QtCore.QRect(10, 130, 360, 20))
        self.var_type_radio1.setObjectName('var_type_radio1')
        self.var_type_radio1.setChecked(True)

        self.var_type_radio2 = QtWidgets.QRadioButton(self.central_widget)
        self.var_type_radio2.setGeometry(QtCore.QRect(10, 150, 360, 20))
        self.var_type_radio2.setObjectName('var_type_radio2')

        self.var_type_radio3 = QtWidgets.QRadioButton(self.central_widget)
        self.var_type_radio3.setGeometry(QtCore.QRect(10, 170, 360, 20))
        self.var_type_radio3.setObjectName('var_type_radio3')

        self.question_text_label = QtWidgets.QLabel(self.central_widget)
        self.question_text_label.setGeometry(QtCore.QRect(10, 190, 360, 15))
        self.question_text_label.setObjectName('question_text_label')

        self.question_text = QtWidgets.QTextEdit(self.central_widget)
        self.question_text.setGeometry(QtCore.QRect(10, 210, 360, 70))
        self.question_text.setObjectName('question_text')

        self.line = QtWidgets.QFrame(self.central_widget)
        self.line.setGeometry(QtCore.QRect(10, 290, 360, 20))
        self.line.setFrameShape(QtWidgets.QFrame.HLine)
        self.line.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line.setObjectName('line')

        self.cancel_button = QtWidgets.QPushButton(self.central_widget)
        self.cancel_button.setGeometry(QtCore.QRect(290, 310, 75, 25))
        self.cancel_button.setObjectName('cancel_button')

        self.ok_button = QtWidgets.QPushButton(self.central_widget)
        self.ok_button.setGeometry(QtCore.QRect(210, 310, 75, 25))
        self.ok_button.setObjectName('ok_button')

        var_view.setCentralWidget(self.central_widget)

        self.menu_bar = QtWidgets.QMenuBar(var_view)
        self.menu_bar.setGeometry(QtCore.QRect(0, 0, 380, 20))
        self.menu_bar.setObjectName('menu_bar')
        var_view.setMenuBar(self.menu_bar)

        self.status_bar = QtWidgets.QStatusBar(var_view)
        self.status_bar.setObjectName('status_bar')
        var_view.setStatusBar(self.status_bar)

        self.retranslate_ui(var_view)
        QtCore.QMetaObject.connectSlotsByName(var_view)

    def retranslate_ui(self, var_view):
        _translate = QtCore.QCoreApplication.translate
        var_view.setWindowTitle(_translate('var_view', 'Редактирование переменной'))
        self.var_name_label.setText(_translate('var_view', 'Имя переменной'))
        self.domain_label.setText(_translate('var_view', 'Домен'))
        self.domain_add_button.setText(_translate('var_view', '+'))
        self.var_type_label.setText(_translate('var_view', 'Тип переменной'))
        self.var_type_radio1.setText(_translate('var_view', 'Запрашиваемая'))
        self.var_type_radio2.setText(_translate('var_view', 'Выводимая'))
        self.var_type_radio3.setText(_translate('var_view', 'Запрашиваемо-выводимая'))
        self.question_text_label.setText(_translate('var_view', 'Текст вопроса(если не указать, будет: {имя_переменной}?)'))
        self.cancel_button.setText(_translate('var_view', 'Отмена'))
        self.ok_button.setText(_translate('var_view', 'OK'))
