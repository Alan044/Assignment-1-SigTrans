import sounddevice as sd
import scipy.signal as signal
import matplotlib.pyplot as plt
import numpy as np

# ----------------------------
# Step 1: Record 10 seconds @ 40 kHz
# ----------------------------
fs = 40_000   # original sampling rate
T = 10
K = int(T * fs)

print("Recording 10 seconds at 40 kHz ...")
x = sd.rec(K, samplerate=fs, channels=1, blocking=True).flatten()

# ----------------------------
# Step 2: Design 4th-order Butterworth lowpass, fc = 3.4 kHz
# ----------------------------
N = 4
fc = 3400                      # Hz
wn = 2*np.pi*fc                # rad/s (because analog=True)

z, p, k = signal.butter(N, wn, analog=True, output='zpk')
H = signal.ZerosPolesGain(z, p, k)

# ----------------------------
# Step 3: Bode plot verification
# ----------------------------
w, mag_db, phase = signal.bode(H, n=2000)
freq = w / (2*np.pi)

fig, ax = plt.subplots()
ax.plot(freq, mag_db)
ax.set_xlim(1000, 10000)
ax.set_xlabel("Frequency (Hz)")
ax.set_ylabel("Magnitude (dB)")
ax.set_title("4th-order Butterworth Lowpass, fc = 3.4 kHz")
ax.grid(which='both')
plt.show()

# ----------------------------
# Step 4: Filter the recorded signal using lsim
# ----------------------------
t = np.arange(K) / fs   # correct time vector

# lsim expects input shape (N,), not (N,1)
_, x_filtered, _ = signal.lsim(H, U=x, T=t)

# ----------------------------
# Step 5: Downsample by a factor of 5 → fs = 8 kHz
# ----------------------------
x_down = x_filtered[::5]

print("Downsampled length:", len(x_down))

# ----------------------------
# Step 6: Play filtered + downsampled signal
# ----------------------------
sd.play(x_down, 8000, blocking=True)
