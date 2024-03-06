Aufgabe 1a)
Ich habe es nicht hinbekommen mit den Inhalten des Kurses die x-Achse in 5-er-Schritten darzustellen. Ansonsten sollte es passen.
plt.plot(date, T, label = "Messwerte")

plt.title("Temperaturverlauf in Heidelberg")
plt.ylim(-20, 30)
plt.xlabel("Zeitpunkt")
plt.ylabel("Temperatur T[$^\circ{}\mathrm{C}$]")
plt.legend(loc = "upper right")

Aufgabe 1b)
plt.scatter(date % 1, T,s = 1 , label = "Messwerte")

plt.title("Jahres-Temperaturverlauf in Heidelberg")
plt.xlim(0, 1)
plt.ylim(-20, 30)
plt.xlabel("Zeitpunkt innerhalb des Jahres")
plt.ylabel("Temperatur T[$^\circ{}\mathrm{C}$]")
plt.legend(loc = "upper right")
