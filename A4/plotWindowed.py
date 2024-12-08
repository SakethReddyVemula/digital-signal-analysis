import numpy as np
import matplotlib.pyplot as plt

# Cutoff frequency
wc = np.pi / 2

# Time indices
n = np.arange(-10, 11)

# Ideal LPF impulse response
hd = np.sin(wc * n) / (np.pi * n)
hd[np.isnan(hd)] = wc  # Handling the case of n = 0

# Rectangular window
w = np.zeros_like(n)
w[(n >= 0) & (n <= 2)] = 1

# Windowed impulse response
h = hd * w

# Frequency response
omega = np.linspace(-np.pi, np.pi, 1000)
H = np.sum(h * np.exp(-1j * omega[:, np.newaxis] * n), axis=1)

# Plot magnitude response
plt.figure(figsize=(8, 6))
plt.plot(omega / np.pi, np.abs(H))
plt.xlabel('Normalized Frequency (ω/π)')
plt.ylabel('Magnitude Response |H(Ω)|')
plt.title('Frequency Response of Windowed LPF (Rectangular Window, Length 3)')
plt.grid(True)
plt.show()