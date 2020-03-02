from scipy.stats import zscore
import csv
import numpy as np

isi = []
isi2 = []
daftar = []

with open('InterArrival.csv',errors='ignore') as csv_file:
    csv_reader = csv.reader(csv_file, delimiter=',')
    for row in csv_reader:
        f = row
        isi.append(f)

print(len(isi))
print(len(isi[0]))

for i in range (len(isi)):
    if float(isi[i][0]) < 2:
        isi2.append(float(isi[i][0]))
    else:
        isi2.append(0.00000001)

print(type(isi2[0]))

isiz = zscore(isi2)

print(isiz)

for m in range (len(isiz)):
    if isiz[m] > 2.5 and isiz[m] < 3.6:
        daftar.append(m)
    #if isiz[m] > maxi:
    #    maxi = isiz[m]
    #if isiz[m] < mini:
    #    mini = isiz[m]

print(daftar)
print(len(daftar))

typei = []
timpe = []


with open('DaftarAnomaliType.csv', newline='') as csvfile:
     spamreader = csv.reader(csvfile, delimiter=',', quotechar='|')
     for row in spamreader:
         typei.append(row)

#print(typei[0][0])
#print(len(typei))
#print(typei[len(typei)-1])

nile = typei[len(typei)-1]

lengak = len(typei[len(typei)-1])
#print(lengak)

daftartime = [[] for i in range (lengak)]

for i in range (lengak):
    #print(typei[len(typei)-1][i]) 
    daftartime[i].append((int(nile[i])*180)-179)
    daftartime[i].append(int(nile[i])*180)

print("")
print("") 
print("Time Window : ")
print(daftartime)