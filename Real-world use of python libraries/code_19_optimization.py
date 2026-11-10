import matplotlib.pyplot as plt
import numpy as np
from scipy.optimize import minimize

# Minimize server capacity planning cost, subject to required capacity.
# Type A: cost 12, capacity 100; Type B: cost 18, capacity 170.
required_capacity = 1000.0

def cost(allocation):
    x, y = allocation
    return 12 * x + 18 * y

def capacity_constraint(allocation):
    x, y = allocation
    return 100 * x + 170 * y - required_capacity

solution = minimize(cost, x0=[5., 3.], method="SLSQP", bounds=[(0, None), (0, None)],
                    constraints={"type": "ineq", "fun": capacity_constraint})
x_opt, y_opt = solution.x
print("Optimization success:", solution.success)
print(f"Continuous Type A allocation: {x_opt:.3f}")
print(f"Continuous Type B allocation: {y_opt:.3f}")
print(f"Total capacity: {100*x_opt + 170*y_opt:.2f}")
print(f"Minimum continuous planning cost: {solution.fun:.2f}")

# Check integer allocations because actual servers are indivisible.
best_integer = None
for a in range(21):
    for b in range(21):
        capacity = 100 * a + 170 * b
        total_cost = 12 * a + 18 * b
        if capacity >= required_capacity and (best_integer is None or total_cost < best_integer[0]):
            best_integer = (total_cost, a, b, capacity)
print("Best integer solution (cost, Type A, Type B, capacity):", best_integer)

# Plot feasible region and the continuous optimum.
y_values = np.linspace(0, 9, 300)
x_boundary = (required_capacity - 170 * y_values) / 100
feasible_x = np.maximum(0, x_boundary)
plt.fill_betweenx(y_values, feasible_x, 12, where=feasible_x <= 12, alpha=0.18, label="Feasible (capacity ≥ target)")
plt.plot(feasible_x, y_values, color="black", label="Capacity boundary")
plt.scatter([x_opt], [y_opt], color="red", zorder=3, label="Continuous optimum")
if best_integer:
    plt.scatter([best_integer[1]], [best_integer[2]], color="green", marker="s", zorder=3, label="Best integer plan")
plt.xlim(0, 12)
plt.ylim(0, 9)
plt.xlabel("Type A server units")
plt.ylabel("Type B server units")
plt.title("Server capacity cost optimization")
plt.legend()
plt.grid(True, alpha=0.3)
plt.tight_layout()
plt.show()
