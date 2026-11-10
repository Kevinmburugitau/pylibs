# Task 2: NumPy arrays and numerical computation

## Original example: hourly temperature sensor readings

The existing `code_02_numpy_arrays.py` example represents 24 hourly outdoor temperature readings. The `time_h` array contains hour labels from 0 to 23, and `temperatures_c` contains temperatures in degrees Celsius at those hours. These are sample readings for demonstrating numerical computation, not a claim about a particular location or day.

### Inputs and mathematical operations

- **Inputs:** 24 temperatures in °C and the corresponding hour numbers.
- `np.mean(temperatures_c)` calculates the arithmetic mean: the sum of the readings divided by 24.
- `np.min(...)` and `np.max(...)` find the lowest and highest reading.
- `1.8 * temperatures_c + 32` performs a vectorized Celsius-to-Fahrenheit conversion for every array element using \(F = 1.8C + 32\).
- Matplotlib plots temperature against hour. The graph now includes all 24 values, including the reading at hour 23.

The mean, minimum, and maximum summarize the day; they do not describe every fluctuation. On the graph, an upward segment means the temperature rose between consecutive hourly readings, while a downward segment means it fell. The maximum occurs around midday in this sample, followed by a general evening decline.

### Parameter/input change and its effect

The last recorded temperature is 19.0 °C at hour 23. If that input is changed to 20.0 °C, the maximum remains 29.4 °C and the minimum remains 17.5 °C, but the daily mean rises by \((20.0-19.0)/24 = 0.0417\) °C (about 0.04 °C). The final plotted point also moves upward by 1.0 °C. This demonstrates that one reading changes the mean and the local graph while not necessarily changing the extrema.

## Related real-world case: household smart-meter energy monitoring

`code_02_energy_monitoring.py` adapts the array computations to simulated hourly electricity consumption. This is a related sensor-data application, but it answers a different question: how much energy was used and what might it cost?

### Assumptions and input data

- The 24 numbers are illustrative hourly energy amounts in kWh, one for each hour 00:00–23:00; they are not actual meter data.
- The daily total is the sum of the hourly amounts. This assumes each number is already energy consumed during that hour, not an instantaneous power reading in kW.
- The example tariff is a flat 0.18 currency units per kWh, with no taxes, fixed fees, time-of-use rates, or other charges. The comparison tariff is 0.22 per kWh.
- The currency is intentionally generic; replace the tariff values and label with the applicable local currency when using real data.

### Outputs and interpretation

NumPy calculates total daily energy (`np.sum`), average hourly energy (`np.mean`), and the peak-usage hour (`np.argmax`). Multiplying total kWh by the assumed tariff estimates the daily variable-energy charge. With the provided values, total energy is **16.93 kWh** and the peak is **1.40 kWh during 18:00–19:00**. At 0.18 per kWh, the estimated cost is **3.0474 currency units** (printed to two decimal places as 3.05); at 0.22 per kWh it is **3.7246** (3.72), an increase of **0.6772** (0.68). The plot shows hourly consumption, and its dashed horizontal line marks the average hourly amount. A peak above that line indicates an hour with greater-than-average use.

Changing `tariff_per_kwh` from 0.18 to 0.22 raises the estimated cost for the same usage by 0.6772 units. The energy readings and graph do not change because only the price parameter changed.

## Run the examples

Install the dependencies if needed:

```bash
python -m pip install numpy matplotlib
```

Run either script from the repository root:

```bash
python "Real-world use of python libraries/code_02_numpy_arrays.py"
python "Real-world use of python libraries/code_02_energy_monitoring.py"
```
