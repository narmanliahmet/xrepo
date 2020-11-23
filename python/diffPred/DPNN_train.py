import pandas as pd
import numpy as np
import cv2 as cv
import sklearn as sk

df = pd.read_csv("bist-30.csv",delimiter=';')
dfi = df.iloc[:-40, 1]
ndf = dfi.to_numpy(dtype=float)
np.nan_to_num(ndf)
ndif = np.diff(ndf, axis=0)
