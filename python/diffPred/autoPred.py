import matplotlib.pyplot as plt
import pandas as pd
from keras.models import Sequential
from keras.layers import Dense
import numpy as np

df = pd.read_csv('data1.csv', delimiter=';')
val = df.iloc[:-20, 0]
tst = df.iloc[-30:-20, 0:4]
rl = df.iloc[-20:-17, 0]
val = pd.DataFrame.to_numpy(val)
tst = pd.DataFrame.to_numpy(tst)
rl = pd.DataFrame.to_numpy(rl)
# rl = rl-minr
train = val.reshape(-1, 1)
train = np.nan_to_num(train)
test = tst.reshape(-1, 1)
reals = rl.reshape(-1, 1)
rlmean = np.mean(reals)
rlstd = np.std(reals)
rlauto = np.corrcoef(reals.reshape(-1), train[-3:].reshape(-1))

predL = len(train)
stdTr = np.zeros(predL)
meanTr = np.zeros(predL)
autoTr = np.zeros(predL-4)
for n in range(20, predL):
    meanTr[n] = np.mean(train[n-20:n])
# fit a model
meanTr[0:20] = np.nan
autoTr = np.nan_to_num(autoTr)
stdTr = np.nan_to_num(stdTr)
meanTr = np.nan_to_num(meanTr)
minAuto = np.min(autoTr)
# autoTr = autoTr - minAuto
model = Sequential()
model1 = Sequential()
model2 = Sequential()
model.add(Dense(300, input_dim=1, activation='relu'))
model1.add(Dense(300, input_dim=1, activation='relu'))
model2.add(Dense(300, input_dim=1, activation='relu'))

model.add(Dense(1))
model1.add(Dense(1))
model2.add(Dense(1))
# compile a model
model.compile(loss='mse', optimizer='adam')
model1.compile(loss='mse', optimizer='adam')
model2.compile(loss='mse', optimizer='adam')
# fit a model
model.fit(meanTr[:-1].reshape(-1, 1), meanTr[1:].reshape(-1, 1), epochs=100, batch_size=100, verbose=0)
model.fit(stdTr[:-1].reshape(-1, 1), stdTr[1:].reshape(-1, 1), epochs=100, batch_size=100, verbose=0)
model.fit(autoTr[:-1].reshape(-1, 1), autoTr[1:].reshape(-1, 1), epochs=100, batch_size=100, verbose=0)
# predict last 1
index = -1
res = model.predict(meanTr[-1].reshape(-1,1))
res1 = model1.predict(stdTr[-1].reshape(-1,1))
res2 = model2.predict(autoTr[-1].reshape(-1,1))

print("Predicted Values")
print("Mean Value")
print(res)
print("Standart Deviation")
print(res1)
print("Autocorrealation")
print(res2)
print("Real Values")
print("Mean Value")
print(rlmean)
print("Standart Deviaton")
print(rlstd)
print("Autocorrelation")
print(rlauto[0,1])
plt.figure()
plt.plot(range(len(meanTr)), meanTr, label='Mean')
plt.plot(range(len(train)), train, label='Real')
plt.legend()
plt.show()