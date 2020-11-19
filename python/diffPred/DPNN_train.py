import pandas as pd
import numpy as np
import cv2 as cv
import sklearn as sk

df = pd.read_csv("data.csv")
df = df.iloc[3270-2050:-1, 5:21:1]
ndf = df.to_numpy(dtype=float)
np.nan_to_num(ndf)
ndif = np.diff(ndf, axis=0)
ndif = (255*(ndif - np.min(ndif))/(np.max(ndif)-np.min(ndif)))
imgD = ndif.astype(np.uint8)
cv.imshow("denem",imgD)
cv.waitKey()


#for i in np.arange(0,2048,16):
 #   cv.imwrite("data1"+str(i/16+1)+".jpg", )




