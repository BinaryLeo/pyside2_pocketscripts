
import sys
from PySide2.QtCore import QSize
from PySide2.QtWidgets import QApplication, QGridLayout, QMainWindow, QWidget
from layout_colorwidget import Color


class MainWindow(QMainWindow):
    def __init__(self, *args, **kwargs):
        super(MainWindow, self).__init__(*args, **kwargs)
        self.setWindowTitle('Grid Layout')
        self.setFixedSize(QSize(400, 300))  # Width / height
        layout = QGridLayout()
        layout.addWidget(Color('#CD1D1B'), 0, 0)
        layout.addWidget(Color('#2BD820'), 1, 0)
        layout.addWidget(Color('#000FFF'), 1, 1)
        layout.addWidget(Color('#2BD820'), 2, 1)
        # Usefully, for QGridLayout you don’t need to fill all the positions in the grid
        widget = QWidget()
        widget.setLayout(layout)
        self.setCentralWidget(widget)


app = QApplication(sys.argv)# We neeed one (only one) instance per application
window = MainWindow()  # create a new window
window.show()  # Windows are hidden by default

app.exec_()  # Start the event loop    