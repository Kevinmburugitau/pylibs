import matplotlib.pyplot as plt
import numpy as np

# GPS samples: time in seconds and position in metres.
time = np.array([0, 1, 2, 3, 4, 5, 6], dtype=float)
position = np.array([0.0, 4.8, 10.2, 16.1, 22.7, 30.0, 38.0])
speed = np.empty_like(position)
# One-sided differences at endpoints and central differences inside.
speed[0] = (position[1] - position[0]) / (time[1] - time[0])
speed[1:-1] = (position[2:] - position[:-2]) / (time[2:] - time[:-2])
speed[-1] = (position[-1] - position[-2]) / (time[-1] - time[-2])

for t, x, v in zip(time, position, speed):
    print(f"t={t:.0f} s, position={x:.1f} m, estimated speed={v:.2f} m/s")

fig, axes = plt.subplots(2, 1, figsize=(7, 7), sharex=True)
axes[0].plot(time, position, marker="o")
axes[0].set_ylabel("Position (m)")
axes[0].set_title("Position samples and finite-difference speed")
axes[1].plot(time, speed, marker="o", color="darkorange")
axes[1].set_xlabel("Time (s)")
axes[1].set_ylabel("Estimated speed (m/s)")
for axis in axes:
    axis.grid(True, alpha=0.3)
fig.tight_layout()
plt.show()
