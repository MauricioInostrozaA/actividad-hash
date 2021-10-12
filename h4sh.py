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

def Lrotate(input,d): 
  
    # slice string in two parts for left and right 
    Lfirst = input[0 : d] 
    Lsecond = input[d :]
    # now concatenate two parts together 
    return(Lsecond + Lfirst)

# Function to find the
# XOR of the two Binary Strings
def xor(a, b, n):
    ans = ""
     
    # Loop to iterate over the
    # Binary Strings
    for i in range(n):
         
        # If the Character matches
        if (a[i] == b[i]):
            ans += "0"
        else:
            ans += "1"
    return ans

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
    
    for i in range(16, 80):
        wordA = output[i-3]
        wordB = output[i-8]
        wordC = output[i-14]
        wordD = output[i-16]

        xorA = xor(wordA,wordB,len(wordA))
        xorB = xor(xorA,wordC,len(xorA))
        xorC = xor(xorB,wordD,len(xorB))
        newWord = Lrotate(xorC, 1)
        output.append(newWord)

    h0 = a = '01100111010001010010001100000001'
    h1 = b = '11101111110011011010101110001001'
    h2 = c = '10011000101110101101110011111110'
    h3 = d = '00010000001100100101010001110110'
    h4 = e = '11000011110100101110000111110000'

    for i in range(80):
        if 0 <= i <= 19:
            f = int(d,2) ^ (int(b,2) & (int(c,2) ^ int(d,2)))
            k = '1011010100000100111100110011001'
        elif 20 <= i <= 39:
            f = int(b,2) ^ int(c,2) ^ int(d,2)
            k = '1101110110110011110101110100001'
        elif 40 <= i <= 59:
            f = (int(b,2) & int(c,2)) | (int(b,2) & int(d,2)) | (int(c,2) & int(d,2))
            k = '10001111000110111011110011011100'
        elif 60 <= i <= 79:
            f = int(b,2) ^ int(c,2) ^ int(d,2)
            k = '11001010011000101100000111010110'

        word = output[i]   
        tempA = bin(int(Lrotate(a,5),2) + int(f))
        tempB = bin(int(tempA,2) + int(e,2))
        tempC = bin(int(tempB,2) + int(k,2))
        temp = bin(int(tempC,2) + int(word,2))  

        temp = temp[2:]
        e = d
        d = c
        c = Lrotate(b,30)
        b = a
        a = temp
    h0 = bin(int(h0,2)+int(a,2))
    h1 = bin(int(h1,2)+int(b,2))
    h2 = bin(int(h2,2)+int(c,2))
    h3 = bin(int(h3,2)+int(d,2))
    h4 = bin(int(h4,2)+int(e,2))

    lasth0 = hex(int(h0[2:34],2))
    lasth1 = hex(int(h1[2:34],2))
    lasth2 = hex(int(h2[2:34],2))
    lasth3 = hex(int(h3[2:34],2))
    lasth4 = hex(int(h4[2:34],2))

    lastH = lasth0 + lasth1 + lasth2 + lasth3 + lasth4

    return (lastH)

def entropy():

    return()

if __name__ == '__main__':
    
    print("[1] Hඞsh a string")
    print("[2] Hඞsh a text file")
    print("[3] Entropy of a text file")
    print("[0] Exit")

    option = int(input("Enter your option: "))

    while option != 0:
        if option == 1:
            print("Hඞshing a string.")
            value = input('Input a string you wanna hඞsh: ')
            print("{} | {} ".format(value, pepew(value)))

        elif option == 2:
            print("Hඞshing a text file.")
            value = input("Input a file you wanna hඞsh: ")
            file1 = open(value, 'r')
            count = 0

            for line in file1:
                count += 1
                eline = line.strip()
                print("{} | {}".format(eline, pepew(eline)))

        elif option == 3:
            print("Calculate Entropy.")
            print("work in progress :(")

        else:
            print("Invalid option.")

print("cya ඞ")
