# pip3 install pyside2

from PySide2.QtWidgets import QApplication, QWidget 
# The handler (QApplication) and a basic empty GUI widget (QWidget)
import sys #Only needed for access to command line arguments

app = QApplication(sys.argv)
# We neeed one (only one) instance (QApplication) per application

window = QWidget() # create a new window (A QWidget)
window.show() # Windows are hidden by default
app.exec_() # Start the event loop
