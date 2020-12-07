import random
import numpy as np
import math
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D

m = 50000
veces = 50
ax = 0
ay = 0
az = -5
bx = 2
by = -4
bz = 8
sa = 0
saa = 0
n = 0
px = []
py = []
pz = []

fig = plt.figure()
axl = fig.gca(projection='3d')
#axl.set_aspect('auto')

for i in range (veces):
    n=0
    for j in range(m):
        r = (random.random())
        x = ax + (bx - ax)*r
        r = (random.random())
        y = ay + (by - ay)*r
        r = (random.random())
        z = az + (bz - az)*r
        if (z<0 and z >= ((2*y)-1)/((2*x+1)) and x>0 and x<(4+y)/2 and y<0 and y>(2*x)-4 ):
        #if (z<0 and z >= ((2*y)-1)/((2*x+1)) and x>0 and x<2 and y<0 and y>(2*x)-4 ):
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
plt.axis([-1,3,0,-5])

plt.show()

print(average)
print(desv)
