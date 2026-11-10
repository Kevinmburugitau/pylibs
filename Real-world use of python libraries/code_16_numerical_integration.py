import matplotlib.pyplot as plt
import numpy as np
from scipy.integrate import simpson, trapezoid

# Smart-meter power samples every two hours; integrate kW over hours to get kWh.
time_hours = np.array([0, 2, 4, 6, 8, 10, 12], dtype=float)
power_kw = np.array([0.8, 1.0, 1.4, 1.8, 1.6, 1.2, 0.9])
energy_trapezoid = trapezoid(power_kw, x=time_hours)
energy_simpson = simpson(power_kw, x=time_hours)
print(f"Energy using trapezoidal rule: {energy_trapezoid:.3f} kWh")
print(f"Energy using Simpson's rule: {energy_simpson:.3f} kWh")
print(f"Difference between estimates: {abs(energy_simpson - energy_trapezoid):.3f} kWh")

fine_time = np.linspace(time_hours.min(), time_hours.max(), 300)
plt.plot(time_hours, power_kw, "o", label="Power samples")
plt.plot(fine_time, np.interp(fine_time, time_hours, power_kw), label="Linear guide between samples")
plt.fill_between(fine_time, np.interp(fine_time, time_hours, power_kw), alpha=0.2, label="Area ≈ energy")
plt.xlabel("Time (hours)")
plt.ylabel("Power (kW)")
plt.title("Numerical integration of household power use")
plt.legend()
plt.grid(True, alpha=0.3)
plt.tight_layout()
plt.show()
