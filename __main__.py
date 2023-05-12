from gui import Ui_MainWindow
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QFileDialog
import sys, os


class MyGui(Ui_MainWindow, QtWidgets.QWidget):
    def __init__(self, dialog):
        Ui_MainWindow.__init__(self)
        QtWidgets.QWidget.__init__(self)
        self.setupUi(dialog)


class MyMainClass():
    def __init__(self) -> None:
        GUI.pushButton_ok.clicked.connect(self.test_click)

    def test_click(self):
        print("got clicked")


class MainWindow(QtWidgets.QMainWindow):
    def init(self):
        QtWidgets.QMainWindow.init(self)

    def closeEvent(self, event):
        close = QtWidgets.QMessageBox.question(self,
                                               "QUIT",
                                               "Are you sure?",
                                               QtWidgets.QMessageBox.Yes | QtWidgets.QMessageBox.No)

        if close == QtWidgets.QMessageBox.Yes:
            event.accept()
        else:
            event.ignore()

if __name__ == '__main__':

    app = QtWidgets.QApplication(sys.argv)
    mainWindow = MainWindow()

    mainWindow.setWindowFlags(mainWindow.windowFlags(
    ) | QtCore.Qt.WindowMinimizeButtonHint | QtCore.Qt.WindowSystemMenuHint)

    try:
        def resource_path(relative_path):
            if hasattr(sys, '_MEIPASS'):
                return os.path.join(sys._MEIPASS, relative_path)
            return os.path.join(os.path.abspath("."), relative_path)

        p = resource_path('favicon.ico')
    except Exception as e:
        print(e)
        pass


    GUI = MyGui(mainWindow)
    mainWindow.showMaximized()

    myMC = MyMainClass()

    app.exec_()
    print("Exit")
    sys.exit()