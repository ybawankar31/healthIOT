from PyQt5 import QtCore, QtGui, QtWidgets
from ui_file import Ui_MainWindow

class MainWin(QtWidgets.QMainWindow):
    def __init__(self):
        super(MainWin, self).__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        self.show()










if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    obj = MainWin()
    sys.exit(app.exec_())