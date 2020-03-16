import numpy as np

code = 0X2C
data_in = np.zeros(8)

num_bit = 0

for j in range(7, 0, -1):
    data_in[7-j] = ((code & 1<<j)>>j)

print(data_in)
