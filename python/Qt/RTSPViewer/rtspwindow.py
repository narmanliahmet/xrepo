import sys
from PyQt5.QtWidgets import QApplication, QMainWindow, QLabel, QPushButton, QTextEdit, QLineEdit, QFrame, \
    QSlider, QFileDialog, QMessageBox
from PyQt5 import QtTest
import vlc
from PyQt5.QtCore import *
from PyQt5.QtGui import *


class MainWindow(QMainWindow):
    # Worker for Thread

    class Worker(QObject):
        pass

    def __init__(self, *args, **kwargs):
        super(MainWindow, self).__init__(*args, **kwargs)
        # Threads

        self.thrd = QThread()
        self.worker = MainWindow.Worker()
        self.worker.moveToThread(self.thrd)
        self.thrd.started.connect(self.update)

        # Popups

        self.dial = QFileDialog()
        # Flags

        self.flag = False
        self.sflag = True
        self.lflag = False
        self.volume = 30

        # Main Style
        self.setWindowTitle("RTSPViewer-0.0.1")
        self.setStyleSheet("background-color: rgb(200,200,200)")
        # Widget Initialization

        # Main head
        self.head = QLabel("RTSP Viewer")
        self.head.setStyleSheet("background-color: rgb(80,80,80);"
                                "border: 4px solid white;"
                                "border-radius: 10px;"
                                "font: 40px;"
                                "color: white;"
                                )
        self.head.setAlignment(Qt.AlignCenter)

        # Load Text Edit and Fps, Resolution Configuration

        self.tedit = QTextEdit()
        self.tedit.setPlaceholderText("RTSP Link")
        self.tedit.setAcceptRichText(False)
        self.tedit.setStyleSheet("background-color: rgb(250,250,250);"
                                 "border: 2px solid gray;"
                                 "border-radius: 7px;"
                                 "font: 20px;}")

        self.load = QPushButton("Load")
        self.load.setStyleSheet("QPushButton {background-color: rgb(80,80,80);"
                                "border: 2px solid white;"
                                "border-radius: 7px;"
                                "font: 20px;"
                                "color: white;}"
                                "QPushButton:pressed {background-color: rgb(100,100,100);}")

        self.res = QLabel("Res(N/A)")
        self.res.setStyleSheet("background-color: rgb(80,80,80);"
                               "border: 2px solid white;"
                               "border-radius: 7px;"
                               "font: 20px;"
                               "color: white;")

        self.fpsl = QLabel("FPS")
        self.fpsl.setStyleSheet("background-color: rgb(80,80,80);"
                                "border: 2px solid white;"
                                "border-radius: 7px;"
                                "font: 20px;"
                                "color: white;"
                                )

        self.fpst = QLineEdit("30")
        self.fpst.setReadOnly(True)
        self.fpst.setAlignment(Qt.AlignCenter)
        self.fpst.setStyleSheet("background-color: rgb(250,250,250);"
                                "border: 2px solid gray;"
                                "border-radius: 7px;"
                                "font: 20px;}")
        self.fpst.setValidator(QIntValidator(1, 500, self))

        # Display Screen
        self.instance = vlc.Instance()
        self.mp = self.instance.media_player_new()

        self.stl = QLabel(self)
        self.stl.setStyleSheet("background-color: #b91;"
                               "border: 3px solid white;"
                               "border-radius: 10px;"
                               )
        self.vf = QFrame()
        self.vf.setFrameShape(QFrame.Box)
        self.vf.setFrameShadow(QFrame.Raised)
        self.vf.setStyleSheet("background-color: rgb(100,100,100);")
        if sys.platform.startswith('linux'):  # for Linux using the X Server
            self.mp.set_xwindow(self.vf.winId())
        elif sys.platform == "win32":  # for Windows
            self.mp.set_hwnd(self.vf.winId())
        elif sys.platform == "darwin":  # for MacOS
            self.mp.set_nsobject(int(self.vf.winId()))

        # Stream Control Widgets

        self.ps = QSlider(Qt.Horizontal)
        self.ps.setTickPosition(QSlider.TicksBelow)
        self.ps.setStyleSheet("QSlider::groove:horizontal {"
                              "border: 1px solid #bbb;"
                              "background: white;"
                              "height: 10px;"
                              "border-radius: 4px;"
                              "}"

                              "QSlider::sub-page:horizontal {"
                              "background: qlineargradient(x1: 0, y1: 0,    x2: 0, y2: 1,"
                              "stop: 0 #b91, stop: 1 #f91);"
                              "border: 1px solid #777;"
                              "height: 10px;"
                              "border-radius: 4px;"
                              "}"

                              "QSlider::add-page:horizontal {"
                              "background: #fff;"
                              "border: 1px solid #777;"
                              "height: 10px;"
                              "border-radius: 4px;"
                              "}"

                              "QSlider::handle:horizontal {"
                              "background: qlineargradient(x1:0, y1:0, x2:1, y2:1,"
                              "stop:0 #eee, stop:1 #ccc);"
                              "border: 1px solid #777;"
                              "width: 13px;"
                              "margin-top: -2px;"
                              "margin-bottom: -2px;"
                              "border-radius: 4px;"
                              "}"

                              "QSlider::handle: horizontal:hover"
                              "{"
                              "background: qlineargradient(x1: 0, y1: 0, x2: 1, y2: 1,"
                              "stop: 0  # fff, stop:1 #ddd);"
                              "border: 1px"
                              "solid  # 444;"
                              "border - radius: 4 px;"
                              "}"

                              "QSlider::sub - page: horizontal:disabled"
                              "{"
                              "background:  # bbb;"
                              "border - color:  # 999;"
                              "}"

                              "QSlider::add - page: horizontal:disabled"
                              "{"
                              "background:  # eee;"
                              "border - color:  # 999;"
                              "}"

                              "QSlider::handle: horizontal:disabled"
                              "{"
                              "background:  # eee;"
                              "border: 1 px"
                              "solid  # aaa;"
                              "border - radius: 4"
                              "px;"
                              "} ")

        self.pp = QPushButton(">")
        self.pp.setStyleSheet("QPushButton {background-color: rgb(80,80,80);"
                              "border: 4px solid white;"
                              "border-radius: 15px;"
                              "font: 40px;"
                              "font-weight: bold;"
                              "color: white;}"
                              "QPushButton:pressed {background-color: rgb(100,100,100);}")

        self.stop = QPushButton("Stop")
        self.stop.setStyleSheet("QPushButton {background-color: rgb(80,80,80);"
                                "border: 4px solid white;"
                                "border-radius: 15px;"
                                "font: 40px;"
                                "color: white;}"
                                "QPushButton:pressed {background-color: rgb(100,100,100);}")
        self.ss = QPushButton("Snap")
        self.ss.setStyleSheet("QPushButton {background-color: rgb(80,80,80);"
                              "border: 4px solid white;"
                              "border-radius: 15px;"
                              "font: 40px;"
                              "color: white;}"
                              "QPushButton:pressed {background-color: rgb(100,100,100);}")
        self.volL = QLabel("Volume")
        self.volL.setStyleSheet("background-color: rgb(80,80,80);"
                                "border: 2px solid white;"
                                "border-radius: 7px;"
                                "font: 20px;"
                                "color: white;"
                                )
        self.vol = QSlider(Qt.Vertical)
        self.vol.setTickPosition(QSlider.TicksRight)
        self.vol.setRange(0, 100)
        self.vol.setValue(self.volume)
        self.vol.setStyleSheet("QSlider::groove:vertical {"
                               "border: 1px solid #bbb;"
                               "background: white;"
                               "width: 10px;"
                               "border-radius: 4px;"
                               "}"

                               "QSlider::add-page:vertical {"
                               "background: qlineargradient(x1: 0, y1: 0,    x2: 0, y2: 1,"
                               "stop: 0 #b91, stop: 1 #f91);"
                               "border: 1px solid #777;"
                               "width: 10px;"
                               "border-radius: 4px;"
                               "}"

                               "QSlider::sub-page:vertical {"
                               "background: #fff;"
                               "border: 1px solid #777;"
                               "width: 10px;"
                               "border-radius: 4px;"
                               "}"

                               "QSlider::handle:vertical {"
                               "background: qlineargradient(x1:0, y1:0, x2:1, y2:1,"
                               "stop:0 #eee, stop:1 #ccc);"
                               "border: 1px solid #777;"
                               "height: 13px;"
                               "margin-right: -2px;"
                               "margin-left: -2px;"
                               "border-radius: 4px;"
                               "}"

                               "QSlider::handle: vertical:hover"
                               "{"
                               "background: qlineargradient(x1: 0, y1: 0, x2: 1, y2: 1,"
                               "stop: 0  # fff, stop:1 #ddd);"
                               "border: 1px"
                               "solid  # 444;"
                               "border - radius: 4 px;"
                               "}"

                               "QSlider::sub - page: vertical:disabled"
                               "{"
                               "background:  # bbb;"
                               "border - color:  # 999;"
                               "}"

                               "QSlider::add - page: vertical:disabled"
                               "{"
                               "background:  # eee;"
                               "border - color:  # 999;"
                               "}"

                               "QSlider::handle: vertical:disabled"
                               "{"
                               "background:  # eee;"
                               "border: 1 px"
                               "solid  # aaa;"
                               "border - radius: 4"
                               "px;"
                               "} ")

        # Indicators

        self.telp = QLabel("00:00:00")
        self.telp.setAlignment(Qt.AlignCenter)
        self.telp.setStyleSheet("background-color: rgb(80,80,80);"
                                "border: 2px solid white;"
                                "border-radius: 7px;"
                                "font: 20px;"
                                "color: white;"
                                )
        self.trem = QLabel("00:00:00")
        self.trem.setAlignment(Qt.AlignCenter)
        self.trem.setStyleSheet("background-color: rgb(80,80,80);"
                                "border: 2px solid white;"
                                "border-radius: 7px;"
                                "font: 20px;"
                                "color: white;"
                                )

        # Widget Resize and Location

        self.head.resize(1900, 80)
        self.head.move(10, 10)
        self.tedit.resize(1455, 40)
        self.tedit.move(10, 100)
        self.load.resize(100, 40)
        self.load.move(1475, 100)
        self.res.resize(100, 40)
        self.res.move(1585, 100)
        self.fpsl.resize(100, 40)
        self.fpsl.move(1695, 100)
        self.fpst.resize(100, 40)
        self.fpst.move(1805, 100)
        self.stl.resize(1910, 710)
        self.stl.move(5, 145)
        self.vf.resize(1900, 700)
        self.vf.move(10, 112)
        self.ps.resize(1700, 30)
        self.ps.move(110, 870)
        self.volL.resize(80, 40)
        self.volL.move(10, 900)
        self.vol.resize(30, 100)
        self.vol.move(35, 950)
        self.stop.resize(200, 100)
        self.stop.move(250, 950)
        self.pp.resize(200, 100)
        self.pp.move(850, 950)
        self.ss.resize(200, 100)
        self.ss.move(1450, 950)
        self.telp.resize(100, 30)
        self.telp.move(10, 860)
        self.trem.resize(100, 30)
        self.trem.move(1810, 860)

        # Widget Parenting

        self.head.setParent(self)
        self.tedit.setParent(self)
        self.load.setParent(self)
        self.res.setParent(self)
        self.fpst.setParent(self)
        self.fpsl.setParent(self)
        self.vf.setParent(self)
        self.ps.setParent(self)
        self.volL.setParent(self)
        self.vol.setParent(self)
        self.stop.setParent(self)
        self.pp.setParent(self)
        self.ss.setParent(self)
        self.telp.setParent(self)
        self.trem.setParent(self)

        # Widget binding

        self.load.clicked.connect(self.loadrtsp)
        self.pp.clicked.connect(self.play)
        self.stop.clicked.connect(self.sstop)
        self.ss.clicked.connect(self.snap)
        self.vol.valueChanged.connect(self.setvol)
        self.ps.sliderMoved.connect(self.settime)
        self.ps.sliderPressed.connect(self.settime)
        self.ps.sliderReleased.connect(self.slrls)

    # Sub functions

    def loadrtsp(self):
        self.media = self.instance.media_new(self.tedit.toPlainText())
        self.mp.set_media(self.media)
        self.mp.play()
        QtTest.QTest.qWait(3000)
        length = self.mp.get_length()
        self.ps.setRange(0, length)
        length = int(length // 1e+3)

        if length == -1 or not self.mp.is_playing():
            mes = QMessageBox(self)
            mes.setText("No Appropriate Media")
            mes.setIcon(QMessageBox.Warning)
            mes.setWindowTitle("Warning")
            mes.exec_()
        else:
            self.flag = True
            self.sflag = False
            self.lflag = True
            self.pp.setText("||")
            if (length // 60 // 60) > 9:
                hour = str(length // 60 // 60)
            else:
                hour = "0" + str(length // 60 // 60)

            if (length // 60) > 9:
                minu = str(length // 60)
            else:
                minu = "0" + str(length // 60)

            if (length % 60) > 9:
                sec = str(length % 60)
            else:
                sec = "0" + str(length % 60)

            self.trem.setText(hour + ":" + minu + ":" + sec)

        QtTest.QTest.qWait(3000)
        reso = self.mp.video_get_size()
        self.res.setText(str(reso[0]) + "p")
        self.fpst.setText(str(self.mp.get_fps()))
        self.thrd.start()

    def play(self):
        self.sflag = False
        if self.lflag:
            if self.flag:
                self.flag = False
                self.pp.setText(">")
                self.mp.pause()
            elif not self.flag:
                self.flag = True
                self.pp.setText("||")
                self.mp.play()

    def sstop(self):
        self.sflag = True
        self.flag = False
        self.pp.setText(">")
        self.mp.stop()

    def snap(self):
        if self.flag:
            self.flag = False
            self.pp.setText(">")
            self.mp.pause()
        if not self.sflag:
            filename = self.dial.getSaveFileName(self, "Take Snapshot", "", ".jpeg")
            aspect = self.mp.video_get_size()
            self.mp.video_take_snapshot(0, filename[0] + filename[1], aspect[0], aspect[1])

    def setvol(self):
        self.volume = self.vol.value()
        self.mp.audio_set_volume(self.volume)

    def settime(self):
        if self.lflag:
            self.mp.pause()
            self.mp.set_time(self.ps.value())

    def slrls(self):
        if self.flag:
            QtTest.QTest.qWait(500)
            self.mp.play()

    # Thread slots

    @pyqtSlot()
    def update(self):
        while True:
            if not self.sflag:
                self.ps.setValue(self.mp.get_time())
                elap = self.mp.get_time()
                rem = self.mp.get_length() - self.mp.get_time()
                elap = int(elap // 1e+3)
                rem = int(rem // 1e+3)
                if (elap // 60 // 60) > 9:
                    houre = str(elap // 60 // 60)
                else:
                    houre = "0" + str(elap // 60 // 60)

                if (elap // 60) > 9:
                    minue = str(elap // 60)
                else:
                    minue = "0" + str(elap // 60)

                if (elap % 60) > 9:
                    sece = str(elap % 60)
                else:
                    sece = "0" + str(elap % 60)

                if (rem // 60 // 60) > 9:
                    hourr = str(rem // 60 // 60)
                else:
                    hourr = "0" + str(rem // 60 // 60)

                if (elap // 60) > 9:
                    minur = str(rem // 60)
                else:
                    minur = "0" + str(rem // 60)

                if (rem % 60) > 9:
                    secr = str(rem % 60)
                else:
                    secr = "0" + str(rem % 60)

                self.telp.setText(houre + ":" + minue + ":" + sece)
                self.trem.setText(hourr + ":" + minur + ":" + secr)
                QtTest.QTest.qWait(100)
            else:
                self.telp.setText("00:00:00")
                self.trem.setText("00:00:00")
                self.ps.setValue(0)
                QtTest.QTest.qWait(100)


if __name__ == "__main__":
    app = QApplication(sys.argv)
    w = MainWindow()
    w.showFullScreen()
    sys.exit(app.exec_())
