"""
Utils
=====

"""
import numpy as np
from acoustics.decibel import dbsum

SOUNDSPEED = 343.0
"""
Speed of sound in air.
"""

esum = dbsum


def mean_tl(tl, surfaces):
    """Mean tl."""
    try:
        tau_axis = tl.ndim - 1
    except AttributeError:
        tau_axis = 0
    tau = 1.0 / (10.0**(tl / 10.0))
    return 10.0 * np.log10(1.0 / np.average(tau, tau_axis, surfaces))


def wavelength(freq, c=SOUNDSPEED):
    """
    Wavelength for one or more frequencies (as ``NumPy array``).
    """
    return c / freq


def w(freq):
    """
    Angular frequency for one o more frequencies (as ``NumPy array``).
    """
    return 2.0 * np.pi * freq


def _is_1d(given):
    if isinstance(given, (int, float)):
        return given
    elif given.ndim == 1:
        return np.array([given])
    elif given.ndim == 2 and given.shape[0] == 1:
        return given[0]
    else:
        return given
    
    
    import math

def calculate_max_mic_diameter(freq, c=None):
    """
    Calculate the maximum diameter of a microphone in inches before the size of the microphone effects the sound field/acoustic wave, based on the given frequency and temperature.

    Args:
        freq (float): The frequency in Hz.
        c (float, optional): The speec of sound in meters per second (m/s). If not provided, a default value of 343m/s is used.

    Returns:
        float: The maximum diameter of the microphone in inches before the size of the microphone effects the sound field/acoustic wave.
    """
    if c is None:
        c = 343  # Default speed of of sound in m/s

    # Calculate microphone min diameter in inches
    w = 2 * math.pi * freq  # rad/s
    d = 0.1/(w/c) # Make sure helmholts number is much less than one (i.e. kd<<1 ... (w/c)*d=0.1 solve for d)
    maxDiameter = d * 39.37  # inch

    return maxDiameter
