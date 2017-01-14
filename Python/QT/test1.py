# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'test1.ui'
#
# Created: Tue Nov 11 14:51:58 2014
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
"background: gray;\n"
"}\n"
"\n"
"#mainFrame {\n"
"border: 3px solid gray;\n"
"border-radius: 40px;\n"
"background: white;\n"
"}"))
        self.mainFrame = QtGui.QFrame(MyLoginForm)
        self.mainFrame.setGeometry(QtCore.QRect(50, 40, 301, 221))
        self.mainFrame.setAutoFillBackground(False)
        self.mainFrame.setFrameShape(QtGui.QFrame.StyledPanel)
        self.mainFrame.setFrameShadow(QtGui.QFrame.Raised)
        self.mainFrame.setObjectName(_fromUtf8("mainFrame"))

        self.retranslateUi(MyLoginForm)
        QtCore.QMetaObject.connectSlotsByName(MyLoginForm)

    def retranslateUi(self, MyLoginForm):
        MyLoginForm.setWindowTitle(_translate("MyLoginForm", "Form", None))

