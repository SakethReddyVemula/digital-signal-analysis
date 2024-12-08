import numpy as np
import matplotlib.pyplot as plt

# Cutoff frequency
wc = np.pi / 2

# Time indices
n = np.arange(-100, 101)  # Larger range to capture the ideal impulse response

# Ideal LPF impulse response
hd = np.sin(wc * n) / (np.pi * n)
hd[np.isnan(hd)] = wc  # Handling the case of n = 0

# Frequency range
omega = np.linspace(-np.pi, np.pi, 1000)

# Frequency response of the ideal LPF
H_ideal = np.sum(hd * np.exp(-1j * omega[:, np.newaxis] * n), axis=1)

# Plot magnitude response
plt.figure(figsize=(8, 6))
plt.plot(omega / np.pi, np.abs(H_ideal))
plt.xlabel('Normalized Frequency (ω/π)')
plt.ylabel('Magnitude Response |H(Ω)|')
plt.title('Frequency Response of Ideal LPF')
plt.grid(True)
plt.show()