import numpy as np
from scipy.integrate import odeint
import matplotlib.pyplot as plt
#This ODE model represents the dynamics of the amount of radioactive material:
#dX/dt=r-bX
#X(t) is amount of radioactive material (e.g. in Bq)
#The dynamics depend on two model parameters:
#r is rate of leak (e.g. Bq s-1)
#b a rate of decay (e.g. s-1) – radioactive decay

# see https://apmonitor.com/pdc/index.php/Main/SolveDifferentialEquations
# function that returns dy/dt


def model(x,t):
    dxdt = r*x*(1-x/K)
    return dxdt

# initial conditions
x0,r,K,dt=1,1,100,0.5
#maximum time
tmax=5
numOfsamples=tmax/dt
# time points
t = np.linspace(0,tmax,num=int(numOfsamples))
print(t)
# solve ODE
x = odeint(model,x0,t)

# plot results
plt.plot(t,x,'r:',label='dt=0.5')
plt.xlabel('time')
plt.ylabel('x(t)')


# initial conditions
x0,r,K,dt=1,1,100,0.1
#maximum time
tmax=5
numOfsamples=tmax/dt
# time points
t = np.linspace(0,tmax,num=int(numOfsamples))
print(t)
# solve ODE
x = odeint(model,x0,t)

# plot results
plt.plot(t,x,'b:',label='dt=01')
plt.xlabel('time')
plt.ylabel('x(t)')
plt.legend(['dt=0.1','dt=0.5'],loc='lower right')
plt.show()