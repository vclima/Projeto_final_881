import numpy as np 
import matplotlib.pyplot as plt
from scipy import signal as sig
import soundfile as sf


baudRate=10

Fs=44100
F1=50
F2=200
t=np.arange(0,1/baudRate,1/Fs)

wave1=np.sin(2*np.pi*F1*t)
wave2=np.sin(2*np.pi*F2*t)

square1=np.ones((1,int(Fs/baudRate)))
square2=-np.ones((1,int(Fs/baudRate)))
sine_output=np.array([0])
square_output=np.array([0])

bit_string=[0,0,1,0,1]

x=np.arange(0,(len(bit_string)/baudRate)+1,1/Fs)
x=x[0:len(bit_string)*len(t)]

for i in range(len(bit_string)):
    if(bit_string[i]==1):
        sine_output=np.append(sine_output,wave1)
        square_output=np.append(square_output,square1)
    else:
        sine_output=np.append(sine_output,wave2)
        square_output=np.append(square_output,square2)

'''
fig, axs = plt.subplots(2)
fig.suptitle('FSK - F1:50Hz F2=200Hz')
axs[0].plot(x, sine_output[0:len(x)])
axs[1].plot(x, square_output[0:len(x)])
plt.show()
'''

mls=sig.max_len_seq(6)
header=np.append([1,1,1,1,0,0],mls[0])
header=np.append(header,[0,0,1,1,1,1])

sf.write('file.wav',sine_output,44100)