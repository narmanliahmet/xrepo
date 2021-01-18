import numpy as np
import scipy as sp
import sounddevice as sd
import matplotlib.pyplot as plt


def client1(no):
    print("Client 1")


def client2(no):
    print("Client 2")


def client3(no):
    print("Client 3")


def client4(no):
    print("Client 4")


def text(no):
    print("Text " + str(no))


def start():
    print("Start")


def stop():
    print("Stop")


def lamp(no):
    print("Lamp " + str(no))


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
