import numpy as np
# import matplotlib.pyplot as plt

# things to talk about 4/21/16

# creating a numpy array (1D,2D)
# indexing
# zeros and ones functions to initialize
# vector/matrix operations (elementwise arithmetic, addition, sum, mean, etc.)
# loops/lists = bad (speed comparison)
# loading data/matrix from file
# plotting, colors, labels, legends
# http://matplotlib.org/examples/color/named_colors.html
# subplots, sizing, saving (vector vs. raster)
# different plot types, scatter
# https://github.com/VictoriaLynn/plotting-examples

# other types of plots
# pandas / time series 

# a list
L = [6, 3, 4, 7, 5]

# a numpy array
A = np.array([6, 3, 7, 4, 5])

# a 2d array (matrix)
A2 = np.array([[6,3,7,4,5], [2,6,3,4,9]])

# indexing [i,j]
# print(A2[0,3])

# get a row (: means "all")
# print(A2[0,:])

# # create a matrix of zeros
# M = np.zeros((10,5))
# M[0,:] = 4 
# print(M)

# what do you expect to happen?
# print(A**A)

M = np.ones((10000000,5))

# print(M.sum())
# s = 0
# for i in range(10000000):
#   for j in range(5):
#     s += M[i,j]

# print(s)










