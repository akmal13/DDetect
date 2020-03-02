import csv
from pandas import DataFrame
import matplotlib.pyplot as plt
from sklearn.cluster import KMeans
import tkinter as tk
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
import numpy as np 
from math import log, e
import time

start = time.time()

def enthropy(labels, base=None):
        """ Computes entropy of label distribution. """

        n_labels = len(labels)
         
        if n_labels <= 1:
                return 0

        value, counts = np.unique(labels, return_counts=True)
        probs = counts / n_labels
        n_classes = np.count_nonzero(probs)

        if n_classes <= 1:
                return 0

        ent = 0.

        # Compute entropy
        base = e if base is None else base
        for i in probs:
                ent -= i * log(i, base)

        return ent

isi = []

with open('InputKM.csv',errors='ignore') as csv_file:
    csv_reader = csv.reader(csv_file, delimiter=',')
    for row in csv_reader:
        f = row
        isi.append(f)  

#print(isi)
print('panjang isi : '+ str(len(isi)))
pandat = len(isi)
pandat = int(pandat/6)
print('pandat = '+ str(pandat))

#print(isi[3])

dataperip = [[] for i in range (pandat)]
datahasil = [[] for i in range (pandat)]

# 0 = Unique source
# 1 = Tujuan IP
# 2 = Type packet ip
# 3 = Length ip
# 4 = Port destination
# 5 = Banyaknya paket ke unisource

for m in range (pandat):
        for x in range (0,6):
                index = (m * 6)+x
                #print(index)
                dataperip[m].append(isi[index])
                if x == 0:
                        datahasil[m].append(isi[index])
                elif x == 1 or x == 2 or x == 3 or x == 4:
                        datahasil[m].append(enthropy(isi[index]))
                elif x == 5:
                        keluar = len(isi[index-4])
                        masuk = int(isi[index][0])
                        if masuk == 0 :
                                datahasil[m].append(0)
                        else :
                                hasil = masuk / keluar
                                datahasil[m].append(hasil)

                        

#print(dataperip[0])
#print(dataperip[1])
#print(dataperip[863])

#labels=[1,3,5,2,3,5,3,2,1,3,4,5]
#labels2=[1,1,1,1,1,1,2]\
#print(enthropy(labels2))

for x in range (0,3):
        print(dataperip[x])
        print(datahasil[x])

#print(dataperip[863])
#print(datahasil[863])

#print(isi[5182])
#print(isi[5183])

# Masukin datahasil kepada a,b,c,d,e

print(len(datahasil))

a = []
b = []
c = []
d = []
e = []

# 0 = Unique source
# 1 = Enthropy Tujuan IP
# 2 = Enthropty Type packet ip
# 3 = Enthropy Length ip
# 4 = Enthropy Port destination
# 5 = Banyaknya paket diterima / paket dikirim

for j in range (len(datahasil)):
        a.append(datahasil[j][1])
        b.append(datahasil[j][2])
        c.append(datahasil[j][3])
        d.append(datahasil[j][4])
        e.append(datahasil[j][5])

print(a)

for m in range (8,14):
        print('Data ke : ' + str(m))
        print(datahasil[m][0])
        print(datahasil[m][1])
        print(datahasil[m][2])
        print(datahasil[m][3])
        print(datahasil[m][4])
        print(datahasil[m][5])

print(len(dataperip[0]))

Data = {'a': e,
        #'b': e,
        #'c': c,
        #'d': d,
        #'e': e,
       }

df = DataFrame(Data,columns=['a'])

#df = DataFrame(Data,columns=['a','b','c','d','e'])
  
kmeans = KMeans(n_clusters=2).fit(df)
centroids = kmeans.cluster_centers_

root= tk.Tk()

canvas1 = tk.Canvas(root, width = 100, height = 100)
canvas1.pack()

label1 = tk.Label(root, text=centroids, justify = 'center')
canvas1.create_window(70, 50, window=label1)

figure1 = plt.Figure(figsize=(5,4), dpi=100)
ax1 = figure1.add_subplot(111)
print(kmeans.labels_.astype(float))
kmscer = kmeans.labels_.astype(int)
#ax1.scatter(df['a'], df['b'], c= kmeans.labels_.astype(float), s=50, alpha=0.5)
#ax1.scatter(centroids[:, 0], centroids[:, 1], c='red', s=50)
#scatter1 = FigureCanvasTkAgg(figure1, root) 
#scatter1.get_tk_widget().pack(side=tk.LEFT, fill=tk.BOTH)
end = time.time()
print('Time : '+ str(end-start))
jumnol = 0
jumsat = 0
jumlanor = 0
jumlafn = 0
print('BANYAKNYA DARI PER IP')

for x in range (len(kmscer)):
        print('Data ke '+ str(x) +' Dengan besar nilai : '+ str(len(dataperip[x][3])))

for x in range (len(kmscer)):
        if kmscer[x] == 0 :
                jumnol = jumnol + len(dataperip[x][3])
        if kmscer[x] == 1 :
                jumsat = jumsat + len(dataperip[x][3])
        if x == 11 or x == 12 or x == 13:
                jumlanor = jumlanor + len(dataperip[x][3])
        if x <= 7 :
                jumlafn = jumlafn + len(dataperip[x][3])

print('Jumlah satu : ' + str(jumsat))
print('Jumlah nol : ' + str(jumnol))
print('Jumlah normal : '+ str(jumlanor))
print('Jumlah FP : ' + str(jumlafn))
print('Jumlah FN : ' + str(jumsat - jumlanor))

root.mainloop()