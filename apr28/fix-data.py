import pandas as pd


reservoirs = ['FOL', 'ORO', 'SHA']
start = '2000-10-01'
stop = '2015-09-30'

for r in reservoirs:
  df = pd.read_csv('data/original/' + r + '.csv', index_col=0, parse_dates=True)
  df.fillna(method='ffill', inplace='True')
  df = df[start:stop]
  df.to_csv('data/' + r + '.csv')
