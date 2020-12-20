import matplotlib.pyplot as plt
import numpy as np
import random
import copy
import imageio


def automata(c):
    
    matrizImg = np.zeros((c,c),dtype='uint8');

    a = [round(np.random.random()) for i in range(c)]
    b = np.array([0 for i in range(c)])

    j = c-1
    while j>=0:
        for i in range(c):
            l=i-1
            r=i+1
            if l<0:
                l=c-1
            if r>c-1:
                r=0
            al=a[l]
            ar=a[r]
            if al==1 and a[i]==1 and ar==1:
                b[i] = 0
            if al==1 and a[i]==1 and ar==0:
                b[i] = 1
            if al==1 and a[i]==0 and ar==1:
                b[i] = 0
            if al==1 and a[i]==0 and ar==0:
                b[i] = 0
            if al==0 and a[i]==1 and ar==1:
                b[i] = 1
            if al==0 and a[i]==1 and ar==0:
                b[i] = 0
            if al==0 and a[i]==0 and ar==1:
                b[i] = 0
            if al==0 and a[i]==0 and ar==0:
                b[i] = 1
        for k in range(c):
            if b[k]==1:
                matrizImg[k,j]=1
        
        a=copy.deepcopy(b)
        j=j-1
    return np.transpose(matrizImg)

if __name__=='__main__':
    c=1500
    img = automata(c)
    
    plt.axis([0,c,0,c])
    plt.imshow(img,'Accent')
    img = np.where(img>=1,img,255)
    imageio.imwrite('automata.jpg',img)
    plt.show()
