import math
file1 = open("pokompresji.txt", 'rb')
data=[]
data = file1.read()
file1.close()

def decimalToBinary(number,amount):
    return bin(number).replace("0b", "").zfill(amount)

data1=[]
for i in data:
    data1.append(i)
print(data1)
slownik=[]
dlugosc=data1[0]
print(data1)
for i in range(1,dlugosc+1):
    slownik.append(chr(data[i]))

N=math.ceil(math.log2(dlugosc))

tekst=''
for i in range(dlugosc+1,len(data1)):
    tekst+=decimalToBinary(data1[i], 8)

liczbajedynek = int(tekst[0:3], 2)
tekst=tekst[3:(len(tekst)-liczbajedynek)]
zdekompresowany=''
for i in range(0, len(tekst), N):
    zdekompresowany+=slownik[(int(tekst[i:i + N], 2))]

print(zdekompresowany)
file2=open("zdekompresowany.txt",'w')
file2.write(zdekompresowany)
file2.close()
