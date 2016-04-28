import numpy as np 
import matplotlib.pyplot as plt
from scipy import stats

# how correlated are daily inflows at Folsom and Oroville?

fol_inflow = np.loadtxt('data/FOL.csv', delimiter=',', skiprows=1, usecols=[4])

oro_inflow = np.loadtxt('data/ORO.csv', delimiter=',', skiprows=1, usecols=[4])

plt.scatter(fol_inflow, oro_inflow, color='steelblue', linewidth=0, alpha=0.5)
plt.xlim([0,140000])
plt.ylim([0,140000])
plt.xlabel('Folsom Inflow (cfs)')
plt.ylabel('Oroville Inflow (cfs)')

# add a regression line
# res = stats.linregress(fol_inflow, oro_inflow)
# print(res.rvalue)

# plt.plot([0, 140000], [res.intercept, res.intercept+140000*res.slope], color='indianred', linewidth=2)
# plt.text(20000,120000, '$R^2 = %0.2f$' % res.rvalue**2, fontsize=16)
plt.show()