import numpy as np 
import matplotlib.pyplot as plt

data = np.loadtxt('data/FOL.csv', delimiter=',', skiprows=1, usecols=[1])

plt.plot(data)
plt.show()