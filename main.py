#! usr/bin/env python3

import sys
from PyQt4.QtGui import QMainWindow, QApplication
from ui_mainwindow import Ui_MainWindow
import ui_aboutdialog

class MainWindow2(QMainWindow, Ui_MainWindow):
    def __init__(self):
        super(MainWindow2, self).__init__()

        # Set up the user interface from Designer.
        self.setupUi(self)


        """Connect up the buttons."""     
        
        #operation_stop_button.clicked.connect(self.operation_stop)
        #btn_TDC.clicked.connect(showdialog_TDC)



    def operation_start():
       	print("Operation started")
        sys.close()

    def operation_stop():
       	print("Operation stopped")

    def showAboutDialog(self):
        print("About Dialog opened")
        d=QDialog()
        about_ui=ui_aboutdialog.Ui_Dialog()
        about_ui.setupUi(d)
        d.show()

            #Menu
        #self.actionManual.activated.connect(show_Manual)
        actionAbout.hovered.connect(showAboutDialog())
        operation_start_button.clicked.connect(operation_start)




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