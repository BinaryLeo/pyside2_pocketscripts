import sys  # Only needed for access to command line arguments
from PySide2.QtCore import QSize
from PySide2.QtWidgets import QApplication, QHBoxLayout, QLabel, QMainWindow, QWidget
from layout_colorwidget import Color


class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle('QVBox Layout')
        layout = QHBoxLayout()# Horizontal Box
        layout.addWidget(Color('#CD1D1B'))
        layout.addWidget(Color('#2BD820'))
        layout.addWidget(Color('#000FFF'))
        widget = QWidget()
        widget.setLayout(layout)
        self.setCentralWidget(widget)
        self.setFixedSize(QSize(400, 300))  # Width / height


# We neeed one (only one) instance per application
app = QApplication(sys.argv)
window = MainWindow()  # create a new window
window.show()  # Windows are hidden by default
app.exec_()  # Start the event loop
