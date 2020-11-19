import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
import numpy as np

fig = plt.figure()
axl = fig.gca(projection='3d')

h=0.01
initAxis=[10,10,10]
speedAxis=[2,0,0]
accelAxis=[-2,-10,4]
axisArr=[[]for i in range(len(initAxis))]

while(True):
	for i in range(len(initAxis)):
		initAxis[i]=initAxis[i]+speedAxis[i]*h
		speedAxis[i]=speedAxis[i]+accelAxis[i]*h

		axisArr[i].append(initAxis[i])
	if(initAxis[1] <= 0):
		break

axl.plot(axisArr[0],axisArr[2],axisArr[1])

plt.xlabel('x axis')
plt.ylabel('z axis')
axl.set_zlabel('y axis', fontsize=10, rotation = 0)
plt.show()
