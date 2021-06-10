#!/usr/bin/env python3
from generator import*

#---------------------------------------
class alsen(generator):
    '''Класс генератор АЛСЕН (потомок generator)'''

    def __init__(self):
        """Инициализация класса"""

        super(alsen,self).__init__()
        self.count_alsen = 0
        self.count_bit = 0
        self.phase = 0
        self.speed = data_rate_alsen
        self.imp_duty_count = 0
        self.diBit_mass = [0]*8
        self.d_phase_dict = (0, (- np.pi/2), np.pi/2, np.pi)
        self.Bauer_dict = (0b00000001, 0b00011111, 0b00101100,
                           0b00110010, 0b01001010, 0b01010100,
                           0b01100111, 0b01111001, 0b10000110,
                           0b10011000, 0b10101011, 0b10110101,
                           0b11001101, 0b11010011, 0b11100000,
                           0b11111110)

    def data_signal(self,t,d_left,d_right):
        '''Генерация сигнала АЛСЕН'''

        data_left  = d_left
        data_right = d_right
        
        for i in range(len(t)):
            if self.imp_duty_count < int((1/self.speed)/(1/self.fs)):
                self.imp_duty_count += 1
            else:
                self.imp_duty_count=0
                if self.count_bit==8:
                    self.count_bit=0
                    Byte1 = self.Bauer_dict[self.code[1]]
                    Byte2 = self.Bauer_dict[self.code[0]]

                    for i in range (8):
                        diBit=((Byte1 & 0x80)>>7) + ((Byte2 & 0x80)>>6)
                        self.diBit_mass[i] = diBit
                        Byte1 = Byte1<<1
                        Byte2 = Byte2<<1

                self.phase += self.d_phase_dict[self.diBit_mass[self.count_bit]]
                if (self.phase > 2 * np.pi):self.phase-= 2 * np.pi
                self.count_bit += 1

            data_left[i] = (self.A_l * self.amplitude *
                            np.sin(2*np.pi*self.frequency*t[i]+ self.phase))
            data_right[i] = (self.A_r * self.amplitude *
                            np.sin(2*np.pi*self.frequency*t[i]+ self.phase))

        return data_left, data_right
