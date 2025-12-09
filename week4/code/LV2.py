#!/usr/bin/env python3

"""
Auther: Ximan Ding (x.ding25@imperial.ac.uk)
Script: LV2.py
Des: Lotka–Volterra model with density-dependent resource (logistic growth).
      Takes parameters from the command line and saves plots as PDF files.
Usage: python3 LV2.py r a z e K
       (all parameters are floats; if omitted, default values are used)
Date: Nov, 2025
"""

# Docstrings are considered part of the running code (normal comments are
# stripped). Hence, you can access your docstrings at run time.

__author__ = "Ximan Ding (x.ding25@imperial.ac.uk)"
__version__ = "0.0.1"

import sys
import numpy as np
import scipy.integrate as integrate
import matplotlib.pylab as p


# -----------------------------
# Global default parameter values
# -----------------------------
# r : intrinsic growth rate of the resource
# a : attack/search rate of consumer on resource
# z : mortality rate of the consumer
# e : efficiency of converting resource into consumer biomass
# K : carrying capacity of the resource (logistic term)
r = 1.0
a = 0.1
z = 1.5
e = 0.75
K = 50.0  # default carrying capacity


def dCR_dt(pops, t=0):
    """
    Returns the derivatives dR/dt and dC/dt for the modified Lotka–Volterra model.
    """
    R = pops[0]
    C = pops[1]

    dRdt = r * R * (1.0 - R / K) - a * C * R
    dCdt = -z * C + e * a * C * R

    return np.array([dRdt, dCdt])


def parse_parameters(argv):
    """
    Parse command line arguments for the LV model parameters.
    """
    global r, a, z, e, K

    if len(argv) == 6:
        try:
            r = float(argv[1])
            a = float(argv[2])
            z = float(argv[3])
            e = float(argv[4])
            K = float(argv[5])
            print(f"Using command line parameters: r={r}, a={a}, z={z}, e={e}, K={K}")
        except ValueError:
            # If conversion fails, fall back to defaults
            print("Could not convert arguments to floats. Using default parameters:")
            print(f"r={r}, a={a}, z={z}, e={e}, K={K}")
    else:
        # Inform user of usage and defaults
        print("Usage: python3 LV2.py r a z e K")
        print("No or incorrect number of parameters supplied; using default values:")
        print(f"r={r}, a={a}, z={z}, e={e}, K={K}")


def run_simulation():
    """
    Run the LV model simulation and return time vector and populations.
    """
    # Time vector: integrate from t=0 to t=50 with 1000 steps
    t = np.linspace(0, 50, 1000)

    # Initial conditions for resource and consumer
    R0 = 10.0
    C0 = 5.0
    RC0 = np.array([R0, C0])

    # Numerically integrate the system
    pops, infodict = integrate.odeint(
        dCR_dt, RC0, t, full_output=True
    )

    # Check integration status (optional debug output)
    if "message" in infodict:
        print("ODE solver message:", infodict["message"])

    return t, pops


def save_time_series_plot(t, pops, outpath="../results/LV2_time_series.pdf"):
    """
    Save a time series plot of resource and consumer densities.
    """
    f1 = p.figure()

    # Plot resource and consumer over time
    p.plot(t, pops[:, 0], "g-", label="Resource density (R)")
    p.plot(t, pops[:, 1], "b-", label="Consumer density (C)")
    p.grid(True)
    p.xlabel("Time")
    p.ylabel("Population density")

    # Add parameter values to the title for clarity
    p.title(
        f"LV with logistic resource: r={r}, a={a}, z={z}, e={e}, K={K}"
    )

    p.legend(loc="best")

    # Save figure without displaying it on screen
    f1.savefig(outpath)
    p.close(f1)


def save_phase_plot(pops, outpath="../results/LV2_phase_plot.pdf"):
    """
    Save the phase-plane plot (R vs C).
    """
    f2 = p.figure()

    # Phase plot: consumer vs resource
    p.plot(pops[:, 0], pops[:, 1], "r-")
    p.grid(True)
    p.xlabel("Resource density (R)")
    p.ylabel("Consumer density (C)")
    p.title(
        f"Phase plot (R vs C) for LV with logistic resource\n"
        f"r={r}, a={a}, z={z}, e={e}, K={K}"
    )

    f2.savefig(outpath)
    p.close(f2)


def main(argv):
    """
    Main entry point of the script.
    """
    # Step 1: Get parameters from command line (if provided)
    parse_parameters(argv)

    # Step 2: Run the simulation
    t, pops = run_simulation()

    # Step 3: Save plots
    save_time_series_plot(t, pops)
    save_phase_plot(pops)

    # Step 4: Print final population values (last time point)
    R_final = pops[-1, 0]
    C_final = pops[-1, 1]
    print(
        f"Final populations at t={t[-1]:.2f}: "
        f"R_final={R_final:.4f}, C_final={C_final:.4f}"
    )

    return 0


if __name__ == "__main__":
    status = main(sys.argv)
    sys.exit(status)