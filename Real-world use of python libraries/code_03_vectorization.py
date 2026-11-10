import timeit

import matplotlib.pyplot as plt
import numpy as np

# Simulated network latency readings (ms), generated reproducibly.
rng = np.random.default_rng(42)
latency_ms = rng.uniform(5, 250, 1_000_000)


def loop_version():
    squared_seconds = []
    for value in latency_ms:
        seconds = value / 1000.0
        squared_seconds.append(seconds**2)
    return squared_seconds


def vectorized_version():
    seconds = latency_ms / 1000.0
    return seconds**2


# Repeat both timings to reduce noise; loop's run count is lower due to its cost.
loop_time = timeit.timeit(loop_version, number=1)
vector_time = timeit.timeit(vectorized_version, number=3) / 3
result = vectorized_version()
speedup = loop_time / vector_time

print("First five squared latency values (s^2):", result[:5])
print(f"Loop time: {loop_time:.4f} s")
print(f"Vectorized time: {vector_time:.4f} s")
print(f"Approximate speed-up: {speedup:.1f}x")

plt.bar(["Python loop", "NumPy vectorized"], [loop_time, vector_time], color=["steelblue", "seagreen"])
plt.ylabel("Execution time (seconds)")
plt.title("One-million-value computation: loop vs vectorization")
plt.grid(axis="y", alpha=0.3)
plt.tight_layout()
plt.show()
