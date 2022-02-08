# pip3 install pyside2
import sys # Only needed for access to command line arguments
from PySide2.QtGui import QPixmap # Using QLabel we can  display an image (SetPixmap)
from PySide2.QtCore import QSize 
from PySide2.QtWidgets import QApplication, QLabel, QMainWindow
class MainWindow(QMainWindow):
  def __init__(self):
      super().__init__()
      self.setWindowTitle("My App")
      widget = QLabel("Hello")
      widget.setPixmap(QPixmap('./resources/cat.jpg')) #resources
      widget.setScaledContents(True) # stretch and scale to fit when is True
      self.setFixedSize(QSize(400,300)) # Width / height
      self.setCentralWidget(widget)# Set the central Widget of the Window
app = QApplication(sys.argv)# We neeed one (only one) instance per application
window = MainWindow()# create a new window
window.show() # Windows are hidden by default
app.exec_() # Start the event loop
