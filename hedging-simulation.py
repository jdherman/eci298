import numpy as np 
import matplotlib.pyplot as plt
from scipy.optimize import minimize

# overly-simplified reservoir simulation
# annual timestep, two point hedging

# Set some parameters
K = 975 # capacity, TAF
D = 1800 # target yield, TAF
a = 0.35
b = 2.3 # cost function parameters
h0 = 1404.
hf = 2700.

# data setup
Q = np.loadtxt('data/folsom-annual.csv', delimiter=',', skiprows=1, usecols=[1])
T = len(Q)

S = np.zeros(T)
R = np.zeros(T)
cost = np.zeros(T)

S[0] = K # start simulation full

for t in range(1,T):

  # new storage: mass balance, max value is K
  S[t] = min(S[t-1] + Q[t-1] - R[t-1], K)

  # determine R from hedging policy
  W = S[t] + Q[t]
  if W > hf:
    R[t] = D
  elif W < h0:
    R[t] = W
  else:
    R[t] = (D-h0)/(hf-h0)*(W-h0)+h0

  shortage = D-R[t]
  cost[t] = a*shortage**b


plt.subplot(2,1,1)
plt.plot(Q, color='steelblue')
plt.plot(R, color='indianred')
plt.legend(['Inflow', 'Delivery'])
plt.ylabel('Flow (TAF/yr)')

plt.subplot(2,1,2)
plt.bar(range(T), cost, color='seagreen', linewidth=0)
plt.ylabel('Shortage Cost ($)')
plt.xlabel('Years (0=1904)')
plt.show()