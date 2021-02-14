import numpy as np
import sounddevice as sd
import time as tm
from PyQt5.QtTest import QTest
from PyQt5.QtCore import QThread, pyqtSignal, pyqtSlot, QObject, QTimer
from PyQt5.QtWidgets import QMessageBox, QPushButton


class Utillities:

    def __init__(self, *args, **kwargs):
        super(Utillities, self).__init__(*args, **kwargs)
        self.buffer = np.ndarray
        self.ap = AudioProcess()
        self.out = np.empty(shape=4, dtype=np.ndarray)
        self.fout = np.empty(shape=4, dtype=np.ndarray)
        self.fs = 48000
        self.dur = 1
        self.N = self.fs * self.dur
        sd.default.samplerate = self.fs
        sd.default.channels = 1

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

    def clientact1(self):

        print("Recording 1")
        self.out[0] = sd.rec(int(self.N))
        sd.wait()
        print(self.out[0])
        self.fout[0] = np.fft.fft(self.out[0][:, 0])
        self.fout[0] = np.abs(np.concatenate([self.fout[0][self.N // 2:], self.fout[0][0:self.N // 2]]))
        print("End of Recording 1")
        self.ap.flag = False

    def clientact2(self):

        print("Recording 2")
        self.out[1] = sd.rec(int(self.N))
        sd.wait()
        print(self.out[1])
        self.fout[1] = np.fft.fft(self.out[1][:, 0])
        self.fout[1] = np.abs(np.concatenate([self.fout[1][self.N // 2:], self.fout[1][0:self.N // 2]]))
        self.ap.flag = False
        print("End of Recording 2")

    def clientact3(self):

        print("Recording 3")
        self.out[2] = sd.rec(int(self.N))
        sd.wait()
        print(self.out[2])
        self.fout[2] = np.fft.fft(self.out[2][:, 0])
        self.fout[2] = np.abs(np.concatenate([self.fout[2][self.N // 2:], self.fout[2][0:self.N // 2]]))
        self.ap.flag = False
        print("End of Recording 3")

    def clientact4(self):

        print("Recording 4")
        self.out[3] = sd.rec(int(self.N))
        sd.wait()
        print(self.out[3])
        self.fout[3] = np.fft.fft(self.out[3][:, 0])
        self.fout[3] = np.abs(np.concatenate([self.fout[3][self.N // 2:], self.fout[3][0:self.N // 2]]))
        self.ap.flag = False
        print("End of Recording 4")

    def client1(self):
        if self.ap.flag:
            return
        self.ap.flag = True
        self.timerq1.start(50)

    def client2(self):
        if self.ap.flag:
            return
        self.ap.flag = True
        self.timerq2.start(50)

    def client3(self):
        if self.ap.flag:
            return
        self.ap.flag = True
        self.timerq3.start(50)

    def client4(self):
        if self.ap.flag:
            return
        self.ap.flag = True
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
        if self.ap.flag:
            return
        self.ap.flag = True
        print("Stream Started")
        self.ap.timer.start()

    def stop(self):
        print("Stop")
        self.ap.flag = False
        self.ap.timer.stop()

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


class AudioProcess:
    def __init__(self, *args, **kwargs):
        super(AudioProcess, self).__init__(*args, **kwargs)

        self.fs = 48000
        self.dur = 1
        self.N = self.fs * self.dur
        self.flag = False
        self.buffer = np.ndarray
        sd.default.samplerate = self.fs
        sd.default.channels = 1
        self.timer = QTimer()
        self.timer.setInterval(1100)
        self.timer.timeout.connect(self.streamAudio)

    def corr(self, x, y):
        return np.corrcoef(x, y)

    def grabClient(self, audio):
        pass

    def createMessage(self):
        pass

    def streamAudio(self):
        # try:
        #     sd.default.device = 2, 4
        # except:
        #     sd.default.device = 1, 3
        if self.flag:
            self.buffer = sd.rec(int(self.N))
            sd.wait()
            print(self.buffer)
