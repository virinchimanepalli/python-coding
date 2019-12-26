import numpy as np
from scipy.misc import imread, imsave, imresize

img = imread('blocks.png')
print(img.dtype,img.shape)


# a = np.array([[1,2], [3, 4], [5, 6]])
# b = (a>2)
# print(b)
# print(a[b])
# print(a[a>2])
# x = np.array([[1,1],[1,1]])
# y = np.array([9,10])
# z = np.array([1,1])
# print(y.dot(z))
# print(np.dot(y,z))
