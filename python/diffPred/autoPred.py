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
model = Sequential()
model.add(Dense(300, input_dim=1, activation='relu'))
model.add(Dense(1))
# compile a model
model.compile(loss='mse', optimizer='adam')
# fit a model
model.fit(dfn[0:-130].reshape(-1, 1), dfn[1:-129].reshape(-1, 1), epochs=900, batch_size=200, verbose=0)
# predict last 1
err = np.zeros(10)
for n in range(10):
    mse = model.predict(dfn[-129+n].reshape(-1, 1), verbose=0)
    err[n] = np.abs(mse-dfn[-128+n])

plt.figure()
plt.plot(range(10), err, label='error')
plt.title("Error of predictions")
plt.legend()
plt.show()