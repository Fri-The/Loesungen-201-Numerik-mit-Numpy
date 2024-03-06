Aufgabe 1a)
from numpy import cos, pi

def T_model(t, T_0, T_A, dt):
    return T_0 + T_A * (1 - np.cos(2 * np.pi * (t + dt))) / 2

Aufgabe 1b)
popt, pcov = curve_fit(T_model, t, T)
T_0 = popt[0]
T_A = popt[1]
dt = popt[2]
