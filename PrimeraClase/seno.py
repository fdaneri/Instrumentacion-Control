import sounddevice as sd
import numpy as np
import pylab as plt
import time
from scipy.signal import find_peaks
from scipy import signal
#hola mundo
def seno(frecuencia, duracion, amplitud=1, fs=192000):
    """
    Esta función tiene como output una funcion seno de una cierta duración y frecuencia.
    """
    tiempo=np.arange(fs*duracion)/fs
    seno=amplitud*np.sin(2*np.pi*frecuencia*tiempo).astype(np.float32)
    
    print(plt.plot(tiempo,seno))
    
    return seno
    
def barrido_frec(frec=0,fmax=30000):
    
    fmin=frec
    frecuencia=[]
    while frec < fmax:
        frecuencia.append(np.exp(frec))
        frec+=2
    
    #print(plt.plot(frecuencia))


def barrido_frec1 (frec=0,fmax=30000):
    
    while frec < fmax:
        seno(frec)
        frec+=2
    
    #print(plt.plot(frecuencia))
        