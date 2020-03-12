#!/usr/bin/env python3

from one_tone import *
from alsen import*
from alsn import*
from krl import*
from ars import*

#---------------------------------------------------------------------------
tone1 = one_tone()
krl = krl_gen()
alsn = alsn_gen()
alsen = alsen_gen()
ars = ars_gen()

#---------------------------------------------------------------------------
tone1.frequency = 800
tone1.amplitude = 0.1
tone1.channel = "left"

#---------------------------------------------------------------------------
krl.frequency = 475
krl.amplitude = 0.1
krl.code = 0x2C

#---------------------------------------------------------------------------
alsn.frequency = 75.0
alsn.code = "RedYellow"
alsn.channel = "both"
alsn.amplitude = 0.1

#---------------------------------------------------------------------------
alsen.amplitude = 0.1
alsen.channel = "both"
alsen.code = [0x2C,0x2C]

#---------------------------------------------------------------------------
ars.frequency1 = 75
ars.frequency2 = 125

ars.amplitude1 = 0.05
ars.amplitude2 = 0.05
ars.sao = False
ars.channel = "both"

#---------------------------------------------------------------------------
#tone1.stream.start()
krl.stream.start()
alsn.stream.start()
#alsen.stream.start()
#ars.stream.start()

#---------------------------------------------------------------------------

input("...Press Enter to exit...")
#---------------------------------------------------------------------------
