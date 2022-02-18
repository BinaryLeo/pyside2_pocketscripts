# pip3 install pyside2
import sys
from PySide2.QtCore import Qt, QSize
from PySide2.QtWidgets import QApplication, QMainWindow , QSpinBox

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle('QT SpinBox')
        self.setFixedSize(QSize(400, 300))  # Width / height
        widget = QSpinBox()
        # Or: widget = QDoubleSpinBox() 
        widget.setMinimum(-10)
        widget.setMaximum(3)
        # Or: widget.setRange(-10,3)

        widget.setPrefix('$')
        widget.setSuffix('c')
        widget.setSingleStep(3)
        # Or: e.g 0.5 for QDoubleSpinBox
        widget.valueChanged.connect(self.valueChanged)
        widget.valueChanged[str].connect(self.valueChanged_str)
        self.setCentralWidget(widget)
        #Set the central Widget of the window

    def valueChanged(self,i):
        print(i)
    def valueChanged_str(self,s):
        print(s)
app = QApplication(sys.argv) # We neeed one (only one) instance per application
window = MainWindow() # create a new window
window.show()# Windows are hidden by default
app.exec_()# Start the event loop        
