Aufgabe:
1a)
a = np.logspace(-20,-10,11)

1b)
b = np.zeros((2,10))

1c)
c = np.eye(3)

1d)
d = np.linspace(-5, 5, 100)

1e)
x, y = np.meshgrid(d,d)

1f)
r = np.sqrt(x**2 + y**2)

1g)
E = x/r * np.sin(np.pi*r)
%matplotlib inline
import matplotlib.pyplot as plt
plt.contour(x, y, E)
Ich glaube hier ist die EM-Strahlung eines herzschen Dipols gemeint.

2a)
x = np.array([ 1, 1, 2, 3, 5, 8 ])
dx = x[1:] - x[:-1]

2b)
x, y = np.meshgrid(np.arange(-5, 6), np.arange(-5, 6))
r = np.sqrt(x**2 + y**2)
binary_donut = (r > 2) & (r < 5) 
print(binary_donut)

2c)
z = x + y
print(z)
n = z[binary_donut]
print(n)

3a)
date, T = np.loadtxt("data/temperatures.txt", unpack = True)

3b)
yearly_temperatures = []

for i in range(1995, 2014):
    Tyi = T[(date < (i + 1)) & ((i) < date ) & (np.abs(T) != 99)]
    a = i
    b = np.mean(Tyi)
    c = np.min(Tyi)
    d = np.max(Tyi)
    yearly_temperatures.append([a, b, c, d])

from tabulate import tabulate
print(tabulate(yearly_temperatures, headers=["Jahr", "Durchschnitt [°C]", "Minimal [°C]", "Maximal [°C]"]))

3c)
monthly_temperatures = []

for j in np.linspace(0,1, 13)[:-1]:
    Tmj = T[((date % 1) > j) & ((date % 1) < (j + 1/12)) & (np.abs(T) != 99)]

    a = j*12 + 1
    b = np.mean(Tmj)
    c = np.min(Tmj)
    d = np.max(Tmj)
    monthly_temperatures.append([a, b, c, d])

from tabulate import tabulate
print(tabulate(monthly_temperatures, headers=["Monat", "Durchschnitt [°C]", "Minimal [°C]", "Maximal [°C]"]))

"3d)"
Ich habe mich erst verlesen und die Aufgabe so verstanden, dass man für jeweils jeden Monat einzeln Durchschnitt, Minimum und Maximum berechnen soll. Ich fand das persönlich noch anspruchsvoller als die 3c). Hier ist mein Code für alle, die sich noch diese kleine Challenge geben wollen:
Ich habe hier Tyi für Temperature in the year i, dyi für date in the year i, und das Gleiche mit m und j für month gemacht. Auch, wenn sie für Code-Analysezwecke ganz nützlich sind, kann es sein, dass nicht alle aus (Tyi, dyi, Tmj, dmj) zwingend notwenig sind.
monthly_temperatures = []
for i in range(1995, 2014):
    Tyi = T[(date < (i + 1)) & ((i) < date ) & (np.abs(T) != 99)]
    dyi = date[(date < (i + 1)) & ((i) < date ) & (np.abs(T) != 99)]
    for j in np.linspace(0,1, 13)[:-1]:
        if (i+j) <= np.max(date):
            Tmj = Tyi[(dyi < (i + 1/12 + j)) & ((i+j) < dyi)]
            dmj = dyi[(dyi < (i + 1/12 + j)) & ((i+j) < dyi)]
            a = (str(round(j*12)+1) + "." + str(i))
            b = np.mean(Tmj)
            c = np.min(Tmj)
            d = np.max(Tmj)
            monthly_temperatures.append([a, b, c, d])

from tabulate import tabulate
print(tabulate(monthly_temperatures, headers=["Monat", "Durchschnitt [°C]", "Minimal [°C]", "Maximal [°C]"]))
