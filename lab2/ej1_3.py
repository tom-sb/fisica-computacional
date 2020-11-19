import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
import numpy as np
it=3
tag=['a','b','c']
h=0.01
x=[0,50,0]
vx=[50,0,-50]
ax=10
px=[[] for i in range(it)]
pv=[[] for i in range(it)]

fig = plt.figure()
axl = fig.gca(projection='3d')
pt = np.arange(0,14,h)
for i in range(it):
	for t in pt:
		x[i]=x[i]+vx[i]*h
		vx[i]=vx[i]+ax*h
		px[i].append(x[i])
		pv[i].append(vx[i])

	axl.plot(pv[i],px[i],pt,label=tag[i])

print("posicion final: ",px[0][len(px[0])-1])
print("posicion final: ",px[1][len(px[1])-1])
print("posicion final: ",px[2][len(px[2])-1])

plt.xlabel('velocidad')
plt.ylabel('espacio')
axl.set_zlabel('tiempo', fontsize=10, rotation = 0)
axl.legend()

plt.show()
