import sys
from PyQt5.QtWidgets import QApplication, QMainWindow, QLabel, QPushButton, QTextEdit
from PyQt5.QtCore import *
from PyQt5.QtGui import *
import utils as utl
from functools import partial


class MainWindow(QMainWindow):

    def __init__(self, *args, **kwargs):
        super(MainWindow, self).__init__(*args, **kwargs)

        # Main Style
        self.setWindowTitle("VoiceGrab-0.01")
        self.setStyleSheet("background-color: rgb(200,200,200)")

        # Widget Initialization

        # Main head
        self.head = QLabel("Voice Grab")
        self.head.setStyleSheet("background-color: rgb(80,80,80);"
                                "border: 4px solid white;"
                                "border-radius: 8px;"
                                "font: 40px;"
                                "color: white;"
                                )
        self.head.setAlignment(Qt.AlignCenter)

        # Push Buttons
        self.button = [QPushButton("Client 1"), QPushButton("Client 2"), QPushButton("Client 3"),
                       QPushButton("Client 4")]

        for n in range(4):
            self.button[n].setStyleSheet("QPushButton {background-color: rgb(170,170,170);"
                                         "border: 2px solid white;"
                                         "border-radius: 7px;"
                                         "font: 20px;}"
                                         "QPushButton:pressed {background-color: rgb(100,100,100);}")

        # Text Edits
        self.tedit = [QTextEdit("Name 1"), QTextEdit("Name 2"), QTextEdit("Name 3"), QTextEdit("Name 4")]
        for n in range(4):
            self.tedit[n].setStyleSheet("background-color: rgb(250,250,250);"
                                        "border: 2px solid white;"
                                        "border-radius: 7px;"
                                        "font: 20px;}")

        # Message Label
        self.mes = QLabel("Message Box")
        self.mes.setStyleSheet("background-color: rgb(220,220,220);"
                               "border: 4px solid white;"
                               "border-radius: 8px;"
                               "font: 40px;"
                               )
        self.mes.setAlignment(Qt.AlignCenter)

        # Lamp Labels
        self.lamp = [QLabel("1"), QLabel("2"), QLabel("3"), QLabel("4")]
        for n in range(4):
            self.lamp[n].setStyleSheet("background-color: rgb(100,100,100);"
                                       "color: white;"
                                       "border: 4px solid white;"
                                       "border-radius: 25px;"
                                       "font: 30px;"
                                       )
            self.lamp[n].setAlignment(Qt.AlignCenter)

        # Start Button
        self.start = QPushButton("Start")
        self.start.setStyleSheet("QPushButton {background-color: rgb(80,80,80);"
                                 "border: 2px solid white;"
                                 "border-radius: 7px;"
                                 "font: 20px;"
                                 "color: white;}"
                                 "QPushButton:pressed {background-color: rgb(100,100,100);}")

        # Stop Button
        self.stop = QPushButton("Stop")
        self.stop.setStyleSheet("QPushButton {background-color: rgb(80,80,80);"
                                "border: 2px solid white;"
                                "border-radius: 7px;"
                                "font: 20px;"
                                "color: white;}"
                                "QPushButton:pressed {background-color: rgb(100,100,100);}")

        # Widget Resize and Location
        self.head.resize(600, 100)
        self.head.move(50, 10)
        for n in range(4):
            self.button[n].resize(100, 50)
            self.button[n].move(550, 60 + (n + 1) * 80)
            self.tedit[n].resize(450, 50)
            self.tedit[n].move(50, 60 + (n + 1) * 80)
            self.lamp[n].resize(50, 50)
            self.lamp[n].move(100 + 150 * n, 620)
        self.mes.resize(450, 120)
        self.mes.move(50, 460)
        self.start.resize(100, 50)
        self.start.move(550, 460)
        self.stop.resize(100, 50)
        self.stop.move(550, 530)

        # Widget Parenting
        self.head.setParent(self)
        for n in range(4):
            self.button[n].setParent(self)
            self.tedit[n].setParent(self)
            self.lamp[n].setParent(self)
        self.mes.setParent(self)
        self.start.setParent(self)
        self.stop.setParent(self)

        # Widget Connect
        self.button[0].clicked.connect(utl.client1)
        self.button[1].clicked.connect(utl.client2)
        self.button[2].clicked.connect(utl.client3)
        self.button[3].clicked.connect(utl.client4)
        self.start.clicked.connect(utl.start)
        self.stop.clicked.connect(utl.stop)


if __name__ == "__main__":
    app = QApplication(sys.argv)
    w = MainWindow()
    w.resize(700, 700)
    w.show()
    sys.exit(app.exec_())
