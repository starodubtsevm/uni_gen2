#!/usr/bin/env python3
from generator import*

#---------------------------------------
class alsen(generator):
    '''Класс генератор АЛСЕН (потомок generator)'''
    def __init__(self):
        super(alsen,self).__init__()
        """Инициализация класса"""
        self.count_alsen = 0
        self.count_bit = 8
        self.diBit = 0
        self.phase = 0
        self.d_phase = 0
        self.code = [0x2C,0x2C]
        self.Byte1 = self.code[0]
        self.Byte2 = self.code[1]
        self.speed = data_rate
        self.imp_duty_count = int((1/self.speed)/(1/self.fs))

    def data_signal(self,t):
        '''Генерация сигнала АЛСЕН'''

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

            data_left[i] = (self.A_l * self.amplitude*np.sin(2*np.pi*self.frequency*t[i]+self.phase))
            data_right[i] = (self.A_r * self.amplitude*np.sin(2*np.pi*self.frequency*t[i]+self.phase))

        return data_left, data_right
