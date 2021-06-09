#!/usr/bin/env python3
from generator import*

#---------------------------------------
class krl(generator):
    '''Класс генератор КРЛ (потомок generator)'''

    def __init__(self):
        """Инициализация класса"""

        super(krl,self).__init__()
        self.data_in= [0]*8
        self.frequency = 475
        self.krl_fdev = 11
        self.krl_speed = data_rate
        self.code = 0xAB
        self.count_bit = 0
        self.count_krl = int((1/self.krl_speed)/(1/self.fs))
        self.channels = [1,2]
        self.amplitude = 0.1
        self.cur_freq = 0

    def data_signal(self,t,d_left,d_right):
        '''Генерация сигнала КРЛ '''

        data_left = d_left
        data_right = d_right

        for i in range(len(t)):
            if self.count_krl < int((1/self.krl_speed)/(1/self.fs)):
                self.count_krl += 1
            else:
                self.count_krl = 0
                if self.count_bit == 8:
                    #print ("---------------")
                    self.count_bit = 0
                    Byte = self.code
                    for i in range (8):
                        if ((Byte & 0x80)>>7) == 1:
                            self.data_in[i] = 1
                        else:
                            self.data_in[i] = 0
                        Byte = Byte<<1

                if self.data_in[self.count_bit] == 1:
                    self.cur_freq = self.frequency + self.krl_fdev
                else:
                    self.cur_freq = self.frequency - self.krl_fdev
                self.count_bit += 1

            data_left[i] = (self.A_l * self.amplitude*np.sin(2*np.pi*
                                          self.cur_freq*t[i]))
            data_right[i] = (self.A_r * self.amplitude*np.sin(2*np.pi*
                                          self.cur_freq*t[i]))

        return data_left, data_right
