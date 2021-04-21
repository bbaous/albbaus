from operator import le
import numpy as np
from numpy.core.arrayprint import dtype_is_implied
from scipy.integrate import odeint
import matplotlib.pyplot as plt
#This ODE model represents the dynamics of the amount of radioactive material:
#dX/dt=rX(1-X/K)
#where X(t) is the population size, and r and K are the model parameters.

def model(x,t):
    return  r*x*(1-x/K)

# initial conditions
x0,r,K,dt,tmax=1,1,100,0.5,10
# time points
t = np.linspace(0,tmax,num=int(tmax/dt))
print(t)
# solve ODE
x = odeint(model,x0,t)
print (x)
# plot results
plt.figure()
plt.plot(t,x,'r',label='Using for odenint')
plt.xlabel('time')
plt.ylabel('x(t)')
plt.legend(['Using odenit & dt=0.5'], loc='lower right')


x1 = np.zeros(int(tmax/dt))
i=0
for j in t:
  
    if i==0:
        x1[i]=x0
    else:
        x1[i]=x1[i-1]+model(x1[i-1],j)
    print ("Time is  : "+str(j)+" i  is : "+str(i)+"  x is : "+str(x1[i]))
    i=i+1

# plot results

plt.plot(t,x1,'b',label='Using for loop')
plt.xlabel('time')
plt.ylabel('x(t)')
plt.legend(['Using odenit dt=0.5','Using for loop dt=0.5'],loc='lower right')
plt.show()
