import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
import numpy as np

fig = plt.figure()
axl = fig.gca(projection='3d')

h=0.01
initAxis=[0,3,0]
speedAxis=[2,3,5]
accelAxis=[0,-10,0]
axisArr=[[]for i in range(len(initAxis))]
maxval = initAxis[1]
coordinate = initAxis 
vector = initAxis[0],initAxis[1],initAxis[2] 
while(True):
	for i in range(len(initAxis)):
		initAxis[i]=initAxis[i]+speedAxis[i]*h
		speedAxis[i]=speedAxis[i]+accelAxis[i]*h
	
		axisArr[i].append(initAxis[i])
	if(initAxis[1] > maxval):
		maxval = initAxis[1]
		coordinate = (initAxis[0],initAxis[1],initAxis[2])
	if(initAxis[1] <= 0):
		break
print("punto alto: ",maxval)
print("coordenadas del punto alto: ",coordinate)
print("coordenadas del punto alto: ",vector)
print("coordenadas del punto alto: ",initAxis)
arrX=[]
arrY=[]
arrZ=[]
arrX.append(vector[0])
arrX.append(initAxis[0])
arrY.append(vector[1])
arrY.append(initAxis[1])
arrZ.append(vector[2])
arrZ.append(initAxis[2])
axl.plot(axisArr[0],axisArr[2],axisArr[1])
axl.plot(arrX,arrZ,arrY)

plt.xlabel('x axis')
plt.ylabel('z axis')
axl.set_zlabel('y axis', fontsize=10, rotation = 0)
plt.show()
