import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
import numpy as np
h=-0.01
x=-3
y=-4
z=-5
vx=0
vy=2
vz=4
ax=0
ay=0
az=0
px=[]
py=[]
pz=[]
pv=[]
pa=[]
pt = np.arange(5,0,h)

for t in pt:
	x=x-vx*h
	y=y-vy*h
	z=z-vz*h
	vx=vx-ax*h
	vy=vy-ay*h
	vz=vz-az*h
	px.append(x)
	py.append(y)
	pz.append(z)
	pv.append(vx)
	pa.append(ax)

fig = plt.figure()
axl = fig.gca(projection='3d')
axl.plot(px,py,pz,label='3d line')
axl.legend()

plt.show()
