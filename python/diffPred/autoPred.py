import matplotlib.pyplot as plt
import pandas as pd
from keras.models import Sequential
from keras.layers import Dense
import numpy as np

df = pd.read_csv('bist-301.csv', delimiter=';')
df = df.iloc[1:, 1]
df = pd.Series.to_numpy(df)
dfn = df.reshape(-1, 1)
# fit a model
res = 0
while np.abs(res-dfn[-129]) > 7:
    model = Sequential()
    model.add(Dense(300, input_dim=1, activation='relu'))
    model.add(Dense(1))
    # compile a model
    model.compile(loss='mse', optimizer='adam')
    # fit a model
    model.fit(dfn[0:-130].reshape(-1, 1), dfn[1:-129].reshape(-1, 1), epochs=400, batch_size=200, verbose=0)
    # predict last 1

    res = model.predict(dfn[-130].reshape(-1, 1), verbose=0)
    print(res)
    print(dfn[-129])
