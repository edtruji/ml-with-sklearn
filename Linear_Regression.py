from scipy import stats
import numpy as np
from matplotlib import pyplot as plt

#Size of the houses
x = np.array([112,345,198,305,372,550,302,420,578,588])

#Price of the houses
y = np.array([1120,1623,2102,2230,2600,3200,3409,3689,4460,4489])

slope, intercept, r_value, p_value, str_err = stats.linregress(x ,y)

plt.plot(x,y,'ro', color='black')

plt.ylabel('Price')
plt.xlabel('Size of House')

#600 pq el size de la casa mayor es 578
#5000 pq el precio de la casa mayor es 4460
plt.axis([0,600, 0, 5000])

plt.plot(x, x*slope+intercept, 'b')

plt.plot()
#Muestra la grafica visualmente
plt.show()

#PREDECIR

#Nuevo size del house
newX = 78
newY = newX * slope + intercept
print(newY)

newX = 350
newY = newX * slope + intercept
print(newY)

