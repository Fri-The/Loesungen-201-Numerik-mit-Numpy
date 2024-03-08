Aufgabe 1a)
from numpy import cos, pi

def T_model(t, T_0, T_A, dt):
    return T_0 + T_A * (1 - np.cos(2 * np.pi * (t + dt))) / 2

Aufgabe 1b)
popt, pcov = curve_fit(T_model, t, T)
T_0 = popt[0]
T_A = popt[1]
dt = popt[2]

Aufgabe 1c)
t_val = np.linspace(0, 1, 100)

plt.plot(t_val, T_model(t_val, popt[0], popt[1], popt[2]), label= "\n".join([r"Fit $T(t)=T_0+T_A\frac{1-\cos{\!(2\pi (t+\Delta t))}}{2}$ mit:", "$T_0 = {:.3f} \pm {:.3f} ^\circ$C".format(popt[0], np.sqrt(pcov[0][0])), "$T_A = {:.3f} \pm {:.3f} ^\circ$C".format(popt[1], np.sqrt(pcov[1][1])), "$\Delta t = {:.3f} \pm {:.3f}$".format(popt[2], np.sqrt(pcov[2][2]))]), c = "black")
plt.scatter(t, T, s = 1, color='gray', label='Messwerte')

plt.xlim(0,1)
plt.ylim(-20, 30)
plt.title("Jahres-Temperaturverlauf in Heidelberg")
plt.ylabel("Temperatur T [$^\circ$C]")
plt.xlabel("Zeitpunkt innerhalb des Jahres $t$")
plt.legend()
