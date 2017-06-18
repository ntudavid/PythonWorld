'''
tutorial (7) - module numpy

2016/07/04

David Hsu
'''

import numpy as np

data = np.array([[1,2,3,4],[5,6,7,8]])
print('data = ',data)
row1 = data[0,:]
print('row1 is',row1)
row2 = data[1,:]
print('row2 is',row2)
# change values in the alias
row1[1] = 20
print('row1 now became',row1)
row2[3] = 80
print('row2 now became',row2)
print('data = ',data)

