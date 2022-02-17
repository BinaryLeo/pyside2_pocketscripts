# pip3 install pyside2
import sys # Only needed for access to command line arguments
from PySide2.QtCore import QSize
from PySide2.QtWidgets import QApplication, QDial ,QMainWindow

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle('QDial')
        self.setFixedSize(QSize(400, 300))  # Width / height
        widget = QDial()
        self.setCentralWidget(widget)
        widget.setRange(-10,100)
        widget.setSingleStep(0.5)
        widget.valueChanged.connect(self.value_changed)
        widget.sliderMoved.connect(self.slider_position)
        widget.sliderPressed.connect(self.slider_pressed)
        widget.sliderReleased.connect(self.slider_released)
        
    def value_changed(self,i):
        print(i)
    def slider_position(self,p):
        print('position',p)
    def slider_pressed(self):
        print('pressed')
    def slider_released(self):
        print('released') 
app = QApplication(sys.argv)# We neeed one (only one) instance per application
window = MainWindow() # create a new window
window.show() # Windows are hidden by default     
app.exec_()# Start the event loop