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

# data setup
Q = np.loadtxt('data/folsom-annual.csv', delimiter=',', skiprows=1, usecols=[1])
T = len(Q)

def simulate(x):
  S = np.zeros(T)
  R = np.zeros(T)
  cost = np.zeros(T)
  h0 = x[0]
  hf = x[1]

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

  return cost.mean() # minimize average annual cost


res = minimize(simulate, [1300,2500], bounds = [(0,D), (D,K+D)], method='L-BFGS-B')

# res.x contains the optimal h0,hf values
# res.fun is the optimal (min) function value
print(res)
