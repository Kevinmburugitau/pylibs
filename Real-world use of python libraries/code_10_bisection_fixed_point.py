import matplotlib.pyplot as plt
import numpy as np
from scipy.optimize import root_scalar

# A simplified heat-balance model; a root means gains equal losses.
def heat_balance(temperature):
    return temperature - 25 - 10 * np.exp(-temperature / 20)

bisect_result = root_scalar(heat_balance, bracket=[20, 40], method="bisect", xtol=1e-10)

# Fixed-point iteration for T = 25 + 10 exp(-T/20).
def fixed_point_map(temperature):
    return 25 + 10 * np.exp(-temperature / 20)

current = 30.0
history = [current]
for _ in range(100):
    updated = fixed_point_map(current)
    history.append(updated)
    if abs(updated - current) < 1e-10:
        break
    current = updated

print(f"Bisection equilibrium temperature: {bisect_result.root:.6f} °C")
print(f"Fixed-point equilibrium temperature: {history[-1]:.6f} °C")
print("Fixed-point iterations:", len(history) - 1)

temperatures = np.linspace(20, 40, 300)
fig, axes = plt.subplots(1, 2, figsize=(11, 4))
axes[0].plot(temperatures, heat_balance(temperatures))
axes[0].axhline(0, color="black", linewidth=0.8)
axes[0].axvline(bisect_result.root, linestyle="--", label=f"Root = {bisect_result.root:.2f} °C")
axes[0].set(xlabel="Temperature (°C)", ylabel="Heat-balance function", title="Root of heat-balance equation")
axes[0].legend()
axes[0].grid(True, alpha=0.3)
axes[1].plot(np.arange(len(history)), history, marker=".")
axes[1].axhline(bisect_result.root, linestyle="--", color="gray", label="Equilibrium")
axes[1].set(xlabel="Iteration", ylabel="Temperature (°C)", title="Fixed-point iteration")
axes[1].legend()
axes[1].grid(True, alpha=0.3)
fig.tight_layout()
plt.show()
