import random
import numpy as np
import math
from matplotlib import pyplot as plt
from mpl_toolkits.mplot3d import Axes3D

m = 1000
veces = 50
ax = -np.sqrt(2)
ay = -np.sqrt(3)
az = -2
bx = np.sqrt(2)
by = np.sqrt(3)
bz = 2
sa = 0
saa = 0
n = 0
px = []
py = []
pz = []

fig = plt.figure()
axl = fig.gca(projection='3d')

for i in range (veces):
    n=0
    for j in range(m):
        r = (random.random())
        x = ax + (bx - ax)*r
        r = (random.random())
        y = ay + (by - ay)*r
        r = (random.random())
        z = az + (bz - az)*r
        if (x**2/2 + y**2/3 + z**2/4 < 1):
            n = n+1
            px.append(x)
            py.append(y)
            pz.append(z)
    volume = n*(by-ay)*(bx-ax)/m*(bz-az)
    sa = sa + volume
    saa = saa + volume**2

avg = sa/veces
desv = np.sqrt(veces*saa-sa**2)/veces

average = str(avg)
desviacion = str(desv)

axl.plot(px,py,pz,'.')
plt.xlabel('x')
plt.ylabel('y')
plt.axis([-2,6,-6,5])

plt.show()

print(average)
print(desv)
