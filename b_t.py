import numpy as np
from scipy.integrate import odeint
import matplotlib.pyplot as plt

r = 0.05
alpha = 0.06

def model(B, t):
    dBdt = r * B - alpha * B
    return dBdt

B0 = 72.832
t = np.linspace(0, 1000, 100)
solution = odeint(model, B0, t)

plt.figure(figsize=(10, 6))
plt.plot(t, solution, label=r"$B(t) = 72.832 e^{-0.01t}$", color="red")
plt.title('Population Below Working Age (in Millions)', fontsize=16)
plt.xlabel("Time t (Years)", fontsize=14)
plt.ylabel("B(t)", fontsize=14)
plt.grid(alpha=0.5)
plt.legend(fontsize=12)
plt.show()