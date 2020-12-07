import random
import numpy as np
import math
from matplotlib import pyplot as plt
from mpl_toolkits.mplot3d import Axes3D

m = 3000
veces = 50
ax = 0
ay = 0
az = -1
bx = np.pi
by = np.pi/2
bz = 1
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
        if (z <= np.sin(x)*np.cos(y-np.pi)):
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

axl.plot(px,py,pz,'.',markersize=0.5)
plt.xlabel('x')
plt.ylabel('y')
plt.axis([-2,6,-6,5])

plt.show()

print(average)
print(desv)
