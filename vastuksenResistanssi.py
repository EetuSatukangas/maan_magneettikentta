import numpy as np
import matplotlib.pyplot as pl

jannite = np.array([0.187,0.391,0.581,0.749,0.994,1.196,1.391,1.596,1.795,1.998,2.195,2.4,2.598,2.804,3,3.199,3.399,3.6,3.797,4.005])
sahkovirta = 10**-3*np.array([0.2,0.4,0.6,0.8,1.0,1.2,1.4,1.6,1.8,2.0,2.2,2.4,2.6,2.8,3,3.2,3.4,3.6,3.8,4])

jannitevirhe = 0.001
sahkovirtavirhe = 10**-5

pl.rc('font', size=14)


pl.plot(sahkovirta, jannite, 'o')
pl.xlabel('sähkövirta (A)')
pl.ylabel('jännite (V)')

x = np.linspace(0, 4.1*10**-3, 100)

sovitus = np.polyfit(sahkovirta, jannite, 1)

pl.plot(x, sovitus[0]*x + sovitus[1], color='blue', label='sovitus')

pl.plot(0.2*10**-3, 0.187, 'o', color='red', label='datapiste')
pl.legend()

pl.text(2*10**-3,3, r'$\Delta V=$%f$\cdot I-$0.018747' %(sovitus[0]), color='blue')
pl.title(r'Vastuksen resistanssin suuruus R ($\Omega$), $\Delta V=R\cdot I$')
pl.errorbar(sahkovirta,jannite,xerr=sahkovirtavirhe,yerr=jannitevirhe, fmt='o', color='red')
print(sovitus)

pl.show()
