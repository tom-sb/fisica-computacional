import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
import numpy as np

fig = plt.figure()
axl = fig.gca(projection='3d')

h=0.01
accelAxis=[[2,-10,0],[-1,-10,0],[2,-10,-1]]

for it in accelAxis:
	initAxis=[0,0,0]
	speedAxis=[5,2,0]
	axisArr=[[]for i in range(len(initAxis))]
	anyTime=0
	while(True):
		for i in range(len(initAxis)):
			initAxis[i]=initAxis[i]+speedAxis[i]*h
			speedAxis[i]=speedAxis[i]+it[i]*h

			axisArr[i].append(initAxis[i])
		if(initAxis[1] <= 0):
			break
		anyTime=anyTime+1
	axl.plot(axisArr[0],axisArr[2],axisArr[1])

	plt.xlabel('x axis')
	plt.ylabel('z axis')
	axl.set_zlabel('y axis', fontsize=10, rotation = 0)
plt.show()
