import numpy as np
import matplotlib.pyplot as plt

# Signal Parameters
T0 = 4.0          # Period of the signal (seconds)
f0 = 1.0 / T0     # Fundamental frequency (0.25 Hz)
N = 50            # Number of harmonics to sum (-N to N)
t = np.linspace(-T0, T0, 1000)

# Calculate Fourier Series coefficient c_k for pulse on [-1, 1]
def compute_ck(k, f0, T0):
    if k == 0:
        return 2.0 / T0  # Average value (DC component)
    else:
        return np.sin(2 * np.pi * k * f0) / (np.pi * k)

# Reconstruct x(t) from Fourier Series sum
x_reconstructed = np.zeros_like(t, dtype=complex)
for k in range(-N, N + 1):
    c_k = compute_ck(k, f0, T0)
    x_reconstructed += c_k * np.exp(1j * 2 * np.pi * k * f0 * t)

# Take the real part
x_reconstructed = np.real(x_reconstructed)

# Ideal rectangular pulse train for comparison
x_ideal = np.where(np.abs((t + T0/2) % T0 - T0/2) <= 1.0, 1.0, 0.0)

# Plotting
plt.figure(figsize=(9, 4))
plt.plot(t, x_ideal, 'r--', label='Ideal Rectangular Signal $x(t)$', linewidth=2)
plt.plot(t, x_reconstructed, 'b-', label=f'Reconstructed F.S. ($N={N}$)', alpha=0.8)

plt.xlabel('Time $t$ (seconds)')
plt.ylabel('$x(t)$')
plt.title(f'Fourier Series Reconstruction ($x(t)=1$ for $-1 \\leq t \\leq 1$, $T_0={T0}$)')
plt.axhline(0, color='black', linewidth=0.5, linestyle=':')
plt.ylim(-0.2, 1.3)
plt.legend(loc='upper right')
plt.grid(True)
plt.tight_layout()
plt.show()
