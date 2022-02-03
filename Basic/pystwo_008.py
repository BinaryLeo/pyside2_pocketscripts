# pip3 install pyside2
from PySide2.QtWidgets import QApplication,QMainWindow,QPushButton
# The handler (QApplication) and a basic empty GUI widget with a
# QMainWindow and a single push-able button (QPushButton)
from PySide2.QtCore import Qt, QSize

import sys # Only needed for access to comand line arguments 
from random import choice
#A list of window titles we’ll select from using random.choice()
window_titles = ['My App','New Title','Another Title','Something went wrong']

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.n_times_clicked = 0
        self.setWindowTitle('My App')
        self.button = QPushButton('Click me!')
        
        self.setFixedSize(QSize(400,300)) # Width / height
        #  maximize control is disabled on Windows & Linux
        
        self.button.clicked.connect(self.the_button_was_clicked)
        
        #Hook up our custom slot method the_window_title_changed to the windows
        #.windowTitleChanged signal.
        self.windowTitleChanged.connect(self.the_window_title_changed)
        
        # Set the central Widget of the Window
        self.setCentralWidget(self.button) 
        
    def the_button_was_clicked(self): #Change the Window Title
        print('Clicked')
        new_window_title = choice(window_titles)
        print('Setting title: %s' % new_window_title)
        self.setWindowTitle(new_window_title)
    def the_window_title_changed(self, window_title):
        print('Window title changed: %s'% window_title)
        if window_title =='Something went wrong':
            self.button.setDisabled(True)  
app = QApplication(sys.argv)# We neeed one (only one) instance per application
window = MainWindow()# create a new window (A QMainWindow)
window.show()# Windows are hidden by default
app.exec_()# Start the event loop     
