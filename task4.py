import numpy as np
import matplotlib.pyplot as plt
from scipy import signal
import sounddevice as sd
import task1 as tsk

alpha = 1000*np.pi
t0 = 0
t1 = 0.02
dt = 0.00001
t2 = np.arange(t0, t1, dt)

def h(t):
    return (alpha**2)*t*np.exp(-alpha*t)

x1 = np.asarray(tsk.result1)[:t2.size]
x2 = np.asarray(tsk.result2)[:t2.size]


d = np.zeros(t2.shape)
d[0] = 1/dt

y3 = dt*signal.convolve(x1+x2, h(t2), method = 'direct')[:t2.size]
y2 = dt*signal.convolve(x2, h(t2), method = 'direct')[:t2.size]
y1 = dt*signal.convolve(x1, h(t2), method = 'direct')[:t2.size]

y4 = y2 + y1


fig, ax = plt.subplots()

ax.plot(t2, y3, label = "Convolved Signal x1 + x2 |--> y3")
ax.plot(t2, y4, label = "Convolved Signal y1+y2 ")

ax.legend()
plt.show()