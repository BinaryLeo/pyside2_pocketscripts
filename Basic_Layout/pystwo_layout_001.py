# pip3 install pyside2
import sys # Only needed for access to command line arguments
from PySide2.QtCore import QSize
from PySide2.QtWidgets import QApplication, QMainWindow
from layout_colorwidget import Color

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle('Color_BG')
        self.setFixedSize(QSize(400, 300))  # Width / height
        widget = Color('#CD1D1B')
        self.setCentralWidget(widget)
app = QApplication(sys.argv) # We neeed one (only one) instance per application
window = MainWindow() # create a new window
window.show()# Windows are hidden by default
app.exec_()# Start the event loop
        
        