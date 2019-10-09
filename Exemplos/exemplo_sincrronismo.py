import numpy as np
from scipy import signal as sig
import random
import matplotlib.pyplot as plt

#Criação do cabeçalho 
mls=sig.max_len_seq(6)
header=np.append([1,1,1,1,0,0],mls[0])
header=np.append(header,[0,0,1,1,1,1])
print(len(header))

#Criação de uma sequência aleatória de 900 bits
sequence=random.choices([0,1],k=900)
position=random.randint(0,len(sequence))

#Inserção do cabeçalho em uma posição aleatória
message=np.insert(sequence,position,header)
print(position)

#Calculo da correlação cruzada
corr=np.correlate(message,header,mode='valid')
corr_position=np.argmax(corr)
print(corr_position)

#Plot da correlação cruzada
plt.plot(corr)
plt.title('Identificação do início do cabeçalho')
plt.plot(corr_position,corr[corr_position],'or')
plt.show()