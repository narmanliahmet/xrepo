import sys
from PyQt5.QtWidgets import QApplication, QMainWindow, QLabel, QPushButton, QTextEdit, QComboBox, QLineEdit, QFrame, \
    QSlider
import vlc
from PyQt5.QtCore import *
from PyQt5.QtGui import *


class MainWindow(QMainWindow):

    def __init__(self, *args, **kwargs):
        super(MainWindow, self).__init__(*args, **kwargs)

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

        self.tedit = QTextEdit("RTSP Link")
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

        self.res = QComboBox()
        self.res.addItems(["1080p", "760p", "480p", "360p", "240p"])
        self.res.setStyleSheet("background-color: rgb(80,80,80);"
                               "border: 2px solid white;"
                               "border-radius: 7px;"
                               "font: 20px;"
                               "color: white;"
                               "selection-background-color: rgb(100,100,100);"
                               "selection-color: rgb(200, 200, 200);")

        self.fpsl = QLabel("FPS")
        self.fpsl.setStyleSheet("background-color: rgb(80,80,80);"
                                "border: 2px solid white;"
                                "border-radius: 7px;"
                                "font: 20px;"
                                "color: white;"
                                )

        self.fpst = QLineEdit("30")
        self.fpst.setAlignment(Qt.AlignCenter)
        self.fpst.setStyleSheet("background-color: rgb(250,250,250);"
                                "border: 2px solid gray;"
                                "border-radius: 7px;"
                                "font: 20px;}")
        self.fpst.setValidator(QIntValidator(1, 500, self))

        # Display Screen
        self.instance = vlc.Instance()
        self.mp = self.instance.media_player_new()
        self.media = self.instance.media_new("rtsp://wowzaec2demo.streamlock.net/vod/mp4:BigBuckBunny_115k.mov")
        self.mp.set_media(self.media)

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
        self.bw = QPushButton("<<")
        self.bw.setStyleSheet("QPushButton {background-color: rgb(80,80,80);"
                              "border: 4px solid white;"
                              "border-radius: 15px;"
                              "font: 40px;"
                              "font-weight: bold;"
                              "color: white;}"
                              "QPushButton:pressed {background-color: rgb(100,100,100);}")
        self.pp = QPushButton(">")
        self.pp.setStyleSheet("QPushButton {background-color: rgb(80,80,80);"
                              "border: 4px solid white;"
                              "border-radius: 15px;"
                              "font: 40px;"
                              "font-weight: bold;"
                              "color: white;}"
                              "QPushButton:pressed {background-color: rgb(100,100,100);}")
        self.fw = QPushButton(">>")
        self.fw.setStyleSheet("QPushButton {background-color: rgb(80,80,80);"
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
        self.vol.setValue(30)
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
        self.pace = QLabel("No Media")
        self.pace.setAlignment(Qt.AlignCenter)
        self.pace.setStyleSheet("background-color: rgb(80,80,80);"
                                "border: 4px solid white;"
                                "border-radius: 15px;"
                                "font: 30px;"
                                "font-weight: bold;"
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
        self.bw.resize(200, 100)
        self.bw.move(550, 950)
        self.pp.resize(200, 100)
        self.pp.move(850, 950)
        self.fw.resize(200, 100)
        self.fw.move(1150, 950)
        self.ss.resize(200, 100)
        self.ss.move(1450, 950)
        self.telp.resize(100, 30)
        self.telp.move(10, 860)
        self.trem.resize(100, 30)
        self.trem.move(1810, 860)
        self.pace.resize(200, 100)
        self.pace.move(1675, 950)

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
        self.bw.setParent(self)
        self.pp.setParent(self)
        self.fw.setParent(self)
        self.ss.setParent(self)
        self.telp.setParent(self)
        self.trem.setParent(self)
        self.pace.setParent(self)
        self.mp.play()


if __name__ == "__main__":
    app = QApplication(sys.argv)
    w = MainWindow()
    w.showFullScreen()
    sys.exit(app.exec_())
