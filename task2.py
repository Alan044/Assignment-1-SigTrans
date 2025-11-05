import numpy as np
import matplotlib.pyplot as plt
from scipy import signal
import sounddevice as sd
import task1 as tsk

dt = 0.00001
alpha = 1000*np.pi
t0 = 0
t1 = 0.02
timevector = np.arange(t0, t1, dt)
# def u(t):
#     if t >= 0:
#         return 1
#     return 0

def h(t):
    return alpha**2 *t*np.exp(-alpha*t) 

result1 = np.zeros(len(timevector))
for i in range(len(timevector)):
    result1[i] = h(timevector[i])
    

y = dt * signal.convolve(timevector, result1, method = 'direct' )

y = y[t0:timevector.shape[0]]

d = np.zeros(timevector.shape)

d[0] = 1/dt

fig, ax  = plt.subplots()

y1 = dt* signal.convolve(timevector, tsk.result1, method = 'direct' )
y2 = dt* signal.convolve(timevector, tsk.result2, method = 'direct' )
# ax.plot(timevector, y  , label = "Convolution Result")
# ax.plot(timevector, d  , label = "Delta Function")  
ax.plot(timevector, y1  , label = "Convolution Result")
ax.plot(timevector, d  , label = "Delta Function")  

plt.show()