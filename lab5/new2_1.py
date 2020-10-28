import matplotlib.pyplot as plt
import numpy as np
import math
h=0.01
r=3
nlines = 19

punto = [[-1,4]for i in range(nlines)]
vPunto = [[0,0.6]for i in range(nlines)]
aPunto = [[0,0]for i in range(nlines)]
"""
j=0
for j in range(nlines):
	punto[j].append(2)
	punto[j].append(4)
	vPunto[j].append(0)
	vPunto[j].append(0.1)
	aPunto[j].append(0)
	aPunto[j].append(0)
"""
pxPunto=[[]for i in range(nlines)]
pyPunto=[[]for i in range(nlines)]

axs = plt.subplot()
axs.set_aspect('equal')

d=6
pt = np.arange(0,400,h)
for it in range(nlines):
	if it>0:
		vPunto[it][0] = vPunto[it-1][0] + 0.25
	for t in pt:
		x=punto[it][0]
		y=punto[it][1]

		aPunto[it][0] = -((x+d) / ((x**2 + d) + y**2)**1.5) - ((x-d) / ((x**2 - d) + y**2)**1.5) 
		aPunto[it][1] = -((y+d) / ((x**2 + d) + y**2)**1.5) - ((y-d) / ((x**2 - d) + y**2)**1.5) 

		vPunto[it][0] = vPunto[it][0] + aPunto[it][0] * h
		vPunto[it][1] = vPunto[it][1] + aPunto[it][1] * h

		punto[it][0] = x + vPunto[it][0] * h
		punto[it][1] = y + vPunto[it][1] * h
		
		pxPunto[it].append(punto[it][0])
		pyPunto[it].append(punto[it][1])

		if(punto[it][0] > 30):
			break
		if(punto[it][1] > 10):
			break

		if(pow(punto[it][0]+d,2) + pow(punto[it][1],2) <= pow(r,2)):
			break
		if(pow(punto[it][0]-d,2) + pow(punto[it][1],2) <= pow(r,2)):
			break
		

cuerpo1 = plt.Circle((0-d, 0), r, color="lightblue", fill=True)
cuerpo2 = plt.Circle((0+d, 0), r, color="lightblue", fill=True)

axs.add_artist(cuerpo1)
axs.add_artist(cuerpo2)

for i in range(nlines):
	plt.plot(pxPunto[i],pyPunto[i])

plt.xlabel('X axis')
plt.ylabel('Y axis')
plt.title('X-Y')
plt.grid(True)
plt.show()

