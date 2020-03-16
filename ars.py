#!/usr/bin/env python3
from generator import*

#---------------------------------------
class ars(generator):
    '''Класс генератор АРС (потомок generator)'''

    def __init__(self):
        super(ars,self).__init__()
        """Инициализация класса"""
        self.ars_on = 1
        self.count_ars = 0
        self.frequency2 = 0
        self.sao = False
        self.sao_param = {
                'pulse1': 1.6,
                'pause1': 3.2
                        }
        self.amplitude2 = 0.0

    def data_signal(self,t,d_left,d_right):
        '''Генерация сигнала АРС '''
        data_left  = d_left
        data_right = d_right

        for i in range(len(t)):
            self.count_ars+= 1.0/self.fs
            if self.sao == True:
                if (self.count_ars <= self.sao_param['pulse1']):
                    self.ars_on = 1
                elif (self.count_ars > self.sao_param['pulse1']) &\
                         (self.count_ars <= self.sao_param['pause1']):
                    self.ars_on = 0
                elif (self.count_ars > self.sao_param['pause1']):
                    self.ars_on = 0
                    self.count_ars = 0

            data_left[i] = (self.A_l *self.ars_on* self.amplitude*np.sin(2*np.pi*self.frequency*t[i])+\
            self.A_l *self.ars_on* self.amplitude2*np.sin(2*np.pi*self.frequency2*t[i]))

            data_right[i] = (self.A_r *self.ars_on* self.amplitude*np.sin(2*np.pi*self.frequency*t[i])+\
            self.A_l *self.ars_on* self.amplitude2*np.sin(2*np.pi*self.frequency2*t[i]))

        return data_left, data_right


