import matplotlib.pyplot as plt
import numpy as np

# Four corners of a square; each row is a point [x, y].
points = np.array([[0., 0.], [1., 0.], [1., 1.], [0., 1.]])
angle = np.deg2rad(45)
rotation = np.array([[np.cos(angle), -np.sin(angle)], [np.sin(angle), np.cos(angle)]])
scale = np.array([[2., 0.], [0., 1.5]])
transformation = rotation @ scale
transformed_points = points @ transformation.T

print("Original points:\n", points)
print("Transformation matrix:\n", transformation)
print("Transformed points:\n", transformed_points)
print("Determinant (area scale factor):", np.linalg.det(transformation))

closed_original = np.vstack([points, points[0]])
closed_transformed = np.vstack([transformed_points, transformed_points[0]])
plt.plot(closed_original[:, 0], closed_original[:, 1], "o-", label="Original square")
plt.plot(closed_transformed[:, 0], closed_transformed[:, 1], "o-", label="Rotated and scaled")
plt.axis("equal")
plt.xlabel("x")
plt.ylabel("y")
plt.title("2D matrix transformation")
plt.legend()
plt.grid(True)
plt.tight_layout()
plt.show()
