#!/usr/bin/env python3
import sounddevice as sd
import sys
import queue
import numpy as np
import time

#---------------------------------------
class krl_gen(object):

    def __audio_callback (self,indata, outdata, frames, time, status):
        """callback function"""
        if status:
            print(status, file=sys.stderr)

#--передача-потока на аудиовыход--------------------------------------------
        t = (self.start_idx + np.arange(frames)) / (sd.default.samplerate)
        t = t.reshape(-1, 1)

        if self.channel == "left" or self.channel == "both":
            A_l = 1
        else:
            A_l = 0
        if self.channel == "right" or self.channel == "both":
            A_r = 1
        else:
            A_r = 0

        data_left  = np.zeros(len(t))
        data_right = np.zeros(len(t))

        for i in range(len(t)):
            if self.data_in[self.num_bit] == 1:
                f_cur = self.frequency + self.krl_fdev
            else:
                f_cur = self.frequency - self.krl_fdev
            data_left[i] = (A_l * self.amplitude*np.sin(2*np.pi*f_cur*t[i]))
            data_right[i] = (A_r * self.amplitude*np.sin(2*np.pi*f_cur*t[i]))

            self.count_krl+= 1.0/self.fs
            if self.count_krl >= 1.0/self.krl_speed:
                self.count_krl = 0
                self.num_bit+= 1
                if self.num_bit > 7:
                    self.num_bit = 0

        data_stereo = np.column_stack([data_left, data_right])
        outdata[::] = data_stereo
        self.start_idx += frames

#--прием потока с микрофоного входа-------------------------------------
        self.q.put(indata[::self.downsample, self.mapping])

    def __init__(self):
        """Инициализация класса"""
        self.start_idx = 0
        self.downsample = 2
        self.fs = 8000
        self.channel = "both"
        self.data_in= []
        self.frequency = 475
        self.krl_fdev = 11
        self.krl_speed = 12.987
        self.code = 0x2C
        self.num_bit = 0
        self.count_krl = 0
        self.channels = [1,2]
        self.amplitude = 0.1
        self.mode = ""
        self.q = queue.Queue()
        sd.default.blocksize = 0
        sd.default.samplerate = self.fs
        sd.default.channels = 2
        self.stream = sd.Stream(device = (sd.default.device, sd.default.device),\
                                                 callback = self.__audio_callback)
        self.mapping = [c - 1 for c in self.channels]
        for j in range(7, -1, -1):
            self.data_in.append((self.code & 1<<j)>>j)

