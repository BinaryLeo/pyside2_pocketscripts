import sys  # Only needed for access to command line arguments
from PySide2.QtCore import QSize
from PySide2.QtWidgets import (
    QApplication, QLabel,QMainWindow,QPushButton,QTabWidget,QWidget
)
from layout_colorwidget import Color

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle('Tab Apps')
        self.setFixedSize(QSize(400, 300))
        tab = QTabWidget()
        tab.setTabPosition(QTabWidget.West) # West, East, North, South
        tab.setMovable(True) # Whether tabs are setMovable with setMOveable(True)

        for n, color in enumerate(["#CD1D1B","#2BD820","#000FFF","#FFD700"]):
            tab.addTab(Color(color), "Tab {}".format(n+1))
        self.setCentralWidget(tab)

app = QApplication(sys.argv) # We neeed one (only one) instance per application
window = MainWindow()  # create a new window
window.show()  # Windows are hidden by default
app.exec_()  # Start the event loop