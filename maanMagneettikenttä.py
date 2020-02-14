import numpy as np
import matplotlib.pyplot as pl

kulma = np.array([8,22,30,31,34,44,48,52,57,59,61,62,66,68,71,73,74,76,77,78,80,81])
kulma=kulma*(np.pi/180)
magneettikenttä = 10**-6*np.array([1.60,5.05,7.11,7.44,8.45,12.1,13.5,15.7,18.9,21,23.9,25,32.1,35,40,44.4,47.6,60.2,69.4,79.9,101,154])

kulmantangentti = np.tan(kulma)
kulmatangentinvirhe = [0.0003,0.0004,0.0005,0.0006,0.0006,0.0011,0.0015,0.0021,0.0034,0.0043,0.0054,0.006,0.011,0.015,0.027,0.041,0.052,0.088,0.118,0.16,0.33,0.5,1.37,2.54,5.2]
magneettikenttävirhe = 4.237*10**-7



pl.plot(kulmantangentti, magneettikenttä, 'o')
pl.xlabel(' kulman tangentti')
pl.ylabel('magneettikentän voimakkuus T')

x = np.linspace(0, 15, 100)

sovitus = np.polyfit(kulmantangentti, magneettikenttä, 1)

pl.plot(x, sovitus[0]*x + sovitus[1], color='blue', label='sovitus')
pl.legend()

#pl.text(-2,1.5, 'y=-0.35*ln(r)+0.8', color='red')
#pl.plot(x, -0.35*x+0.8, color='red', label='virhe')
#pl.text(-3, 0.7, 'y=-0.52*ln(r)+0.2', color='red')
#pl.legend()
#pl.plot(x, -0.52*x+0.2, color='red')

pl.text(2,400*10**-6, 'y=%f*tan(x)+%f' %(sovitus[0], sovitus[1]), color='blue')
#pl.title('B=')
pl.errorbar(kulmantangentti,magneettikenttä,xerr=kulmatangentinvirhe,yerr=magneettikenttävirhe, fmt='o')
print(sovitus)

pl.show()
