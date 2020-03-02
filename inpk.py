import csv
from pandas import DataFrame
import matplotlib.pyplot as plt
from sklearn.cluster import KMeans
import tkinter as tk
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
import numpy as np 

isi = []
daftar = []
waktud = []

with open('DataTest.csv',errors='ignore') as csv_file:
    csv_reader = csv.reader(csv_file, delimiter=',')
    for row in csv_reader:
        f = row
        isi.append(f)  

with open('DaftarAnomaliType.csv',errors='ignore') as csv_file:
    csv_reader = csv.reader(csv_file, delimiter=',')
    for row in csv_reader:
        f = row
        daftar.append(f)

waktud = daftar[int(len(daftar))-1]
print(waktud)
del daftar[(int(len(daftar))-1)]
print(daftar)

print(waktud[0])
print(len(waktud))
print(len(daftar))

Anin = [[0 for i in range(2)] for i in range (len(waktud))]

#Mengisi apa yang diperhatikan dari suatu waktu
#Isi dari Anin pada 0 adalah 2

for i in range (len(daftar)):
        for x in range (len(waktud)):
                if(str(waktud[x]) in daftar[i]):
                        Anin[x][0]=((int(waktud[x])-1)*20)+1
                        Anin[x][1]=int(waktud[x])*20
                        Anin[x].append(daftar[i][0])

daftartime = []
print(isi[800][1])

for i in range (len(isi)):
        daftartime.append(isi[i][1])

print(daftartime[940])

for x in range (len(daftartime)):
        daftartime[x] = int(float(daftartime[x]))

print(daftartime[940])

# Sekarang Cari dari index dari waktu yang lucu untuk gantiin dari yang Anin

#for x in range (len(Anin)):\
print(len(Anin))
print(Anin)

awal = 0
ma = max(daftartime)
nilai = ma
print('Panjang daftartime : ' + str(len(daftartime)))
awal = 0
for x in range (len(Anin)):
        for i in range (0,2):
                nilai = ma
                for m in range (awal,len(daftartime)):
                        Mak = 0
                        bam = 0
                        Mak = int(float(Anin[x][i]))
                        #print('Nilai Mak :')
                        #print(Mak)
                        bam = daftartime[m]
                        #print('Nilai bam :')
                        #print(bam)
                        if Mak == bam :
                                Anin[x][i] = m
                                awal = m
                                break
                        elif Mak < bam :
                                Anin[x][i] = m
                                awal = m
                                break
                        
print(Anin)

print(len(Anin))

dataout = []

for x in range (len(Anin)):
        #print(len(Anin[x]))
        for m in range (Anin[x][0],Anin[x][1]):
                for n in range (2,len(Anin[x])):
                        # -1
                        #print('Nilai isi : ')
                        #print(isi[m][4])
                        #print('Nilai n : ')
                        #print(Anin[x][n])
                        if isi[m][4] == Anin[x][n]:
                               dataout.append(isi[m])

print('len dari dataout : ' + str(len(dataout)))
              
#for j in range (0,5):
#        print(dataout[j])

datasource = []
datadest = []
datatype = []
datalength = []
dataport = []



for m in range (len(dataout)):
        datasource.append(dataout[m][2])
        datadest.append(dataout[m][3])
        datatype.append(dataout[m][4])
        datalength.append(dataout[m][5])
        dataport.append(dataout[m][7])

print(datasource[0])
print(datadest[0])
print(datatype[0])
print(datalength[0])
print(dataport[0])

unisource = np.unique(datasource)

print(len(unisource))
print(unisource)

#Data yang diambil :
#1.	Data destination dari source ip unique
#2.	Data destination ke ip unique dari source terserah (count aja boleh)
#3.	Data port dari ip unique
#4.	Data packet type dari ip unique
#5.	Data packet length dari ip unique


