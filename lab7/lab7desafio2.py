import numpy as np
from matplotlib.colors import Normalize
from matplotlib import cm
import matplotlib.pyplot as plt
import matplotlib.pylab as p
import imageio


def feval(funcName, *args):
    return eval(funcName)(*args)

def meshgrid_of(A):
    x = range(np.shape(A)[1])
    y = range(np.shape(A)[0])
    xx, yy = p.meshgrid(x,y)
    return xx, yy

def surf(Z, colormap=cm.RdYlGn):
    X, Y = meshgrid_of(Z)
    C = Z

    fig = plt.figure()
    scalarMap = cm.ScalarMappable(norm=Normalize(vmin=C.min(), vmax=C.max()), cmap=colormap)
    C_colored = scalarMap.to_rgba(C,0.3)

    ax = fig.gca(projection='3d')
    surf = ax.plot_surface(X, Y, Z,rstride=1,cstride=1,facecolors=C_colored)
    cset = ax.contour(X,Y,Z,zdir='z',offset=-1,cmap=cm.RdYlGn)
    #fig.colorbar(surf,shrink=0.5,aspect=5)

    plt.show()
    return surf

#f = lambda x: x**2-x + np.sin(2*np.pi*x)
#g = lambda x: 0
f = lambda x: 2*x if 0<=x<=0.5 else (2-2*x if 0.5<=x<=1 else 0)
g = lambda x: 0


def wave(f, g, a, b, v, h, k):
    

    row = int(a/h+1)
    col = int(b/k+1)
    r = v*k/h
    print(r)
    r1 = r**2
    r2 = r**2/2
    s1 = 1-r**2
    s2 = 2*(1-r**2)

    U = np.zeros((row,col),np.float)
    #print(U)
    #print(row,col)
    #arr=[]
    for i in range(1,row-1):
        U[i,0] = feval(f,(i-1)*h)
        U[i,1] = s1*feval(f,h*(i-1)) + k*feval(g,h*(i-1)) + r2*(feval(f,h*i) + feval(f,h*(i-2)))


    #print(U)

    for j in range(1,col-1):
        for k in range(1,row-1):
            #U[k][j+1] = s2 * U[k][j] + r1 * (U[k-1][j] + U[k+1][j]) - U([k][j-2])
            U[k,j+1] = s2*U[k,j]+r1*(U[k-1,j]+U[k+1,j])-U[k,j-1]
        #surf(np.transpose(U))


        plt.plot(U)
        #plt.savefig('desaf'+str(j))
        #plt.show()
#main
wave('f','g',1,1,1,0.05,0.01)

