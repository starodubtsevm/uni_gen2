#!/usr/bin/env python3
from generator import*

#---------------------------------------
class alsn(generator):
    '''Класс генератор АЛСН (потомок generator)'''

    def __init__(self):
        """Инициализация класса"""

        super(alsn,self).__init__()
        self.count_alsn = 0
        self.code = None
        self.alsn_on = 0
        self.alsn_green = {
                'pause1': 0.57,
                'pulse1': 0.92,
                'pause2': 1.04,
                'pulse2': 1.26,
                'pause3': 1.38,
                'pulse3': 1.6
                }
        self.alsn_yellow = {
                'pause1': 0.72,
                'pulse1': 1.1,
                'pause2': 1.22,
                'pulse2': 1.6,
                }
        self.alsn_redyellow = {
                'pulse1': 0.23,
                'pause1': 0.80
                }

    def data_signal(self,t,d_left,d_right):
        '''Генерация сигнала АЛСН'''

        data_left  = d_left
        data_right = d_right
        self.alsn_on = 0

        if self.code not in ("Green","Yellow","RedYellow"):
            self.code = None
        
        for i in range(len(t)):
            self.count_alsn+= 1.0/self.fs

            if self.code == "Green":
                if self.count_alsn <=\
                         self.alsn_green['pause1']:
                    self.alsn_on = 0

                elif self.count_alsn <=\
                         self.alsn_green['pulse1']:
                    self.alsn_on = 1

                elif self.count_alsn <=\
                         self.alsn_green['pause2']:
                    self.alsn_on = 0

                elif self.count_alsn <=\
                         self.alsn_green['pulse2']:
                    self.alsn_on = 1

                elif self.count_alsn <=\
                         self.alsn_green['pause3']:
                    self.alsn_on = 0

                elif self.count_alsn <=\
                         self.alsn_green['pulse3']:
                    self.alsn_on = 1
                elif self.count_alsn >=\
                         self.alsn_green['pulse3']:
                    self.count_alsn = 0

            elif self.code == "Yellow":
                if self.count_alsn <=\
                         self.alsn_yellow['pause1']:
                    self.alsn_on = 0
                elif self.count_alsn <=\
                         self.alsn_yellow['pulse1']:
                    self.alsn_on = 1
                elif self.count_alsn <=\
                         self.alsn_yellow['pause2']:
                    self.alsn_on = 0
                elif self.count_alsn <=\
                         self.alsn_yellow['pulse2']:
                    self.alsn_on = 1
                elif self.count_alsn >=\
                         self.alsn_yellow['pulse2']:
                    self.count_alsn = 0

            elif self.code == "RedYellow":
                if self.count_alsn <=\
                         self.alsn_redyellow['pulse1']:
                    self.alsn_on = 1
                elif self.count_alsn <=\
                         self.alsn_redyellow['pause1']:
                    self.alsn_on = 0
                elif self.count_alsn >=\
                         self.alsn_redyellow['pause1']:
                    self.count_alsn = 0
            else:
                self.alsn_on = 0
 
            data_left[i] = (self.A_l *self.alsn_on* self.amplitude*np.sin(2*np.pi*self.frequency*t[i]))
            data_right[i] = (self.A_r *self.alsn_on* self.amplitude*np.sin(2*np.pi*self.frequency*t[i]))

        return data_left, data_right

