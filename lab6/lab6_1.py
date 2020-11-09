import numpy as np
from gaussJordan import gaussJordan
from matplotlib.colors import Normalize
from matplotlib import cm
import matplotlib.pyplot as plt
import matplotlib.pylab as p
#import imageio

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
	C_colored = scalarMap.to_rgba(C)

	ax = fig.gca(projection='3d')
	surf = ax.plot_surface(X, Y, Z,facecolors=C_colored)
	fig.colorbar(surf,shrink=0.5,aspect=5)
	plt.show()
	return surf


def makeMatrix0(row,col,f1,f2,f3,f4,innerVal):
	matrixOut = np.full((row, col), innerVal)
	for i in range(row-1):
		matrixOut[i][0]=f3
		matrixOut[i][col-1]=f4
	for j in range(col-1):
		matrixOut[row-1][j]=f1
		matrixOut[0][j]=f2
	matrixOut[0][0] = (f2+f3)/2
	matrixOut[row-1][0] = (f1+f3)/2
	matrixOut[0][col-1] = (f2+f4)/2
	matrixOut[row-1][col-1] = (f1+f4)/2
	return matrixOut

def makeMatrixEquations(M,n,m):
	size = (n-2)*(m-2)
	matrixA = np.zeros([size,size])
	matrixX=[]
	print("\n\nEcuaciones de la matriz:")
	k=0
	for i in range(1,n-1):
		for j in range(1,m-1):
			
			print(4,"*0",end='',sep='')
			print("-",M[i][j-1],end='',sep='') if M[i][j-1]>0 else print("-","0",end='',sep='')
			print("-",M[i][j+1],end='',sep='') if M[i][j+1]>0 else print("-","0",end='',sep='')
			print("-",M[i-1][j],end='',sep='') if M[i-1][j]>0 else print("-","0",end='',sep='')
			print("-",M[i+1][j],end='',sep='') if M[i+1][j]>0 else print("-","0",end='',sep='')
			print()
				
			center = (((i-1) * (m-2)) + (j-1))
			matrixA[k][(((i-1)*(m-2))+(j-1))] = 4

			if((center - 1) > 0 and (center - 1) < (n-2)*(m-2)):
				matrixA[k][center - 1] = -1
			if((center + 1) > 0 and (center + 1) < (n-2)*(m-2)):
				matrixA[k][center + 1] = -1
			if((center - (m-1)) > 0 and (center-(m-1)) < (n-2)*(m-2)):
				matrixA[k][center - (m-1)] = -1
			if((center + (m-1)) > 0 and (center + (m-1)) < (n-2)*(m-2)):
				matrixA[k][center + (m-1)] = -1
			
			matrixX.append(M[i][j+1]+M[i][j-1]+M[i+1][j]+M[i-1][j])
			k=k+1

	print("\nNumero de ecuaciones: ",len(matrixX))
	return matrixX,matrixA

def fillMatrix(M,B,n,m):
	for i in range(1,n-1):
		for j in range(1,m-1):
			M[i][j] = B[((i-1)*(m-2)+(j-1))]
	return M

def makeOmega(n,m):
	omega = 4/(2 + np.sqrt(4 - (np.cos(np.pi/(n-1)) + np.cos(np.pi/(m-1)))**2))
	return omega

def acrossMatrix(w,epsilon,rmax,M,n,m):
	#n,m = M.shape
	while(rmax>epsilon):
		rmax = 0
		for i in range(1,n-1):
			for j in range(1,m-1):
				rij = avg(M[i-1][j], M[i+1][j], M[i][j-1], M[i][j+1],M[i][j])
				M[i][j] = M[i][j] + w*rij
				if rmax <= abs(rij):
					rmax = abs(rij)
		#print(M)
	surf(M)
	return M

def avg(up,down,left,right,center):
	answer = (up+down+left+right-(4*center))/4
	return answer



def laplace(f1,f2,f3,f4,a,b,h,epsilon):
	n = int(np.fix(a/h) +1)	
	m = int(np.fix(b/h) +1)
	pp = (a*(f1+f2) + b*(f3+f4))/(2*a + 2*b)

	#U = pp*np.ones([n,m])*0.9	
	#print(U)
	inner=pp*1*0.9	
	matrix1 = makeMatrix0(n,m,300,20,80,1,inner)
	#print(matrix1)
	omega = makeOmega(n,m)
	matrixOut = acrossMatrix(omega,epsilon,rmax,matrix1,n,m)


	
row = 7
col = 6
rmax = 1
epsilon = 0.1
h = 0.5

laplace(300,20,80,1,row,col,0.1,0.01)

"""
matrix = makeMatrix0(row,col,20,20,20,20,0.9)
print(matrix)
omega = makeOmega(row,col)
print(omega)
matrixOut = acrossMatrix(omega,epsilon,rmax,matrix,row,col)
print(matrixOut)
"""
### generando las ecuaciones y tbn matrices A y X para gaussJordan
matrix0 = makeMatrix0(row,col,300,20,80,1,0)

X,A = makeMatrixEquations(matrix0,row,col)
print("\nMatriz X:")
print(X)
print("\nMatriz A:")
print(A)
print("\nGaussJordan:")
n=(row-2)*(col-2)
B = gaussJordan(n,A,X)
for i in range(len(B)):
	print(B[i]
matrixGJ = fillMatrix(matrix0,B,row,col)
print(matrixGJ)

