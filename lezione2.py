import numpy as np
import random
a = np.array([x for x in range(1,20)])
print(a)
print(any(a>5))
print(all(a>5))

print(np.where(a>15))
print(np.argmin(a))
print(np.argmax(a))
#ritorna la prima occorrenza del valore massimo e minimo

#NONE viene scritto come np.nan

array = np.array([random.randint(100000,150000) for x in range(1,10)])
noise = np.random.normal(0, 5000, array.size) #5000 è tanto grande
print(array)
print(noise)
print(array+noise)

#quando si comparano i float non usare == ma usa np.isclose()
a = np.array([0.1+0.2,0.3])
b = np.array([0.3,0.3])
print(a==b, np.isclose(a,b))