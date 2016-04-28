import numpy as np 
import matplotlib.pyplot as plt
import pandas as pd
from scipy import stats

# def taf_to_cfs(Q):
#   return Q * 1000 / 86400 * 43560

# read CSV data into a pandas dataframe
df = pd.read_csv('data/folsom-daily.csv', index_col=0, parse_dates=True)

# dates are used as indexes
print(df['1995-10-01':'1995-10-10'])

# column headers are variables ("series") in the dataframe
df.inflow.plot()
plt.show()

# really handy time series stuff: resampling
# resample('A') is annual, but here we want water-year
# annual_maxes = df.inflow.resample('AS-OCT').max()
# annual_maxes = taf_to_cfs(annual_maxes)
# annual_maxes.plot(color='steelblue', linewidth=2)

# # let's add a moving-average trend line
# MA = annual_maxes.rolling(window=5, center=True).mean()
# MA.plot(color='k', linewidth=2)

# plt.ylabel('Folsom inflow (cfs)')
# plt.legend(['Annual Peak Flow', '5-yr Moving Average'])
# plt.show()

# Do these look lognormal-ish?
# logQ = np.log(annual_maxes)
# logQ.plot(kind='hist', color='steelblue', linewidth=0)
# plt.show()

# # what is the estimate of the 100-year flood?
# # assuming 2-parameter lognormal
# mu = logQ.mean()
# sigma = logQ.std()
# Z = stats.norm.ppf(0.99)
# Q100 = np.exp(mu + Z*sigma)
# print(Q100)
