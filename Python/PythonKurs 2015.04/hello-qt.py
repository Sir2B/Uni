#!/usr/bin/env python
# -*- coding: utf-8 -*-
__author__ = 'Tobias'

import sys
from PyQt4 import QtGui

app = QtGui.QApplication(sys.argv)
label = QtGui.QLabel("Hello World!")
button = QtGui.QPushButton("test")
label.show()
print(button.text())
sys.exit(app.exec_())