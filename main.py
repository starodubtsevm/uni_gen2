#!/usr/bin/env python3

from one_tone import *
from alsen import*
from alsn import*
from krl import*
from ars import*


#---------------------------------------------------------------------------
tone1 = one_tone()
tone2 = one_tone()
krl = krl_gen()

#alsn = alsn_gen()
#alsen = alsen_gen()
#ars = ars_gen()

#---------------------------------------------------------------------------
tone1.frequency = 800
tone1.amplitude = 0.1
tone1.channel = "left"

#---------------------------------------------------------------------------
tone2.frequency = 325
tone2.amplitude = 0.1
tone2.channel = "both"

#---------------------------------------------------------------------------
krl.frequency = 600
krl.amplitude = 0.1
krl.code = 0x2C

#---------------------------------------------------------------------------
#alsn.mode = "alsn"
#alsn.frequency = 400
#alsn.amplitude = 0.1

#---------------------------------------------------------------------------
#alsn.mode = "alsen"
#alsn.frequency = 400
#alsn.amplitude = 0.1

#---------------------------------------------------------------------------
#tone1.stream.start()
#tone2.stream.start()
krl.stream.start()
#---------------------------------------------------------------------------

input("...Press Enter to exit...")
#---------------------------------------------------------------------------
