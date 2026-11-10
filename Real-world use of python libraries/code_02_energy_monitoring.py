"""Analyze simulated hourly smart-meter readings with NumPy.

This related Task 2 example applies array operations to household energy use.
The readings are illustrative, not measurements from a real household.
"""

import numpy as np
import matplotlib.pyplot as plt

hours = np.arange(24)
# Simulated electricity consumption during each hour, in kilowatt-hours (kWh).
energy_kwh = np.array([
    0.35, 0.30, 0.28, 0.27, 0.30, 0.45,
    0.80, 1.10, 0.75, 0.60, 0.55, 0.58,
    0.62, 0.57, 0.60, 0.72, 0.95, 1.25,
    1.40, 1.15, 0.90, 0.72, 0.55, 0.42
])

# Assumed electricity tariff. Change this parameter to explore the bill impact.
tariff_per_kwh = 0.18  # currency units per kWh
comparison_tariff_per_kwh = 0.22

total_energy_kwh = np.sum(energy_kwh)
mean_hourly_energy_kwh = np.mean(energy_kwh)
peak_hour_index = int(np.argmax(energy_kwh))
peak_hour_energy_kwh = energy_kwh[peak_hour_index]
estimated_cost = total_energy_kwh * tariff_per_kwh
comparison_cost = total_energy_kwh * comparison_tariff_per_kwh
cost_difference = comparison_cost - estimated_cost

print(f"Total daily energy: {total_energy_kwh:.2f} kWh")
print(f"Mean hourly energy: {mean_hourly_energy_kwh:.2f} kWh")
print(
    f"Peak usage: {peak_hour_energy_kwh:.2f} kWh at "
    f"{peak_hour_index:02d}:00"
)
print(f"Estimated daily cost at {tariff_per_kwh:.2f}/kWh: {estimated_cost:.2f}")
print(
    f"Estimated daily cost at {comparison_tariff_per_kwh:.2f}/kWh: "
    f"{comparison_cost:.2f} "
    f"(increase of {cost_difference:.2f})"
)

plt.plot(hours, energy_kwh, marker="o", label="Hourly consumption")
plt.axhline(mean_hourly_energy_kwh, color="orange", linestyle="--", label="Daily hourly mean")
plt.xlabel("Hour of day")
plt.ylabel("Energy consumed (kWh)")
plt.title("Simulated household electricity use")
plt.xticks(np.arange(0, 24, 2))
plt.grid(True)
plt.legend()
plt.tight_layout()
plt.show()
