import matplotlib.pyplot as plt
import numpy as np
import math
h=0.01
a=2
r=8
m=5

x=r*np.cos(np.pi/4)
y=r*np.sin(np.pi/4)

vx=-4*np.cos(np.pi/4)
vy=4*np.sin(np.pi/4)

px=[]
py=[]
pv=[]
pa=[]
pt = np.arange(0,13,h)

for t in pt:
	ax= -(a*x/r)
	ay= -(a*y/r)

	x = x + vx * h
	y = y + vy * h

	vx = vx + ax * h
	vy = vy + ay * h

	px.append(x)
	py.append(y)
	
	pv.append([vx,vy])
	pa.append([ax,ay])
	

#print("(a) posicion final: ",px[len(px)-1])
#print("(b) posicion final: ",px2[len(px2)-1])
#print("(c) posicion final: ",px3[len(px3)-1])

plt.subplot(2,2,1)
plt.plot(pt,px)
plt.xlabel('tiempo')
plt.ylabel('espacio')
plt.title('x-t')
plt.grid(True)

plt.subplot(2,2,2)
plt.plot(pt,pv)
plt.xlabel('tiempo')
plt.ylabel('velocidad')
plt.title('v-t')
plt.grid(True)

plt.subplot(2,2,3)
plt.plot(pt,pa)
plt.xlabel('tiempo')
plt.ylabel('aceleracion')
plt.title('a-t')
plt.grid(True)

plt.subplot(2,2,4)
plt.plot(px,py)
plt.xlabel('espacio')
plt.ylabel('velocidad')
plt.title('espacio de fases')
plt.grid(True)

plt.show()

axs=plt.subplot()
axs.set_aspect('equal')
plt.plot(px,py)
plt.xlabel('X axis')
plt.xlabel('Y axis')
plt.title('X-Y')
plt.grid(True)
plt.show()

rsim = math.sqrt(x*x + y*y)
print('R simulada:' ,rsim)
print('error: :' ,abs(8-rsim)/8*1)
