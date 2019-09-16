# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'c:\py\test01.ui'
#
# Created by: PyQt5 UI code generator 5.13.0
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(458, 91)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.txt_s = QtWidgets.QLineEdit(self.centralwidget)
        self.txt_s.setGeometry(QtCore.QRect(20, 50, 113, 20))
        self.txt_s.setObjectName("txt_s")
        self.txt_d = QtWidgets.QLineEdit(self.centralwidget)
        self.txt_d.setGeometry(QtCore.QRect(150, 50, 113, 20))
        self.txt_d.setObjectName("txt_d")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(20, 30, 56, 12))
        self.label.setObjectName("label")
        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        self.label_2.setGeometry(QtCore.QRect(150, 30, 56, 12))
        self.label_2.setObjectName("label_2")
        self.btn_join = QtWidgets.QPushButton(self.centralwidget)
        self.btn_join.setGeometry(QtCore.QRect(280, 22, 75, 51))
        self.btn_join.setObjectName("btn_join")
        self.btn_print = QtWidgets.QPushButton(self.centralwidget)
        self.btn_print.setGeometry(QtCore.QRect(360, 22, 75, 51))
        self.btn_print.setObjectName("btn_print")
        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)
        self.btn_join.clicked.connect(MainWindow.join)
        self.btn_print.clicked.connect(MainWindow.printExcel)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.label.setText(_translate("MainWindow", "학생명"))
        self.label_2.setText(_translate("MainWindow", "학과명"))
        self.btn_join.setText(_translate("MainWindow", "조인"))
        self.btn_print.setText(_translate("MainWindow", "출력"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
