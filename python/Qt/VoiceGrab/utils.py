import numpy as np
import sounddevice as sd
import time as tm
from PyQt5.QtTest import QTest
from PyQt5.QtCore import QThread, pyqtSignal, pyqtSlot, QObject, QTimer
from PyQt5.QtWidgets import QMessageBox, QPushButton
import functools as ft
import matplotlib.pyplot as plt

class Utillities:

    def __init__(self, *args, **kwargs):
        super(Utillities, self).__init__(*args, **kwargs)
        self.buffer = np.ndarray
        self.out = np.empty(shape=4, dtype=np.ndarray)
        self.fout = np.empty(shape=4, dtype=np.ndarray)
        self.fs = 48000
        self.dur = 4
        self.dur2 = 1
        self.N = self.fs * self.dur
        self.N2 = self.fs * self.dur2
        self.flag = False
        self.corr1 = []
        self.corr2 = []
        self.corr3 = []
        self.corr4 = []
        sd.default.samplerate = self.fs
        sd.default.channels = 1
        self.recFlag = [False] * 4

        self.buffer = np.ndarray
        self.timerq1 = QTimer()
        self.timerq2 = QTimer()
        self.timerq3 = QTimer()
        self.timerq4 = QTimer()
        self.timerq1.timeout.connect(self.clientact1)
        self.timerq2.timeout.connect(self.clientact2)
        self.timerq3.timeout.connect(self.clientact3)
        self.timerq4.timeout.connect(self.clientact4)

        self.timerq1.setSingleShot(True)
        self.timerq2.setSingleShot(True)
        self.timerq3.setSingleShot(True)
        self.timerq4.setSingleShot(True)

        self.timer = QTimer()
        self.timer.setInterval(1000)
        self.timer.timeout.connect(self.streamAudio)

    def clientact1(self):

        print("Recording 1")
        self.out[0] = sd.rec(int(self.N))
        sd.wait()
        print(self.out[0])
        self.fout[0] = np.fft.fft(self.out[0][:, 0])
        self.fout[0] = self.fout[0][::4]
        print("End of Recording 1")
        self.flag = False
        self.recFlag[0] = True

    def clientact2(self):

        print("Recording 2")
        self.out[1] = sd.rec(int(self.N))
        sd.wait()
        print(self.out[1])
        self.fout[1] = np.fft.fft(self.out[1][:, 0])
        self.fout[1] = self.fout[1][::4]
        print("End of Recording 2")
        self.flag = False
        self.recFlag[1] = True

    def clientact3(self):

        print("Recording 3")
        self.out[2] = sd.rec(int(self.N))
        sd.wait()
        print(self.out[2])
        self.fout[2] = np.fft.fft(self.out[2][:, 0])
        self.fout[2] = self.fout[2][::4]
        print("End of Recording 3")
        self.flag = False
        self.recFlag[2] = True

    def clientact4(self):

        print("Recording 4")
        self.out[3] = sd.rec(int(self.N))
        sd.wait()
        print(self.out[3])
        self.fout[3] = np.fft.fft(self.out[3][:, 0])
        self.fout[3] = self.fout[3][::4]
        print("End of Recording 4")
        self.flag = False
        self.recFlag[3] = True

    def client1(self):
        if self.flag:
            return
        self.flag = True
        self.timerq1.start(50)

    def client2(self):
        if self.flag:
            return
        self.flag = True
        self.timerq2.start(50)

    def client3(self):
        if self.flag:
            return
        self.flag = True
        self.timerq3.start(50)

    def client4(self):
        if self.flag:
            return
        self.flag = True
        self.timerq4.start(50)

    def text1(self):
        print("Text 1")

    def text2(self):
        print("Text 2")

    def text3(self):
        print("Text 3")

    def text4(self):
        print("Text 4")

    def start(self):
        if self.flag:
            return
        self.flag = True
        print("Stream Started")
        self.timer.start()

    def stop(self):
        print("Stop")
        self.flag = False
        self.timer.stop()

    def lamp1(self):
        print("Lamp 1")

    def lamp2(self):
        print("Lamp 1")

    def lamp3(self):
        print("Lamp 1")

    def lamp4(self):
        print("Lamp 1")

    def message(self):
        print("Message")

    def grabClient(self, audio):
        pass

    def createMessage(self):
        pass

    def streamAudio(self):
        if self.flag:
            self.buffer = sd.rec(int(self.N2))
            sd.wait()
            if self.recFlag[0]:
                print(np.fft.fft(self.buffer))
                print(self.fout[0])
                self.corr1 = np.corrcoef(np.transpose(np.abs(np.fft.fft(self.buffer))), np.abs(self.fout[0]))
                print("Correlation of user 1")
                print(self.corr1[0, 1])
            if self.recFlag[1]:
                self.corr2 = np.corrcoef(np.transpose(np.abs(np.fft.fft(self.buffer))), np.abs(self.fout[1]))
                print("Correlation of user 2")
                print(self.corr2[0, 1])
            if self.recFlag[2]:
                self.corr3 = np.corrcoef(np.transpose(np.abs(np.fft.fft(self.buffer))), np.abs(self.fout[2]))
                print("Correlation of user 3")
                print(self.corr3[0, 1])
            if self.recFlag[3]:
                self.corr4 = np.corrcoef(np.transpose(np.abs(np.fft.fft(self.buffer))), np.abs(self.fout[3]))
                print("Correlation of user 4")
                print(self.corr4[0, 1])
