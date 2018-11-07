import pytest
import numpy as np
import pylab as plt 
import nidaqmx
import random
from nidaqmx import system, constants

import collections
import re

import pytest
import time
from nidaqmx.constants import (
    Edge, TriggerType, AcquisitionType, LineGrouping, Level, TaskMode)
#---------------------------------------------------------------------
#---------------------   Lazo de control   ---------------------------
#---------------------------------------------------------------------


sample_rate=12000  #dividimos a la mitad la frecuencia de toma de datos. 24K para cada canal
samples_per_channel=1000 #maximo = 1000
numero_de_dispositivo = 4
frecuencia = '-'
señal = 'Funte-Voltaje'
que_medimos = 'test-analog-imput'


#---------------------------------------------------------------------
#---------------------   Emision de pulso - vemos la salida por el line0 = pin1 ---------------------------


do_line = 'Dev4/port0/line0'

with nidaqmx.Task() as task:
    task.do_channels.add_do_chan(
            do_line, line_grouping=LineGrouping.CHAN_PER_LINE)    #definimos al pin "do_line" como un digital output
    data = [False,True,False,True,False,True,False,True]
    
    i=0
    read_data=[]
    while i<len(data):
        if data[i] == True:
            task.write(True)
            read_data.append(task.read())
            time.sleep(2)
            
        else:
            task.write(False)            
            read_data.append(task.read())
            time.sleep(0.5)
        i+=1
    task.write(False)   

#
####------->    Lectura    Canal 0
with nidaqmx.Task() as task:
    task.ai_channels.add_ai_voltage_chan("Dev{}/ai0".format(numero_de_dispositivo), 
                      terminal_config=constants.TerminalConfiguration.RSE, 
                      units=constants.VoltageUnits.VOLTS)  #pusimos esta linea para setear el modo de medición
    task.timing.cfg_samp_clk_timing(sample_rate) #agregamos frecuencia de sample rate
    data0 = task.read(number_of_samples_per_channel=samples_per_channel)
 
    
    
    
    
#    cin=0
#    while task.read(number_of_samples_per_channel=samples_per_channel) > 10:
#        c1+=1
#    cout=0
#    while task.read(number_of_samples_per_channel=samples_per_channel) < -10:
#        c2+=1
#        
#    tin = cin/sample_rate
#    tout = cout/sample_rate
#    tiempo = tin+tout
#    
    plt.plot(np.arange(samples_per_channel)/sample_rate, data0,'s-', label = 'Canal 0')
    plt.xlabel('seg')
    plt.ylabel('V')
    plt.legend(loc='upper right')
    plt.show()
#


####------->    Guardamos 
#
#NAMES  = np.array(['tiempo','canal0'])
#FLOATS = np.array([np.arange(samples_per_channel)/sample_rate, data0])
#DAT =  np.column_stack((NAMES, FLOATS)).T
#
##Nombre del archivo txt  
#np.savetxt('{}-Frec={}-Sample_rate={}-señal={}'.format(que_medimos,frecuencia,sample_rate,señal), DAT, delimiter="\t", fmt='%s')


