#!/usr/bin/env python3
import sounddevice as sd
import sys
import queue
import numpy as np
import time

#---------------------------------------
class ars_gen(object):

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
            self.count_ars+= 1.0/self.fs
            if self.sao == True:
                print ("sao on")
                if (self.count_ars <= self.sao_param['pulse1']):
                    self.ars_on = 1
                elif (self.count_ars > self.sao_param['pulse1']) &\
                         (self.count_ars <= self.sao_param['pause1']):
                    self.ars_on = 0
                elif (self.count_ars > self.sao_param['pause1']):
                    self.ars_on = 0
                    self.count_ars = 0

            data_left[i] = (A_l *self.ars_on* self.amplitude1*np.sin(2*np.pi*self.frequency1*t[i])+\
            A_l *self.ars_on* self.amplitude2*np.sin(2*np.pi*self.frequency2*t[i]))

            data_right[i] = (A_r *self.ars_on* self.amplitude1*np.sin(2*np.pi*self.frequency1*t[i])+\
            A_l *self.ars_on* self.amplitude2*np.sin(2*np.pi*self.frequency2*t[i]))

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
        self.ars_on = 1
        self.count_ars = 0
        self.frequency1 = 800
        self.frequency2 = 0
        self.sao = False
        self.sao_param = {
                'pulse1': 1.6,
                'pause1': 3.2
                        }
        self.amplitude1 = 0.1
        self.amplitude2 = 0.0
        self.channels = [1,2]
        self.q = queue.Queue()
        sd.default.blocksize = 0
        sd.default.samplerate = self.fs
        sd.default.channels = 2
        self.stream = sd.Stream(device = (sd.default.device, sd.default.device),\
                                                 callback = self.__audio_callback)
        self.mapping = [c - 1 for c in self.channels]


