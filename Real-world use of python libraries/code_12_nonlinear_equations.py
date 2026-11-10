import matplotlib.pyplot as plt
import numpy as np
from scipy.optimize import root

# Find intersections of a circle x^2+y^2=4 and a parabola y=x^2-1.
def equations(z):
    x, y = z
    return np.array([x**2 + y**2 - 4, y - (x**2 - 1)])

solutions = []
for guess in ([1., 1.], [-1., 1.], [1., -1.], [-1., -1.]):
    result = root(equations, guess)
    if result.success and not any(np.linalg.norm(result.x - old) < 1e-6 for old in solutions):
        solutions.append(result.x)
    print("Initial guess:", guess)
    print("Solution:", result.x)
    print("Residuals:", equations(result.x))
    print("Converged:", result.success)
    print()

x = np.linspace(-2, 2, 500)
y_circle = np.sqrt(np.maximum(0, 4 - x**2))
plt.plot(x, x**2 - 1, label="Parabola: y=x²−1")
plt.plot(x, y_circle, label="Circle upper half")
plt.plot(x, -y_circle, label="Circle lower half")
if solutions:
    points = np.array(solutions)
    plt.scatter(points[:, 0], points[:, 1], color="red", zorder=3, label="Numerical intersections")
plt.xlim(-2, 2)
plt.ylim(-2.2, 2.2)
plt.xlabel("x")
plt.ylabel("y")
plt.title("Nonlinear system: circle and parabola intersections")
plt.legend()
plt.grid(True, alpha=0.3)
plt.tight_layout()
plt.show()
