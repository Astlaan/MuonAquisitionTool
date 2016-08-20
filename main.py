#! /usr/bin/env python3
import sys
import ui_aboutdialog
import subprocess
from PyQt4.QtGui import QMainWindow, QApplication, QDialog
from PyQt4 import QtCore, QtGui
from ui_mainwindow import Ui_MainWindow
from operations import Librarian

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
    def __init__(self, test=False):
        super(MainWindow2, self).__init__()

        # Set up the user interface from Designer. Test flag
        self.setupUi(self)

        """Initial settings"""
        self.display_radio1.setChecked(True)
        self.aquire_status=False
        self.update_status=True #(Graph update)

        # try:
        self.listener = subprocess.Popen(["python3","listener.py", "test" if test==True else ""], bufsize=1, stdin=subprocess.PIPE, stdout=subprocess.PIPE)
        #print(self.listener.communicate()[0])
            #bufsize=1 -> Line buffered. 0 for no buffering
            # print("Listening process activated.")
        # except:
            # print("Failed to activated Listening process.")

        # self.parent, self.child = multiprocessing.Pipe()
        # self.listener1=Listener(self.child)
        # self.listening_proc=multiprocessing.Process(target=listener1)
        # self.listening_proc.start() #Starts the multiprocessing process

        """Booting up the Graphics"""
        self.librarian=Librarian(test, parentBox=self.groupBox_2)  


        # self.preview_plot = pg.PlotWidget(self.groupBox_2)
        # self.preview_plot.resize(500, 500)
        # self.data1 = numpy.random.normal(size=100)
        # self.curve1 = self.preview_plot.plot(self.data1)





        #self.graphdata=[]
        #preview_timer=QTimer()
        #preview_timer.timeout.connect(graphx.update)
        #self.preview_plot = pg.PlotWidget(self.groupBox_2)






        """Connect up the buttons."""
        self.actionAbout.triggered.connect(self.showAboutDialog)

        self.operation_start_button.clicked.connect(self.operation_start) 
        self.operation_stop_button.clicked.connect(self.operation_stop)

        self.display_radio1.clicked.connect(self.on_display_radio)
        self.display_radio2.clicked.connect(self.on_display_radio)
        self.display_radio3.clicked.connect(self.on_display_radio)
        self.display_radio4.clicked.connect(self.on_display_radio)

        self.preview_state_button.clicked.connect(self.on_preview_state_button)
        self.preview_refresh_button.clicked.connect(self.on_preview_refresh_button)

        self.hv_slider.valueChanged.connect(self.on_hv_slider)
        self.hv_spinbox.valueChanged.connect(self.on_hv_spinbox)
        self.hv_set_button.clicked.connect(self.on_hv_set_button)

    def operation_start(self):
        print("Operation started")
        self.operation_status_label.setText(_translate("MainWindow", "<html><head/><body><p><span style=\" font-weight:600; color:#00ff00;\">Running...</span></p></body></html>", None))
        self.operation_start_button.setEnabled(False)
        self.operation_stop_button.setEnabled(True)
        #print(self.listener.communicate(input=bytes("start", "ascii"))[0])
        self.listener.stdin.write(bytes("start\n", "ascii"))
        self.listener.stdin.flush()
        print(self.listener.stdout.readline())
        self.listener.stdout.flush()
        #print(self.listener.stdout.readline() + " SUCCESSFULL")
        #if self.update_status==True:
            #get data function



    def operation_stop(self):
        print("Operation stopped")
        self.operation_status_label.setText(_translate("MainWindow", "<html><head/><body><p><span style=\" font-weight:600; color:#ff0000;\">Stopped.</span></p></body></html>", None))
        self.operation_start_button.setEnabled(True)
        self.operation_stop_button.setEnabled(False)
        self.listener.stdin.write(bytes("stop\n", "ascii"))
        self.listener.stdin.flush()
        print(self.listener.stdout.readline())
        self.listener.stdout.flush()

    def on_display_radio(self):
        print("on_display_radio")
        #if b.isChecked==True:
        b=self.sender().objectName()
        if b=="display_radio1":  #1 minute
            print("Last 15 seconds")
            librarian.setRange(15)
        elif b=="display_radio2": #1 hour
            print("Last minute")
            librarian.setRange(60)
        elif b=="display_radio3":  #1 day
            print("Last hour")
            librarian.setRange(3600)
        else:
            print("4") 
        
    def showAboutDialog(self):
        print("About Dialog opened")
        self.d=QDialog()
        self.about_ui=ui_aboutdialog.Ui_Dialog()
        self.about_ui.setupUi(self.d)

        self.d.btn_about_close.clicked.connect(self.d.close)
        self.d.show()

    def on_hv_slider(self, value):
        self.hv_spinbox.setValue(value)

    def on_hv_spinbox(self, value):
        self.hv_slider.setValue(value)

    def on_hv_set_button(self):  #Falta............
        True

    def on_preview_state_button(self):
        print("Preview state button pushed")

        if self.preview_state_button.text()=="Resume":
            self.preview_state_button.setText("Pause")
            self.update_status=False
            #stop timer

        else: #pause
            self.preview_state_button.setText("Resume")
            self.update_status=True
            #get_last_events
            #resume timer


    def on_preview_refresh_button(self):
        print("Refreshing")
        self.librarian.refreshData(refreshgraph_flag=True)


            #Menu
        #self.actionManual.activated.connect(show_Manual)

    def __del__(self):
        #self.librarian.__del__()
        self.listener.stdin.write(bytes("exit\n", "ascii"))
        self.listener.stdin.flush()




if __name__=="__main__":
    app=QApplication(sys.argv)
    window = MainWindow2(test=True if len(sys.argv)==2 else False)
    window.show()   

    """Starting the Listener""" #I tried to put this multiprocessing part inside the class, but it didn't work, somehow...
    # parent, child = multiprocessing.Pipe()
    # listener1=Listener(child)
    # listening_proc=multiprocessing.Process(target=listener1)
    # listening_proc.start()

    # from IPython.Shell import IPShellEmbed

    # ipshell = IPShellEmbed()

    # ipshell() # this call anywhere in your program will start IPython

    close_signal=app.exec_()
    # parent.send("exit") #command that tells the listener to close.
    # listening_proc.join()
    sys.exit(close_signal)


"""Notes

It is probably possible to pack all graphics related stuff into a class with methods (for organization) with multiple inheritance,
though I am not skilled with this aspect of python. So I went with a simpler approach to have an earlier release date.

THIS PROGRAM USES EPOCH (UNIX) TIME.

Database has timestamp default as current_timestamp(), be careful, always send the timestamp yourself to MySQL.

 """

