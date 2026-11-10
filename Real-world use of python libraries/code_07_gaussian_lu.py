import matplotlib.pyplot as plt
import numpy as np
from scipy.linalg import lu_factor, lu_solve

# A simple three-zone thermal/resource model. Reuse A for several measurements.
A = np.array([[4., -1., 0.], [-1., 4., -1.], [0., -1., 3.]])
measurement_sets = [
    np.array([15., 10., 10.]),
    np.array([16., 11., 9.]),
    np.array([14., 12., 11.]),
]
lu, piv = lu_factor(A)  # factor the coefficient matrix once
solutions = []
for i, b in enumerate(measurement_sets, start=1):
    x = lu_solve((lu, piv), b)
    solutions.append(x)
    residual = b - A @ x
    print(f"Measurement set {i}")
    print("Solution:", x)
    print("Residual norm:", np.linalg.norm(residual))
    print()
print("Direct solution for first set:", np.linalg.solve(A, measurement_sets[0]))

solutions = np.array(solutions)
for zone in range(solutions.shape[1]):
    plt.plot(np.arange(1, len(solutions) + 1), solutions[:, zone], marker="o", label=f"Zone {zone + 1}")
plt.xlabel("Measurement set")
plt.ylabel("Solved value (model units)")
plt.title("Solutions from repeated LU solves")
plt.xticks([1, 2, 3])
plt.legend()
plt.grid(True, alpha=0.3)
plt.tight_layout()
plt.show()
