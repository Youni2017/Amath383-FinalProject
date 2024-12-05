import numpy as np
import matplotlib.pyplot as plt

def R(t):
    return np.exp(-0.041867754 * t) * (641.08 * np.exp(0.03678 * t) - 601.488 * np.exp(0.0318678 * t) + c_1)

c_1 = 15.59952
t = np.linspace(0, 1000, 100)
r_values = R(t)

plt.figure(figsize=(10, 6))
plt.plot(t, r_values, label=r"$R(t) = e^{-0.041867754t}(641.08e^{0.03678t} - 601.488e^{0.0318678t} + 15.59952)$", color="blue")
plt.title("Population Over Working Age (in Millions)", fontsize=16)
plt.xlabel("Time t (Years)", fontsize=14)
plt.ylabel("R(t)", fontsize=14)
plt.grid(alpha=0.5)
plt.legend(fontsize=12)
plt.show()