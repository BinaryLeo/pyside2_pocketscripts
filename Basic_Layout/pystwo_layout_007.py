import sys  # Only needed for access to command line arguments  
from PySide2.QtWidgets import QApplication, QLabel, QWidget, QMainWindow, QStackedLayout
from PySide2.QtCore import QSize

from layout_colorwidget import Color

class MainWindow(QMainWindow):
 def __init__(self):
        super().__init__()
        self.setWindowTitle('Stacked Layout')
        self.setFixedSize(QSize(400, 300))  # Width / height
        layout = QStackedLayout()
        layout.addWidget(Color('#CD1D1B'))
        layout.addWidget(Color('#2BD820'))
        layout.addWidget(Color('#000FFF'))
        layout.setCurrentIndex(2)
        widget = QWidget()
        widget.setLayout(layout)
        self.setCentralWidget(widget)
app= QApplication(sys.argv)# We neeed one (only one) instance per application
window = MainWindow()  # create a new window
window.show()  # Windows are hidden by default
app.exec_()  # Start the event loop