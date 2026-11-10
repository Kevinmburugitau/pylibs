import matplotlib.pyplot as plt
import numpy as np
from scipy.optimize import root_scalar

# Initial investment and subsequent annual cash inflows (currency units).
cash_flows = np.array([-10000., 3000., 3500., 4000., 2500.])


def npv(rate):
    periods = np.arange(cash_flows.size)
    return np.sum(cash_flows / (1 + rate) ** periods)


def d_npv(rate):
    periods = np.arange(1, cash_flows.size)
    return np.sum(-periods * cash_flows[1:] / (1 + rate) ** (periods + 1))


newton = root_scalar(npv, fprime=d_npv, x0=0.10, method="newton", xtol=1e-12)
secant = root_scalar(npv, x0=0.05, x1=0.20, method="secant", xtol=1e-12)
print(f"IRR using Newton-Raphson: {newton.root:.6%}")
print(f"IRR using Secant method: {secant.root:.6%}")
print(f"NPV at Newton solution: {npv(newton.root):.6f}")

rates = np.linspace(-0.2, 0.6, 400)
plt.plot(rates * 100, [npv(rate) for rate in rates], label="Net present value")
plt.axhline(0, color="black", linewidth=0.8)
plt.axvline(newton.root * 100, linestyle="--", label=f"IRR = {newton.root:.2%}")
plt.xlabel("Discount rate (%)")
plt.ylabel("NPV (currency units)")
plt.title("IRR is the discount rate where NPV equals zero")
plt.legend()
plt.grid(True, alpha=0.3)
plt.tight_layout()
plt.show()
