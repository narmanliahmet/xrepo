import numpy as np
import sounddevice as sd
import asyncio
from PyQt5.QtTest import QTest
from PyQt5.QtCore import QThread, pyqtSignal


class Utillities:

    def __init__(self, *args, **kwargs):
        super(Utillities, self).__init__(*args, **kwargs)
        self.out = np.empty(shape=4, dtype=np.ndarray)
        self.fout = np.empty(shape=4, dtype=np.ndarray)
        self.buffer = np.ndarray
        self.fs = 48000
        self.dur = 8
        self.N = self.fs * self.dur
        self.ap = AudioProcess()
        sd.default.samplerate = self.fs
        sd.default.channels = 1

    def client1(self):
        try:
            sd.default.device = 2, 4
        except:
            sd.default.device = 1, 3
        print("Recording 1")
        self.out[0] = sd.rec(int(self.N))
        sd.wait()
        self.fout[0] = np.fft.fft(self.out[0][:, 0])
        self.fout[0] = np.abs(np.concatenate([self.fout[0][self.N // 2:], self.fout[0][0:self.N // 2]]))

    def client2(self):
        try:
            sd.default.device = 2, 4
        except:
            sd.default.device = 1, 3
        print("Recording 2")
        self.out[1] = sd.rec(int(self.N))
        sd.wait()
        self.fout[1] = np.fft.fft(self.out[1][:, 0])
        self.fout[1] = np.abs(np.concatenate([self.fout[1][self.N // 2:], self.fout[1][0:self.N // 2]]))

    def client3(self):
        try:
            sd.default.device = 2, 4
        except:
            sd.default.device = 1, 3
        print("Recording 3")
        self.out[2] = sd.rec(int(self.N))
        sd.wait()
        self.fout[2] = np.fft.fft(self.out[2][:, 0])
        self.fout[2] = np.abs(np.concatenate([self.fout[2][self.N // 2:], self.fout[2][0:self.N // 2]]))

    def client4(self):
        try:
            sd.default.device = 2, 4
        except:
            sd.default.device = 1, 3
        print("Recording 4")
        self.out[3] = sd.rec(int(self.N))
        sd.wait()
        self.fout[3] = np.fft.fft(self.out[3][:, 0])
        self.fout[3] = np.abs(np.concatenate([self.fout[3][self.N // 2:], self.fout[3][0:self.N // 2]]))

    def text1(self):
        print("Text 1")

    def text2(self):
        print("Text 2")

    def text3(self):
        print("Text 3")

    def text4(self):
        print("Text 4")

    def start(self):
        self.ap.flag = True
        self.ap.streamAudio(self.buffer)

    def stop(self):
        print("Stop")
        self.ap.flag = False

    def lamp1(self):
        print("Lamp 1")

    def lamp2(self):
        print("Lamp 1")

    def lamp3(self):
        print("Lamp 1")

    def lamp4(self):
        print("Lamp 1")


def message():
    print("Message")


class AudioProcess:

    def __init__(self, *args, **kwargs):
        super(AudioProcess, self).__init__(*args, **kwargs)
        self.fs = 48000
        self.dur = 1
        self.N = self.fs * self.dur
        self.flag = True
        sd.default.samplerate = self.fs
        sd.default.channels = 1

    def corr(self, x, y):
        return np.corrcoef(x, y)

    def streamAudio(self, buffer):
        print("Stream Started")
        try:
            sd.default.device = 2, 4
        except:
            sd.default.device = 1, 3
        while self.flag:
            buffer = sd.rec(int(self.N))
            QTest.qWait(1000)
            print(buffer)
        print("Stream Finished")
        print(buffer)

    def grabClient(self, audio):
        pass

    def createMessage(self):
        pass
