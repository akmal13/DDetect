import numpy
import matplotlib.pyplot as plt
from pandas import read_csv
import math
import tensorflow as tf
from tensorflow.python.keras.models import Sequential
from tensorflow.python.keras.layers import Dense
from tensorflow.python.keras.layers import LSTM
from tensorflow.python.keras.layers import Dropout
from sklearn.preprocessing import MinMaxScaler
from sklearn.metrics import mean_squared_error
import csv
import time

match = []
testpredictas = []

maxacc = 0
los = [0 for x in range (0,50)]
varlos = [0 for x in range (0,50)]
valacc = [0 for x in range (0,50)]
waktu = 0

def create_dataset(dataset, look_back=1):
	dataX, dataY = [], []
	for i in range(len(dataset)-look_back-1):
		a = dataset[i:(i+look_back), 0]
		dataX.append(a)
		dataY.append(dataset[i + look_back, 0])
	return numpy.array(dataX), numpy.array(dataY)

def create_dataset2(dataset, look_back=1):
	dataX, dataY = [], []
	for i in range(len(dataset)-look_back):
		a = dataset[i:(i+look_back), 0]
		dataX.append(a)
		dataY.append(dataset[i + look_back, 0])
	return numpy.array(dataX), numpy.array(dataY)

with open('match.csv', newline='') as csvfile:
     spamreader = csv.reader(csvfile, delimiter=',', quotechar='|')
     for row in spamreader:
         match.append(row)

for m in range (0,len(match)-1):
	for i in range (len(match[0])):
		match[m][i] = int(match[m][i])

print(match)
print(match[0][0])
print(type(match[0][0]))
print(match[1][0])

for j in range (len(match[2])):
	match[2][j] = match[2][j].replace("/",".")

for i in range (len(match[0])):
	# Load dataset
	numpy.random.seed(7)
	dataframe = read_csv('TypeFrequency.csv', usecols=[match[0][i]], engine='python')

	dataset = dataframe.values
	dataset = dataset.astype('float32')
	print('Panjang Dataset1 : '+str(len(dataset)))

	scaler = MinMaxScaler(feature_range=(0, 1))
	dataset = scaler.fit_transform(dataset)
	
	# Load Train dan test dataset
	train_size = int(len(dataset) * 0.95)
	test_size = len(dataset) - train_size
	train, test = dataset[0:train_size,:], dataset[train_size:len(dataset),:]
	
	# Data menjadi X=t dan Y=t+1

	look_back = 1
	trainX, trainY = create_dataset(train, look_back)
	testX, testY = create_dataset(test, look_back)

	# Mengubah input untuk Network
	trainX = numpy.reshape(trainX, (trainX.shape[0], 1, trainX.shape[1]))
	testX = numpy.reshape(testX, (testX.shape[0], 1, testX.shape[1]))

	# Membuat dan fit data
	model = Sequential()
	model.add(LSTM(40, batch_input_shape=(1,1, look_back),activation='relu', return_sequences = True))
	model.add(Dropout(0.2))
	model.add(LSTM(20,activation='relu', return_sequences = True))
	model.add(Dropout(0.2))
	model.add(LSTM(10,activation='relu', return_sequences = True))
	model.add(Dropout(0.2))
	model.add(LSTM(5,activation='relu'))
	model.add(Dropout(0.2))
	model.add(Dense(1))
	model.summary()
	model.compile(loss='mean_squared_error', optimizer='Nadam', metrics=['accuracy'])
	his = model.fit(trainX, trainY, validation_split=0.15, epochs=50,batch_size=1, verbose=2)

	los = [x + y for x, y in zip(his.history['loss'], los)]
	varlos = [x + y for x, y in zip(his.history['val_loss'], varlos)]
	valacc = [x + y for x, y in zip(his.history['val_acc'], valacc)]
	maxacc = max(valacc) + maxacc
	print('loss : ' + str(los))
	print('Val loss :' + str(varlos))
	print('Val acc : ' + str(valacc))
	print('Maxacc : '+ str(maxacc))

	# Membuat prediksi
	trainPredict = model.predict(trainX)
	testPredict = model.predict(testX)

	# Invert prediksi
	trainPredict = scaler.inverse_transform(trainPredict)
	trainY = scaler.inverse_transform([trainY])
	testPredict = scaler.inverse_transform(testPredict)
	testY = scaler.inverse_transform([testY])

	# Menghitung MSE
	trainScore = math.sqrt(mean_squared_error(trainY[0], trainPredict[:,0]))
	print('Train Score: %.2f RMSE' % (trainScore))
	testScore = math.sqrt(mean_squared_error(testY[0], testPredict[:,0]))
	print('Test Score: %.2f RMSE' % (testScore))

	# Train prediction dan plot
	trainPredictPlot = numpy.empty_like(dataset)
	trainPredictPlot[:, :] = numpy.nan
	trainPredictPlot[look_back:len(trainPredict)+look_back, :] = trainPredict


	# Test predictions dan plotting
	testPredictPlot = numpy.empty_like(dataset)
	testPredictPlot[:, :] = numpy.nan
	testPredictPlot[len(trainPredict)+(look_back*2)+1:len(dataset)-1, :] = testPredict
	

	# Menampilkan plot
	plt.plot(scaler.inverse_transform(dataset))
	plt.plot(trainPredictPlot)
	plt.plot(testPredictPlot)
	plt.xlabel("Time")
	plt.ylabel("Frequency")
	nama = str(i+1)+'.'+str(match[2][i])+'.png'
	plt.savefig(nama)
	plt.clf()
	#plt.show()
	

	dataframe2 = read_csv('TypeFrequency2.csv', usecols=[match[1][i]], engine='python')
	dataset2 = dataframe2.values
	dataset2 = dataset2.astype('float32')
	

	dataset2 = scaler.fit_transform(dataset2)
	testXa, testYa = create_dataset2(dataset2, look_back)
	print('Panjang Dataset 2 : '+ str(len(testXa)))
	start = time.time()
	testXa = numpy.reshape(testXa, (testXa.shape[0], 1, testXa.shape[1]))
	testPredicta = model.predict(testXa)
	testPredicta = scaler.inverse_transform(testPredicta)
	print("Hasil Test Predict")
	testpredictas.append(testPredicta)
	print(testpredictas[i])
	end = time.time()
	waktu = waktu + (end-start)
	#print(testpredictas[i][i])
	print(len(testpredictas))
	print("Hasil Test Predict Akhir")

print('Len match 0' + str(len(match[0])))

print(los)

for x in range(len(los)):
	los[x] = los[x]/(len(match[0]))
	varlos[x] = varlos[x]/(len(match[0]))
	valacc[x] = valacc[x]/(len(match[0]))

print('Loss Akhir : ' + str(los))
print('Val Loss Akhir : ' + str(varlos))
print('Val acc Akhir : ' + str(valacc))
print('Val Acc Max :' + str(maxacc) +'  Dan hasil bagi : '+ str(maxacc/((len(match[0]))-7)))

plt.plot(los)
plt.plot(varlos)
plt.title('model loss')
plt.ylabel('loss')
plt.xlabel('epoch')
plt.legend(['train', 'test'], loc='upper left')
plt.show()

print('Hasil waktu')
print(waktu)
with open('HasPredict.csv', 'w', newline='') as csvfile:
    spamwriter = csv.writer(csvfile, delimiter=',',
                            quotechar='|', quoting=csv.QUOTE_MINIMAL)
    for m in range (len(testpredictas)):
        spamwriter.writerow(testpredictas[m]) 