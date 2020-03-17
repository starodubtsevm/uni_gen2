#!/usr/bin/env python3
from generator import*

#---------------------------------------
class krl(generator):
    '''Класс генератор КРЛ (потомок generator)'''

    def __init__(self):
        """Инициализация класса"""

        super(krl,self).__init__()
        self.data_in= np.zeros(8)
        self.frequency = 475
        self.krl_fdev = 11
        self.krl_speed = data_rate
        self.code = 0x00
        self.num_bit = 0
        self.count_krl = 0
        self.channels = [1,2]
        self.amplitude = 0.1
        for j in range(0, 7, 1):
            self.data_in[7-j] = ((self.code & 1<<j)>>j)

    def data_signal(self,t,d_left,d_right):
        '''Генерация сигнала КРЛ '''

        data_left = d_left
        data_right = d_right
        for i in range(len(t)):
            if self.data_in[self.num_bit] == 1:
                f_cur = self.frequency + self.krl_fdev
            else:
                f_cur = self.frequency - self.krl_fdev
            data_left[i] = (self.A_l * self.amplitude*np.sin(2*np.pi*f_cur*t[i]))
            data_right[i] = (self.A_r * self.amplitude*np.sin(2*np.pi*f_cur*t[i]))

            self.count_krl+= 1.0/self.fs
            if self.count_krl >= 1.0/self.krl_speed:
                self.count_krl = 0
                self.num_bit+= 1
                if self.num_bit > 7:
                    self.num_bit = 0
                    for j in range(0, 7, 1):
                        self.data_in[7-j] = ((self.code & 1<<j)>>j)
        return data_left, data_right

