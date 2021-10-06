import base64  
import binascii
import textwrap
import random

def encrypt_func(txt, s):  
    result = ""  
    # transverse the plain txt  
    for i in range(len(txt)):  
        char = txt[i]  
        # encypt_func uppercase characters in plain txt  
  
        if (char.isupper()):  
            result += chr((ord(char) + s - 64) % 26 + 65)  
        # encypt_func lowercase characters in plain txt  
        else:  
            result += chr((ord(char) + s - 96) % 26 + 97)  
    return result

def basesf(msg):
    msg_bytes = msg.encode('ascii')
    base64_bytes = base64.b64encode(msg_bytes)
    base64_msg = base64_bytes.decode('ascii')
    return(base64_msg)

def intToBinaryPad(value):
    bint = '{:0b}'.format(value) #to binary
    padded = bint.zfill(8) #paddzeros till 8
    return(padded)

def intToBinary(value):
    bint = '{:0b}'.format(value) #to binary
    return(bint)

def pepew(text):
    result = text
    seed = random.randrange(0,26)
    encryptText = encrypt_func(result,seed)
    basesfText = basesf(encryptText)
    #Transforma el String ingresado en formato ascii
    asciiText = list(bytes(basesfText, 'ascii'))  
    #Usando la función intToBinary, transformamos de ascii a binario y paddeamos con 0's hasta tener un largo de 8
    binaryText = list(map(intToBinaryPad, asciiText))
    #join & append +1
    joinText = (''.join(binaryText)) + '1'
    #padzero hasta tener un largo de 448
    while len(joinText)%512 != 448:
        joinText += '0'
    ####
    length = len((''.join(binaryText)))
    binaryLength = intToBinary(length)
    paddedBinaryLength = binaryLength.zfill(64)
    ####

    binary512 = joinText + paddedBinaryLength

    output = textwrap.wrap(binary512, 32)
    
    lastOutput = []
    lastOutput.append(output[0])
    lastOutput.append(output[-1])
    lastOutput.append(output[-2])
    lastOutput.append(output[1])

    h0 = f'{int(lastOutput[0],2):x}'.zfill(8)
    h1 = f'{int(lastOutput[1],2):x}'.zfill(8)
    h2 = f'{int(lastOutput[2],2):x}'.zfill(8)
    h3 = f'{int(lastOutput[3],2):x}'.zfill(8)


    H = h1+h2+h0+h3
    return (H)

if __name__ == '__main__':

    value = input('input what u wanna "hash": ')
    print(pepew(value))