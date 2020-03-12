#!/usr/bin/env python3
from const import*

#---------------------------------------
class alsn_gen(object):

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
        
        alsn_on = 0
        if    self.alsn_code not in ("Green","Yellow","RedYellow"):
            self.alsn_code = None

        for i in range(len(t)):
            self.count_alsn+= 1.0/self.fs

            if self.alsn_code == "Green":
                if self.count_alsn <=\
                         self.alsn_green['pause1']:
                    alsn_on = 0

                elif self.count_alsn <=\
                         self.alsn_green['pulse1']:
                    alsn_on = 1

                elif self.count_alsn <=\
                         self.alsn_green['pause2']:
                    alsn_on = 0

                elif self.count_alsn <=\
                         self.alsn_green['pulse2']:
                    alsn_on = 1

                elif self.count_alsn <=\
                         self.alsn_green['pause3']:
                    alsn_on = 0

                elif self.count_alsn <=\
                         self.alsn_green['pulse3']:
                    alsn_on = 1
                elif self.count_alsn >=\
                         self.alsn_green['pulse3']:
                    self.count_alsn = 0

            elif self.alsn_code == "Yellow":
                if self.count_alsn <=\
                         self.alsn_yellow['pause1']:
                    alsn_on = 0
                elif self.count_alsn <=\
                         self.alsn_yellow['pulse1']:
                    alsn_on = 1
                elif self.count_alsn <=\
                         self.alsn_yellow['pause2']:
                    alsn_on = 0
                elif self.count_alsn <=\
                         self.alsn_yellow['pulse2']:
                    alsn_on = 1
                elif self.count_alsn >=\
                         self.alsn_yellow['pulse2']:
                    self.count_alsn = 0

            elif self.alsn_code == "RedYellow":
                if self.count_alsn <=\
                         self.alsn_redyellow['pulse1']:
                    alsn_on = 1
                elif self.count_alsn <=\
                         self.alsn_redyellow['pause1']:
                    alsn_on = 0
                elif self.count_alsn >=\
                         self.alsn_redyellow['pause1']:
                    self.count_alsn = 0
            else:
                alsn_on = 0

            data_left[i] = (A_l *alsn_on* self.amplitude*np.sin(2*np.pi*self.frequency*t[i]))
            data_right[i] = (A_r *alsn_on* self.amplitude*np.sin(2*np.pi*self.frequency*t[i]))

        data_stereo = np.column_stack([data_left, data_right])
        outdata[::] = data_stereo
        self.start_idx += frames

#--прием потока с микрофоного входа-------------------------------------
        self.q.put(indata[::self.downsample, self.mapping])

    def __init__(self):
        """Инициализация класса"""
        self.start_idx = 0
        self.downsample = 2
        self.fs = fs
        self.channel = "both"
        self.count_alsn = 0
        self.frequency = 50
        self.amplitude = 0.1
        self.alsn_code = "RedYellow"
        self.alsn_green = {
                'pause1': 0.03,
                'pulse1': 0.38,
                'pause2': 0.5,
                'pulse2': 0.72,
                'pause3': 0.84,
                'pulse3': 1.06
                }
        self.alsn_yellow = {
                'pause1': 0.03,
                'pulse1': 0.41,
                'pause2': 0.53,
                'pulse2': 0.91,
                }
        self.alsn_redyellow = {
                'pulse1': 0.23,
                'pause1': 0.80
                }
        self.frequency = 75
        self.channels = [1,2]
        self.amplitude = 0.1
        self.q = queue.Queue()
        sd.default.blocksize = 0
        sd.default.samplerate = self.fs
        sd.default.channels = 2
        self.stream = sd.Stream(device = (sd.default.device, sd.default.device),\
                                                 callback = self.__audio_callback)
        self.mapping = [c - 1 for c in self.channels]


