from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *


class DrawCircles(QWidget):

    def __init__(self, parent=None):
        QWidget.__init__(self, parent)
        # setGeometry(x_pos, y_pos, width, height)
        self.setGeometry(0, 0, 1960, 900)
        self.setWindowTitle('FireWithFire')
        self.label = QLabel("NO \n GODS",self)
        self.label2 = QLabel("NO \n MASTERS",self)
        self.label.move(100,100)
        self.label2.move(1960-500,100)
        self.label.setFont(QFont('Times',50))
        self.label2.setFont(QFont('Times', 50))
        self.label.setStyleSheet("background-color: white")
        self.label2.setStyleSheet("background-color: white")

    def paintEvent(self, event):
        paint = QPainter()
        paint.begin(self)

        paint.setRenderHint(QPainter.Antialiasing)
        paint.setBrush(Qt.black)
        paint.drawRect(event.rect())
        for rad in range(400,350,-1):
            radx = rad
            rady = rad
            paint.setPen(Qt.red)
            center = QPoint(1960/2, 900/2)
            paint.drawEllipse(center, radx, rady)
        for k in range(0,50,1):
            paint.drawLine(300,550-k,1960-300,550-k)
        for k in range(0,60,1):
            paint.drawLine(400+k,800,1960/2+k,10)
            paint.drawLine(1960-400-k,800,1960/2-k,10)
        paint.end()
app = QApplication([])
circles = DrawCircles()
circles.show()
app.exec_()