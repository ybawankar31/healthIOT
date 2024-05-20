import time
import mysql.connector

import threading

from PyQt5.QtCore import QTime, Qt, QTimer
from PyQt5 import QtCore, QtGui, QtWidgets


#******************************************************************

from cloud_file import representation_value_cloud
from edge_file import representation_value_edge
from sensor_code import *

#VALUES****TO REPRESENT IN THE WINDOW*************************************
try:
    value_pc = sensor_data_queue3.get(timeout= 3)
except Exception as e:
    value_pc = "Fetching"

try:
    value_pe = sensor_data_queue4.get(timeout= 3)
except Exception as e:
    value_pe = "Fetching"

try:
    value_fc = representation_value_cloud.get(timeout= 3)
except Exception as e:
    value_fc = "Fetching"

try:
    value_fe = representation_value_edge.get(timeout=3)
except Exception as e:
    value_fe = "Fetching"

#*************************************************************************
class Ui_MainWindow(object):
    
    def __init__(self):

        self.timer = QTimer()  # Create a QTimer object
        # self.timer.setInterval(1000)
        self.timer.timeout.connect(self.update_clock)  # Connect to update_clock slot
        self.timer.start(1000)

    def update_clock(self):
        # current_time = QTime.currentTime().toString('hh:mm:ss')
        # Update the text of the clock labels with the formatted current time
        

        self.temp_pc.setText(f"{value_pc[0]}")
        self.time_pc.setText(f"{value_pc[1]}")
        
        self.temp_pe.setText(f"{value_pe[0]}")
        self.time_pe.setText(f"{value_pe[1]}")
        
        self.temp_fc.setText(f"{value_fc[0]}")
        self.time_fc.setText(f"{value_fc[1]}")
        
        self.temp_fe.setText(f"{value_fe[0]}")
        self.time_fe.setText(f"{value_fe[1]}")



    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(1900, 1000)
        # MainWindow.setSizeGripEnabled(False)
        self.horizontalLayoutWidget = QtWidgets.QWidget(MainWindow)
        self.horizontalLayoutWidget.setGeometry(QtCore.QRect(9, 10, 1800, 81))
        self.horizontalLayoutWidget.setObjectName("horizontalLayoutWidget")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.horizontalLayoutWidget)
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.label_cloud = QtWidgets.QLabel(self.horizontalLayoutWidget)
        self.label_cloud.setObjectName("label_cloud")
        self.horizontalLayout.addWidget(self.label_cloud)
        self.edge_label = QtWidgets.QLabel(self.horizontalLayoutWidget)
        self.edge_label.setObjectName("edge_label")
        self.horizontalLayout.addWidget(self.edge_label)
        self.verticalLayoutWidget_3 = QtWidgets.QWidget(MainWindow)
        self.verticalLayoutWidget_3.setGeometry(QtCore.QRect(9, 480, 441, 111))
        self.verticalLayoutWidget_3.setObjectName("verticalLayoutWidget_3")
        self.verticalLayout_6 = QtWidgets.QVBoxLayout(self.verticalLayoutWidget_3)
        self.verticalLayout_6.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_6.setObjectName("verticalLayout_6")
        self.Difference = QtWidgets.QLabel(self.verticalLayoutWidget_3)
        self.Difference.setObjectName("Difference")
        self.verticalLayout_6.addWidget(self.Difference)
        self.ave_diff = QtWidgets.QLabel(self.verticalLayoutWidget_3)
        self.ave_diff.setObjectName("ave_diff")
        self.verticalLayout_6.addWidget(self.ave_diff)
        self.push = QtWidgets.QLabel(MainWindow)
        self.push.setGeometry(QtCore.QRect(10, 100, 67, 17))
        self.push.setObjectName("push")
        self.fetch = QtWidgets.QLabel(MainWindow)
        self.fetch.setGeometry(QtCore.QRect(10, 280, 67, 17))
        self.fetch.setObjectName("fetch")



        self.temp_pc = QtWidgets.QLabel(MainWindow)
        self.temp_pc.setGeometry(QtCore.QRect(20, 130, 400, 34))
        self.temp_pc.setObjectName("temp_pc")
        self.time_pc = QtWidgets.QLabel(MainWindow)
        self.time_pc.setGeometry(QtCore.QRect(20, 190, 400, 34))
        self.time_pc.setObjectName("time_pc")

        self.temp_pe = QtWidgets.QLabel(MainWindow)
        self.temp_pe.setGeometry(QtCore.QRect(920, 130, 400, 34))
        self.temp_pe.setObjectName("temp_pe")
        self.time_pe = QtWidgets.QLabel(MainWindow)
        self.time_pe.setGeometry(QtCore.QRect(920, 190, 400, 34))
        self.time_pe.setObjectName("time_pe")

        self.temp_fc = QtWidgets.QLabel(MainWindow)
        self.temp_fc.setGeometry(QtCore.QRect(20, 320, 400, 34))
        self.temp_fc.setObjectName("temp_fc")
        self.time_fc = QtWidgets.QLabel(MainWindow)
        self.time_fc.setGeometry(QtCore.QRect(20, 360, 400, 34))
        self.time_fc.setObjectName("time_fc")

        self.temp_fe = QtWidgets.QLabel(MainWindow)
        self.temp_fe.setGeometry(QtCore.QRect(920, 320, 400, 34))
        self.temp_fe.setObjectName("temp_fe")
        self.time_fe = QtWidgets.QLabel(MainWindow)
        self.time_fe.setGeometry(QtCore.QRect(920, 360, 400, 34))
        self.time_fe.setObjectName("time_fe")


        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "HealthIOT"))
        self.label_cloud.setText(_translate("MainWindow", "Cloud Layer"))
        self.edge_label.setText(_translate("MainWindow", "Edge Layer"))
        self.Difference.setText(_translate("MainWindow", "Time Difference: "))
        self.ave_diff.setText(_translate("MainWindow", "Average Time Difference: "))
        self.push.setText(_translate("MainWindow", "PUSH"))
        self.fetch.setText(_translate("MainWindow", "FETCH"))

        self.temp_pc.setText(_translate("MainWindow", f"Fetching"))
        self.time_pc.setText(_translate("MainWindow", f"Fetching"))
        
        self.temp_pe.setText(_translate("MainWindow", f"Fetching"))
        self.time_pe.setText(_translate("MainWindow", f"Fetching"))
        
        self.temp_fc.setText(_translate("MainWindow", f"Fetching"))
        self.time_fc.setText(_translate("MainWindow", f"Fetching"))
        
        self.temp_fe.setText(_translate("MainWindow", f"Fetching"))
        self.time_fe.setText(_translate("MainWindow", f"Fetching"))




if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QDialog()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())







