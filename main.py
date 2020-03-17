#!/usr/bin/env python3

from alsen import*
from alsn import*
from krl import*
from ars import*
from const import*
from generator import*

#---------------------------------------------------------------------------
krl1 = krl()

krl1.frequency = 475
krl1.amplitude = 0.01
krl1.code = 0x2C
krl1.channel = "both"

krl1.stream.start()

#---------------------------------------------------------------------------
krl2 = krl()

krl2.frequency = 525
krl2.amplitude = 0.08
krl2.code = 0x4A
krl2.channel = "both"

#krl2.stream.start()

#---------------------------------------------------------------------------
alsn = alsn()

alsn.frequency = 75.0
alsn.code = "Green"
alsn.channel = "both"
alsn.amplitude = 0.35

#alsn.stream.start()

#---------------------------------------------------------------------------
alsen = alsen()

alsen.amplitude = 0.7
alsen.frequency = 174.9
alsen.channel = "both"
alsen.code = [0x2C,0x2C]

#alsen.stream.start()

#---------------------------------------------------------------------------
ars = ars()

ars.frequency = 75
ars.frequency2 = 125

ars.amplitude = 0.35
ars.amplitude2 = 0.35
ars.sao = False
ars.channel = "both"

ars.stream.start()

#---------------------------------------------------------------------------

input("...Press Enter to exit...")
#---------------------------------------------------------------------------

