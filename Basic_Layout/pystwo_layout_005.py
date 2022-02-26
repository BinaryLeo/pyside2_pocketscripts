#Nest layouts for

import sys
from PySide2.QtCore import QSize
from PySide2.QtWidgets import QApplication, QHBoxLayout, QVBoxLayout, QLabel, QMainWindow, QWidget
from layout_colorwidget import Color

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle('Nest Layout')
        self.setFixedSize(QSize(400, 300))  # Width / height
        layout1 = QHBoxLayout()
        layout2 = QVBoxLayout()
        layout3 = QVBoxLayout()

        layout2.addWidget(Color('#CD1D1B'))
        layout2.addWidget(Color('#2BD820'))
        layout2.addWidget(Color('#000FFF'))

        layout1.addLayout(layout2)
        layout1.addWidget(Color('#2BD820'))
        layout3.addWidget(Color('#CD1D1B'))
        layout3.addWidget(Color('#8000FF'))

        layout1.addLayout(layout3)
        widget = QWidget()
        widget.setLayout(layout1)
        self.setCentralWidget(widget)

app = QApplication(sys.argv)# We neeed one (only one) instance per application
window = MainWindow()  # create a new window
window.show()  # Windows are hidden by default

app.exec_()  # Start the event loop