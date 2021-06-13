from __future__ import print_function
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from PyQt5.QtCore import *
import numpy as np
import cv2 as cv
import requests
import os, sys
from PyQt5 import QtTest
from time import sleep


class Process:

    def __init__(self):
        super().__init__()
        key = 'TomTomAPIKeyHere'
        zoom = 14
        x = 9272
        y = 6319
        thick = 4
        res = 512
        lon_deg = 23.742565152156075
        lat_deg = 38.00283462485616
        print('[INFO]: Longtitude: ' + str(lon_deg))
        print('[INFO]: Lattitude: ' + str(lat_deg))
        self.url = 'https://api.tomtom.com/traffic/map/4/tile/flow/absolute/' + str(zoom) + '/' + str(x) + '/' + str(
            y) + '.png?thickness=' + str(thick) + '&tileSize=' + str(res) + '&key=' + key
        self.url_m = 'https://api.tomtom.com/map/1/staticimage?layer=basic&style=main&format=png&zoom=' + str(
            zoom) + '&center=' + str(lon_deg - 0.0011) + '%2C%20' + str(lat_deg + 0.00189) + '&width=' + str(
            res) + '&height=' + str(res) + '&view=IN&key=' + key

    # while True:
    def insert_polution(self, img, center_, circle_radius):
        for n in range(circle_radius):
            cv.circle(img, center_, 5 * (n + 1), (n * 2, n * 8, 255 - 2 * n))
        return True

    def run_once(self, win):
        try:
            response = requests.get(self.url_m)
        except:
            print("[WARNING]: Request URL is not in reach! Check your internet connection.")
            response = False
        finally:
            if not response:
                # sys.exit()
                return
            print("[INFO]: Map data downloaded.")
        with open("img_m.png", "wb+") as file:
            file.write(response.content)
        file_r = 'img_r.png'
        if response:
            try:
                response = requests.get(self.url)
            except:
                print("[WARNING]: Request URL is not in reach! Check your internet connection.")
                response = False
            finally:
                if not response:
                    # sys.exit()
                    return
                print("[INFO]: Road data downloaded.")
        with open(file_r, "wb+") as file:
            file.write(response.content)
            # print(img_m)
        # alpha = 1
        # try:
        #     raw_input          # Python 2
        # except NameError:
        #     raw_input = input  # Python 3
        alpha = 0.5
        # [load]
        src1 = cv.imread(file_r)
        src2 = cv.imread(file_r)
        map_g = cv.imread('img_m.png', cv.IMREAD_GRAYSCALE)
        map_r = cv.imread(file_r, cv.IMREAD_GRAYSCALE)
        # map_r = cv.cvtColor(map_r,cv.COLOR_GRAY2RGB)
        _, binar = cv.threshold(map_g, 237, 237, cv.THRESH_BINARY_INV)
        rand_b = np.random.randint(1, 100)
        cv.imwrite('binary.png', binar)
        # [oad]
        if src1 is None:
            print("Error loading src1")
            exit(-1)
        elif src2 is None:
            print("Error loading src2")
            exit(-1)
        # [lend_images]
        # bta = (1.0 - alpha)
        # dt = cv.addWeighted(src1, alpha, src2, beta, 0.4)
        # [lend_images]
        # [isplay]
        step = 1
        filename = 'blended.png'
        bufd = src2.copy()
        bufc = src2.copy()
        ind = np.where(map_r)
        win.lon = len(ind[0]) // step
        win.prog.setMaximum(win.lon)
        for n in range(0, len(ind[0]), step):
            buf = bufd
            self.insert_polution(buf, (ind[0][n], ind[1][n]), map_r[ind[0][n], ind[1][n]])
            cv.addWeighted(src2, 1 - 1 / (n + 2), buf, 1 / (n + 2), 0, src2)
            win.nth = n + 1
            win.prog.setValue(win.nth)
            print('Processing... ' + str(n // step) + '/' + str(len(ind[0]) // step), end='\r')
        win.nth = 0
        print("Sub-process ended.", end='\r')
        alpha = 0.2
        binar = cv.cvtColor(binar, cv.COLOR_GRAY2RGB)
        cv.addWeighted(bufc, alpha, src2, 1 - alpha, 2.0, src2)
        src2[binar == 237] = 255
        cv.imwrite(filename, src2)
        print()
        print("Blended image saved: " + filename)


class Worker(QObject):
    finished = pyqtSignal()

    def __init__(self, var_):
        super().__init__()
        self.proc = Process()
        self.var = var_
        self.sleep = 60 # seconds

    def process(self):
        while True:
            self.proc.run_once(self.var)
            self.var.pic.setPixmap(QPixmap(os.getcwd() + "/blended.png"))
            self.var.pic.show()
            # print("working")
            QThread.sleep(self.sleep)


class App(QMainWindow):
    # Initialization class with title and initUI
    def __init__(self):
        super().__init__()
        self.lon = 0
        self.nth = 0
        self.title = "KCEM-v1.0.0"
        self.setStyleSheet("background-color: rgb(80,50,40)")
        self.initUI()

    def initUI(self):
        # Defining window title
        self.setWindowTitle(self.title)
        self.setFixedSize(550, 512 + 50 + 20 + 20)
        # Defining timers for further use
        self.thread = QThread()
        # Step 3: Create a worker object
        self.worker = Worker(self)
        # Step 4: Move worker to the thread
        self.worker.moveToThread(self.thread)
        # Step 5: Connect signals and slots
        self.thread.started.connect(self.worker.process)
        self.worker.finished.connect(self.thread.quit)
        self.worker.finished.connect(self.worker.deleteLater)
        self.thread.finished.connect(self.thread.deleteLater)
        # Step 6: Start the thread
        self.prog = QProgressBar(self)
        self.prog.setStyleSheet(
            "background: qlineargradient(x1: 0, y1: 0,    x2: 0, y2: 1,"
            "stop: 0 #b91, stop: 1 #f91);"
            "border: 1px solid #777;"
            "height: 10px;"
            "border-radius: 4px;"
            "font: 20px;"
            "color: rgb(255,255,255);"
        )
        self.prog.resize(500, 20)
        self.prog.move((550 - 512 + 10) // 2, 512 + 60)
        self.prog.show()
        self.pic = QLabel('Waiting for First...', self)
        self.pic.setAlignment(Qt.AlignCenter)
        self.pic.setStyleSheet("background-color: rgb(100,130,50);"
                               "border: 4px solid green;"
                               "border-radius: 4px;"
                               "border-style: outset;"
                               "font: 50px;"
                               "color: rgb(220,140,20);")
        # GUI title configuration with previous steps
        title = QLabel("Kypsila Carbon Emission Monitor", self)
        title.setAlignment(Qt.AlignCenter)
        title.resize(550, 50)
        title.setStyleSheet("background-color: rgb(150,80,40);"
                            "border: 4px rgb(100,180,40);;"
                            "border-radius: 8px;"
                            "border-style: outset;"
                            "font: 30px;"
                            "color: rgb(170,250,110);")
        title.move(0, 0)
        self.pic.resize(512, 512)
        self.pic.move((550 - 512) // 2, 55)

        # Displaying all widgets
        title.show()
        self.pic.show()
        # Defining window open up size as maximized
        self.thread.start()
        self.show()


# Execution of app
if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = App()
    sys.exit(app.exec_())
