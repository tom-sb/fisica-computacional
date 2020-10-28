import matplotlib.pyplot as plt
import numpy as np
import math
h=0.1
r=3
nlines = 2

punto = [[7.1,4.0000],[7.1,4.0001]]
vPunto = [[0,0.36],[0,0.36]]
aPunto = [[0,0],[0,0]]

pxPunto=[[]for i in range(nlines)]
pyPunto=[[]for i in range(nlines)]

axs = plt.subplot()
axs.set_aspect('equal')

#d=6
pt = np.arange(0,1000000,h)
for it in range(nlines):
	#if it>0:
	#	vPunto[it][0] = vPunto[it-1][0] + 0.7
	for t in pt:
		aPunto[it][0] = -punto[it][0] / pow((pow(punto[it][0],2)) + pow(punto[it][1],2),1.5)
		#aPunto[it][0] = -((punto[it][0]+d) / pow((pow(punto[it][0],2)+d) + pow(punto[it][1],2),1.5)) -((punto[it][0]-d) / pow((pow(punto[it][0],2)-d) + pow(punto[it][1],2),1.5)) 

		aPunto[it][1] = -punto[it][1] / pow((pow(punto[it][0],2)) + pow(punto[it][1],2),1.5)
		#aPunto[it][1] = -((punto[it][1]+d) / pow((pow(punto[it][0],2)+d) + pow(punto[it][1],2),1.5)) -((punto[it][1]-d) / pow((pow(punto[it][0],2)-d) + pow(punto[it][1],2),1.5)) 

		vPunto[it][0] = vPunto[it][0] + aPunto[it][0] * h
		vPunto[it][1] = vPunto[it][1] + aPunto[it][1] * h

		punto[it][0] = punto[it][0] + vPunto[it][0] * h
		punto[it][1] = punto[it][1] + vPunto[it][1] * h
		
		pxPunto[it].append(punto[it][0])
		pyPunto[it].append(punto[it][1])

		if(punto[it][0] > 18):
			break
		if(punto[it][1] > 20):
			break

		if(pow(punto[it][0],2) + pow(punto[it][1],2) <= pow(r,2)):
			break
		#if(pow(punto[it][0]-(2*d),2) + pow(punto[it][1],2) <= pow(r,2)):
		#	break
		

cuerpo1 = plt.Circle((0, 0), r, color="lightblue", fill=True)
#cuerpo2 = plt.Circle((0+(2*d), 0), r, color="lightblue", fill=True)

axs.add_artist(cuerpo1)
#axs.add_artist(cuerpo2)

for i in range(nlines):
	plt.plot(pxPunto[i],pyPunto[i])

plt.xlabel('X axis')
plt.ylabel('Y axis')
plt.title('X-Y')
plt.grid(True)
plt.show()

