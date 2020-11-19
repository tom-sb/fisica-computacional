import matplotlib.pyplot as plt
import matplotlib.animation as animation
import numpy as np

h=0.01
x=0
y=0
vx=3
vy=7
ax=0
ay=0
px=[]
py=[]
pv=[]
pa=[]
pt = np.arange(0,150,h)

for t in pt:
	if x <= 10 and x >= 0:
		if y > 20:	
			vy = vy*(-1)
		if y < 0:	
			vy = vy*(-1)
	else:
		if x > 10:	
			vx = vx*(-1)
		if x < 0:	
			vx = vx*(-1)
	x=x+vx*h
	y=y+vy*h
	vx=vx+ax*h
	vy=vy+ay*h
	px.append(x)
	py.append(y)

fig, ax = plt.subplots()

ax=plt.axis([0,10,0,20])
redDot, = plt.plot([8],[np.sin(8)],'ro')

def animate(i):
	i = int(i)
	redDot.set_data(px[i],py[i])
	return redDot,

myAnimation = animation.FuncAnimation(fig,animate,frames=np.arange(0,3000,2.5),interval=10,blit=True,repeat=True)

plt.show()

writer = animation.PillowWriter(fps=35)
myAnimation.save("desafio.gif", writer=writer)
