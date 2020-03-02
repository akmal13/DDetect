import csv
from scipy.stats import zscore

HasP = []
Data = []
Nilsem = []
timeno = []

with open('HasPredict.csv', newline='') as csvfile:
     spamreader = csv.reader(csvfile, delimiter=',', quotechar='|')
     for row in spamreader:
         HasP.append(row)

with open('TypeFrequency2.csv', newline='') as csvfile:
     spamreader = csv.reader(csvfile, delimiter=',', quotechar='|')
     for row in spamreader:
         Data.append(row)
#print(HasP[0][1])

for i in range (len(HasP)):
    for m in range (len(HasP[0])):
        x = HasP[i][m].replace("[", "")
        x = x.replace("]", "")
        x = float(x)
        HasP[i][m] = x

daftaran = [[] for i in range (len(Data[0]))]

print('Len daftaran[0] : '+str(len(daftaran[0])))
print('Len daftaran : '+str(len(daftaran)))
        
print(len(HasP[0]))
print('Len Data : '+str(len(Data)))
print('Len Data[0] : '+str(len(Data[0])))
print(Data[0][0])
print(Data[2][0])

for i in range (len(HasP)):
    for m in range (len(HasP[0])):
        x = float(Data[m+2][i])
        Data[m+2][i] = x
        #print('i : '+str(i)+'m : '+str(m))
        print('Data : '+str(Data[m+2][i])+'HasP : '+str(HasP[i][m]))
        Data[m+2][i] = abs(Data[m+2][i]-HasP[i][m])
         
print(Data)
print('Panjang Data : '+str(len(Data)))
#Masih Bagus sampe sini
for i in range (len(Data[0])):
    for m in range (2,len(Data)):
        Nilsem.append(float(Data[m][i]))
    #print(Nilsem)
    isiz = zscore(Nilsem)
    print('Panjang isiz : '+str(len(isiz)))
    print(isiz)
    daftaran[i].append(Data[0][i])
    for n in range (len(isiz)):
        if isiz[n] > 3.6:   ### Adjust sampe ketemu yang paling bagus
            daftaran[i].append(n+2) 
    Nilsem = []

print(daftaran)
print(daftaran[0][0])

for x in range (len(daftaran)):
    daftaran[x].append(-5)

wu = 0
for m in range (len(daftaran)):
   for n in range (1,len(daftaran[m])-1):
       wu = daftaran[m][n]
       print('wu : '+str(wu))
       if daftaran[m][n+1] == wu+1:
           continue
       elif (daftaran[m][n-1] == (daftaran[m][n]-1)):
            daftaran[m][n] = -5 

# Temukan yang berurutan , hilangin yang paling akhir

for i in range (len(daftaran)):
    ban = daftaran[i].count(-5)
    for m in range (ban):
        daftaran[i].remove(-5)

sementara = []

for i in range (len(daftaran)):
    for n in range (1, len(daftaran[i])):
        sementara.append(daftaran[i][n])

mylist = list(dict.fromkeys(sementara))
mylist.sort()

print(mylist)

#print(len(daftaran[0]))

with open('DaftarAnomaliType.csv', 'w', newline='') as csvfile:
    spamwriter = csv.writer(csvfile, delimiter=',',
                            quotechar='|', quoting=csv.QUOTE_MINIMAL)
    for i in range (len(daftaran)):
        spamwriter.writerow(daftaran[i])
    spamwriter.writerow(mylist)