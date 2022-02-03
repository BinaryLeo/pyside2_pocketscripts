# pip3 install pyside2

from PySide2.QtWidgets import QApplication, QPushButton
# The handler (QApplication) and a basic empty GUI widget with a single 
# push-able button (QPushButton).

import sys # Only needed for access to command line arguments 

app = QApplication(sys.argv)
#We neeed one (only one) instance per application
window = QPushButton('Push me plz') # create a new window (A QWidget)
window.show() # Windows are hidden by default
app.exec_()# Start the event loop
