
import sys
import numpy as np
import pandas as pd
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from PyQt5.QtCore import *
from PyQt5 import QtTest
from matplotlib.backends.backend_qt4agg import FigureCanvasQTAgg as FigureCanvas
from matplotlib.figure import Figure
# Imported required libraries


# Creating class for main app window from PyQT
class App(QMainWindow):
    # Initialization class with title and initUI
    def __init__(self):
        super().__init__()

        self.title = "AoE2 Log Save Display - 0.0.1"
        self.initUI()

    def initUI(self):
        # Defining window title
        self.setWindowTitle(self.title)
        # Defining timers for further use
        self.timer = QTimer(self)
        self.timerp = QTimer(self)
        self.timero = QTimer(self)
        # Defining a class variable n form live plot iteration
        self.n = 0
        # Defining a pause cut class variable
        self.cut = False
        # Defining line select boolean array to determine displayed data lines
        self.select = [True] * 8
        # Creating empty scores array for assign of log data
        self.scores = np.empty(0)
        # Creating empty time array to use with score data with later assign
        self.time1 = np.empty(0)
        # Creating empty array of data frame for later assign
        self.df = np.empty(0)
        # Creating empty array of unique player names for later assign
        self.unq = np.empty(0)

        # Creating objects of labels for player names
        self.p1Label = QLabel("Player 1", self)
        self.p2Label = QLabel("Player 2", self)
        self.p3Label = QLabel("Player 3", self)
        self.p4Label = QLabel("Player 4", self)
        self.p5Label = QLabel("Player 5", self)
        self.p6Label = QLabel("Player 6", self)
        self.p7Label = QLabel("Player 7", self)
        self.p8Label = QLabel("Player 8", self)

        # Setting player name labels font type and size
        self.p1Label.setFont(QFont('Arial font', 20))
        self.p2Label.setFont(QFont('Arial font', 20))
        self.p3Label.setFont(QFont('Arial font', 20))
        self.p4Label.setFont(QFont('Arial font', 20))
        self.p5Label.setFont(QFont('Arial font', 20))
        self.p6Label.setFont(QFont('Arial font', 20))
        self.p7Label.setFont(QFont('Arial font', 20))
        self.p8Label.setFont(QFont('Arial font', 20))

        # Defining player labels' display geometry
        self.p1Label.setGeometry(0, 0, 200, 30)
        self.p2Label.setGeometry(0, 0, 200, 30)
        self.p3Label.setGeometry(0, 0, 200, 30)
        self.p4Label.setGeometry(0, 0, 200, 30)
        self.p5Label.setGeometry(0, 0, 200, 30)
        self.p6Label.setGeometry(0, 0, 200, 30)
        self.p7Label.setGeometry(0, 0, 200, 30)
        self.p8Label.setGeometry(0, 0, 200, 30)

        # Positioning player name labels
        self.p1Label.move(40, 130)
        self.p2Label.move(40, 230)
        self.p3Label.move(40, 330)
        self.p4Label.move(40, 430)
        self.p5Label.move(40, 530)
        self.p6Label.move(40, 630)
        self.p7Label.move(40, 730)
        self.p8Label.move(40, 830)

        # Defining players' display check buttons
        self.player1Btn = QPushButton(self)
        self.player2Btn = QPushButton(self)
        self.player3Btn = QPushButton(self)
        self.player4Btn = QPushButton(self)
        self.player5Btn = QPushButton(self)
        self.player6Btn = QPushButton(self)
        self.player7Btn = QPushButton(self)
        self.player8Btn = QPushButton(self)

        # Defining display geometry of player check buttons
        self.player1Btn.setGeometry(200, 150, 50, 50)
        self.player2Btn.setGeometry(200, 150, 50, 50)
        self.player3Btn.setGeometry(200, 150, 50, 50)
        self.player4Btn.setGeometry(200, 150, 50, 50)
        self.player5Btn.setGeometry(200, 150, 50, 50)
        self.player6Btn.setGeometry(200, 150, 50, 50)
        self.player7Btn.setGeometry(200, 150, 50, 50)
        self.player8Btn.setGeometry(200, 150, 50, 50)

        # Defining player check buttons shape and background color
        self.player1Btn.setStyleSheet("border-radius : 25; border: 5px solid black; background-color: #c0c0c0")
        self.player2Btn.setStyleSheet("border-radius : 25; border: 5px solid black; background-color: #c0c0c0")
        self.player3Btn.setStyleSheet("border-radius : 25; border: 5px solid black; background-color: #c0c0c0")
        self.player4Btn.setStyleSheet("border-radius : 25; border: 5px solid black; background-color: #c0c0c0")
        self.player5Btn.setStyleSheet("border-radius : 25; border: 5px solid black; background-color: #c0c0c0")
        self.player6Btn.setStyleSheet("border-radius : 25; border: 5px solid black; background-color: #c0c0c0")
        self.player7Btn.setStyleSheet("border-radius : 25; border: 5px solid black; background-color: #c0c0c0")
        self.player8Btn.setStyleSheet("border-radius : 25; border: 5px solid black; background-color: #c0c0c0")

        # Positioning player check buttons' locations
        self.player1Btn.move(280, 120)
        self.player2Btn.move(280, 220)
        self.player3Btn.move(280, 320)
        self.player4Btn.move(280, 420)
        self.player5Btn.move(280, 520)
        self.player6Btn.move(280, 620)
        self.player7Btn.move(280, 720)
        self.player8Btn.move(280, 820)

        # Assigning relevant methods to player check buttons
        self.player1Btn.clicked.connect(self.playersel1)
        self.player2Btn.clicked.connect(self.playersel2)
        self.player3Btn.clicked.connect(self.playersel3)
        self.player4Btn.clicked.connect(self.playersel4)
        self.player5Btn.clicked.connect(self.playersel5)
        self.player6Btn.clicked.connect(self.playersel6)
        self.player7Btn.clicked.connect(self.playersel7)
        self.player8Btn.clicked.connect(self.playersel8)

        # File open button definition
        self.openBtn = QPushButton("Open File", self)
        # File open button label font and size configuration
        self.openBtn.setFont(QFont("Arial font", 30))
        # File open button geometry configuration
        self.openBtn.setGeometry(200, 150, 300, 200)
        # File open button button style configuration
        self.openBtn.setStyleSheet("border-radius : 75; border: 5px solid black; background-color: #ff9933")
        # Positioning open file button
        self.openBtn.move(1600, 200)
        # Assigning method for file open button
        self.openBtn.clicked.connect(self.opencall)

        # Creating plot canvas object for plot
        self.m = PlotCanvas(self, width=12, height=6)
        # Initial plot with null values with legend
        self.m.plot(self.time1, self.scores, self.unq)
        # Positioning plot frame
        self.m.move(350, 100)

        # GUI title configuration with previous steps
        title = QLabel("                   Age of Empires 2 - Saved Log Displayer", self)
        title.setFont(QFont('Arial font', 40))
        title.setGeometry(0, 0, 2000, 100)
        title.setStyleSheet("background-color:#ffb266")
        title.move(0, 0)

        # Defining play/pause button with previous steps
        self.playBtn = QPushButton("PLAY", self)
        self.playBtn.setFont(QFont("Arial font", 15))
        self.playBtn.setGeometry(200, 150, 100, 100)
        self.playBtn.setStyleSheet("border-radius : 50; border: 5px solid black; background-color: #ff9933")
        self.playBtn.move(525, 750)
        self.playBtn.clicked.connect(self.playpause)

        # Defining 2x 4x 16x buttons with previous steps
        self.twoBtn = QPushButton("2X", self)
        self.twoBtn.setFont(QFont("Arial font", 15))
        self.twoBtn.setGeometry(200, 150, 100, 100)
        self.twoBtn.setStyleSheet("border-radius : 50; border: 5px solid black; background-color: #ff9933")
        self.twoBtn.move(725, 750)
        self.twoBtn.clicked.connect(self.twotimes)

        self.fourBtn = QPushButton("4X", self)
        self.fourBtn.setFont(QFont("Arial font", 15))
        self.fourBtn.setGeometry(200, 150, 100, 100)
        self.fourBtn.setStyleSheet("border-radius : 50; border: 5px solid black; background-color: #ff9933")
        self.fourBtn.move(925, 750)
        self.fourBtn.clicked.connect(self.fourtimes)

        self.sixBtn = QPushButton("16X", self)
        self.sixBtn.setFont(QFont("Arial font", 15))
        self.sixBtn.setGeometry(200, 150, 100, 100)
        self.sixBtn.setStyleSheet("border-radius : 50; border: 5px solid black; background-color: #ff9933")
        self.sixBtn.move(1125, 750)
        self.sixBtn.clicked.connect(self.sixtimes)

        self.resBtn = QPushButton("RESET", self)
        self.resBtn.setFont(QFont("Arial font", 15))
        self.resBtn.setGeometry(200, 150, 100, 100)
        self.resBtn.setStyleSheet("border-radius : 50; border: 5px solid black; background-color: #ff9933")
        self.resBtn.move(1325, 750)
        self.resBtn.clicked.connect(self.rescall)

        # Creating null labels for GUI style with previous steps
        self.styleL1 = QLabel("", self)
        self.styleL1.setGeometry(100, 100, 10, 900)
        self.styleL1.setStyleSheet("border: 2px solid black; background-color: #c0c0c0")
        self.styleL1.move(350, 100)

        self.styleL2 = QLabel("", self)
        self.styleL2.setGeometry(100, 100, 10, 900)
        self.styleL2.setStyleSheet("border: 2px solid black; background-color: #c0c0c0")
        self.styleL2.move(1550, 100)

        self.styleL3 = QLabel("", self)
        self.styleL3.setGeometry(100, 100, 2000, 10)
        self.styleL3.setStyleSheet("border: 2px solid black; background-color: #c0c0c0")
        self.styleL3.move(0, 100)

        self.styleL4 = QLabel("", self)
        self.styleL4.setGeometry(100, 100, 1194, 10)
        self.styleL4.setStyleSheet("border: 2px solid black; background-color: #c0c0c0")
        self.styleL4.move(358, 700)

        # Displaying all widgets
        title.show()
        self.playBtn.show()
        self.twoBtn.show()
        self.fourBtn.show()
        self.sixBtn.show()
        self.resBtn.show()
        self.player1Btn.show()
        self.player2Btn.show()
        self.player3Btn.show()
        self.player4Btn.show()
        self.player5Btn.show()
        self.player6Btn.show()
        self.player7Btn.show()
        self.player8Btn.show()
        self.p1Label.show()
        self.p2Label.show()
        self.p3Label.show()
        self.p4Label.show()
        self.p5Label.show()
        self.p6Label.show()
        self.p7Label.show()
        self.p8Label.show()
        self.openBtn.show()
        self.styleL1.show()
        self.styleL2.show()
        self.styleL3.show()
        self.styleL4.show()

        # Defining window open up size as maximized
        self.showMaximized()

    def playpause(self):
        # Defining time interval for 1x as 100 ms
        self.pace = 100
        # Play/pause switch conditional block. Configures color and label name
        if self.playBtn.text() == "PLAY":
            self.playBtn.setText("PAUSE")
            self.playBtn.setStyleSheet("border-radius : 50; border: 5px solid black; background-color: #80ff00")
            self.cut = False  # Pause value is falsified
            self.animate(self.scores, self.pace)  # animate method for live plot with acquired data
        else:
            self.playBtn.setText("PLAY")  # From play to pause texture switch
            self.playBtn.setStyleSheet("border-radius : 50; border: 5px solid black; background-color: #ff9933")
            self.twoBtn.setStyleSheet("border-radius : 50; border: 5px solid black; background-color: #ff9933")
            self.fourBtn.setStyleSheet("border-radius : 50; border: 5px solid black; background-color: #ff9933")
            self.sixBtn.setStyleSheet("border-radius : 50; border: 5px solid black; background-color: #ff9933")
            self.cut = True  # Pause value is affirmed

    # Same procedure for 2x, 4x and 16x with turn to 1x addition on second press
    def twotimes(self):

        if self.playBtn.text() == "PAUSE":
            self.pace = 100 / 2

            if self.twoBtn.palette().color(QPalette.Background) == QColor("#ff9933"):
                self.twoBtn.setStyleSheet("border-radius : 50; border: 5px solid black; background-color: #80ff00")
                self.fourBtn.setStyleSheet("border-radius : 50; border: 5px solid black; background-color: #ff9933")
                self.sixBtn.setStyleSheet("border-radius : 50; border: 5px solid black; background-color: #ff9933")
                self.cut = False
                self.animate(self.scores, self.pace)
            else:
                self.twoBtn.setStyleSheet("border-radius : 50; border: 5px solid black; background-color: #ff9933")
                self.pace = 100
                self.animate(self.scores, self.pace)

    def fourtimes(self):

        if self.playBtn.text() == "PAUSE":
            self.pace = 100 / 4

            if self.fourBtn.palette().color(QPalette.Background) == QColor("#ff9933"):
                self.fourBtn.setStyleSheet("border-radius : 50; border: 5px solid black; background-color: #80ff00")
                self.twoBtn.setStyleSheet("border-radius : 50; border: 5px solid black; background-color: #ff9933")
                self.sixBtn.setStyleSheet("border-radius : 50; border: 5px solid black; background-color: #ff9933")
                self.cut = False
                self.animate(self.scores, self.pace)
            else:
                self.fourBtn.setStyleSheet("border-radius : 50; border: 5px solid black; background-color: #ff9933")
                self.pace = 100
                self.animate(self.scores, self.pace)

    def sixtimes(self):

        if self.playBtn.text() == "PAUSE":
            self.pace = 100 / 16

            if self.sixBtn.palette().color(QPalette.Background) == QColor("#ff9933"):
                self.sixBtn.setStyleSheet("border-radius : 50; border: 5px solid black; background-color: #80ff00")
                self.twoBtn.setStyleSheet("border-radius : 50; border: 5px solid black; background-color: #ff9933")
                self.fourBtn.setStyleSheet("border-radius : 50; border: 5px solid black; background-color: #ff9933")
                self.cut = False
                self.animate(self.scores, self.pace)
            else:
                self.sixBtn.setStyleSheet("border-radius : 50; border: 5px solid black; background-color: #ff9933")
                self.pace = 100
                self.animate(self.scores, self.pace)

    # File open method
    def opencall(self):
        # Creating short time style change on click for file open button
        self.openBtn.setStyleSheet("border-radius : 75; border: 5px solid black; background-color: #80ff00")
        self.timero.timeout.connect(self.resopen)
        self.timero.start(1500)
        # Getting file name
        self.filename = QFileDialog.getOpenFileName(self, caption="Open AoE2 Log File", filter="AoE2 Log Files (*.txt)")
        try:
            # Try block as assigning txt to data frame
            self.df = pd.read_csv(self.filename[0])
            # Defining Unique names of players
            self.unq = np.unique(self.df['player'])
            # Reshaping df for equal time spans
            self.df = self.df[:len(self.df) - len(self.df) % len(self.unq)]
            self.scores = np.zeros((int(len(self.df) / len(self.unq)), len(self.unq)))
            # Creating time span
            self.time1 = np.arange(0, len(self.scores) / 10, 0.1)

            # Assigning scores values to scores array with give formulation
            for n in np.arange(len(self.unq)):
                player = self.df[self.df['player'] == self.unq[n]]
                self.scores[:, n] = player['mils'] * 75 * 0.2 + player['vils'] * 50 * 0.2 + (player['food'] +
                                    player['wood'] + player['gold'] + player['stone']) * 0.2
            # Plotting data
            self.m.plot2(self.time1, self.scores, self.unq)
            # Activating player select buttons and changing label names with player names with respect to player numbers
            if len(self.unq) > 0:
                self.player1Btn.setStyleSheet("border-radius : 25; border: 5px solid black; background-color: #80ff00")
                self.p1Label.setText(self.unq[0])
            if len(self.unq) > 1:
                self.player2Btn.setStyleSheet("border-radius : 25; border: 5px solid black; background-color: #80ff00")
                self.p2Label.setText(self.unq[1])
            if len(self.unq) > 2:
                self.player3Btn.setStyleSheet("border-radius : 25; border: 5px solid black; background-color: #80ff00")
                self.p3Label.setText(self.unq[2])
            if len(self.unq) > 3:
                self.player4Btn.setStyleSheet("border-radius : 25; border: 5px solid black; background-color: #80ff00")
                self.p4Label.setText(self.unq[3])
            if len(self.unq) > 4:
                self.player5Btn.setStyleSheet("border-radius : 25; border: 5px solid black; background-color: #80ff00")
                self.p5Label.setText(self.unq[4])
            if len(self.unq) > 5:
                self.player6Btn.setStyleSheet("border-radius : 25; border: 5px solid black; background-color: #80ff00")
                self.p6Label.setText(self.unq[5])
            if len(self.unq) > 6:
                self.player7Btn.setStyleSheet("border-radius : 25; border: 5px solid black; background-color: #80ff00")
                self.p7Label.setText(self.unq[6])
            if len(self.unq) > 7:
                self.player8Btn.setStyleSheet("border-radius : 25; border: 5px solid black; background-color: #80ff00")
                self.p8Label.setText(self.unq[7])
        # Giving warning message box at situation of non-compatible files
        except:
            self.warn = QMessageBox()
            self.warn.setIcon(QMessageBox.Warning)
            self.warn.setText("Chosen file is not compatible")
            self.warn.setWindowTitle("Warning")
            self.warn.exec()

    def resopen(self):
        # Open file button short animation block for resetting it to initial position
        self.openBtn.setStyleSheet("border-radius : 75; border: 5px solid black; background-color: #ff9933")

    # Reset button call method
    def rescall(self):
        # Pause cut is on
        self.cut = True
        # All players are active if it is on file
        self.select = [True] * 8
        if len(self.unq) > 0:
            self.player1Btn.setStyleSheet("border-radius : 25; border: 5px solid black; background-color: #80ff00")
            self.p1Label.setText(self.unq[0])
        if len(self.unq) > 1:
            self.player2Btn.setStyleSheet("border-radius : 25; border: 5px solid black; background-color: #80ff00")
            self.p2Label.setText(self.unq[1])
        if len(self.unq) > 2:
            self.player3Btn.setStyleSheet("border-radius : 25; border: 5px solid black; background-color: #80ff00")
            self.p3Label.setText(self.unq[2])
        if len(self.unq) > 3:
            self.player4Btn.setStyleSheet("border-radius : 25; border: 5px solid black; background-color: #80ff00")
            self.p4Label.setText(self.unq[3])
        if len(self.unq) > 4:
            self.player5Btn.setStyleSheet("border-radius : 25; border: 5px solid black; background-color: #80ff00")
            self.p5Label.setText(self.unq[4])
        if len(self.unq) > 5:
            self.player6Btn.setStyleSheet("border-radius : 25; border: 5px solid black; background-color: #80ff00")
            self.p6Label.setText(self.unq[5])
        if len(self.unq) > 6:
            self.player7Btn.setStyleSheet("border-radius : 25; border: 5px solid black; background-color: #80ff00")
            self.p7Label.setText(self.unq[6])
        if len(self.unq) > 7:
            self.player8Btn.setStyleSheet("border-radius : 25; border: 5px solid black; background-color: #80ff00")
            self.p8Label.setText(self.unq[7])
        # Short color animation on button
        self.timer.timeout.connect(self.resresbtn)
        self.timer.start(1500)
        # Resetting all buttons to initial display
        self.resBtn.setStyleSheet("border-radius : 50; border: 5px solid black; background-color: #ff3333")
        self.playBtn.setStyleSheet("border-radius : 50; border: 5px solid black; background-color: #ff9933")
        self.playBtn.setText("PLAY")
        self.sixBtn.setStyleSheet("border-radius : 50; border: 5px solid black; background-color: #ff9933")
        self.twoBtn.setStyleSheet("border-radius : 50; border: 5px solid black; background-color: #ff9933")
        self.fourBtn.setStyleSheet("border-radius : 50; border: 5px solid black; background-color: #ff9933")
        self.sixBtn.setStyleSheet("border-radius : 50; border: 5px solid black; background-color: #ff9933")
        # Draw initial plot
        self.m.plot2(self.time1, self.scores, self.unq)
        # Iterative number for animation becomes zero
        self.n = 0
        # Live stream speed reset to 1x
        self.pace = 100

    # Switch of mini animation over reset button
    def resresbtn(self):
        # Turning back to initial button style
        self.resBtn.setStyleSheet("border-radius : 50; border: 5px solid black; background-color: #ff9933")

    # Defining a stream plot method to plot data up to iterative number
    def streamplot(self):

        self.m.plot2(self.time1[:self.n],
                     np.compress(self.select[:len(self.unq)], self.scores[:self.n, :], axis=1),
                     np.compress(self.select[:len(self.unq)], self.unq))

    def animate(self, data, msec):
        # animate method to plot n points of data up to length of data
        while self.n < len(data):
            self.streamplot()
            QtTest.QTest.qWait(msec)  # This defines the speed as waiting interval
            if self.cut == True:  # Cutting the stream on pause or reset
                break
            self.n = self.n + 1  # Iterative number incrementation

    # From player 1 to 8 defining button check bind methods
    def playersel1(self):

        if len(self.unq) > 0:  # To be sure that there is a player loaded
            if self.player1Btn.palette().color(QPalette.Background) == QColor("#80ff00"):  # By color condition
                if sum(self.select[:len(self.unq)]) != 1:  # If not checked alone
                    self.player1Btn.setStyleSheet("border-radius : 25; border: 5px solid black; background-color: #c0c0c0")
                    self.select[0] = False # Deactive and change color
            else:
                self.player1Btn.setStyleSheet("border-radius : 25; border: 5px solid black; background-color: #80ff00")
                self.select[0] = True  # Switch to counterpart active mode
        if self.playBtn.text() == "PLAY":  # On live mode continue the plot with new player select
            self.m.plot2(self.time1, np.compress(self.select[:len(self.unq)], self.scores, axis=1),
                         np.compress(self.select[:len(self.unq)], self.unq))

    def playersel2(self):

        if len(self.unq) > 1:
            if self.player2Btn.palette().color(QPalette.Background) == QColor("#80ff00"):
                if sum(self.select[:len(self.unq)]) != 1:
                    self.player2Btn.setStyleSheet("border-radius : 25; border: 5px solid black; background-color: #c0c0c0")
                    self.select[1] = False
            else:
                self.player2Btn.setStyleSheet("border-radius : 25; border: 5px solid black; background-color: #80ff00")
                self.select[1] = True
            if self.playBtn.text() == "PLAY":
                self.m.plot2(self.time1, np.compress(self.select[:len(self.unq)], self.scores, axis=1),
                             np.compress(self.select[:len(self.unq)], self.unq))

    def playersel3(self):

        if len(self.unq) > 2:
            if self.player3Btn.palette().color(QPalette.Background) == QColor("#80ff00"):
                if sum(self.select[:len(self.unq)]) != 1:
                    self.player3Btn.setStyleSheet("border-radius : 25; border: 5px solid black; background-color: #c0c0c0")
                    self.select[2] = False
            else:
                self.player3Btn.setStyleSheet("border-radius : 25; border: 5px solid black; background-color: #80ff00")
                self.select[2] = True
            if self.playBtn.text() == "PLAY":
                self.m.plot2(self.time1, np.compress(self.select[:len(self.unq)], self.scores, axis=1),
                             np.compress(self.select[:len(self.unq)], self.unq))

    def playersel4(self):

        if len(self.unq) > 3:
            if self.player4Btn.palette().color(QPalette.Background) == QColor("#80ff00"):
                if sum(self.select[:len(self.unq)]) != 1:
                    self.player4Btn.setStyleSheet("border-radius : 25; border: 5px solid black; background-color: #c0c0c0")
                    self.select[3] = False
            else:
                self.player4Btn.setStyleSheet("border-radius : 25; border: 5px solid black; background-color: #80ff00")
                self.select[3] = True
            if self.playBtn.text() == "PLAY":
                self.m.plot2(self.time1, np.compress(self.select[:len(self.unq)], self.scores, axis=1),
                             np.compress(self.select[:len(self.unq)], self.unq))

    def playersel5(self):

        if len(self.unq) > 4:
            if self.player5Btn.palette().color(QPalette.Background) == QColor("#80ff00"):
                if sum(self.select[:len(self.unq)]) != 1:
                    self.player5Btn.setStyleSheet("border-radius : 25; border: 5px solid black; background-color: #c0c0c0")
                    self.select[4] = False
            else:
                self.player5Btn.setStyleSheet("border-radius : 25; border: 5px solid black; background-color: #80ff00")
                self.select[4] = True
            if self.playBtn.text() == "PLAY":
                self.m.plot2(self.time1, np.compress(self.select[:len(self.unq)], self.scores, axis=1),
                             np.compress(self.select[:len(self.unq)], self.unq))

    def playersel6(self):

        if len(self.unq) > 5:
            if self.player6Btn.palette().color(QPalette.Background) == QColor("#80ff00"):
                if sum(self.select[:len(self.unq)]) != 1:
                    self.player6Btn.setStyleSheet("border-radius : 25; border: 5px solid black; background-color: #c0c0c0")
                    self.select[5] = False
            else:
                self.player6Btn.setStyleSheet("border-radius : 25; border: 5px solid black; background-color: #80ff00")
                self.select[5] = True
            if self.playBtn.text() == "PLAY":
                self.m.plot2(self.time1, np.compress(self.select[:len(self.unq)], self.scores, axis=1),
                             np.compress(self.select[:len(self.unq)], self.unq))

    def playersel7(self):

        if len(self.unq) > 6:
            if self.player7Btn.palette().color(QPalette.Background) == QColor("#80ff00"):
                if sum(self.select[:len(self.unq)]) != 1:
                    self.player7Btn.setStyleSheet("border-radius : 25; border: 5px solid black; background-color: #c0c0c0")
                    self.select[6] = False
            else:
                self.player7Btn.setStyleSheet("border-radius : 25; border: 5px solid black; background-color: #80ff00")
                self.select[6] = True
            if self.playBtn.text() == "PLAY":
                self.m.plot2(self.time1, np.compress(self.select[:len(self.unq)], self.scores, axis=1),
                             np.compress(self.select[:len(self.unq)], self.unq))

    def playersel8(self):

        if len(self.unq) > 7:
            if self.player8Btn.palette().color(QPalette.Background) == QColor("#80ff00"):
                if sum(self.select[:len(self.unq)]) != 1:
                    self.player8Btn.setStyleSheet("border-radius : 25; border: 5px solid black; background-color: #c0c0c0")
                    self.select[7] = False
            else:
                self.player8Btn.setStyleSheet("border-radius : 25; border: 5px solid black; background-color: #80ff00")
                self.select[7] = True
            if self.playBtn.text() == "PLAY":
                self.m.plot2(self.time1, np.compress(self.select[:len(self.unq)], self.scores, axis=1),
                             np.compress(self.select[:len(self.unq)], self.unq))


