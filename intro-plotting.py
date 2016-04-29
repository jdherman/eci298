import numpy as np 
import matplotlib.pyplot as plt

# plot historical storage for folsom, oroville, and shasta

reservoirs = ['FOL', 'ORO', 'SHA']
colors = ['steelblue', 'indianred', 'seagreen']

for i,r in enumerate(reservoirs):
  data = np.loadtxt('data/' + r + '.csv', 
                    delimiter=',', 
                    skiprows=1, 
                    usecols=[1,2,3])

  storage = data[:,0] # TAF
  # elevation = data[:,1] # ft
  # outflow = data[:,2] # mean cfs per day

  plt.plot(storage, color=colors[i], linewidth=2)


plt.xlabel('Days since Oct 1 2000')
plt.ylabel('Storage (TAF)')
plt.legend(reservoirs)
plt.show()
# plt.savefig('whatever.pdf') # or .png
