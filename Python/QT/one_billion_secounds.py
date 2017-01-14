#!/usr/bin/env python
# -*- coding: utf-8 -*-

import sys
import time, datetime
from PyQt4.QtCore import *
from PyQt4.QtGui import *




class Calendar(QDialog):
    def __init__(self, parent=None):
        super(Calendar, self).__init__(parent)
        self.setWindowTitle('Calendar widget')
        self.resize(300,100)
        
        # vertical layout for widgets
        layout = QVBoxLayout()
                
        # Create a calendar widget and add it to our layout
        self.description = QLabel()
        layout.addWidget(self.description)    
        self.description.setText("""Enter your birthday and I will tell you, when you're 1 billions seconds old""")            
        
        self.cal = QCalendarWidget()
        layout.addWidget(self.cal)

        # Create a label which we will use to show the date a week from now
        self.lbl = QLabel()
        layout.addWidget(self.lbl)
        
        self.setLayout(layout)
        
        # Connect the clicked signal to the centre handler
        self.connect(self.cal, SIGNAL('selectionChanged()'), self.date_changed)

    def date_changed(self):
        """
        Handler called when the date selection has changed
        """
        # Fetch the currently selected date, this is a QDate object
        startDate = QDateTime(self.cal.selectedDate())
        endDate = self.calculateDate(startDate)

        # Show this date in our label
        self.lbl.setText('Date will be: {date}'.format(date=endDate.toString('dd.MM.yyyy hh:mm:ss')))
        
    def calculateDate(self, startDate):
        try:
            seconds = startDate.toTime_t() +10**9
        except AttributeError:
            raise AttributeError
        return QDateTime.fromTime_t(seconds)


# If the program is run directly or passed as an argument to the python
# interpreter then create a Calendar instance and show it
if __name__ == "__main__":
    app = QApplication(sys.argv)
    gui = Calendar()
    gui.show()
    app.exec_()
