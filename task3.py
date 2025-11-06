import numpy as np
import matplotlib.pyplot as plt
from scipy import signal
import sounddevice as sd
import task1 as tsk

alpha = 1000*np.pi
t0 = 0
t1 = 0.01
dt = 0.00001
t2 = np.arange(t0, t1, dt)

def h(t):
    return (alpha**2)*t*np.exp(-alpha*t)

x1 = np.asarray(tsk.result1)[:t2.size]
x2 = np.asarray(tsk.result2)[:t2.size]

d = np.zeros(t2.shape)
d[0] = 1/dt

y1 = dt*signal.convolve(x1, h(t2), method = 'direct')[:t2.size]
y2 = dt*signal.convolve(x2, h(t2), method = 'direct')[:t2.size]




fig, ax = plt.subplots()

ax.plot(t2, y1, label = "Convolved Signal 1")
ax.plot(t2, y2, label = "Convolved Signal 2")

ax.legend()
plt.show()