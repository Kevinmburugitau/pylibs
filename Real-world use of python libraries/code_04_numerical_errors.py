import matplotlib.pyplot as plt
import numpy as np

# Floating-point values are approximations in binary representation.
calculated = 0.1 + 0.2
expected = 0.3
print("0.1 + 0.2 =", calculated)
print("Exact comparison:", calculated == expected)
print("Tolerance-based comparison:", np.isclose(calculated, expected))

# Compare an approximation to the known value sqrt(2).
true_value = np.sqrt(2)
approx_value = 1.414
absolute_error = abs(true_value - approx_value)
relative_error = absolute_error / abs(true_value)
print(f"Absolute error: {absolute_error:.8f}")
print(f"Relative error: {relative_error:.8%}")

# Algebraically equivalent expressions; the rationalized one avoids cancellation.
x_values = np.logspace(-14, -2, 100)
direct_values = (np.sqrt(1 + x_values) - 1) / x_values
stable_values = 1 / (np.sqrt(1 + x_values) + 1)
for x in [1e-4, 1e-8, 1e-12]:
    direct = (np.sqrt(1 + x) - 1) / x
    stable = 1 / (np.sqrt(1 + x) + 1)
    print(f"x={x:.0e}: direct={direct:.12f}, stable={stable:.12f}")

plt.semilogx(x_values, np.abs(direct_values - 0.5), label="Direct formula error")
plt.semilogx(x_values, np.abs(stable_values - 0.5), label="Stable formula error")
plt.xlabel("x")
plt.ylabel("Absolute error from limiting value 0.5")
plt.title("Cancellation error for small x")
plt.legend()
plt.grid(True, which="both", alpha=0.3)
plt.tight_layout()
plt.show()
