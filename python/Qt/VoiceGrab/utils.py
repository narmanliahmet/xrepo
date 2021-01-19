import numpy as np
import scipy as sp
import sounddevice as sd
import matplotlib.pyplot as plt


class Utillities:
    def __init__(self, *args, **kwargs):
        super(Utillities, self).__init__(*args, **kwargs)
        self.out = np.empty(shape=4, dtype=np.ndarray)
        self.fs = 48000
        self.dur = 8
        sd.default.samplerate = self.fs
        sd.default.channels = 1

    def client1(self):
        try:
            sd.default.device = 2, 4
        except:
            sd.default.device = 1, 3
        print("Recording 1")
        self.out[0] = sd.rec(int(self.dur * self.fs))
        sd.wait()
        print("Playing 1")
        sd.play(self.out[0])

    def client2(self):
        try:
            sd.default.device = 2, 4
        except:
            sd.default.device = 1, 3
        self.out[1] = sd.rec(int(self.dur * self.fs))
        sd.wait()
        sd.play(self.out[1])

    def client3(self):
        try:
            sd.default.device = 2, 4
        except:
            sd.default.device = 1, 3
        self.out[2] = sd.rec(int(self.dur * self.fs))
        sd.wait()
        sd.play(self.out[2])

    def client4(self):
        try:
            sd.default.device = 2, 4
        except:
            sd.default.device = 1, 3
        self.out[3] = sd.rec(int(self.dur * self.fs))
        sd.wait()
        sd.play(self.out[3])

    def text1(self):
        print("Text 1")

    def text2(self):
        print("Text 2")

    def text3(self):
        print("Text 3")

    def text4(self):
        print("Text 4")

    def start(self):
        print("Start")

    def stop(self):
        print("Stop")

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
    def fourier(self, x):
        return np.fft.fft(x)

    def corr(self, x, y):
        return np.corrcoef(x, y)

    def streamAudio(self):
        pass

    def grabClient(self, audio):
        pass

    def createMessage(self):
        pass
