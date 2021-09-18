from PyQt5 import QtCore, QtGui, QtWidgets
from view.pyqt5_exten.TableWidgetDragRows import TableWidgetDragRows


class Ui_DomenEditorWindow(object):
    def setupUi(self, DomenEditorWindow, domen=None):
        DomenEditorWindow.setObjectName('DomenEditorWindow')
        DomenEditorWindow.resize(351, 375)
        DomenEditorWindow.setMinimumSize(QtCore.QSize(351, 375))
        DomenEditorWindow.setMaximumSize(QtCore.QSize(351, 375))
        self.centralwidget = QtWidgets.QWidget(DomenEditorWindow)
        self.centralwidget.setObjectName('centralwidget')
        self.domenNameLabel = QtWidgets.QLabel(self.centralwidget)
        self.domenNameLabel.setGeometry(QtCore.QRect(10, 0, 91, 16))
        self.domenNameLabel.setObjectName('domenNameLabel')
        self.domenNameText = QtWidgets.QLineEdit(self.centralwidget)
        self.domenNameText.setGeometry(QtCore.QRect(10, 20, 331, 20))
        self.domenNameText.setObjectName('domenNameText')
        self.domenValLabel = QtWidgets.QLabel(self.centralwidget)
        self.domenValLabel.setGeometry(QtCore.QRect(10, 50, 61, 16))
        self.domenValLabel.setObjectName('domenValLabel')
        self.domenValView = TableWidgetDragRows(self.centralwidget)
        self.domenValView.setGeometry(QtCore.QRect(10, 70, 331, 141))
        self.domenValView.setObjectName('domenValView')
        self.domenValView.setColumnCount(1)
        self.domenValView.setHorizontalHeaderLabels(['Значения'])
        self.domenValView.horizontalHeader().setSectionResizeMode(0, QtWidgets.QHeaderView.Stretch)

        self.domenValText = QtWidgets.QLineEdit(self.centralwidget)
        self.domenValText.setGeometry(QtCore.QRect(10, 250, 291, 20))
        self.domenValText.setObjectName('domenValText')
        self.domenValInpLabel = QtWidgets.QLabel(self.centralwidget)
        self.domenValInpLabel.setGeometry(QtCore.QRect(10, 210, 61, 16))
        self.domenValInpLabel.setObjectName('domenValInpLabel')
        self.domenAddButton = QtWidgets.QPushButton(self.centralwidget)
        self.domenAddButton.setGeometry(QtCore.QRect(300, 229, 22, 22))
        self.domenAddButton.setObjectName('domenAddButton')
        self.delDomenValButton = QtWidgets.QPushButton(self.centralwidget)
        self.delDomenValButton.setGeometry(QtCore.QRect(10, 260, 331, 25))
        self.delDomenValButton.setObjectName('delDomenValButton')
        self.line = QtWidgets.QFrame(self.centralwidget)
        self.line.setGeometry(QtCore.QRect(10, 290, 331, 16))
        self.line.setFrameShape(QtWidgets.QFrame.HLine)
        self.line.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line.setObjectName('line')
        self.cancelButton = QtWidgets.QPushButton(self.centralwidget)
        self.cancelButton.setGeometry(QtCore.QRect(260, 310, 75, 25))
        self.cancelButton.setObjectName('cancelButton')
        self.okButton = QtWidgets.QPushButton(self.centralwidget)
        self.okButton.setGeometry(QtCore.QRect(180, 310, 75, 25))
        self.okButton.setObjectName('okButton')
        DomenEditorWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(DomenEditorWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 351, 21))
        self.menubar.setObjectName('menubar')
        DomenEditorWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(DomenEditorWindow)
        self.statusbar.setObjectName('statusbar')
        DomenEditorWindow.setStatusBar(self.statusbar)

        self.retranslateUi(DomenEditorWindow)
        self.domenEditorWindow = DomenEditorWindow
        self.connectButtons()
        self.connectHotkeys()
        QtCore.QMetaObject.connectSlotsByName(DomenEditorWindow)
        self.domen = domen if domen is not None else None
        if self.domen is not None:
            self.fillDomen()

    def retranslateUi(self, DomenEditorWindow):
        _translate = QtCore.QCoreApplication.translate
        DomenEditorWindow.setWindowTitle(_translate('DomenEditorWindow', 'Редактирование домена'))
        self.domenNameLabel.setText(_translate('DomenEditorWindow', 'Имя домена:'))
        self.domenValLabel.setText(_translate('DomenEditorWindow', 'Значения:'))
        self.domenValInpLabel.setText(_translate('DomenEditorWindow', 'Значение:'))
        self.domenAddButton.setToolTip(_translate('DomenEditorWindow', 'Добавить'))
        self.domenAddButton.setText(_translate('DomenEditorWindow', '+'))
        self.delDomenValButton.setText(_translate('DomenEditorWindow', 'Удалить'))
        self.cancelButton.setText(_translate('DomenEditorWindow', 'Отмена'))
        self.okButton.setText(_translate('DomenEditorWindow', 'OK'))

    def connectHotkeys(self):
        self.shortcutDel = QtWidgets.QShortcut(QtGui.QKeySequence('Delete'), self.domenEditorWindow)
        self.shortcutDel.activated.connect(self.delValue)

    def connectButtons(self):
        self.domenAddButton.clicked.connect(self.addValue)
        self.delDomenValButton.clicked.connect(self.delValue)
        self.okButton.clicked.connect(self.okClick)

        self.cancelButton.clicked.connect(lambda: self.domenEditorWindow.close())

    def addValue(self, val):
        if not val:
            val = self.domenValText.text().upper().strip()

        if self.domenValView.findItems(val, QtCore.Qt.MatchExactly):
            error = QtWidgets.QErrorMessage(self.domenEditorWindow)
            error.setWindowTitle('Ошибка!')
            error.showMessage('Такое значение уже есть')
            return False

        row = self.domenValView.rowCount()
        self.domenValView.setRowCount(row + 1)
        self.domenValView.setItem(row, 0, QtWidgets.QTableWidgetItem(val))

    def delValue(self):
        rows = sorted(set(item.row() for item in self.domenValView.selectedItems()))
        for row_index in reversed(rows):
            self.domenValView.removeRow(row_index)

    def okClick(self):
        expSys = self.domenEditorWindow.prevWindow.es_main_window.expertSystem
        if expSys.getDomenByName(self.domenNameText.text()):
            if self.domen is not None and self.domen.getName() != self.domenNameText.text() or self.domen is None:
                error = QtWidgets.QErrorMessage(self.domenEditorWindow)
                error.setWindowTitle('Ошибка!')
                error.showMessage('Данное имя уже используется')
                return False
        self.domenValView.selectAll()
        domenVals = [item.text() for item in self.domenValView.selectedItems()]
        if self.domen is not None:
            try:
                self.domen.setName(self.domenNameText.text())
                self.domen.setValues(domenVals)
            except Exception as e:
                error = QtWidgets.QErrorMessage(self.domenEditorWindow)
                error.setWindowTitle('Ошибка!')
                error.showMessage(str(e))
                return False
        else:
            expSys.addDomen(self.domenNameText.text(), domenVals)
        expSys.updateDicts()
        self.domenEditorWindow.prevWindow.on_domains_change()
        self.domenEditorWindow.close()

    def fillDomen(self):
        self.domenNameText.setText(self.domen.getName())
        for domenVal in self.domen.getValues():
            self.addValue(domenVal)


if __name__ == '__main__':
    import sys
    app = QtWidgets.QApplication(sys.argv)
    DomenEditorWindow = QtWidgets.QMainWindow()
    ui = Ui_DomenEditorWindow()
    ui.setupUi(DomenEditorWindow)
    DomenEditorWindow.show()
    sys.exit(app.exec_())
