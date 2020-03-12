#!/usr/bin/env python3
import sounddevice as sd
import sys
import queue
import numpy as np
import time

#---------------------------------------
class alsen_gen(object):

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
            if self.imp_duty_count < int((1/self.speed)/(1/self.fs)):
                self.imp_duty_count=self.imp_duty_count+1
            else:
                self.imp_duty_count=0
                if self.count_bit==0:
                    self.count_bit=8
                    self.Byte1=self.code[0]
                    self.Byte2=self.code[1]
                self.diBit=((self.Byte1 & 0x80)>>6)+((self.Byte2 & 0x80)>>7)
                if self.diBit == 0:
                    self.d_phase = np.pi*0
                elif self.diBit == 1:
                    self.d_phase = np.pi/2
                elif self.diBit == 3:
                    self.d_phase = np.pi
                elif self.diBit == 2:
                    self.d_phase = 3/2*np.pi
                self.phase = self.phase + self.d_phase
                if self.phase > 2*np.pi:
                    self.phase -= 2*np.pi
                #print (diBit,Byte1,Byte2,phase)
                self.Byte1=self.Byte1<<1
                self.Byte2=self.Byte2<<1
                self.count_bit=self.count_bit-1

            data_left[i] = (A_l * self.amplitude*np.sin(2*np.pi*self.frequency*t[i]+self.phase))
            data_right[i] = (A_r * self.amplitude*np.sin(2*np.pi*self.frequency*t[i]+self.phase))

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
        self.count_alsen = 0
        self.count_bit = 8
        self.diBit = 0
        self.phase = 0
        self.d_phase = 0
        self.code = [0x2C,0x2C]
        self.Byte1 = self.code[0]
        self.Byte2 = self.code[1]
        self.frequency = 174.89
        self.speed = 12.897
        self.imp_duty_count = int((1/self.speed)/(1/self.fs))
        self.channels = [1,2]
        self.amplitude = 0.1
        self.q = queue.Queue()
        sd.default.blocksize = 0
        sd.default.samplerate = self.fs
        sd.default.channels = 2
        self.stream = sd.Stream(device = (sd.default.device, sd.default.device),\
                                                 callback = self.__audio_callback)
        self.mapping = [c - 1 for c in self.channels]


