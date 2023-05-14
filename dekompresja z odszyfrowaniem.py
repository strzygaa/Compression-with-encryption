import math
file1 = open("zaszyfrowany.txt", 'rb')
data=[]
data = file1.read()
file1.close()

######
file3=open("klucz.txt", 'r')
klucz=file3.read()
file3.close()
klucz=list(klucz)
tekstklucz=[]

for i in range(0, len(data)):
    m = i % len(klucz)
    tekstklucz.append(klucz[m])


tekstodszyfrowany = []
for i in range(0, len(data)):
    tekstodszyfrowany.append((int(data[i] - ord(tekstklucz[i])+256)) % 256)

def decimalToBinary(number,amount):
    return bin(number).replace("0b", "").zfill(amount)

tekstodszyfrowany1=[]
for i in tekstodszyfrowany:
    tekstodszyfrowany1.append(i)

slownik=[]
dlugosc=tekstodszyfrowany1[0]

for i in range(1,dlugosc+1):
    slownik.append(chr(tekstodszyfrowany[i]))

N=math.ceil(math.log2(dlugosc))

tekst=''
for i in range(dlugosc+1,len(tekstodszyfrowany1)):
    tekst+=decimalToBinary(tekstodszyfrowany1[i], 8)

liczbajedynek = int(tekst[0:3], 2)
tekst=tekst[3:(len(tekst)-liczbajedynek)]
zdekompresowany=''
for i in range(0, len(tekst), N):
    zdekompresowany+=slownik[(int(tekst[i:i + N], 2))]


file2=open("odszyfrowany.txt",'w')
file2.write(zdekompresowany)
file2.close()
