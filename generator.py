#!/usr/bin/env python3
from const import*

#---------------------------------------
class generator(object):
    "Класс генератор синусоидального сигнала"

    def __audio_callback (self,indata, outdata, frames, time, status):
        """callback function"""

        t = (self.start_idx + np.arange(frames)) / (sd.default.samplerate)
        t = t.reshape(-1, 1)

        d_left  = np.zeros(len(t))
        d_right = np.zeros(len(t))

        data_left, data_right = self.data_signal(t,d_left,d_right)
        data_stereo = np.column_stack([data_left, data_right])
        outdata[::] = data_stereo
        self.start_idx += frames

    def __init__(self):
        """Общая инициализация класса"""

        sd.default.blocksize = 0
        sd.default.samplerate = fs
        sd.default.channels = 2
        self.stream = sd.Stream(device = (sd.default.device,\
                        sd.default.device), callback = self.__audio_callback)
        self.channels = [1,2]
        self.mapping = [c - 1 for c in self.channels]
        self.channel = "both"
        self.start_idx = 0
        self.fs = fs
        if self.channel == "left" or self.channel == "both":
            self.A_l = 1
        else:
            self.A_l = 0
        if self.channel == "right" or self.channel == "both":
            self.A_r = 1
        else:
            self.A_r = 0

        self.frequency = 800
        self.amplitude = 0.1

    def data_signal(self,td,d_left,d_right):
        '''Генерация синусоидального сигнала '''

        data_right = d_right
        data_left = l_left

        for i in range(len(t)):
            data_left[i]  = (self.A_l * self.amplitude*np.sin\
                                            (2*np.pi*self.frequency*t[i]))
            data_right[i] = (self.A_r * self.amplitude*np.sin\
                                             (2*np.pi*self.frequency*t[i]))

        return data_left, data_right


