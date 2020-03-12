#!/usr/bin/env python3
import sounddevice as sd
import sys
import queue
import numpy as np
import time

#---------------------------------------
class gen_device(object):

    def __audio_callback (self,indata, outdata, frames, time, status):
        """callback function"""
        if status:
            print(status, file=sys.stderr)

#--передача-потока на аудиовыход--------------------------------------------
        t = (self.start_idx + np.arange(frames)) / (sd.default.samplerate)
        t = t.reshape(-1, 1)
        data_left  = 1 * self.amplitude * np.sin(2 * np.pi * self.frequency * t)
        data_right = 1 * self.amplitude * np.sin(2 * np.pi * self.frequency * t)
        data_stereo = np.column_stack([data_left, data_right])
        outdata[::] = data_stereo
        self.start_idx += frames
#--прием потока с микрофоного входа-------------------------------------
        self.q.put(indata[::self.downsample, self.mapping])

    def __init__(self):
        """Инициализация класса"""
        self.start_idx = 0
        self.downsample = 2
        self.data_left  = []
        self.data_right = []
        self.frequency = 800
        self.channels = [1,2]
        self.amplitude = 0.1
        self.mode = ""
        self.q = queue.Queue()
        sd.default.blocksize = 0
        sd.default.samplerate = 8000
        sd.default.channels = 2
        self.stream = sd.Stream(device = (sd.default.device, sd.default.device),\
                                                 callback = self.__audio_callback)
        self.mapping = [c - 1 for c in self.channels]

