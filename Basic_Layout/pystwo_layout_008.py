import sys  # Only needed for access to command line arguments
from PySide2.QtWidgets import (
    QApplication, QHBoxLayout,QLabel,QMainWindow,QPushButton,QStackedLayout,QVBoxLayout,QWidget
)
from layout_colorwidget import Color
from PySide2.QtCore import QSize

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle('Stacked widget')
        self.setFixedSize(QSize(400, 300))
        pagelayout = QVBoxLayout()
        button_layout = QHBoxLayout()
        self.stacklayout = QStackedLayout()

        pagelayout.addLayout(button_layout)
        pagelayout.addLayout(self.stacklayout)

        btn = QPushButton("Red")
        btn.pressed.connect(self.activate_tab_1)
        button_layout.addWidget(btn)
        self.stacklayout.addWidget(Color('#CD1D1B'))

        btn = QPushButton("Green")
        btn.pressed.connect(self.activate_tab_2)
        button_layout.addWidget(btn)
        self.stacklayout.addWidget(Color('#2BD820'))

        btn = QPushButton("Blue")
        btn.pressed.connect(self.activate_tab_3)
        button_layout.addWidget(btn)
        self.stacklayout.addWidget(Color('#000FFF'))   

        btn = QPushButton("Yellow")
        btn.pressed.connect(self.activate_tab_4)
        button_layout.addWidget(btn)
        self.stacklayout.addWidget(Color('#FFD700'))  

        widget = QWidget()
        widget.setLayout(pagelayout)
        self.setCentralWidget(widget)

    def activate_tab_1(self):
     self.stacklayout.setCurrentIndex(0)
    def activate_tab_2(self):
     self.stacklayout.setCurrentIndex(1)
    def activate_tab_3(self):
     self.stacklayout.setCurrentIndex(2)
    def activate_tab_4(self):
     self.stacklayout.setCurrentIndex(3)              

app = QApplication(sys.argv) # We neeed one (only one) instance per application
window = MainWindow()  # create a new window
window.show()  # Windows are hidden by default
app.exec_()  # Start the event loop
