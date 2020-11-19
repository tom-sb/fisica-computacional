import matplotlib.pyplot as plt
import numpy as np
h=0.01
x=-3
y=-4
vx=2
vy=4
ax=0
ay=0
px=[]
py=[]
pv=[]
pa=[]
pt = np.arange(0,5,h)

for t in pt:
	x=x+vx*h
	y=y+vy*h
	vx=vx+ax*h
	vy=vy+ay*h
	px.append(x)
	py.append(y)
	pv.append(vx)
	pa.append(ax)

plt.plot(px,py)
plt.xlabel('x')
plt.ylabel('y')
plt.title('x-y')
plt.grid(True)

plt.show()
