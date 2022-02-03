#pip3 install pyside2
from PySide2.QtWidgets import QApplication, QMainWindow, QPushButton
# The handler (QApplication) and a MainWindow with a single 
# push-able button (QPushButton)
 
from PySide2.QtCore import Qt
import sys #Only needed for access to comand line arguments 

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        button = QPushButton("Press me!")
        button.setCheckable(True)
        button.clicked.connect(self.the_button_was_clicked)
        
        # Set the central widget of the windows
        self.setCentralWidget(button)
        
    def the_button_was_clicked(self):
        print("Clicked")   #print a message when button is pressed 
app = QApplication(sys.argv)#We neeed one (only one) instance per application
window = MainWindow() # create a new window (A QMainWindow)
window.show()#Windows are hidden by default
app.exec_()# Start the event loop  
        
