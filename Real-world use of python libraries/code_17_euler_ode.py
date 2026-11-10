import matplotlib.pyplot as plt
import numpy as np

# Newton's law of cooling: dT/dt = -k(T - T_ambient).
ambient_c = 25.0
initial_c = 90.0
cooling_rate_per_min = 0.12
step_minutes = 1.0
end_minutes = 30.0


def rate(temperature):
    return -cooling_rate_per_min * (temperature - ambient_c)


time = np.arange(0, end_minutes + step_minutes, step_minutes)
temperature = np.zeros_like(time)
temperature[0] = initial_c
for i in range(len(time) - 1):
    temperature[i + 1] = temperature[i] + step_minutes * rate(temperature[i])
exact = ambient_c + (initial_c - ambient_c) * np.exp(-cooling_rate_per_min * time)
print(f"Euler temperature after {end_minutes:.0f} min: {temperature[-1]:.2f} °C")
print(f"Exact temperature after {end_minutes:.0f} min: {exact[-1]:.2f} °C")
print(f"Final absolute error: {abs(temperature[-1] - exact[-1]):.4f} °C")

plt.plot(time, temperature, marker="o", markevery=3, label="Euler approximation")
plt.plot(time, exact, linestyle="--", label="Exact solution")
plt.xlabel("Time (minutes)")
plt.ylabel("Temperature (°C)")
plt.title("Cooling of a hot object")
plt.legend()
plt.grid(True, alpha=0.3)
plt.tight_layout()
plt.show()
