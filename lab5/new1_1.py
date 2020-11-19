import matplotlib.pyplot as plt
import matplotlib.animation as animation
import numpy as np
import math
h=1
r=5
nlines = 17

punto = [[0,7]for i in range(nlines)]
vPunto = [[0,0]for i in range(nlines)]
aPunto = [[0,0]for i in range(nlines)]

pxPunto=[[]for i in range(nlines)]
pyPunto=[[]for i in range(nlines)]

fig, axs = plt.subplots()
axs.set_aspect('equal')

pt = np.arange(0,400,h)
for it in range(nlines):
	if it>0:
		vPunto[it][0] = vPunto[it-1][0] + 0.28
	for t in pt:
		aPunto[it][0] = -punto[it][0] / pow(pow(punto[it][0],2) + pow(punto[it][1],2),1.5)
		aPunto[it][1] = -punto[it][1] / pow(pow(punto[it][0],2) + pow(punto[it][1],2),1.5)

		vPunto[it][0] = vPunto[it][0] + aPunto[it][0] * h
		vPunto[it][1] = vPunto[it][1] + aPunto[it][1] * h

		punto[it][0] = punto[it][0] + vPunto[it][0] * h
		punto[it][1] = punto[it][1] + vPunto[it][1] * h
		
		pxPunto[it].append(punto[it][0])
		pyPunto[it].append(punto[it][1])

		if(punto[it][0] > 20):
			break

		if(pow(punto[it][0],2) + pow(punto[it][1],2) <= pow(r,2)):
			break
		

cuerpo1 = plt.Circle((0, 0), r, color="lightblue", fill=True)
axs.add_artist(cuerpo1)
axs = plt.axis([-10,10,-10,10])

for i in range(nlines):
	plt.plot(pxPunto[i],pyPunto[i])

redDot, = plt.plot([8],[np.sin(8)],'ro')

def animate(i):

	i = int(i)
	redDot.set_data(pxPunto[16][i],pyPunto[16][i])
	return redDot,

myAnimation = animation.FuncAnimation(fig,animate,frames=np.arange(0,300,2.5),interval=10,blit=True,repeat=True)


plt.xlabel('X axis')
plt.ylabel('Y axis')
plt.title('X-Y')
plt.grid(True)
plt.show()

writer = animation.PillowWriter(fps=35)
myAnimation.save("desafio.gif", writer=writer)
