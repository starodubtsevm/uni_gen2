#!/usr/bin/env python3

from alsen import*
from alsn import*
from krl import*
from ars import*
from const import*
from generator import*

#---------------------------------------------------------------------------
tone1 = generator()
krl = krl()
alsn = alsn()
alsen = alsen()
ars = ars()

#---------------------------------------------------------------------------
krl.frequency = 475
krl.amplitude = 0.7
krl.code = 0x2C

#---------------------------------------------------------------------------
alsn.frequency = 275.0
alsn.code = "RedYellow"
alsn.channel = "both"
alsn.amplitude = 0.1

#---------------------------------------------------------------------------
alsen.amplitude = 0.1
alsen.channel = "both"
alsen.code = [0x2C,0x2C]

#---------------------------------------------------------------------------
ars.frequency = 75
ars.frequency2 = 125

ars.amplitude = 0.05
ars.amplitude2 = 0.05
ars.sao = False
ars.channel = "both"

#---------------------------------------------------------------------------
#tone1.stream.start()
krl.stream.start()
#ars.stream.start()
#alsn.stream.start()
#alsen.stream.start()

#---------------------------------------------------------------------------

input("...Press Enter to exit...")
#---------------------------------------------------------------------------

