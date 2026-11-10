# Task 2: NumPy arrays and numerical computation

## Original example: hourly temperature sensor readings

`code_02_numpy_arrays.py` represents 24 hourly outdoor temperature readings. The `time_h` array contains hour labels 0–23, and `temperatures_c` contains temperatures in °C. These are sample readings for demonstrating numerical computation, not measurements from a particular place or date.

### Inputs and mathematical operations

- **Inputs:** 24 temperatures in °C and corresponding hour numbers.
- `np.mean` calculates the arithmetic mean (sum divided by 24); `np.min` and `np.max` find the lowest and highest reading.
- `1.8 * temperatures_c + 32` converts each Celsius value to Fahrenheit using \(F=1.8C+32\), vectorized across the array.
- Matplotlib plots all 24 readings, including hour 23. Rising segments indicate warming between sampled hours; falling segments indicate cooling. The sample reaches its maximum around midday and cools later.

### Input change and effect

Changing the hour-23 reading from 19.0 °C to 20.0 °C increases the daily mean by \((20-19)/24\approx0.04\) °C. The plotted final point rises by 1 °C, while the minimum and maximum remain unchanged because the altered value is still between them.

## Related real-world case: household smart-meter monitoring

`code_02_energy_monitoring.py` applies NumPy arrays to simulated hourly household electricity consumption.

### Assumptions and input data

- The 24 inputs are illustrative kWh consumed in each hourly interval, 00:00–23:00; they are not actual meter measurements.
- The values represent energy for each hour, not instantaneous power in kW, so summing them gives daily kWh.
- A flat tariff of 0.18 currency units/kWh is compared with 0.22 units/kWh. Taxes, fixed charges and time-of-use pricing are excluded; replace the generic currency and rates for local use.

### Output and interpretation

NumPy sums the readings, computes the mean hourly energy and identifies the maximum with `np.argmax`. The data total **16.18 kWh**; mean use is about **0.674 kWh per hour**; peak use is **1.40 kWh during 18:00–19:00**. Estimated costs are 16.18×0.18 = **2.9124** (2.91) and 16.18×0.22 = **3.5596** (3.56), a difference of **0.6472** (0.65) currency units. On the chart, the line shows hourly use and the dashed line is the hourly mean. Values above it are higher-use periods.

Changing the tariff from 0.18 to 0.22 increases the estimated variable charge by 0.6472 units. The consumption data and its graph do not change, since only the price parameter changed.

## Running the examples

Install dependencies if required:

```bash
python -m pip install numpy matplotlib
```

Run from the repository root:

```bash
python "Real-world use of python libraries/code_02_numpy_arrays.py"
python "Real-world use of python libraries/code_02_energy_monitoring.py"
```
