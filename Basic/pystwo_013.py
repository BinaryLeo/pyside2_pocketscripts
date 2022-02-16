import sys  # Only needed for access to command line arguments
from PySide2.QtWidgets import QMainWindow, QApplication, QListWidget
from PySide2.QtCore import QSize

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("My List App")
        widget = QListWidget()
        widget.addItems(['One', 'Two', 'Three'])
        widget.currentItemChanged.connect(self.index_changed)
        widget.currentTextChanged.connect(self.text_changed)
        self.setFixedSize(QSize(400, 300))  # Width / height
        self.setCentralWidget(widget)  # Set the central Widget of the Window

    def index_changed(self, i): # Not an index, i is a QListItem
        print(i.text())
    def text_changed(self,s): # Not an index, i is a QListItem
        print(s)

app = QApplication(sys.argv) # We neeed one (only one) instance per application
window = MainWindow() # create a new window
window.show()  # Windows are hidden by default
app.exec_() # Start the event loop
