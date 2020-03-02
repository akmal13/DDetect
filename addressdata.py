import csv

data = []
data1 = []
match = []
match1 = []
nama = []

with open('TypeFrequency.csv',errors='ignore') as csv_file:
    csv_reader = csv.reader(csv_file, delimiter=',')
    for row in csv_reader:
        f = row
        data.append(f)
        break
		
		
with open('TypeFrequency2.csv',errors='ignore') as csv_file:
    csv_reader = csv.reader(csv_file, delimiter=',')
    for row in csv_reader:
        f = row
        data1.append(f)
        break

#print(data)
#print(data1)

for i in range (len(data[0])):
    for n in range (len(data1[0])):
        if data[0][i] == data1[0][n]:
            print(data[0][i],data1[0][n])
            nama.append(data[0][i])
            match1.append(i)
            match.append(n)

#print(match)
#print(len(match))

print(nama)

with open('match.csv', 'w', newline='') as csvfile:
    spamwriter = csv.writer(csvfile, delimiter=',',
                            quotechar='|', quoting=csv.QUOTE_MINIMAL)
    spamwriter.writerow(match1)
    spamwriter.writerow(match)
    spamwriter.writerow(nama)