from PyQt5 import QtCore, QtWidgets


class UIConsultWindow(object):
    def setup_ui(self, consult_view):
        consult_view.setObjectName('consult_view')
        consult_view.resize(350, 100)

        grid = QtWidgets.QGridLayout()
        consult_view.setLayout(grid)

        grid.setSpacing(5)

        self.answer_b = QtWidgets.QPushButton()
        self.exit_b = QtWidgets.QPushButton()

        self.answer_cb = QtWidgets.QComboBox(consult_view)

        self.question_l = QtWidgets.QLabel('Выберите цель консультации')

        grid.addWidget(self.question_l, 0, 0, 1, 5)
        grid.addWidget(self.answer_cb, 1, 0, 1, 4)
        grid.addWidget(self.answer_b, 1, 4, 1, 1)
        grid.addWidget(self.exit_b, 2, 0, 1, 5)

        self.retranslate_ui(consult_view)

    def retranslate_ui(self, consult_view):
        _translate = QtCore.QCoreApplication.translate
        consult_view.setWindowTitle(_translate('ConsultWindow', 'Консультация'))
        self.answer_b.setText(_translate('ConsultWindow', 'Ответить'))
        self.exit_b.setText(_translate('ConsultWindow', 'Выход'))
