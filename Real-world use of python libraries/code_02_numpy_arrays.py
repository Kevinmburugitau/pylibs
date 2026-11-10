import numpy as np
import matplotlib.pyplot as plt

# Hours of the day: one sensor reading for each hour, from 00:00 to 23:00.
time_h = np.arange(24)

# Simulated outdoor temperature readings in degrees Celsius.
temperatures_c = np.array([
    18.5, 18.0, 17.8, 17.5, 17.9, 19.0,
    21.5, 23.8, 25.6, 27.1, 28.3, 29.0,
    29.4, 29.1, 28.5, 27.6, 26.2, 24.8,
    23.4, 22.1, 21.0, 20.2, 19.6, 19.0
])

# NumPy reductions summarize the day's readings.
mean_temp = np.mean(temperatures_c)
min_temp = np.min(temperatures_c)
max_temp = np.max(temperatures_c)

# Vectorized Celsius-to-Fahrenheit conversion: applies to all 24 values.
temperatures_f = 1.8 * temperatures_c + 32

print(f"Daily mean temperature: {mean_temp:.2f} °C")
print(f"Minimum temperature: {min_temp:.2f} °C")
print(f"Maximum temperature: {max_temp:.2f} °C")
print("First six Fahrenheit readings:", np.round(temperatures_f[:6], 2))

# Plot all 24 readings, including the 23:00 measurement.
plt.plot(time_h, temperatures_c, marker="o", label="Temperature")
plt.xlabel("Time of day (hours)")
plt.ylabel("Temperature (°C)")
plt.title("Simulated outdoor temperature over 24 hours")
plt.xticks(np.arange(0, 24, 2))
plt.legend()
plt.grid(True)
plt.tight_layout()
plt.show()
