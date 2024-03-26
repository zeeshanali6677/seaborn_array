
# import matplotlib.pyplot as plt
#  arr = [2,3,4,5,6,7,45]
#  arr1 = [0, 3, 4, 5, 6, 7, 45]
#  arr3 = [2, 3, 4, 5, 6, 745]
#  plt.plot(arr)
#  plt.xlable('index')
#  plt.ylable('value')
#  plt.title('my first grapg to show array')


# plt.plot([0,1,2,3],[4,5,6,7], 'ro')
# plt.axis((0, 6, 0, 20))
# plt.show()



import numpy as np
import matplotlib.pyplot as plt
plt.plot([0,1,2,3,4],[4,5,6,7,8,],[9,2.0,3.0,4.0],'ro')
plt.axis((0,6,0,20))
plt.show()

t = np.arange(0., 5., 0.2)
plt.plot(t, t, 'r--', t, t**2, 'bs', t, t**3, 'g^')
plt.show()
