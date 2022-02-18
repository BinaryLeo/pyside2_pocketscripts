# pip3 install pyside2
import sys
from PySide2.QtCore import Qt, QSize
from PySide2.QtWidgets import QApplication, QLineEdit, QMainWindow
class MainWindow(QMainWindow):
    def __init__(self):
      super().__init__()
      self.setWindowTitle("My App")
      widget = QLineEdit()
      widget.setMaxLength(10)
      widget.setPlaceholderText("Type your text")
      # widget.setReadOnly(True) # uncomment this to make readonly
      widget.returnPressed.connect(self.return_pressed)
      widget.selectionChanged.connect(self.selection_changed)
      widget.textChanged.connect(self.text_changed)
      widget.textEdited.connect(self.text_edited)
      self.setFixedSize(QSize(400, 300))  # Width / height
      self.setCentralWidget(widget)  # Set the central Widget of the Window
    def return_pressed(self):
      print("Return pressed!")
      self.centralWidget().setText("Hellooo!")
    def selection_changed(self):
      print("Selection changed")
      print(self.centralWidget().selectedText())
    def text_changed(self, s):
          print("Text changed...")
          print(s)
    def text_edited(self,s):
          print("text edited")
          print(s)    
app = QApplication(sys.argv)# We neeed one (only one) instance per application
window = MainWindow()
window.show()# Windows are hidden by default
app.exec_()
