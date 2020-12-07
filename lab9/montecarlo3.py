import random
import numpy as np
import math
from matplotlib import pyplot as plt

m = 1000
veces = 50
ax = 0
ay = 0
bx = 1
by = 1
sa = 0
saa = 0
n = 0
px = []
py = []

for i in range (veces):
    n=0
    for j in range(m):
        r = (random.random())
        x = ax + (bx - ax)*r
        r = (random.random())
        y = ay + (by - ay)*r
        if (y > x**2 and y < np.sqrt(x)):
            n = n+1
            px.append(x)
            py.append(y)
    area = n*(by-ay)*(bx-ax)/m
    sa = sa + area
    saa = saa + area**2

avg = sa/veces
desv = np.sqrt(veces*saa-sa**2)/veces

average = str(avg)
desviacion = str(desv)

plt.plot(px,py)
plt.xlabel('x')
plt.ylabel('y')
plt.axis([-2,6,-6,5])

plt.show()

print(average)
print(desv)
