import utils
import numpy as np

util = utils.Utillities()
proc = utils.AudioProcess()

util.client1()
util.client2()
util.client3()
util.client4()

util.text1()
util.text2()
util.text3()
util.text4()

util.start()
util.stop()

util.lamp1()
util.lamp2()
util.lamp3()
util.lamp4()

a = np.random.rand(1000)
b = np.random.randn(1000)
corf = proc.corr(a, b)
