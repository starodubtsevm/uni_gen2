import numpy as np


Byte = 0x1F
Bits_mass =[0]*8

for i in range (8):
    if ((Byte & 0x80)>>7) == 1:
        Bits_mass[i] = 1
    else:
        Bits_mass[i] = 0
    print(i)
    Byte = Byte<<1


print(Bits_mass)

