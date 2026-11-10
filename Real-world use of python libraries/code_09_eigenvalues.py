import matplotlib.pyplot as plt
import numpy as np

# Adjacency matrix for a small undirected network; nodes are A, B, C, D.
adjacency = np.array([[0., 1., 1., 0.], [1., 0., 1., 1.],
                      [1., 1., 0., 1.], [0., 1., 1., 0.]])
eigenvalues, eigenvectors = np.linalg.eig(adjacency)
index = np.argmax(np.real(eigenvalues))
dominant_value = np.real(eigenvalues[index])
vector = np.real(eigenvectors[:, index])
centrality = np.abs(vector) / np.abs(vector).sum()
nodes = ["A", "B", "C", "D"]

print("Dominant eigenvalue:", dominant_value)
print("Eigenvector-based importance:")
for node, score in zip(nodes, centrality):
    print(f"{node}: {score:.4f}")
print("Verification error:", np.linalg.norm(adjacency @ vector - dominant_value * vector))

plt.bar(nodes, centrality, color="slateblue")
plt.xlabel("Network node")
plt.ylabel("Normalized eigenvector centrality")
plt.title("Relative importance in the example network")
plt.grid(axis="y", alpha=0.3)
plt.tight_layout()
plt.show()
