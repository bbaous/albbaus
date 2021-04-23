import numpy as np
from scipy.integrate import odeint
import matplotlib.pyplot as plt
import math
#This ODE model represents the dynamics of the amount of radioactive material:
#dX/dt=rX(1-X/K)
#where X(t) is the population size, and r and K are the model parameters.


# initial conditions
x0,r,K,dt,tmax=1,1,100,0.1,10
x0_100,r,K,dt,tmax=100,1,100,0.1,10
x0_200,r,K,dt,tmax=200,1,100,0.1,10
numOfsamples=int(tmax/dt)
# time points
t = np.linspace(0,tmax,num=numOfsamples)

X = np.zeros(numOfsamples)
X[0] = x0
for n in range(int(numOfsamples)-1):
    print(str(n)+" and  X : "+str(X[n]) + "  "+str(t[n]))
    X[n+1] = X[n]*K*math.exp(r*t[n])/(K+X[n]*(math.exp(r*t[n])-1))

X_100 = np.zeros(numOfsamples)
X_100[0] = x0_100
for n in range(int(numOfsamples)-1):
    print(str(n)+" and  X_100 : "+str(X_100[n]) + "  "+str(t[n]))
    X_100[n+1] = X_100[n]*K*math.exp(r*t[n])/(K+X_100[n]*(math.exp(r*t[n])-1))

X_200 = np.zeros(numOfsamples)
X_200[0] = x0_200
for n in range(int(numOfsamples)-1):
    print(str(n)+" and  X_200 : "+str(X_200[n]) + "  "+str(t[n]))
    X_200[n+1] = X_200[n]*K*math.exp(r*t[n])/(K+X_200[n]*(math.exp(r*t[n])-1))

# plot results
plt.plot(t,X,'b')
plt.plot(t,X_100,'g')
plt.plot(t,X_200,'r')
plt.xlabel('time')
plt.ylabel('x(t)')
plt.legend(['x0=0','x0=100',"x0=200"],loc='lower right')
plt.show()