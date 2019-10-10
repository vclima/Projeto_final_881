import numpy as np

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


def app_decoder(bit_stream):
    bittype_code=bit_stream[0:15]
    type_code=[]
    for i in range(3):
        bits=bittype_code[5*i:5*i+5]
        if(sum(bits)>2):
            type_code[i]=1
        else:
            type_code[i]=0

    if(type_code==[0,0,0]):
        recebido=bit_stream[15:]
        objetivo=np.array([])
        while len(recebido)<len(objetivo):
            recebido=np.append(recebido,0)

        recebido=recebido[0:len(objetivo)]
        acerto=sum(recebido==objetivo)/len(objetivo)
        print('Taxa de acerto: '+str(acerto))
        try:
            out=bintotext(recebido)
            print(out)
        except:
            print('Não consigo exibir o dado recebido')

    elif(type_code==[0,0,1]):
        recebido=bit_stream[15:]
        objetivo=np.array([])
        while len(recebido)<len(objetivo):
            recebido=np.append(recebido,0)
        recebido=recebido[0:len(objetivo)]
        acerto=sum(recebido==objetivo)/len(objetivo)
        print('Taxa de acerto: '+str(acerto))
        try:
            out=bintoimg(recebido)
            print(out)
        except:
            print('Não consigo exibir o dado recebido')
    
    elif(type_code==[0,1,0]):
        recebido=bit_stream[15:]
        objetivo=np.array([])
        while len(recebido)<len(objetivo):
            recebido=np.append(recebido,0)
        recebido=recebido[0:len(objetivo)]
        acerto=sum(recebido==objetivo)/len(objetivo)
        print('Taxa de acerto: '+str(acerto))
        try:
            out=bintotext(recebido)
            print(out)
        except:
            print('Não consigo exibir o dado recebido')
    
    elif(type_code==[0,1,1]):
        recebido=bit_stream[15:]
        objetivo=np.array([])
        while len(recebido)<len(objetivo):
            recebido=np.append(recebido,0)
        recebido=recebido[0:len(objetivo)]
        acerto=sum(recebido==objetivo)/len(objetivo)
        print('Taxa de acerto: '+str(acerto))
        try:
            out=bintotext(recebido)
            print(out)
        except:
            print('Não consigo exibir o dado recebido')

    else:
        recebido=bit_stream[15:]
        print('Codigo não reconhecido')
        try:
            out=bintotext(recebido)
            print(out)
        except:
            print('Não consigo exibir o dado recebido')
    return