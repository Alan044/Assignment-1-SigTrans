import sounddevice as sd

fs = 4*10**4
T = 10
K = T*fs
x = sd.rec(int(K), fs, channels=1, blocking=True)

x = x[::5]
print(x.shape)

sd.play(x, fs/5, blocking=True)
