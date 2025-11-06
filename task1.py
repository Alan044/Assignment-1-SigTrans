import numpy as np
import matplotlib.pyplot as plt
from scipy import signal
import sounddevice as sd


# Generate a time array 't'
T1 = 0.01
f2 = 10**3
omega2 = 2*np.pi*f2
omega1 = 2*np.pi/T1
start = 0
stop = 5
tspan = (start, stop)
dt = 0.00001
vector1 = np.arange(start, stop, dt) 

def x1(t):
    return np.sin(omega1 * t)

def x2(t):
    return np.sin(omega2 * t)

result1 = np.zeros(len(vector1))
result2 = np.zeros(len(vector1))


for i in range(len(vector1)):
    result1[i] = x1(vector1[i])
for i in range(len(vector1)):
    result2[i] = x2(vector1[i])


fig, ax  = plt.subplots()

# ax.plot(vector1, result1  , label = "My Signal 1")
# ax.plot(vector1, result2  , label = "My Signal 2")

# xlim = (0, 0.01)

# ax.set_xlim(xlim)
# ax.grid(True)

# ax.set_xlabel('t')
# ax.set_ylabel('x(t)')
# ax.legend()
# sd.play(result1, 1/dt, blocking=True)
# sd.play(result2, 1/dt, blocking=True)
# plt.show()