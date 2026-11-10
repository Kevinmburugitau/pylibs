import matplotlib.pyplot as plt
import numpy as np

# Simplified steady-state temperature model at five interior grid points.
# The diagonally dominant system is suitable for Jacobi and Gauss-Seidel.
A = np.array([[2., -1., 0., 0., 0.], [-1., 2., -1., 0., 0.],
              [0., -1., 2., -1., 0.], [0., 0., -1., 2., -1.],
              [0., 0., 0., -1., 2.]])
b = np.array([100., 0., 0., 0., 20.])  # boundary contributions


def jacobi(matrix, rhs, tol=1e-8, max_iter=500):
    diagonal = np.diag(matrix)
    remainder = matrix - np.diagflat(diagonal)
    x = np.zeros_like(rhs)
    errors = []
    for _ in range(max_iter):
        x_new = (rhs - remainder @ x) / diagonal
        error = np.linalg.norm(x_new - x, ord=np.inf)
        errors.append(error)
        if error < tol:
            return x_new, errors
        x = x_new
    return x, errors


def gauss_seidel(matrix, rhs, tol=1e-8, max_iter=500):
    x = np.zeros_like(rhs)
    errors = []
    for _ in range(max_iter):
        old = x.copy()
        for i in range(len(rhs)):
            x[i] = (rhs[i] - matrix[i, :i] @ x[:i] - matrix[i, i + 1:] @ old[i + 1:]) / matrix[i, i]
        error = np.linalg.norm(x - old, ord=np.inf)
        errors.append(error)
        if error < tol:
            return x, errors
    return x, errors


x_j, err_j = jacobi(A, b)
x_gs, err_gs = gauss_seidel(A, b)
x_exact = np.linalg.solve(A, b)
print("Jacobi temperatures:", x_j)
print("Gauss-Seidel temperatures:", x_gs)
print("Direct solution:", x_exact)

plt.semilogy(np.arange(1, len(err_j) + 1), err_j, label="Jacobi")
plt.semilogy(np.arange(1, len(err_gs) + 1), err_gs, label="Gauss-Seidel")
plt.xlabel("Iteration")
plt.ylabel("Maximum change (°C)")
plt.title("Convergence of iterative temperature solution")
plt.legend()
plt.grid(True, which="both", alpha=0.3)
plt.tight_layout()
plt.show()
