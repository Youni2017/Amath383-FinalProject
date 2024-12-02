import numpy as np
from scipy.integrate import odeint
import matplotlib.pyplot as plt

r_1 = 0.057
r_2 = 0.058
r_3 = 0.059
r_4 = 0.060
r_5 = 0.061
r_6 = 0.062
r_7 = 0.063

alpha = 0.06

def model(B, t, r):
    dBdt = r * B - alpha * B
    return dBdt

B0 = 72.832
t = np.linspace(0, 1000, 100)
solution = R(t)

def R(t):
    return np.exp(-0.041867754 * t) * (641.08 * np.exp(0.03678 * t) - 601.488 * np.exp(0.0318678 * t) + c_1)

c_1 = 15.59952
r_1values = odeint(model, B0, t, args=(r_1,))
r_2values = odeint(model, B0, t, args=(r_2,))
r_3values = odeint(model, B0, t, args=(r_3,))
r_4values = odeint(model, B0, t, args=(r_4,))
r_5values = odeint(model, B0, t, args=(r_5,))
r_6values = odeint(model, B0, t, args=(r_6,))
r_7values = odeint(model, B0, t, args=(r_7,))

plt.figure(figsize=(10, 6))
plt.plot(t, r_1values, label=r"$B(t); r = 0.057$", color="red")
plt.plot(t, r_2values, label=r"$B(t); r = 0.058$", color="green")
plt.plot(t, r_3values, label=r"$B(t); r = 0.059$", color="skyblue")
plt.plot(t, r_4values, label=r"$B(t); r = 0.060$", color="blue")
plt.plot(t, r_5values, label=r"$B(t); r = 0.061$", color="navy")
plt.plot(t, r_6values, label=r"$B(t); r = 0.062$", color="fuchsia")
plt.plot(t, r_7values, label=r"$B(t); r = 0.063$", color="purple")
plt.plot(t, solution, label=r"$R(t)$", color="orange")
plt.title("People over Working Age and People Under Working Age With Varying Birth Rate", fontsize=16)
plt.xlabel("Time t (Years)", fontsize=14)
plt.ylabel("Population (Millions)", fontsize=14)
plt.grid(alpha=0.5)
plt.ylim((-10,250))
plt.legend(fontsize=12, loc='upper right')
plt.show()