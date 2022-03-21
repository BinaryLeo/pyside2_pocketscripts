import sys
from PySide2.QtCore import QSize, Qt
from PySide2.QtWidgets import (
   QApplication, QLabel, QMainWindow, QPushButton, QTabWidget, QWidget, QToolBar, QAction
)
class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Toolbar button")
        self.setFixedSize(QSize(400, 300))
        label = QLabel("Hello!")
        label.setAlignment(Qt.AlignCenter)
        self.setCentralWidget(label)
        toolbar = QToolBar("My main toolbar")
        self.addToolBar(toolbar)

        button_action = QAction("Button", self)
        button_action.setStatusTip("Click to show a message box")
        button_action.triggered.connect(self.onMyToolBarButtonClick)
        toolbar.addAction(button_action)

    def onMyToolBarButtonClick(self, s):
        print("click", s)

    # The signal passed indicates whether the action is checked,and since our button is not checkable — just clickable — it is
    #always false.
# We neeed one (only one) instance per application
app = QApplication(sys.argv)
window = MainWindow()  # create a new window
window.show()  # Windows are hidden by default
app.exec_()  # Start the event loop