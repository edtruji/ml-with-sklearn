import nltk
print('La version de nltk es {}.'.format(nltk.__version__))
import sklearn
print('La version de scikit-learn es {}.'.format(sklearn.__version__))
import matplotlib
print('La version de matplotlib es {}.'.format(matplotlib.__version__))
import numpy
print('La version de numpy es {}.'.format(numpy.__version__))

import numpy as np
from matplotlib import pyplot as plt
from sklearn.naive_bayes import GaussianNB

xBlue = np.array([95,93,89,92,95,90])
yBlue = np.array([5,4.5,6,4.9,6.2,5.5])

xRed = np.array([70,73,69,77,75,80])
yRed = np.array([3.5,3.3,3.8,2.9,3.9,4.1])

train_features_X = np.array([[95,5],[93,4.5],[89,6],[92,4.9],[95,6.2],[90,5.5],[70,3.5],[73,3.3],[69,3.8],[77,2.9],[75,3.9],[80,4.1]])
# print(train_features_X.shape)
train_labels_y   = np.array([0,0,0,0,0,0,1,1,1,1,1,1]) #0: Reggaeton #1: Balada
# print(train_labels_y.shape)

plt.plot(xBlue , yBlue , 'ro' , color = 'blue', markersize=12, marker='o' ,label = 'Reggaeton')
plt.plot(xRed  , yRed  , 'ro' , color = 'red' , markersize=12, marker='s' ,label = 'Balada')

plt.axis([50,100,-0.5,10])
gausian_classifier = GaussianNB()
gausian_classifier.fit(train_features_X,train_labels_y)

plt.plot(85,4.5, 'ro', color= 'green', markersize=12, marker='.')
pred = gausian_classifier.predict([85,4.5])
print(pred)

plt.xlabel('Tempo')
plt.ylabel('Bajo')

plt.legend(loc='upper left')                         
plt.grid(which='minor', alpha=0.8)                                                
plt.grid(which='major', alpha=0.8)  
plt.grid(True)
plt.show()