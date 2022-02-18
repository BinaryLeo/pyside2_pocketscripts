# pip3 install pyside2
import sys  # Only needed for access to command line arguments
from PySide2.QtWidgets import QApplication, QMainWindow, QCheckBox
# The handler (QApplication) and a basic empty GUI widget with a combobox
from PySide2.QtCore import QSize, Qt


class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("My App")
        widget = QCheckBox("This is a checkbox")
        widget.setCheckState(Qt.Checked)
        widget.stateChanged.connect(self.show_state)
        self.setFixedSize(QSize(400, 300))  # Width / height
        self.setCentralWidget(widget)  # Set the central Widget of the Window

    def show_state(self, s):
        print(s == Qt.Checked)
        print(s)


# We neeed one (only one) instance per application
app = QApplication(sys.argv)
window = MainWindow()  # create a new window
window.show()  # Windows are hidden by default
app.exec_()  # Start the event loop
