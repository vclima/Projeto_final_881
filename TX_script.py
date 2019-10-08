import numpy as np 
import matplotlib.pyplot as plt

baudRate=60

Ts=16000
F1=1000
F2=4000
t=np.arange(0,1/baudRate,1/Ts)

wave1=np.sin(2*np.pi*F1*t)
wave2=np.sin(2*np.pi*F2*t)

square1=np.ones((1,1/baudRate))
square2=-np.ones((1,1/baudRate))

sine_output=np.array([])
square_output=np.array([])

bit_string=[0,0,1,0,1]

for i in arange(len(bit_string)):
    if(bit_string[i]==1):
        np.append(sine_output,wave1)
        np.append(square_output,square1)
    else:
        np.append(sine_output,wave2)
        np.append(square_output,square2)

fig, axs = plt.subplots(2)
fig.suptitle('Vertically stacked subplots')
axs[0].plot(t, sine_output)
axs[1].plot(t, square_output)
plt.show()