#  Plot canvas class for main plot area
class PlotCanvas(FigureCanvas):
    # Initialization of canvas
    def __init__(self, parent=None, width=600, height=400, dpi=100):
        fig = Figure(figsize=(width, height), dpi=dpi)
        fig.set_facecolor((229 / 255, 1, 204 / 255))
        FigureCanvas.__init__(self, fig)
        self.setParent(parent)
        FigureCanvas.updateGeometry(self)

    def plot(self, x, y, leg):
        # Basic plot method with y axis (horizontal) grids and some style configurations
        self.ax = self.figure.add_subplot(111)
        self.ax.set_facecolor((1, 254 / 255, 153 / 255))
        self.ax.grid(axis='y')
        self.ax.set_title('Scores of Players over Time')
        self.ax.set_xlabel('Time(s)')
        self.ax.set_ylabel('Score')
        self.ax.plot(x, y)
        self.ax.tick_params(labelcolor='tab:orange')
        self.ax.legend(leg)
        self.draw()

    def plot2(self, x, y, leg):
        # Same method for out of initial phase use with clear method
        self.ax.clear()
        self.ax.grid(axis='y')
        self.ax.set_title('Scores of Players over Time')
        self.ax.set_xlabel('Time(s)')
        self.ax.set_ylabel('Score')
        self.ax.plot(x, y)
        self.ax.tick_params(labelcolor='tab:orange')
        self.ax.legend(leg)
        self.draw()


# Execution of app
if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = App()
    sys.exit(app.exec_())
