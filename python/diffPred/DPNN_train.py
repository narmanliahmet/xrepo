import pandas as pd
from numpy import *
from keras import *
from keras.layers import *

df = pd.read_csv("bist-30.csv", delimiter=';')
dfi = df.iloc[:-100, 1]
dfn = df.iloc[-100:, 1]
ndf = dfi.to_numpy(dtype=float)
ndfn = dfn.to_numpy(dtype=float)
nan_to_num(ndfn)
nan_to_num(ndf)
ndif = diff(ndf, axis=0)
ndifv = diff(ndfn, axis=0)
verbose, epochs, batch_size = 0, 10, 32
n_timesteps, n_features, n_outputs = 10, 0, len(ndif)-10
model = Sequential()
model.add(Conv1D(filters=64, kernel_size=3, activation='relu', input_shape=(n_timesteps, n_features)))
model.add(Conv1D(filters=64, kernel_size=3, activation='relu'))
model.add(Dropout(0.5))
model.add(MaxPooling1D(pool_size=2))
model.add(Flatten())
model.add(Dense(100, activation='relu'))
model.add(Dense(n_outputs, activation='softmax'))
model.compile(loss='categorical_crossentropy', optimizer='adam', metrics=['accuracy'])
# fit network
model.fit(ndif[:-10], ndif[10:], epochs=epochs, batch_size=batch_size, verbose=verbose)
# evaluate model
_, accuracy = model.evaluate(ndifv[:-10], ndifv[10:], batch_size=batch_size, verbose=verbose)
print(accuracy)