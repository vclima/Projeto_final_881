import numpy as np 
import matplotlib.pyplot as plt
from scipy import signal as sig
import imageio
import soundfile as sf

def escreve_bits2(bit_string,filename):
    baudRate=20

    Fs=24000
    F1=800
    F2=1200
    t=np.arange(0,1/baudRate,1/Fs)

    mls=sig.max_len_seq(6)
    header=np.append([1,1,1,1,0,0],mls[0])
    header=np.append(header,[0,0,1,1,1,1])

    bit_string=np.append(header,bit_string)

    wave1=np.cos(2*np.pi*F1*t)
    wave2=np.cos(2*np.pi*F2*t)
    sine_output=np.array([0])

    x=np.arange(0,(len(bit_string)/baudRate)+1,1/Fs)
    x=x[0:len(bit_string)*len(t)]

    for i in range(len(bit_string)):
        if(bit_string[i]=='0'):
            sine_output=np.append(sine_output,wave1)
        else:
            sine_output=np.append(sine_output,wave2)
            
    sf.write(filename,sine_output,Fs)
    
def escreve_bits4(bit_string,filename):
    baudRate=20

    Fs=24000
    F1=600
    F2=800
    F3=1000
    F4=1200
    t=np.arange(0,1/baudRate,1/Fs)

    mls=sig.max_len_seq(6)
    header=np.append([1,1,1,1,0,0],mls[0])
    header=np.append(header,[0,0,1,1,1,1])

    bit_string=np.append(header,bit_string)

    wave1=np.cos(2*np.pi*F1*t)
    wave2=np.cos(2*np.pi*F2*t)
    wave3=np.cos(2*np.pi*F3*t)
    wave4=np.cos(2*np.pi*F4*t)
    sine_output=np.array([0])

    x=np.arange(0,(len(bit_string)/baudRate)+1,1/Fs)
    x=x[0:len(bit_string)*len(t)]

    if(not(len(bit_string)%2)):
        bit_string=np.append(bit_string,'0')

    for i in range(int(len(bit_string)/2)):
        if(bit_string[2*i]=='0' and bit_string[2*i+1]=='0'):
            sine_output=np.append(sine_output,wave1)
        elif(bit_string[2*i]=='0' and bit_string[2*i+1]=='1'):
            sine_output=np.append(sine_output,wave2)
        elif(bit_string[2*i]=='1' and bit_string[2*i+1]=='1'):
            sine_output=np.append(sine_output,wave3)
        else:
            sine_output=np.append(sine_output,wave4)
            
    sf.write(filename,sine_output,Fs)

'''
fig, axs = plt.subplots(2)
fig.suptitle('FSK - F1:50Hz F2=200Hz')
axs[0].plot(x, sine_output[0:len(x)])
axs[1].plot(x, square_output[0:len(x)])
plt.show()
'''

def texttobin(input_string):
    bit_string=[]
    ascii_array=bytearray(input_string,'ascii')
    for i in ascii_array:
        bin_char=bin(i)
        byte=bin_char[2:]
        byte_size=len(byte)
        while(byte_size<8):
            byte='0'+byte
            byte_size=len(byte)
        for bit in byte:
            bit_string=np.append(bit_string,bit)
    return bit_string

def bintotext(bin_string):
    while not len(bin_string)%8:
        bin_string=np.append(bin_string,'0')
    byte_string=[]
    for i in range(int(len(bin_string)/8)):
        byte='0b'
        for j in range(8):
            byte=byte+bin_string[8*i+j]
        byte_string=np.append(byte_string,byte)
    string=''
    for i in byte_string:
        string=string+chr(int(i,2))
    return string

def imgtobin(file):
    image=imageio.imread(file)
    image=image[:,:,0]
    shape=image.shape
    image=np.reshape(image,(1,-1))
    image=np.insert(image,0,shape)
    bit_string=[]
    for i in image:
        bin_char=bin(i)
        byte=bin_char[2:]
        byte_size=len(byte)
        while(byte_size<8):
            byte='0'+byte
            byte_size=len(byte)
        for bit in byte:
            bit_string=np.append(bit_string,bit)
    return bit_string

def bintoimg(bin_string):
    while not len(bin_string)%8:
        bin_string=np.append(bin_string,'0')
    byte_string=[]
    for i in range(int(len(bin_string)/8)):
        byte='0b'
        for j in range(8):
            byte=byte+bin_string[8*i+j]
        byte=int(byte,2)
        byte_string=np.append(byte_string,byte)
    img_shape=byte_string[0:2]
    img=np.array(byte_string[2:])
    img=np.reshape(img,img_shape.astype(int))
    return img

def add_preamble(bit_string,msg):

    size=len(bit_string)
    size=bin(size)[2:]
    bin_size=[]

    for i in size:
        bin_size=np.append(bin_size,i)

    while(len(bin_size)<16):
        bin_size=np.append(0,bin_size)

    bit_string=np.append(bin_size,bit_string)

    if(msg==0):
        bits=np.append([0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],bit_string)
    elif(msg==1):
        bits=np.append([0,0,0,0,0,0,0,0,0,0,1,1,1,1,1],bit_string)
    elif(msg==2):
        bits=np.append([0,0,0,0,0,1,1,1,1,1,0,0,0,0,0],bit_string) 
    elif(msg==3):
        bits=np.append([0,0,0,0,0,1,1,1,1,1,1,1,1,1,1],bit_string)  

    return bits

bitstr=texttobin('Uma noite destas, vindo da cidade para o Engenho Novo, encontrei num trem da Central um rapaz aqui do bairro, que eu conheco de vista e de chapeu.')
bits=add_preamble(bitstr,0)
print(list(bits.astype(int)))
escreve_bits2(bits,'teste_2fsk.wav')
escreve_bits4(bits,'teste_4fsk.wav')
