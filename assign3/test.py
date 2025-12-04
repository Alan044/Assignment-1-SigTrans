import numpy as np
import matplotlib.pyplot as plt
from scipy import signal

# --- Filter parameters ---
N = 4                # Order
fc = 3400            # Cutoff frequency in Hz
wc = 2 * np.pi * fc  # Convert cutoff to rad/s

# --- Butterworth filter (analog), zero-pole-gain format ---
z, p, k = signal.butter(N, wc, analog=True, output='zpk')

# --- Create transfer function object ---
H = signal.ZerosPolesGain(z, p, k)

# --- Bode response ---
w, mag, phase = signal.bode(H, n=2000)  # w in rad/s

# --- Convert to Hz ---
f = w / (2 * np.pi)

# --- Convert magnitude from dB → linear gain ---
gain = 10**(mag / 20)

# --- Plot amplitude response ---
plt.figure(figsize=(10, 5))
plt.semilogx(f, gain)
plt.xlim(1e3, 1e4)    # 1 kHz to 10 kHz as required
plt.ylim(1e-3, 2)
plt.grid(which='both', linestyle='--', alpha=0.7)
plt.xlabel("Frequency (Hz)")
plt.ylabel("Amplitude (Gain)")
plt.title("Butterworth Low-pass Filter (Order 4, fc = 3.4 kHz)\nAmplitude Response")
plt.show()

# --- Plot phase response ---
plt.figure(figsize=(10, 5))
plt.semilogx(f, phase)
plt.xlim(1e3, 1e4)
plt.grid(which='both', linestyle='--', alpha=0.7)
plt.xlabel("Frequency (Hz)")
plt.ylabel("Phase (degrees)")
plt.title("Butterworth Low-pass Filter (Order 4, fc = 3.4 kHz)\nPhase Response")
plt.show()
