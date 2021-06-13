from __future__ import print_function
import cv2 as cv
import requests
import numpy as np


class Process:

    key = 'TomTomAPIKeyHere'
    zoom = 14
    x = 9272
    y = 6319
    thick = 4
    res = 512
    lon_deg = 23.742565152156075
    lat_deg = 38.00283462485616
    print(lon_deg)
    print(lat_deg)
    url = 'https://api.tomtom.com/traffic/map/4/tile/flow/absolute/' + str(zoom) + '/' + str(x) + '/' + str(
        y) + '.png?thickness=' + str(thick) + '&tileSize=' + str(res) + '&key=' + key
    url_m = 'https://api.tomtom.com/map/1/staticimage?layer=basic&style=main&format=png&zoom=' + str(
        zoom) + '&center=' + str(lon_deg - 0.0011) + '%2C%20' + str(lat_deg + 0.00189) + '&width=' + str(
        res) + '&height=' + str(res) + '&view=IN&key=' + key
    while True:
        response = requests.get(url_m)
        with open("img_m.png", "wb+") as file:
            file.write(response.content)

        file_r = 'img_r.png'
        response = requests.get(url)
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
        # [load]
        if src1 is None:
            print("Error loading src1")
            exit(-1)
        elif src2 is None:
            print("Error loading src2")
            exit(-1)
        # [blend_images]
        # beta = (1.0 - alpha)
        # dst = cv.addWeighted(src1, alpha, src2, beta, 0.4)
        # [blend_images]
        # [display]

        step = 3
        filename = 'blendedstep.png'

        def insert_polution(img, center, circle_radius):
            for n in range(circle_radius):
                cv.circle(img, center, 5 * (n + 1), (n // 2, n, 255 - 2 * n))
            return True

        bufd = src2.copy()
        bufc = src2.copy()
        ind = np.where(map_r)

        for n in range(0, len(ind[0]), step):
            buf = bufd
            insert_polution(buf, (ind[0][n], ind[1][n]), map_r[ind[0][n], ind[1][n]])
            cv.addWeighted(src2, 1 - 1 / (n + 2), buf, 1 / (n + 2), 0, src2)
            print('Processing... ' + str(n // step) + '/' + str(len(ind[0]) // step), end='\r')
        print("Sub-process ended.", end='\r')
        alpha = 0.2
        binar = cv.cvtColor(binar, cv.COLOR_GRAY2RGB)
        cv.addWeighted(bufc, alpha, src2, 1 - alpha, 2.0, src2)
        src2[binar == 237] = 255

        cv.imwrite(filename, src2)
        print()
        print("Blended image saved: " + filename)
