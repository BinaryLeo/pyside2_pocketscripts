# pip3 install pyside2
import sys # Only needed for access to command line arguments
from PySide2.QtCore import Qt, QSize
from PySide2.QtWidgets import QApplication, QMainWindow, QSlider

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle('QSlider')
        self.setFixedSize(QSize(400, 300))  # Width / height
        widget = QSlider()
        widget.setMinimum(-10)
        widget.setMaximum(3)
        # Or: widget.setRange(-10,3)
        widget.setSingleStep(3)

        widget.valueChanged.connect(self.value_changed)
        widget.sliderMoved.connect(self.slider_position)
        widget.sliderPressed.connect(self.slider_pressed)
        widget.sliderReleased.connect(self.slider_released)

        self.setCentralWidget(widget)
        #Set the central Widget of the window
    def value_changed(self,i):
        print(i)
    def slider_position(self,p):
        print('position', p)
    def slider_pressed(self):
        print('Pressed') 
    def slider_released(self):
        print('Released')
app = QApplication(sys.argv) # We neeed one (only one) instance per application
window = MainWindow() # create a new window
window.show()  # Windows are hidden by default
app.exec_() # Start the event loop     



#Config
#Vertical -> widget.QSlider(Qt.Vertical)
#Horizontal -> widget.QSlider(Qt.Horizontal)