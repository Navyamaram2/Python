import sys
from PyQt5.QtWidgets import QApplication,QLabel,QMainWindow,QPushButton

class Mainwindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setGeometry(700,300,500,500)
        self.setWindowTitle("PyQt5 window")
        self.initUI()
    def initUI(self):
        self.button1=QPushButton("submit",self)
        self.button1.setGeometry(150,200,200,100)
        self.button1.setStyleSheet("font-size:12px;"
                                   "color:blue;"
                                   "background-color:green;")
        self.button1.clicked.connect(self.on_click)
    def on_click(self):
        print("button is clicked")
        self.button1.setText("submitted")
        self.button1.setDisabled(True)
if __name__=="__main__":
    app=QApplication(sys.argv)
    window=Mainwindow()
    window.show()
    sys.exit(app.exec_())
