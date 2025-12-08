#!/usr/bin/env python3

"""
Auther: Ximan Ding (x.ding25@imperial.ac.uk)
Script: LV1.py
Des: Simulate the Lotka-Volterra predator-prey model and save
     (1) time-series plot and
     (2) phase-plane plot (Resource vs Consumer)
     as PDF files in the ../results directory.
Usage: python3 LV1.py (in terminal)
Date: Nov, 2025
"""

# Docstrings are considered part of the running code (normal comments are
# stripped). Hence, you can access your docstrings at run time.

__author__ = "Ximan Ding (x.ding25@imperial.ac.uk)"
__version__ = "0.0.1"


## imports ##
import sys

import numpy as np                      # Numerical arrays and tools
import scipy.integrate as integrate     # ODE solver (odeint)
import matplotlib.pylab as p            # Plotting (Matplotlib)


## functions ##

def dCR_dt(pops, t=0, r=1., a=0.1, z=1.5, e=0.75):
    """
    Returns the growth rates of resource (R) and consumer (C)
    populations at time t for the Lotka-Volterra model.

    Parameters:
    pops : array-like, shape (2,)
        Current population densities [R, C].
    t : float, optional
        Time (not used explicitly because the system is autonomous,
        but required by odeint's API).
    r : float, optional
        Intrinsic growth rate of the resource.
    a : float, optional
        Consumer search rate * attack success probability.
    z : float, optional
        Consumer mortality rate.
    e : float, optional
        Efficiency of converting consumed resource into consumer biomass.

    Returns:
    numpy.ndarray, shape (2,)
        [dRdt, dCdt], time derivatives of resource and consumer.
    """
    R = pops[0]
    C = pops[1]

    # Resource equation: dR/dt = rR - aCR
    dRdt = r * R - a * R * C

    # Consumer equation: dC/dt = -zC + e a C R
    dCdt = -z * C + e * a * R * C

    return np.array([dRdt, dCdt])


def simulate_lv(t_max=15, n_steps=1000,
                R0=10, C0=5,
                r=1., a=0.1, z=1.5, e=0.75):
    """
    Simulate the Lotka-Volterra model over a time interval.

    Parameters:
    t_max : float
        Final time of simulation.
    n_steps : int
        Number of time points between 0 and t_max.
    R0 : float
        Initial resource density.
    C0 : float
        Initial consumer density.
    r, a, z, e : float
        Lotka-Volterra model parameters.

    Returns:
    t : numpy.ndarray
        Time points of the simulation.
    pops : numpy.ndarray, shape (n_steps, 2)
        Population trajectories; column 0 = R(t), column 1 = C(t).
    """
    # Time vector
    t = np.linspace(0, t_max, n_steps)

    # Initial conditions array
    RC0 = np.array([R0, C0])

    # Solve ODE system
    pops, info = integrate.odeint(
        dCR_dt, RC0, t,
        args=(r, a, z, e),
        full_output=True
    )

    # Optional: check if integration was successful
    # print(info["message"])

    return t, pops


def make_time_series_plot(t, pops, outfile):
    """
    Create and save a time-series plot of R(t) and C(t).

    Parameters:
    t : numpy.ndarray
        Time points.
    pops : numpy.ndarray
        Population trajectories (columns: 0 = R, 1 = C).
    outfile : str
        Path to the PDF file where the figure will be saved.
    """
    f = p.figure()

    # Plot resource and consumer densities over time
    p.plot(t, pops[:, 0], 'g-', label='Resource density')
    p.plot(t, pops[:, 1], 'b-', label='Consumer density')

    p.grid(True)
    p.legend(loc='best')
    p.xlabel('Time')
    p.ylabel('Population density')
    p.title('Lotka-Volterra Consumer-Resource Dynamics')

    # Save figure to file (no display)
    f.savefig(outfile)
    p.close(f)   # Close figure to free memory


def make_phase_plot(pops, outfile):
    """
    Create and save a phase-plane plot (Resource vs Consumer).

    Parameters
    ----------
    pops : numpy.ndarray
        Population trajectories (columns: 0 = R, 1 = C).
    outfile : str
        Path to the PDF file where the figure will be saved.
    """
    f = p.figure()

    # Phase plot: Resource (R) on x-axis, Consumer (C) on y-axis
    p.plot(pops[:, 0], pops[:, 1], 'r-')
    p.xlabel('Resource density')
    p.ylabel('Consumer density')
    p.title('Lotka-Volterra Phase Plot (C vs R)')
    p.grid(True)

    # Save figure to file (no display)
    f.savefig(outfile)
    p.close(f)


def main(argv):
    """
    Main entry point of the program.

    Simulates the Lotka-Volterra model and saves two figures:
    1. Time-series plot  -> ../results/LV_model.pdf
    2. Phase-plane plot  -> ../results/LV_model_CR.pdf
    """
    # Simulate dynamics
    t, pops = simulate_lv(
        t_max=15,
        n_steps=1000,
        R0=10,
        C0=5,
        r=1.,
        a=0.1,
        z=1.5,
        e=0.75
    )

    # Define output paths (relative to script location)
    time_series_out = "../results/LV_model.pdf"
    phase_plot_out = "../results/LV_model_CR.pdf"

    # Create and save figures (they will not be displayed)
    make_time_series_plot(t, pops, time_series_out)
    make_phase_plot(pops, phase_plot_out)

    print("Saved time-series plot to:", time_series_out)
    print("Saved phase-plane plot to:", phase_plot_out)

    return 0


if __name__ == "__main__":
    """
    Ensures main() runs only when the script is executed directly.
    """
    status = main(sys.argv)
    sys.exit(status)