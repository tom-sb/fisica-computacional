# -*- coding: utf-8 -*-


#Funciones
def mat(n):
    for i in range (n):
        matriz.append([])
        for j in range (n):
            matriz[i].append(0)
    return matriz

def llenar(n):
    matriz = mat(n)
    for x in range (n):
        for y in range (n):
            matriz[x][y] = float(input('Valor de [' + str(x) + '][' + str(y) + '] = '))
        res.append(float(input('Valor del resultado de la matriz [' + str(x) + '] = ')))
        
def gauss(n):
    for z in range (n-1):
        for x in range(1, n-z):
            if (matriz[z][z] != 0 ):
                p = matriz[x+z][z] / matriz[z][z]
                for y in range (n):
                    matriz[x+z][y] = matriz[x+z][y] - (matriz[z][y]*p)
                res[x+z] = res [x+z] - (res[z]*p)

def gjordan(n):
    for z in range (n-1, 0, -1):
        for x in range (z):
            if (matriz[z][z] != 0):
                p = matriz[x][z] / matriz[z][z]
                matriz[x][z] = matriz [x][z] - (matriz[z][z] * p)
                res[x] = res[x] - (res[z] * p)
                
def sol(n):
    print("\n")
    for i in range (n):
        if (matriz[i][i] != 0):
            ms=True
        else:
            ms=False
            break
    if (ms == True):
        for i in range(n):
            print ("El valor de x" + str(i) + ' es = ' + str(res[i]/matriz[i][i]))
    else:
        print ('La matriz no tiene solucion')

def det(n):
    deter=1
    for x in range (n):
        deter=matriz[x][x]*deter
    print ('\nEl determinante de la matriz es = ', deter)
                    
def im(n):
    print("\nMatriz resultante:")
    for i in range (n):
            print (matriz[i][:])

def gJordanRun(matriz,res,n):
	#Variables
#	matriz = matrix
#	res = res

	gjordan(n)
	sol(n)
	im(n)


