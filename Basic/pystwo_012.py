import sys # Only needed for access to command line arguments
from PySide2.QtWidgets import QApplication, QMainWindow, QComboBox
from PySide2.QtCore import QSize
class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("My Cmb App")
        widget = QComboBox()
        widget.addItems(['One', 'Two', 'Three'])
        widget.currentIndexChanged.connect(self.index_changed)
        widget.currentTextChanged.connect(self.text_changed)

        self.setFixedSize(QSize(400, 300))  # Width / height
        self.setCentralWidget(widget)  # Set the central Widget of the Window
        
    def index_changed(self, i): #i i an int (cmb index)
        print(i)

    def text_changed(self, s): #s is a string (text from cmb)
        print(s)
app = QApplication(sys.argv)
window = MainWindow()  # create a new window
window.show()  # Windows are hidden by default
app.exec_()  # Start the event loop