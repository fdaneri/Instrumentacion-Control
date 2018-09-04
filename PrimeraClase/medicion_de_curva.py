#la idea de este programa es permitir emitir una señal entre 20Hz y 20kHz y grabar 2 entradas 
import sounddevice as sd
import numpy as np
import pylab as plt
import time
from scipy.signal import find_peaks
from scipy import signal

def generador_de_senhal(frecuencia, duracion, amplitud, funcion, fs=192000):
    """
    Genera una señal de forma seniodal o de rampa, con una dada frecuencia y duracion.
    """
    cantidad_de_periodos = duracion*frecuencia
    puntos_por_periodo = int(fs/frecuencia)
    puntos_totales = puntos_por_periodo*cantidad_de_periodos
           
    tiempo = np.linspace(0, duracion, puntos_totales)
    if funcion=='sin':
        data = amplitud*np.sin(2*np.pi*frecuencia*tiempo)
    elif funcion=='rampa':
        data = amplitud*signal.sawtooth(2*np.pi*frecuencia*tiempo)
    else:
        print("Input no válido. Introducir sin o rampa")
        data = 0
    return tiempo, data
 
def play_tone(frecuencia, duracion, amplitud=1, fs=192000, wait=True):
    """
    Esta función tiene como output un tono de una cierta duración y frecuencia.
    """
    sd.default.samplerate = fs #frecuencia de muestreo
    
    tiempo, data = generador_de_senhal(frecuencia, duracion, amplitud, 'sin')   
    sd.play(data)
    
    if wait:
        time.sleep(duracion)
        
    return data

def playrec_tone(frecuencia, duracion, amplitud=0.1, fs=192000):
    """
    Emite un tono y lo graba.
    """
    sd.default.samplerate = fs #frecuencia de muestreo
    sd.default.channels = 2,2 #por las dos salidas de audio
    
    tiempo, data = generador_de_senhal(frecuencia, duracion, amplitud, 'sin')      
    grabacion = sd.playrec(data, blocking=True)
    
    return tiempo, data, grabacion

def medicion_curva():
    """
    Permite en teoria, medir emitir 20 tonos por decada y grabalos entre 10hz y 20khz
    """
    array_decena=range(10,100,5)
    array_centena=range(100,1000,50)
    array_mil=range(1000,20000,500)
    array_completo=list(array_decena)+list(array_centena)+list(array_mil)
    tones = np.array(array_completo)
    for i in tones:
        tiempo, data, grabacion = playrec_tone(i, 1)
        time.sleep(1)
        print(i)
    return grabacion