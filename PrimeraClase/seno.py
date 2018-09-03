import sounddevice as sd
import numpy as np
import pylab as plt
import time
from scipy.signal import find_peaks
from scipy import signal

def seno(frecuencia, duracion, amplitud=1, fs=192000):
    """
    Esta función tiene como output una funcion seno de una cierta duración y frecuencia.
    """
    tiempo=np.arange(fs*duracion)/fs
    seno=amplitud*np.sin(2*np.pi*frecuencia*tiempo).astype(np.float32)
    
    plt.plot(tiempo,seno)
    plt.title('señal original')
    plt.xlabel('Tiempo(s)')
    plt.ylabel('Amplitud')
    
    plt.show()
    
    return seno
    


def max_sin(frecuencia, duracion, amplitud=1, fs=192000):
    """
    Esta función tiene como output los primeros 10 máximos de la función de entrada
    """
    #array de la función de entrada
    sin=[]       
    sin=seno(frecuencia, duracion, amplitud=1, fs=192000)
    #array del tiempo
    tiempo=np.arange(fs*duracion)/fs
    
    
    maximos=[]   #array de los maximos de la señal
    ubic_max=[]  #array de la ubicación de los maximos
    
    j=0    # j es un contador de maximos
    i=1    # i recorre todo el array del seno

    #busco los primeros 10 maximos----> j<10
    while i<len(sin)-1 and j<10:
        
        if sin[i-1] < sin[i] and sin[i] > sin[i+1]:
            maximos.append(sin[i])        #guardo los maximos de la señal 
            ubic_max.append(tiempo[i])    #guardo la ubicación de los maximos de la señal
            j+=1
        
        i+=1
 
    #grafico señal y maximos       
    plt.plot(tiempo[:i+1],sin[:i+1])
    plt.title('primeros 10 picos')
    plt.xlabel('Tiempo(s)')
    plt.ylabel('Amplitud')
    plt.plot(ubic_max[:],maximos[:], 'rs')
    plt.show()    
    
    return j,maximos  # pido ver cuantos maximos tengo y sus valores

    
def frecuencias(frec=0,fmax=30000):
    
    fmin=frec
    frecuencia=[1]
    
    while frecuencia[-1] < fmax:
        frec+=0.2
        frecuencia.append(np.exp(frec))
        
    
    print(plt.plot(frecuencia))


def barrido_frec1 (frec=0,fmax=30000):
    
    while frec < fmax:
        seno(frec)
        frec+=2
    
    #print(plt.plot(frecuencia))
        