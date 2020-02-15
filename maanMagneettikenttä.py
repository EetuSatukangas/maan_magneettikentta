import numpy as np
import matplotlib.pyplot as pl

kulma = np.array([8,22,30,31,34,44,48,52,57,59,61,62,66,68,71,73,74,76,77,78,80])
kulma=kulma*(np.pi/180)
magneettikenttä = 10**-6*np.array([1.60,5.05,7.11,7.44,8.45,12.1,13.5,15.7,18.9,21,23.9,25,32.1,35,40,44.4,47.6,60.2,69.4,79.9,101])

kulmantangentti = np.tan(kulma)
kulmatangentinvirhe = [0.018,0.02,0.023,0.024,0.025,0.034,0.046,0.059,0.066,0.074,0.079,0.105,0.124,0.164,0.204,0.229,0.3,0.344,0.402,0.577,0.711]
magneettikenttävirhe = 4.237*10**-7



pl.plot(kulmantangentti, magneettikenttä, 'x', color='blue', label='datapisteet')
pl.xlabel('kulman tangentti')
pl.ylabel('magneettikentän voimakkuus (T)')

x = np.linspace(0, 6.3, 100)

sovitus = np.polyfit(kulmantangentti, magneettikenttä, 1)

pl.plot(x, sovitus[0]*x + sovitus[1], color='blue', label='sovitus')
pl.legend()

pl.text(3.5 , 100*10**-6, r'$y_{ylävirhe}=2,41\cdot 10^{-5}\cdot$tan$(x)-22\cdot 10^{-6}$', color='red')
pl.plot(x, 2.41*10**-5*x-22*10**-6, color='red', label='virhe')
pl.text(5 , 60*10**-6, r'$y_{alavirhe}=1,35\cdot 10^{-5}\cdot$tan$(x)+5\cdot 10^{-6}$', color='red')
pl.legend()
pl.plot(x, 1.35*10**-5*x+5*10**-6, color='red')

pl.text(1.1 , 50*10**-6, r'$B=1,7055627\cdot 10^{-5} \cdot$tan$(x)-5,2783963\cdot 10^{-6}$', color='blue')
pl.title(r'Maan magneettikentän x-suuntainen komponentti $B_{käämi}=B_{Maa_{x}}\cdot$tan$(x)$')
pl.errorbar(kulmantangentti, magneettikenttä, xerr=kulmatangentinvirhe, yerr=magneettikenttävirhe, fmt='x')
#print(sovitus)

pl.show()
