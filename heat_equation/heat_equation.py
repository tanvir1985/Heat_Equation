#solving the heat equation using finite difference method
import numpy as np
from tqdm.notebook import tqdm_notebook
import shutil
import os

def heatBC(a,b,c,d,T,dx,dy):
    
    # 'N' refers to Neumann boundary condition where the heat flux is specified on the boundary
    # 'D' refers to Dirichlet boundary condition where the temperature is specified on the boundary

    #left
    if a[0]=='N':
        T[:, 0]=a[1]*dx+T[:, 1]
    elif a[0]=='D':
        T[:,0]=a[1]
    else:
        return('Please enter a valid BC type')

    if b[0]=='N':
        T[:, -1]=b[1]*dx+T[:, -2]
    elif b[0]=='D':
        T[:, -1]=b[1]
    else:
        return('Please enter a valid BC type')

    #top
    if c[0]=='N':
        T[-1,:]=c[1]*dy+T[-2, :]
    elif c[0]=='D':
        T[-1,:]=c[1]
    else:
        return('Please enter a valid BC type')

    #bottom
    if d[0]=='N':
        T[0,:]=d[1]*dy+T[1, :]
    elif d[0]=='D':
        T[0,:]=d[1]
    else:
        return('Please enter a valid BC type')


def heat_equation(T,dx,dy,alpha,dt,ds,nt,TBCs):
    Tn = np.empty_like(T)
    i=0
    for n in tqdm_notebook(range(nt)):
        Tn = T.copy()
        i=i+1
        T[1:-1,1:-1]=Tn[1:-1,1:-1]+(alpha*dt/dx**2)*(Tn[2:,1:-1]-2*Tn[1:-1,1:-1]+Tn[0:-2,1:-1])+(alpha*dt/dy**2)*(Tn[1:-1,2:]- 2 * Tn[1:-1, 1:-1] + Tn[1:-1, 0:-2])
        
        if ((n+1)%ds==0):
            np.savetxt('T'+str(i)+'.csv', T, delimiter=',')

        TLeft=TBCs[0]
        TRight=TBCs[1]
        TTop=TBCs[2]
        TBottom=TBCs[3]

        heatBC(TLeft,TRight,TTop,TBottom,T,dx,dy)
    return T

def clearResults():
    fileList=os.listdir('./')
    
    if os.path.isdir('./Results'):
        shutil.rmtree('./Results')
        os.mkdir('Results')
    else:
        os.mkdir('Results')
    
    for file in fileList:
        if file.endswith('.csv'):
            shutil.move(file,'Results/.')


"""def heatBC(a,b,c,d,T,dx,dy):
    #left
    if a[0]=='N':
        T[0,:]=a[1]*dy+T[1, :]
    elif a[0]=='D':
        T[0,:]=a[1]
    else:
        return('Please enter a valid BC type')

    if b[0]=='N':
        T[-1,:]=b[1]*dy+T[-2, :]
    elif b[0]=='D':
        T[-1,:]=b[1]
    else:
        return('Please enter a valid BC type')

    #top
    if c[0]=='N':
        T[:, -1]=c[1]*dx+T[:, -2]
    elif c[0]=='D':
        T[:, -1]=c[1]
    else:
        return('Please enter a valid BC type')

    #bottom
    if d[0]=='N':
        T[:, 0]=d[1]*dx+T[:, 1]
    elif d[0]=='D':
        T[:, 0]=d[1]
    else:
        return('Please enter a valid BC type')
"""
