import numpy as np
from matplotlib import pyplot as plt

def feval(funcName, *args):
    return eval(funcName)(*args)

fig = plt.figure()
axl = fig.gca(projection='3d')

duffing = lambda t,x,v,m,b,c,d,f0,w: (b*x-c*x**3)/m -(d/m)*v + f0*np.cos(w*t)

n = 0
m = 10

t = 1
x = 0.1
v = 0

b = 0.01
c = 0.01
d = 0.01
w = 0.5
f0 = 0.1

tfin = 200

pt = []
pv = []
px = []
h = t/100

while(t < tfin):
    n = n*1
    for i in range(m):
        a = feval('duffing', t, x, v, m, b,c,d,f0,w)
        k1 = h*a
        a = feval('duffing', t+0.5*h, x+h*0.5*v, v+0.5*k1, m, b,c,d,f0,w)
        k2 = h*a
        a = feval('duffing', t+0.5*h, x+0.5*h*(v+0.5*k1), v+0.5*k2, m, b,c,d,f0,w)
        k3 = h*a
        a = feval('duffing', t+h, x+h*v+h*k2*0.5, v+k3, m,b,c,d,f0,w)
        k4 = h*a
        x = x+h*v+h*(k1+k2+k3)/6
        v = v+(k1+2*k2+2*k3+k4)/6
        t = t+h
        if x > np.pi:
            x = x-2*np.pi
        if x < -np.pi:
            x = x+2*np.pi

    px.append(x)
    pv.append(v)
    pt.append(t)


axl.plot(px,pv,pt,'.',markersize=2,color='purple')
#plt.plot(px,pv,'.')
plt.xlabel('x')
plt.ylabel('v')

plt.show()
