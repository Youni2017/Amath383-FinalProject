import numpy as np
from scipy.integrate import odeint
import matplotlib.pyplot as plt

r_values = np.linspace(0.05, 0.085, 8)
alpha = 0.06
beta = 0.0193
gamma = 0.0137
delta = 0.04186

B0 = 72.832
R0 = 55.19152
W0 = 211.52284
C_values = []

t = np.linspace(0, 1000, 100)

def C_solve(r):
    right_side = (alpha * B0) / (r - alpha - (gamma - beta))
    return W0 - right_side

C_values = [C_solve(r) for r in r_values]

def model_b(B, t, r):
    return r * B - alpha * B

def model_r(R, t, r, C):
    B_term = (alpha * B0) / (r - alpha - (gamma - beta)) * np.exp((r - alpha) * t)
    return -delta * R + beta * (B_term + C * np.exp((gamma - beta) * t))

B_solutions = []
R_solutions = []

for r, C in zip(r_values, C_values):
    B_solution = odeint(model_b, B0, t, args=(r,))
    R_solution = odeint(model_r, R0, t, args=(r, C))
    B_solutions.append(B_solution.flatten())
    R_solutions.append(R_solution.flatten())

fig, axes = plt.subplots(2, 4, figsize=(20, 10))
axes = axes.flatten()

custom_xlim = (0, 1000)
custom_ylim = (0, 800)

plt.setp(axes, xlim=custom_xlim)


for i, r in enumerate(r_values):
    axes[i].plot(t, B_solutions[i], label=f"$B(t)$; r = {r:.3f}", color="red", linestyle='--')
    axes[i].plot(t, R_solutions[i], label=f"$R(t)$; r = {r:.3f}", color="blue")
    axes[i].legend()
    axes[i].set_title(f"Plots for r = {r:.3f}")
    axes[i].set_xlabel("Time")
    axes[i].set_ylabel("Value")
    axes[i].set_ylim(bottom=0)

plt.tight_layout()
plt.show()
