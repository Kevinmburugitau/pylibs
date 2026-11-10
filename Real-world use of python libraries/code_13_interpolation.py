import matplotlib.pyplot as plt
import numpy as np
from scipy.interpolate import CubicSpline, interp1d

# Hourly temperature sensor readings (illustrative data).
hours = np.array([8, 9, 10, 11, 12, 13, 14], dtype=float)
temperature = np.array([18.0, 20.0, 22.5, 24.0, 25.0, 25.5, 25.0])
linear = interp1d(hours, temperature, kind="linear")
cubic = CubicSpline(hours, temperature)
query_times = np.linspace(hours.min(), hours.max(), 121)
linear_estimates = linear(query_times)
cubic_estimates = cubic(query_times)

target_time = 10.5
print(f"Linear estimate at 10:30: {float(linear(target_time)):.2f} °C")
print(f"Cubic estimate at 10:30: {float(cubic(target_time)):.2f} °C")

plt.scatter(hours, temperature, color="black", label="Hourly measurements", zorder=3)
plt.plot(query_times, linear_estimates, label="Linear interpolation")
plt.plot(query_times, cubic_estimates, label="Cubic spline")
plt.xlabel("Hour of day")
plt.ylabel("Temperature (°C)")
plt.title("Estimating temperatures between sensor readings")
plt.legend()
plt.grid(True, alpha=0.3)
plt.tight_layout()
plt.show()
