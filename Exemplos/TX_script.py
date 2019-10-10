import numpy as np 
import matplotlib.pyplot as plt
from scipy import signal as sig
import imageio
import soundfile as sf

def escreve_bits(bit_string):
    baudRate=10

    Fs=44100
    F1=50
    F2=200
    t=np.arange(0,1/baudRate,1/Fs)

    mls=sig.max_len_seq(6)
    header=np.append([1,1,1,1,0,0],mls[0])
    header=np.append(header,[0,0,1,1,1,1])

    bit_string=np.append(header,bit_string)

    wave1=np.sin(2*np.pi*F1*t)
    wave2=np.sin(2*np.pi*F2*t)
    sine_output=np.array([0])

    x=np.arange(0,(len(bit_string)/baudRate)+1,1/Fs)
    x=x[0:len(bit_string)*len(t)]

    for i in range(len(bit_string)):
        if(bit_string[i]=='1'):
            sine_output=np.append(sine_output,wave1)
        else:
            sine_output=np.append(sine_output,wave2)
            
    sf.write('file.wav',sine_output,44100)

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

bitstr=texttobin('Ao longo de seus 50 anos de historia, a FEEC se consolidou como uma das unidades com maior qualidade de ensino e de pesquisa na Unicamp e no Brasil. A FEEC esta comprometida com a excelencia academica nas areas de ensino, pesquisa e extensao. Na graduacao, oferece o curso de Engenharia Eletrica nos periodos diurno (integral) e noturno e o curso de Engenharia de Computacao, este ministrado em conjunto com o Instituto de Computacao.')
bits=np.append([0,0,0,0,0,1,1,1,1,1,1,1,1,1,1],bitstr)
print(list(bits.astype(int)))
print(list(bitstr.astype(int)))