aktivitastujuanip = [[] for x in range (len(unisource))] # 1  # Udah
aktivitastypacip = [[] for x in range (len(unisource))]  # 4  # Udah
aktivitaskeip = [[] for x in range (len(unisource))]     # 2  # Udah
aktivitaslengthip = [[] for x in range (len(unisource))] # 5  # Udah
aktivitasportip = [[] for x in range (len(unisource))]   # 3  # Udah

print(len(aktivitastujuanip))
print(len(aktivitastujuanip[0]))

count = 0

for x in range (len(unisource)):
        count = 0
        for m in range (len(dataout)):
                if unisource[x] == datasource[m]:
                        aktivitastujuanip[x].append(datadest[m])    # Dari unique append jika source sama dengan unique
                        aktivitastypacip[x].append(datatype[m])     # Dari unique jika sama dengan source maka append typenya
                        aktivitaslengthip[x].append(datalength[m])  # Dari unique jika sama dengan source maka append length
                        aktivitasportip[x].append(dataport[m])      # Dari unique jika sama dengan source maka append portnya

                if unisource[x] == datadest[m]:
                        count = count + 1            # Jika Unique sama dengan tujuan maka tambahin kepada count untuk hitung aktivitas kepada ip unique tersebut
        aktivitaskeip[x] = count

# for x in range (0,len(unisource)):
#         print("DATA KE : "+str(x))
#         print("Unisource IP :")
#         print(unisource[x])
#         print("Hasil tujuan IP :")
#         print(aktivitastujuanip[x])
#         print("Hasil type IP :")
#         print(aktivitastypacip[x])
#         print("Hasil Length IP :")
#         print(aktivitaslengthip[x])
#         print("Hasil count kepada IP :")
#         print(aktivitaskeip[x])
#         print("Port yang digunakan :")
#         print(aktivitasportip[x])

print(len(unisource))
print(len(aktivitastujuanip[0]))
print(len(aktivitastypacip))
print(len(aktivitaslengthip))
print(len(aktivitaskeip))
print(len(aktivitasportip))
print(aktivitaskeip)

insideip = ['192.168.74.128']

print(len(insideip))
print(len(insideip[0]))
print(insideip[0])

#for x in range (len(unisource)):
#        print(unisource[x])

#print(unisource[54])
#print(insideip[0])
#if unisource[54] == insideip[0]:
#        print("SAMA")

with open('InputKM.csv', 'w', newline='') as csvfile:
    spamwriter = csv.writer(csvfile, delimiter=',',
                            quotechar='|', quoting=csv.QUOTE_MINIMAL)
        
    for i in range (len(unisource)):
                if unisource[i] != insideip[0]:
                     spamwriter.writerow(unisource[i])
                     spamwriter.writerow(aktivitastujuanip[i])
                     spamwriter.writerow(aktivitastypacip[i])
                     spamwriter.writerow(aktivitaslengthip[i])
                     spamwriter.writerow(aktivitasportip[i])
                     man = []
                     man.append(aktivitaskeip[i])
                     spamwriter.writerow(man)  
    
#     for i in range (len(unisource)):
#         if unisource[i] != insideip[0] and insideip[0] in aktivitastujuanip[i]:
#                     spamwriter.writerow(unisource[i])
#                     spamwriter.writerow(aktivitastujuanip[i])
#                     spamwriter.writerow(aktivitastypacip[i])
#                     spamwriter.writerow(aktivitaslengthip[i])
#                     spamwriter.writerow(aktivitasportip[i])
#                     man = []
#                     man.append(aktivitaskeip[i])
#                     spamwriter.writerow(man)
#         elif i == 59 or i == 60 or i == 50 or i == 51 or i == 42 or i == 40 or i == 17 or i == 23 or i == 28 or i == 25 :
#                     spamwriter.writerow(unisource[i])
#                     spamwriter.writerow(aktivitastujuanip[i])
#                     spamwriter.writerow(aktivitastypacip[i])
#                     spamwriter.writerow(aktivitaslengthip[i])
#                     spamwriter.writerow(aktivitasportip[i])
#                     man = []
#                     man.append(aktivitaskeip[i])
#                     spamwriter.writerow(man)
     