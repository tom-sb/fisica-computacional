import numpy as np
from matplotlib import pyplot as plt

def feval(funcName, *args):
    return eval(funcName)(*args)

fig = plt.figure()
#axl = fig.gca(projection='3d')

duffing = lambda t,x,v,m,b,c,d,f0,w: (b*x-c*x**3)/m-d/m*v +f0*np.cos(w*t)

n = 0
m = 1

c = 1
b = 1
d = 0.01
f0 = 1
w = 0.1

t = 0.01
x = 1
v = -1
tfin = 300

pt = []
pv = []
px = []
h = 0.2

while(t < tfin):
    n = n*1
#    for i in range(m):
    a = feval('duffing', t, x, v, m, b, c, d, f0, w)
    k1 = h*a
    a = feval('duffing', t+0.5*h, x+h*0.5*v, v+0.5*k1, m, b, c, d, f0, w)
    k2 = h*a
    a = feval('duffing', t+0.5*h, x+0.5*h*(v+0.5*k1), v+0.5*k2, m, b, c, d, f0, w)
    k3 = h*a
    a = feval('duffing', t+h, x+h*v+h*k2*0.5, v+k3, m, b, c, d, f0, w)
    k4 = h*a
    x = x+h*v+h*(k1+k2+k3)/6
    v = v+(k1+2*k2+2*k3+k4)/6
    t = t+h
    """
    if x > np.pi:
        x = x-2*np.pi
    if x < -np.pi:
        x = x+2*np.pi
    """
    px.append(x)
    pv.append(v)
    pt.append(0)

#axl.plot(px,pv,pt)
plt.plot(px,pv,'.',markersize=3)
plt.xlabel('x')
plt.xlabel('y')

plt.show()
