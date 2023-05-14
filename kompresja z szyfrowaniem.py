import math
file1 = open("dokompresji.txt", 'r')
data = file1.read()
file1.close()

####
file3=open("klucz.txt", 'r')
klucz=file3.read()
file3.close()
klucz=list(klucz)
tekstklucz=[]
#####

def decimalToBinary(number, amount):
    return bin(number).replace("0b", "").zfill(amount)


slownik=list(set(data))
slownik=sorted(slownik)
dlugoscslownika=len(slownik)

N=math.ceil(math.log2(dlugoscslownika))

R=(8-(3+N*len(data)) %8 ) % 8

slowniktekst=''
with open("zaszyfrowany.txt", 'wb') as file2:

    byte_array=bytearray()
    byte_array.append(dlugoscslownika)
    for i in slownik:
        slowniktekst+=i

    for char in slowniktekst:
        byte_array.append(ord(char))

    slownikbinarnie=[]
    for i in range(0,len(slownik)):
        slownikbinarnie.append(decimalToBinary(i,N))

    binarnie=''
    for i in data:
        binarnie+=slownikbinarnie[slownik.index(i)]

    binarnie2=''
    binarnie2+=decimalToBinary(R,3)
    binarnie2+=binarnie
    binarnie2+=str(1)*R
    for i in range(0, len(binarnie2), 8):
        chunk = chr(int(binarnie2[i:(i + 8)], 2))
        byte_array.append(ord(chunk))

####
    for i in range(0, len(byte_array)):
        m = i % len(klucz)
        tekstklucz.append(klucz[m])
    tekstzaszyfrowany = []
    for i in range(0, len(byte_array)):
        tekstzaszyfrowany.append((ord(tekstklucz[i]) + int(byte_array[i])) % 256)

    print(tekstzaszyfrowany)
    
    byte_array2=bytearray()
    for i in range(0,len(tekstzaszyfrowany)):
        byte_array2.append(tekstzaszyfrowany[i])
    file2.write(bytes(byte_array2))



