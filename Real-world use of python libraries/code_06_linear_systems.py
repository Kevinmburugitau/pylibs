import matplotlib.pyplot as plt
import numpy as np

# Resource accounting model: x=Type A servers, y=Type B servers.
# A uses 4 CPU units and 8 GB memory; B uses 2 CPU units and 12 GB memory.
A = np.array([[4., 2.], [8., 12.]])
b = np.array([20., 72.])  # observed CPU and memory usage
solution = np.linalg.solve(A, b)
residual = b - A @ solution

print(f"Type A servers: {solution[0]:.0f}")
print(f"Type B servers: {solution[1]:.0f}")
print("Reconstructed resource usage [CPU, GB]:", A @ solution)
print("Residual:", residual)
print("Residual norm:", np.linalg.norm(residual))

labels = ["CPU units", "Memory (GB)"]
observed = b
reconstructed = A @ solution
positions = np.arange(len(labels))
width = 0.36
plt.bar(positions - width / 2, observed, width, label="Observed")
plt.bar(positions + width / 2, reconstructed, width, label="From solution")
plt.xticks(positions, labels)
plt.ylabel("Resource amount")
plt.title("Linear-system solution check")
plt.legend()
plt.grid(axis="y", alpha=0.3)
plt.tight_layout()
plt.show()
