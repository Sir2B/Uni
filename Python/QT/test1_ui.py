# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'test1.ui'
#
# Created: Tue Nov 11 15:19:36 2014
#      by: PyQt4 UI code generator 4.10.4
#
# WARNING! All changes made in this file will be lost!

from PyQt4 import QtCore, QtGui

try:
    _fromUtf8 = QtCore.QString.fromUtf8
except AttributeError:
    def _fromUtf8(s):
        return s

try:
    _encoding = QtGui.QApplication.UnicodeUTF8
    def _translate(context, text, disambig):
        return QtGui.QApplication.translate(context, text, disambig, _encoding)
except AttributeError:
    def _translate(context, text, disambig):
        return QtGui.QApplication.translate(context, text, disambig)

class Ui_MyLoginForm(object):
    def setupUi(self, MyLoginForm):
        MyLoginForm.setObjectName(_fromUtf8("MyLoginForm"))
        MyLoginForm.resize(400, 300)
        MyLoginForm.setStyleSheet(_fromUtf8("#MyLoginForm {\n"
"background-color:qlineargradient(spread:pad, x1:0, y1:1, x2:1, y2:0, stop:0 rgba(75, 93, 72, 255), stop:1 rgba(156, 166, 62, 255))\n"
"}\n"
"\n"
"#mainFrame {\n"
"border: 3px solid gray;\n"
"border-radius: 40px;\n"
"background-color: rgba(255,255,255, 50%);\n"
"}\n"
"QLineEdit {\n"
"padding: 1px;\n"
"border-style: solid;\n"
"border: 2px solid gray;\n"
"border-radius: 8px;\n"
"}\n"
"QPushButton {\n"
"color: white;\n"
"background-color: QLinearGradient( x1: 0, y1: 0, x2: 0, y2: 1, stop: 0 #88d, stop: 0.1 #99e, stop: 0.49 #77c, stop: 0.5 #66b, stop: 1 #77c);\n"
"border-width: 1px;\n"
"border-color: #339;\n"
"border-style: solid;\n"
"border-radius: 7;\n"
"padding: 3px;\n"
"font-size: 10px;\n"
"padding-left: 5px;\n"
"padding-right: 5px;\n"
"min-width: 50px;\n"
"max-width: 150px;\n"
"min-height: 13px;\n"
"max-height: 13px;\n"
"}"))
        self.mainFrame = QtGui.QFrame(MyLoginForm)
        self.mainFrame.setGeometry(QtCore.QRect(50, 40, 301, 221))
        self.mainFrame.setAutoFillBackground(False)
        self.mainFrame.setFrameShape(QtGui.QFrame.StyledPanel)
        self.mainFrame.setFrameShadow(QtGui.QFrame.Raised)
        self.mainFrame.setObjectName(_fromUtf8("mainFrame"))
        self.gridLayout = QtGui.QGridLayout(self.mainFrame)
        self.gridLayout.setObjectName(_fromUtf8("gridLayout"))
        self.lineEdit = QtGui.QLineEdit(self.mainFrame)
        self.lineEdit.setObjectName(_fromUtf8("lineEdit"))
        self.gridLayout.addWidget(self.lineEdit, 0, 2, 1, 1)
        self.label = QtGui.QLabel(self.mainFrame)
        self.label.setObjectName(_fromUtf8("label"))
        self.gridLayout.addWidget(self.label, 0, 1, 1, 1)
        spacerItem = QtGui.QSpacerItem(40, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.gridLayout.addItem(spacerItem, 0, 0, 1, 1)
        self.pushButton = QtGui.QPushButton(self.mainFrame)
        self.pushButton.setObjectName(_fromUtf8("pushButton"))
        self.gridLayout.addWidget(self.pushButton, 1, 2, 1, 1)
        spacerItem1 = QtGui.QSpacerItem(40, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.gridLayout.addItem(spacerItem1, 0, 3, 1, 1)

        self.retranslateUi(MyLoginForm)
        QtCore.QMetaObject.connectSlotsByName(MyLoginForm)

    def retranslateUi(self, MyLoginForm):
        MyLoginForm.setWindowTitle(_translate("MyLoginForm", "Form", None))
        self.label.setText(_translate("MyLoginForm", "Name:", None))
        self.pushButton.setText(_translate("MyLoginForm", "Blöder Button", None))

