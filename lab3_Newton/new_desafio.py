import matplotlib.pyplot as plt
import numpy as np
import math
h=0.01

v=[14,14]
r=0.000020
m=0.00000145
c=0.8
rho=1000
Area = np.pi * (r**2)
k=(c*Area*rho)/(2*m)
print(k)

ball = [[0,1.6],[0,1.6]]
vBall = [[v[0]*np.cos(np.pi/3) , v[0] * np.sin(np.pi/3)], [v[1]*np.cos(np.pi/3) , v[1] * np.sin(np.pi/3)]]
#vxa = v * np.cos(np.pi/3)
#vya = v * np.sin(np.pi/3)
aBall = [[0,-10],[0,-10]]

#axa=0
#aya=-10


pxBall=[[]for i in range(len(ball))]
pyBall=[[]for i in range(len(ball))]

axs=plt.subplot()
axs.set_aspect('equal')

pt = np.arange(0,20,h)
for it in range(len(ball)):
	for t in pt:
		if(it==0):
			v[it] = np.sqrt(vBall[it][0]**2+vBall[it][1]**2)
			aBall[it][0] = -k*v[it]*vBall[it][0]
			aBall[it][1] = -10-k*v[it]*vBall[it][1]

		ball[it][0] = ball[it][0] + vBall[it][0] * h
		ball[it][1] = ball[it][1] + vBall[it][1] * h

		vBall[it][0] = vBall[it][0] + aBall[it][0] * h
		vBall[it][1] = vBall[it][1] + aBall[it][1] * h
		
		pxBall[it].append(ball[it][0])
		pyBall[it].append(ball[it][1])
		if(ball[it][1] <= 0):
			break
		
plt.plot(pxBall[0],pyBall[0])
plt.plot(pxBall[1],pyBall[1])

plt.xlabel('X axis')
plt.xlabel('Y axis')
plt.title('X-Y')
plt.grid(True)
plt.show()
"""
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
"""
