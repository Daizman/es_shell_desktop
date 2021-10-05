from PyQt5 import QtCore, QtWidgets


class UIConsultWindow(object):
    def setup_ui(self, consult_view):
        consult_view.setObjectName('consult_view')
        consult_view.resize(350, 150)

        self.central_widget = QtWidgets.QWidget(consult_view)
        self.central_widget.setObjectName('central_widget')

        grid = QtWidgets.QGridLayout()
        consult_view.setLayout(grid)

        grid.setSpacing(5)

        self.answer_b = QtWidgets.QPushButton(self.central_widget)
        self.exit_b = QtWidgets.QPushButton(self.central_widget)

        self.answer_cb = QtWidgets.QComboBox(self.central_widget)

        self.question_l = QtWidgets.QLabel(self.central_widget)
        self.question_l.setText('Выберите цель консультации')

        consult_view.setCentralWidget(self.central_widget)

        grid.addWidget(self.question_l, 0, 0, 1, 5)
        grid.addWidget(self.answer_cb, 1, 0, 1, 4)
        grid.addWidget(self.answer_b, 1, 5, 1, 1)
        grid.addWidget(self.answer_b, 2, 0, 1, 5)

        self.retranslate_ui(consult_view)

    def retranslate_ui(self, consult_view):
        _translate = QtCore.QCoreApplication.translate
        consult_view.setWindowTitle(_translate('ConsultWindow', 'Консультация'))
        self.answer_b.setText(_translate('ConsultWindow', 'Ответить'))
        self.exit_b.setText(_translate('ConsultWindow', 'Выход'))
