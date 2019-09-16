# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'c:\py\test02.ui'
#
# Created by: PyQt5 UI code generator 5.13.0
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(339, 156)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.btn_ok = QtWidgets.QPushButton(self.centralwidget)
        self.btn_ok.setGeometry(QtCore.QRect(260, 120, 61, 23))
        self.btn_ok.setObjectName("btn_ok")
        self.txt_save = QtWidgets.QLineEdit(self.centralwidget)
        self.txt_save.setGeometry(QtCore.QRect(10, 30, 320, 20))
        self.txt_save.setObjectName("txt_save")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(10, 10, 56, 12))
        self.label.setObjectName("label")
        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        self.label_2.setGeometry(QtCore.QRect(10, 80, 56, 12))
        self.label_2.setObjectName("label_2")
        self.txt_fName = QtWidgets.QLineEdit(self.centralwidget)
        self.txt_fName.setGeometry(QtCore.QRect(10, 80, 320, 12))
        self.txt_fName.setObjectName("txt_fName")
        self.label_3 = QtWidgets.QLabel(self.centralwidget)
        self.label_3.setGeometry(QtCore.QRect(10, 50, 321, 12))
        self.label_3.setObjectName("label_3")
        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)
        self.btn_ok.clicked.connect(MainWindow.print_ok)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.btn_ok.setText(_translate("MainWindow", "확인"))
        self.txt_save.setText(_translate("MainWindow", "c:\\"))
        self.label.setText(_translate("MainWindow", "저장 위치"))
        self.label_2.setText(_translate("MainWindow", "파일명"))
        self.label_3.setText(_translate("MainWindow", "저장 위치를 입력하지 않으시면 C드라이브에 저장됩니다."))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
