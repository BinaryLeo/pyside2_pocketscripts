# pip3 install pyside2
import sys
from PySide2.QtCore import QSize, Qt
from PySide2.QtWidgets import QApplication, QMainWindow ,QPushButton
# The handler (QApplication) and a basic empty GUI widget with a
# QMainWindow and a single push-able button (QPushButton)

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        
        self.setWindowTitle("QMain Application")
        button = QPushButton('Press me!')
        
        #Set the central Widget of the window
        self.setCentralWidget(button)
        #set window size
        self.setFixedSize(QSize(400,300)) 
        #  maximize control is disabled on Windows & Linux
        
app = QApplication(sys.argv)
window = MainWindow()
window.show()
app.exec_()
