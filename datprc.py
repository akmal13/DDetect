import csv
import statistics 
import math
import ctypes 
from collections import Counter


time = []
length = []   # Besarnya dari paket || Pakai
tipe = []
bedtipe = []
interarrival = []  # jarak antara waktu dari pengiriman dan sampai || Pakai
#deskripsi = []
tipe1 = []  # Tipe dari protocol yang berbeda
tipe2 = []  # Banyaknya yang muncul dari protocol tersebut || Pakai


## Yang untuk tipe dari satu hari harus dibagi menjadi per 2 menit, Dari data yang dari 1 haru menjadi

count = 0
with open('dat.csv',errors='ignore') as csv_file:
    csv_reader = csv.reader(csv_file, delimiter=',')
    for row in csv_reader:
        f = row[0]
        m=f.replace('"','')
        count = count + 1
        kala1 = int(row[5])
        length.append(kala1)
        kala2 = float(row[1])
        time.append(kala2)
        str3 = ''.join(str(e) for e in row[4])
        tipe.append(str3)
        #str4 = ''.join(str(e) for e in row[6])
        #deskripsi.append(str4)
        
csv_file.close()

for i in range (0,len(time)-1):
    waktu = time[i+1]-time[i]
    interarrival.append(waktu)

m = statistics.median(interarrival)
interarrival.append(m)

# kalo ada ACK maka bukan -1 

#for i in range (0,len(deskripsi)):
#    if (str(deskripsi[i]).find("[ACK]")) == -1:
#        deskripsi[i] = 0
#    else:
#        deskripsi[i] = 1 

for x in tipe:
    if x not in tipe1:
        tipe1.append(x)
print(tipe1)

counttype = [[]*len(tipe1)]   
count = 0
for i in tipe1:
    tipe2.append(tipe.count(i))
    count = count+1
print(tipe2)

pembagi = 20
awal = 0

akhirdata = len(time) - 1
waktuterakhir = time[akhirdata]

banyakpembag = math.floor(waktuterakhir/20)
daftarpembagi = []
pembatas = 20
for i in range (0,len(time)):
    if (time[i]>=pembatas):
        daftarpembagi.append(i)
        pembatas = pembatas+20

print(daftarpembagi)
maxpacket = 0
for i in range (0,len(daftarpembagi)):
    if daftarpembagi[i] > maxpacket:
        maxpacket = daftarpembagi[i]

print(maxpacket)
Matriks = [[[]for m in range(2)] for y in range(banyakpembag)]

mats = []

for m in range (0,len(daftarpembagi)):
    for i in range (0,daftarpembagi[m]):
        ### Masukin data yang per 20 detik pada array
        Matriks[m][0].append(tipe[i])
        Matriks[m][1].append(length[i])


print(len(Matriks))

# Matriks[x][y][z]  , X untuk waktu batch pertama, y untuk tipe data 0(tipe), 1(length), z data 
daftart = []
for m in range (len(Matriks)):
    listtipe = set(Matriks[m][0])
    #listlength = set(Matriks[m][1])
    for e in listtipe:
        daftart.append(e)

daftart = set(daftart)
#print(listlength)

daftartipe = []
# daftartipe adalah daftar dari tipe packet pada traffic
for e in daftart:
    daftartipe.append(e)

print(daftartipe) 

#daftarlength = [[[]for i in range (len(daftartipe))]for n in range (len(Matriks))]
# daftarlength adalah daftar dari length per tipe packet [m][n][z] . M adalah batch waktu, n adalah tipe packet , z adalah daftar dari length

#for m in range (len(Matriks)):
#    for i in range (len(Matriks[m][0])):
#        for x in range (len(daftartipe)):
#            if Matriks[m][0][i] == daftartipe[x] :
#                daftarlength[m][x].append(Matriks[m][1][i])

#setlength = [[[] for i in range (len(daftartipe))]for m in range (len(Matriks))]
# Setlength adalah set untuk length per tipe packet

nilae = 0
#for i in range (len (daftarlength[0])):
#    nilae += len(daftarlength[0][i])

#print(nilae)

#sementara = 0

#for m in range (len(Matriks)):
#    for x in range (len(daftarlength[0])):
#        sementara = set(daftarlength[m][x])
#        for e in sementara:
#            setlength[m][x].append(e)

#print(daftarlength[0][3])
#print(setlength[0][3])

# Count tipe dari tiap 3 menit

counttipe = [[]for i in range (len(Matriks))]

print(daftartipe)

# Matriks[m][0][z] , m waktu, 0 menandakan tipe, z menandakan isinya

for i in daftartipe:
        for n in range (len(Matriks)):
                counttipe[n].append(Matriks[n][0].count(i))
    
print(counttipe)

# Count length per 3 menit

#print(setlength[0][0][0])
#print(len(setlength))
#print(len(setlength[0]))
#print(len(setlength[0][0]))
#print(len(setlength[0][0][0])) Sudah data

#gablength = [[]for m in range (len(setlength))]

#for m in range (len(setlength)):
#        for n in range (len(setlength[m])):
#                for i in range (len(setlength[m][n])):
#                        gablength[m].append(setlength[m][n][i])

#for n in range (len(gablength)):
#        gablength[n] = set(gablength[n])

#gabungantipelength = []

#for m in range (len(gablength)):
#        for e in gablength[m]:
#                gabungantipelength.append(e)

#print(gabungantipelength)

#print(Matriks[0][1][1])

#hasilcount = [[]for i in range (len(Matriks))]

#for n in range (len(Matriks)):
#        for i in gabungantipelength:
#                hasilcount[n].append(Matriks[n][1].count(i))
        
#print(hasilcount)

# Check Nilai hasil count sesuai
#jumla = 0
#for x in range (len(hasilcount[0])):
#        jumla += hasilcount[0][x]

#print(jumla)

# Check Nilai hasil count sesuai
print('Penanda Print')

with open('InterArrival2.csv', 'w', newline='') as csvfile:
    fieldnames = ['InterArrival']
    writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
    writer.writeheader()
    for i in range (len(interarrival)):
            writer.writerow({'InterArrival': interarrival[i]})
    
#with open('LengthFrequency.csv', 'w', newline='') as csvfile:
#    spamwriter = csv.writer(csvfile, delimiter=',',
#                            quotechar='|', quoting=csv.QUOTE_MINIMAL)
#    spamwriter.writerow(gabungantipelength)
#    for i in range (len(hasilcount)):
#        spamwriter.writerow(hasilcount[i])

for i in range (len(counttipe[0])):
    for j in range (len(counttipe)-1,1,-1):
        counttipe[j][i] = int(counttipe[j][i])-int(counttipe[j-1][i])

with open('TypeFrequency2.csv', 'w', newline='') as csvfile:
    spamwriter = csv.writer(csvfile, delimiter=',',
                            quotechar='|', quoting=csv.QUOTE_MINIMAL)
    spamwriter.writerow(daftartipe)    
    for i in range (len(counttipe)):
        spamwriter.writerow(counttipe[i])    

#print(length)

#print(time) 

#print(source) 

#print(destination)    

#print(tipe)

#print(deskripsi)

#print(len(time))

#print(interarrival)
#print(len(interarrival))