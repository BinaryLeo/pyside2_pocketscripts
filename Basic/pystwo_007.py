# pip3 install pyside2
from PySide2.QtWidgets import QApplication, QMainWindow, QPushButton
# The handler (QApplication) and a basic empty GUI widget with a
# QMainWindow and a single push-able button (QPushButton)
from PySide2.QtCore import Qt, QSize
import sys # Only needed for access to comand line arguments 

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle('My App')
        self.button = QPushButton('Press me!')
        self.button.clicked.connect(self.the_button_was_clicked)
        self.setFixedSize(QSize(400,300)) 
        #  maximize control is disabled on Windows & Linux
        
        # Set the central Widget of the Window
        self.setCentralWidget(self.button)
        
    def the_button_was_clicked(self):
        self.button.setText('You alredy clicked me.')   
        self.button.setEnabled(False)
        
        #Change the Window Title
        self.setWindowTitle('My App text has changed') 
app = QApplication(sys.argv)# We neeed one (only one) instance per application
window = MainWindow()# create a new window (A QMainWindow)
window.show()# Windows are hidden by default
app.exec_()# Start the event loop    
