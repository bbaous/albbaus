import numpy as np
import matplotlib.pyplot as plt
import math

def model(x):
    return  dt*r*x*(1-x/K)

# initial conditions
x0,r,K,dt,tmax=1,1,100,0.5,10
# time points
t = np.linspace(0,tmax,num=int(tmax/dt))

x1 = np.zeros(int(tmax/dt))
i=0
for j in t:
    if i==0:
        x1[i]=x0
    else:
        x1[i]=x1[i-1]+model(x1[i-1])
    i=i+1

# Prepare to plot results
plt.plot(t,x1,'r',label='Using for loop')
plt.xlabel('time')
plt.ylabel('x(t)')

# Exact solution calculation
X = np.zeros(int(tmax/dt))
X[0] = x0
for n in range(int(tmax/dt)-1):
    print(str(n)+" and  "+str(X[n]) + "  "+str(t[n]))
    X[n+1] = x0*K*math.exp(r*t[n])/(K+x0*(math.exp(r*t[n])-1))

# Finally plot all results
plt.plot(t,X)
plt.xlabel('time with dt=0.5')
plt.ylabel('x(t)')
plt.legend(['ODE','ExactSolution'],loc='upper left')
plt.show()



