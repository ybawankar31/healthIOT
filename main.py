from PyQt5 import QtCore, QtGui, QtWidgets
from ui_file import Ui_MainWindow
import threading
from cloud_file import *
from sensor_code import *
from edge_file import *

class MainWin(QtWidgets.QMainWindow):
    def __init__(self):
        super(MainWin, self).__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        self.show()










if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)

    #Thread 1 to get data from sensor and put it in queue
    thread1_sensor_pipeline = threading.Thread(target=generate_sensor_data)
    thread1_sensor_pipeline.start()

    obj = MainWin()
    
    #Thread 2 to push the data to cloud

    thread2_push_to_cloud = threading.Thread(target= cloud_engine)
    thread2_push_to_cloud.start()

    #Thread 3 to push the data to edge ie., local mysql database
    
    thread3_push_to_edge = threading.Thread(target = edge_engine)
    thread3_push_to_edge.start()

    #Thread 4 to pull the data from edge into window. ie., local mysql database
    
    thread4_pull_from_edge = threading.Thread(target = edge_to_window)
    thread4_pull_from_edge.start()

    #Thread 5 to pull the data from cloud into window. ie., free sql database
    
    thread5_pull_from_cloud = threading.Thread(target = cloud_to_window)
    thread5_pull_from_cloud.start()
    



    sys.exit(app.exec_())