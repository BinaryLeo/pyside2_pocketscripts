import sys # Only needed for access to command line arguments
from PySide2.QtCore import QSize
from PySide2.QtWidgets import QApplication, QMainWindow, QVBoxLayout,QWidget
from layout_colorwidget import Color

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle('QVBox Layout')
        layout = QVBoxLayout()
        layout.addWidget(Color('#CD1D1B'))
        widget = QWidget()
        widget.setLayout(layout)
        self.setCentralWidget(widget)
        self.setFixedSize(QSize(400, 300))# Width / height
app = QApplication(sys.argv) # We neeed one (only one) instance per application
window = MainWindow()# create a new window  
window.show()# Windows are hidden by default
app.exec_()# Start the event loop     
