import numpy as np
import matplotlib.pyplot as plt
from BeatDetect import BeatDetect
from shimi import *
from motion.move import *
from config.definitions import *
from motion.recorder import *
from motion.playback import *
from motion.generative_phrase import *
from motion.jam import *
from utils.utils import *
from threading import Thread, Lock

import time

from copy import deepcopy

import threading

# Load Shimi
shimi = Shimi(silent=False)

local_gestures = {}

### Proper Recording and playback of motor movements

#r = Recorder(shimi, shimi.all_motors, 10.0)
#r.record()
#r.plot(plt.axes())
#r.play(vel_ax=plt.axes())

### Jam
#TEMPOCALLBACK = multiprocessing.Value('d', 0.0)

tempoLock = Lock()
class Tempo(object):
    def __init__(self, tempo):
        self.tempo = tempo

    def setTempo(self, tempo):
        self.tempo = tempo
    def getTempo(self):
        return self.tempo

t = Tempo(2)

b = BeatDetect()

bpmThread=threading.Thread(target=b.run, args=(tempoLock, t,))



# have the code start only when there is input signal
# simplify head movement to make more noticeable to tempo
# find a better threshold wait for 4 beats
# change to multithreading instead of multiprocessing




#danceThread.start()
bpmThread.start()
sleepTime = 4

while True:
    time.sleep(sleepTime)
    tempoLock.acquire()
    temp = t.getTempo()
    tempoLock.release()
    print('printing from main:' , temp)
    if (temp != 1):
        j = Jam(shimi, 1, tempoLock, t, 4.0)
        danceThread = threading.Thread(target=j.run)
        danceThread.start()
        danceThread.join()
        sleepTime = ((60 / temp) * 8) - 0.1
        break

   

