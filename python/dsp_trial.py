import numpy as np
from matplotlib import pyplot as plt

plt.style.use('ggplot')

n = np.arange(-20,21)
pi = np.pi
y1 = np.sin((2 * pi / 5) * n)
y2 = np.sin((2 * pi / 3) * n)

y3 = np.sinc(n/pi)
y4 = y2 * y3

fig, ((ax1, ax2), (ax3, ax4)) = plt.subplots(2, 2)
ax1.stem(n, y1, label='Sin')
ax2.stem(n, y2, label='Another Sin')
ax3.stem(n, y3, label='Sinc')
ax4.stem(n, y4, label='Enveloped')
plt.show()
