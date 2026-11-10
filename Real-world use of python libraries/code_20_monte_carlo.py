import matplotlib.pyplot as plt
import numpy as np

# Monte Carlo estimate of overload risk for an illustrative server workload.
rng = np.random.default_rng(42)
capacity = 1000.0
mean_demand = 850.0
std_demand = 120.0
number_of_simulations = 100_000
demand = rng.normal(mean_demand, std_demand, number_of_simulations)
overloaded = demand > capacity
overload_probability = overloaded.mean()
print(f"Estimated overload probability: {overload_probability:.4%}")
print(f"Number of overload cases: {overloaded.sum()} out of {number_of_simulations}")

running_probability = np.cumsum(overloaded) / np.arange(1, number_of_simulations + 1)
indices = np.unique(np.logspace(1, np.log10(number_of_simulations), 200).astype(int)) - 1

fig, axes = plt.subplots(1, 2, figsize=(11, 4))
axes[0].hist(demand, bins=60, density=True, alpha=0.75, color="steelblue")
axes[0].axvline(capacity, color="red", linestyle="--", label=f"Capacity = {capacity:.0f}")
axes[0].set(xlabel="Demand (work units)", ylabel="Density", title="Simulated demand distribution")
axes[0].legend()
axes[0].grid(True, alpha=0.2)
axes[1].semilogx(indices + 1, running_probability[indices], label="Running estimate")
axes[1].axhline(overload_probability, color="red", linestyle="--", label="Final estimate")
axes[1].set(xlabel="Number of simulations", ylabel="Estimated overload probability", title="Monte Carlo convergence")
axes[1].legend()
axes[1].grid(True, which="both", alpha=0.2)
fig.tight_layout()
plt.show()
