import sys
from PyQt5.QtWidgets import QApplication,QLabel,QMainWindow
from PyQt5.QtGui import QFont,QPixmap



class Mainwindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setGeometry(700,300,500,500)
        self.setWindowTitle("PyQt5 window")
        label=QLabel("hello world!",self)
        label.setFont(QFont("Arial",10))
        label.setGeometry(0,0,500,100)
        
        label.setStyleSheet("color:blue;"
                            "font-weight:bold;"
                            "background-color:yellow;"
                            "font-size:50px;"
                            )
        label1=QLabel(self)
        pixmap=QPixmap("img.jpg")
        label1.setGeometry(0,0,250,250)
        label1.setPixmap(pixmap)
        label1.move(200,200)
        


    
def main():
    app=QApplication(sys.argv) 
    window=Mainwindow()
    window.show()
    sys.exit(app.exec_())
if __name__=="__main__":
    main()
   

