import numpy as np
from scipy.integrate import odeint
import matplotlib.pyplot as plt
import math
#This ODE model represents the dynamics of the amount of radioactive material:
#dX/dt=r-bX
#X(t) is amount of radioactive material (e.g. in Bq)
#The dynamics depend on two model parameters:
#r is rate of leak (e.g. Bq s-1)
#b a rate of decay (e.g. s-1) – radioactive decay

# see https://apmonitor.com/pdc/index.php/Main/SolveDifferentialEquations
# function that returns dy/dt


def model(x,t):
    dxdt = r*x*(1-x/K)*dt
    return dxdt

# initial conditions
x0,r,K,dt=1,1,100,0.5
#maximum time
tmax=5
numOfsamples=int(tmax/dt)
# time points
t = np.linspace(0,tmax,num=int(numOfsamples))
# solve ODE
#x = odeint(model,x0,t)

x05 = np.zeros(numOfsamples)
i=0
for j in t:
    if i==0:
        x05[i]=x0
    else:
        x05[i]=x05[i-1]+model(x05[i-1],j)
    i=i+1

XE_05 = np.zeros(int(tmax/dt))
XE_05[0] = x0
for n in range(int(tmax/dt)-1):
    XE_05[n+1] = XE_05[n]*K*math.exp(r*t[n])/(K+XE_05[n]*(math.exp(r*t[n])-1))


#plot results
plt.plot(t,x05,'r')
plt.plot(t,XE_05,'g',label='dt=0.1')
plt.xlabel('time')
plt.ylabel('x(t)')
plt.legend(['dt=0.5',"Exact Sol/dt=0.5"],loc='lower right')
plt.show()



# initial conditions
x0,r,K,dt=1,1,100,0.1
#maximum time
tmax=5
numOfsamples=int(tmax/dt)
# time points
t = np.linspace(0,tmax,num=numOfsamples)
# solve ODE
#x = odeint(model,x0,t)


X01=np.zeros(numOfsamples)
i=0
for j in t:
    if i==0:
        X01[i]=x0
    else:
        X01[i]=X01[i-1]+model(X01[i-1],j)
    i=i+1

XE_01 = np.zeros(int(tmax/dt))
XE_01[0] = x0
for n in range(int(tmax/dt)-1):
    XE_01[n+1] = XE_01[n]*K*math.exp(r*t[n])/(K+XE_01[n]*(math.exp(r*t[n])-1))

#plot results
plt.plot(t,X01,'r')
plt.plot(t,XE_01,'g',label='dt=0.1')
plt.xlabel('time')
plt.ylabel('x(t)')
plt.legend(['dt=0.1',"Exact Sol/dt=0.1"],loc='lower right')
plt.show()





