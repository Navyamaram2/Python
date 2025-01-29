import sys
from PyQt5.QtWidgets import QApplication, QLabel, QVBoxLayout, QWidget
from PyQt5.QtCore import QTimer, QTime, Qt

class DigitalClock(QWidget):
    def __init__(self):
        super().__init__()
        self.time_Label = QLabel(self)
        self.timer = QTimer(self)

        self.initUI()

    def initUI(self):
        self.setWindowTitle("Digital Clock")
        self.setGeometry(600, 400, 300, 300)

        # Set alignment and styling for the time label
        self.time_Label.setAlignment(Qt.AlignCenter)
        self.time_Label.setStyleSheet(
            "font-size: 100px;"
            "color: blue;"
            "font-weight: bold;"
            "font-family:monospace;"
        )

        # Set the layout
        vbox = QVBoxLayout()
        vbox.addWidget(self.time_Label)
        self.setLayout(vbox)

        # Start the timer and connect it to the update method
        self.timer.timeout.connect(self.Update_time)
        self.timer.start(1000)  # Trigger every second

        self.Update_time()  # Set the initial time
        self.setStyleSheet("background-color:black;")

    def Update_time(self):
        # Get the current time in 12-hour format with AM/PM
        current_time = QTime.currentTime().toString("hh:mm:ss ap")
        self.time_Label.setText(current_time)

if __name__ == "__main__":
    app = QApplication(sys.argv)
    clock = DigitalClock()
    clock.show()
    sys.exit(app.exec_())
