import numpy as np 
import matplotlib.pyplot as plt

for i in range(10):

  data = np.loadtxt('data/FOL.csv', 
                    delimiter=',', 
                    skiprows=1, 
                    usecols=[1,2,3])

  storage = data[:,0] # TAF
  elevation = data[:,1] # ft
  outflow = data[:,2] # mean cfs per day

  plt.plot(storage, color='steelblue', linewidth=2)
  plt.xlabel('Days')
  plt.ylabel('Storage (TAF)')
  plt.title('Folsom Reservoir 2008-2015')

  plt.savefig('whatever' + str(i) + '.pdf')