#!/usr/bin/env python3

from generator import *

#---------------------------------------------------------------------------

krl = gen_device()
ars = gen_device()
#alsn = gen_device()
#alsen = gen_device()

krl.mode = "krl"
krl.frequency = 800
krl.amplitude = 0.1

ars.mode = "asr"
ars.frequency = 325
ars.amplitude = 0.1

#alsn.mode = "alsn"
#alsn.frequency = 400
#alsn.amplitude = 0.1

#alsn.mode = "alsen"
#alsn.frequency = 400
#alsn.amplitude = 0.1


krl.stream.start()
ars.stream.start()

input("...Press Enter to exit...")
#---------------------------------------------------------------------------
