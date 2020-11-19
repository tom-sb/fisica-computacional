import matplotlib.pyplot as plt
import numpy as np
h=0.1
x=-10
vx=-20
ax=-10
px=[]
pv=[]
pa=[]

x2=10
vx2=20
ax2=10
px2=[]
pv2=[]
pa2=[]

x3=0
vx3=0
ax3=10
px3=[]
pv3=[]
pa3=[]

pt = np.arange(0,10,h)

for t in pt:
	x=x+vx*h
	vx=vx+ax*h
	px.append(x)
	pv.append(vx)
	pa.append(ax)
	x2=x2+vx2*h
	vx2=vx2+ax2*h
	px2.append(x2)
	pv2.append(vx2)
	pa2.append(ax2)
	x3=x3+vx3*h
	vx3=vx3+ax3*h
	px3.append(x3)
	pv3.append(vx3)
	pa3.append(ax3)

print("(a) posicion final: ",px[len(px)-1])
print("(b) posicion final: ",px2[len(px2)-1])
print("(c) posicion final: ",px3[len(px3)-1])

plt.subplot(2,2,1)
plt.plot(pt,px)
plt.plot(pt,px2)
plt.plot(pt,px3)
plt.xlabel('tiempo')
plt.ylabel('espacio')
plt.title('x-t')
plt.grid(True)

plt.subplot(2,2,2)
plt.plot(pt,pv)
plt.plot(pt,pv2)
plt.plot(pt,pv3)
plt.xlabel('tiempo')
plt.ylabel('velocidad')
plt.title('v-t')
plt.grid(True)

plt.subplot(2,2,3)
plt.plot(pt,pa)
plt.plot(pt,pa2)
plt.plot(pt,pa3)
plt.xlabel('tiempo')
plt.ylabel('aceleracion')
plt.title('a-t')
plt.grid(True)

plt.subplot(2,2,4)
plt.plot(px,pv)
plt.plot(px2,pv2)
plt.plot(px3,pv3)
plt.xlabel('espacio')
plt.ylabel('velocidad')
plt.title('espacio de fases')
plt.grid(True)

plt.show()
