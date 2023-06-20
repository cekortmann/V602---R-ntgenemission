import matplotlib.pyplot as plt
import matplotlib as mpl
import numpy as np
from numpy import sqrt
import pandas as pd
import scipy.constants as const
from scipy.optimize import curve_fit                        # Funktionsfit:     popt, pcov = curve_fit(func, xdata, ydata) 
from uncertainties import ufloat                            # Fehler:           fehlerwert =  ulfaot(x, err)
from uncertainties import unumpy as unp 
from uncertainties.unumpy import uarray                     # Array von Fehler: fehlerarray =  uarray(array, errarray)
from uncertainties.unumpy import (nominal_values as noms,   # Wert:             noms(fehlerwert) = x
                                  std_devs as stds)         # Abweichung:       stds(fehlerarray) = errarray


z, E = np.genfromtxt('E.txt', unpack=True, skip_header=1)
#U = U/(2*0.9892978920131985)            # Normierung 
  # Standardabweichung

# Ausgleichsrechung nach Gaußverteilung
def g(x, a, b):
    return a*x+b     # b = 2*sigma**2

para, pcov = curve_fit(g, z, np.sqrt(E))
a, b = para
pcov = np.sqrt(np.diag(pcov))
fa, fb = pcov
ua = ufloat(a, fa) 
ub = ufloat(b, fb)

xx = np.linspace(35, 42, 10**4)

plt.plot(z, np.sqrt(E), 'xr', markersize=6 , label = 'Messdaten', alpha=0.5)
plt.plot(xx, g(xx, *para), '-b', linewidth = 1, label = 'Ausgleichsfunktion', alpha=0.5)
plt.xlabel(r'$z $')
plt.ylabel(r'$E \, / \, eV$')
plt.legend(loc="best")                  # legend position
plt.grid(True)                          # grid style
print(ua)

plt.savefig('build/plot.pdf', bbox_inches = "tight")
plt.clf() 
