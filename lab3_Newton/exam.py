import matplotlib.pyplot as plt
import numpy as np
import math
h=0.0005

v=[10,10]
r=0
m=0
c=0
rho=0
Area = 0
k=0#(c*Area*rho)/(2*m)
ball = [[0,0],[0,0]]
vBall = [[v[0]*np.cos(np.pi/6) , v[0] * np.sin(np.pi/6)], [v[1]*np.cos(np.pi/3) , v[1] * np.sin(np.pi/3)]]
aBall = [[0,-10],[0,-10]]
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
			print(ball[it][0])
			break
		
plt.plot(pxBall[0],pyBall[0])
plt.plot(pxBall[1],pyBall[1])

plt.xlabel('X axis')
plt.ylabel('Y axis')
plt.title('X-Y')
plt.grid(True)
plt.show()
