import matplotlib.pyplot as plt
import numpy as np
from scipy.integrate import solve_ivp

# RC charging circuit: dV/dt=(Vs-V)/(R*C).
supply_voltage = 5.0
resistance_ohms = 1000.0
capacitance_farads = 0.001
initial_voltage = 0.0

def rc_circuit(_time, voltage):
    return [(supply_voltage - voltage[0]) / (resistance_ohms * capacitance_farads)]

t_eval = np.linspace(0, 5, 200)
solution = solve_ivp(rc_circuit, (0, 5), [initial_voltage], t_eval=t_eval, rtol=1e-9, atol=1e-11)
exact = supply_voltage * (1 - np.exp(-solution.t / (resistance_ohms * capacitance_farads)))
print("Solver success:", solution.success)
print(f"Capacitor voltage at 5 s: {solution.y[0, -1]:.4f} V")
print(f"Maximum error against exact solution: {np.max(np.abs(solution.y[0] - exact)):.3e} V")

plt.plot(solution.t, solution.y[0], label="SciPy solve_ivp")
plt.plot(solution.t, exact, linestyle="--", label="Exact solution")
plt.xlabel("Time (s)")
plt.ylabel("Capacitor voltage (V)")
plt.title("RC circuit charging")
plt.legend()
plt.grid(True, alpha=0.3)
plt.tight_layout()
plt.show()
