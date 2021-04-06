import numpy as np

x = [1, 10, 100]
for i in x: 
  y = np.log(1 / np.e**(np.sin(i) + 1) / (5 / 4 + 1 / i**15)) / np.log(1 + i**2)
  print(y)
