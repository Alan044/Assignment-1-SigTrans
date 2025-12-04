import numpy as np
import matplotlib.pyplot as plt
import scipy as sci
import sounddevice as sd
# Ts = 0.0001
fs = 2000
Ts = 1 / fs
def x(t): 
    return np.sin(2000*np.pi*t)



timespan = np.arange(0, 5, Ts)
result = np.array(timespan)
j = 0 
for i in range (np.size(timespan)):
    current_value = timespan[j]
    result[j] = x(current_value)
    j+=1
print(np.size(result))

sd.play(result, fs, blocking=True)
