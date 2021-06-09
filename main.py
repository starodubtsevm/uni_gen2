#!/usr/bin/env python3

from alsen import*
from alsn import*
from krl import*
from ars import*
from const import*
from generator import*

Us = 0.0088
#---------------------------------------------------------------------------
krl1 = krl()

krl1.frequency = 475
krl1.amplitude = Us
krl1.code = 0x2c
krl1.channel = "both"

#krl1.stream.start()

#---------------------------------------------------------------------------
krl2 = krl()

krl2.frequency = 675
krl2.amplitude = Us*35
krl2.code = 0x67 
krl2.channel = "both"

#krl2.stream.start()

#---------------------------------------------------------------------------
alsn = alsn()

alsn.frequency = 75.0
alsn.code = "Green"
alsn.channel = "both"
alsn.amplitude = 0.35

alsn.stream.start()

#---------------------------------------------------------------------------
alsen = alsen()

alsen.amplitude = 0.22
alsen.frequency = 174.9
alsen.channel = "both"
alsen.code = [14,14]

#alsen.stream.start()

#---------------------------------------------------------------------------
ars = ars()

ars.frequency = 75
ars.frequency2 = 125

ars.amplitude = 0.35
ars.amplitude2 = 0.35
ars.sao = False
ars.channel = "both"

#ars.stream.start()

#---------------------------------------------------------------------------

input("...Press Enter to exit...")
#---------------------------------------------------------------------------

