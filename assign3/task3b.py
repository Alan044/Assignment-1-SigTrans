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
wn = fc                # rad/s (because analog=True)

z, p, k = signal.butter(N, wn, analog=True, output='zpk')
H = signal.ZerosPolesGain(z, p, k)

# ----------------------------
# Step 3: Bode plot verification
# ----------------------------
w, mag_db, phase = signal.bode(H, n=1000)
freq = w / (2*np.pi)
gain = 10**(mag_db/20)
rad = phase * (np.pi/180)

fig, ax = plt.subplots(2,1)
ax[0].plot(freq, gain)
ax[1].plot(freq, rad)
ax[0].set_xlim(1000, 10000)
ax[0].set_xlabel("Frequency (Hz)")
ax[0].set_ylabel("Gain")
ax[0].set_title("4th-order Butterworth Lowpass, fc = 3.4 kHz")

ax[1].set_xlim(1000, 10000)
ax[1].set_xlabel("Frequency (Hz)")
ax[1].set_ylabel("Rad")

ax[0].grid(True)
ax[1].grid(True)
fig.tight_layout(pad = 0.5)
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
