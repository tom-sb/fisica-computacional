def metodoGauss(n, A, b):    
        for k in range (0, n-1):        
            for i in range (k+1, n):            
                m = -A[i][k]/A[k][k]
                A[i][k] = 0
                for j in range (k+1, n):
                    A[i][j] = A[i][j] + m*A[k][j]
                b[i] = b[i] + m*b[k]        
        print("Matriz A")
        for i in range(n):
            print(A[i]) 
        print("b = ", b)
        
def gaussPivoteamento(n, A, b):    
        for k in range (0, n-1):        
            for i in range (k+1, n):            
                if (abs(A[k][k]) < abs(A[i][k])):
                    for j in range (0,n):
                        aux=A[k][j]
                        A[k][j]=A[i][j]
                        A[i][j]=aux
                    aux = b[k]
                    b[k]=b[i]
                    b[i]=aux
                m = -A[i][k]/A[k][k]
                A[i][k] = 0
                for j in range (k+1, n):
                    A[i][j] = A[i][j] + m*A[k][j]
                b[i] = b[i] + m*b[k]        
        print("Matriz A")
        for i in range(n):
            print(A[i])  
        print("b = ", b)
        
def gaussJordan(n, A, b):
        for k in range (n):        
            for j in range (k+1, n):
                A[k][j] = A[k][j] / A[k][k]
            b[k] = b[k] / A[k][k]
            A[k][k] = 1        
            for i in range(n):
                if i != k:
                    for j in range (k+1, n):
                        A[i][j] = A[i][j] - A[i][k] * A[k][j]
                    b[i] = b[i] - A[i][k] * b[k]
                    A[i][k] = 0
#        print("Matriz A")
#        for i in range(n):
#            print(A[i])
#        print("b = ", b)
        return b
"""
# Entrada da primeira questao. 
A = [ [3.0, 3.0, -1.0, 0.0, 0.0],
      [1.0, -1.0, 0.0, 0.0, 0.0],
      [0.0, -1.0, 9.0, 0.0, 0.0],
      [0.0, 1.0, 8.0, -11.0, 2.0],
      [3.0, 1.0, 0.0, 0.0, -4.0]
     ]
b = [50.0, 0.0, 0.0, 0.0, 0.0]

metodoGauss(5, A, b)
"""
