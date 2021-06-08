#!/usr/bin/env python3


Byte1 = 0x2c
Byte2 = 0x32

print (bin(Byte1))
print (bin(Byte2))
print("------------")

for i in range (8):
    diBit=((Byte1 & 0x80)>>6)+((Byte2 & 0x80)>>7)

    Byte1=Byte1<<1
    Byte2=Byte2<<1
    print(diBit)
    print("---------------")


