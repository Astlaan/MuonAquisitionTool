#! usr/bin/env python3

import sys
from PyQt4.QtGui import QMainWindow, QApplication, QDialog
from PyQt4 import QtCore, QtGui
from ui_mainwindow import Ui_MainWindow
import ui_aboutdialog

#import graphx
import numpy 
import pyqtgraph as pg

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

class MainWindow2(QMainWindow, Ui_MainWindow):
    def __init__(self):
        super(MainWindow2, self).__init__()

        # Set up the user interface from Designer.

        self.setupUi(self)

        """Booting up the Graphics"""
        self.preview_plot = pg.PlotWidget(self.groupBox_2)
        self.preview_plot.adjustSize()
        self.data1 = numpy.random.normal(size=300)
        self.curve1 = self.preview_plot.plot(self.data1)

        #self.preview_widget= QtGui.QWidget(self.groupBox_2)


        """Connect up the buttons."""
        self.actionAbout.triggered.connect(self.showAboutDialog)
        self.operation_start_button.clicked.connect(self.operation_start) 


        
        #operation_stop_button.clicked.connect(self.operation_stop)
        #btn_TDC.clicked.connect(showdialog_TDC)



    def operation_start(self):
       	print("Operation started")
        self.operation_status_label.setText("<html><head/><body><p><span style=\" font-weight:600; color:#ff0000;\">Stopped.</span></p></body></html>")


    def operation_stop():
       	print("Operation stopped")
        self.operation_status_label.setText(_translate("MainWindow", "<html><head/><body><p><span style=\" font-weight:600; color:#00ff00;\">Running...</span></p></body></html>", None))

    def showAboutDialog(self):
        print("About Dialog opened")
        self.d=QDialog()
        about_ui=ui_aboutdialog.Ui_Dialog()
        about_ui.setupUi(self.d)

        self.d.btn_about_close(self.d.close)
        self.d.show()



            #Menu
        #self.actionManual.activated.connect(show_Manual)








app=QApplication(sys.argv)
window = MainWindow2()
#ui = MainWindow()
#ui.setupUi(window)



window.show()

"""from PyQt4.QtGui import QDialog
windows2=QDialog()
ui2=ui_aboutdialog.Ui_Dialog()
ui2.setupUi(windows2)

windows2.show()"""


sys.exit(app.exec_())