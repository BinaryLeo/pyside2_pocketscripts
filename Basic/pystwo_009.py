# pip3 install pyside2
import sys# Only needed for access to comand line arguments 
from PySide2.QtCore import Qt, QSize
from PySide2.QtWidgets import QApplication, QMainWindow , QLabel
# The handler (QApplication), a QMainWindow and A label

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        self.setWindowTitle('My App')
        self.setFixedSize(QSize(400,300)) # Width / height
        #  maximize control is disabled on Windows & Linux
        widget = QLabel('Hello')
        font = widget.font()# get the current font
        font.setPointSize(30)#font-size
        widget.setFont(font)
        widget.setAlignment(Qt.AlignHCenter | Qt.AlignVCenter)#font alignment
        self.setCentralWidget(widget) # Set the central Widget of the Window
app = QApplication(sys.argv)# We neeed one (only one) instance per application
window = MainWindow() # create a new window
window.show()# Windows are hidden by default
app.exec_()# Start the event loop     
     

