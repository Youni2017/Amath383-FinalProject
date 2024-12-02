import numpy as np
import matplotlib.pyplot as plt
def W(t):
    return -993.1636364 * np.exp(-0.01 * t) + 1204.69 * np.exp(-0.0056 * t)

t = np.linspace(0, 1000, 100)
w_values = W(t)

plt.figure(figsize=(10, 6))
plt.plot(t, w_values, label=r"$W(t) = -993.1636364e^{-0.01t} + 1204.69e^{-0.0056t}$", color="blue")
plt.title("Population in Working Age (in Millions)", fontsize=16)
plt.xlabel("Time t (Years)", fontsize=14)
plt.ylabel("W(t)", fontsize=14)
plt.grid(alpha=0.5)
plt.legend(fontsize=12)
plt.show()
