import numpy as np
from scipy.integrate import odeint
import matplotlib.pyplot as plt
#This ODE model represents the dynamics of the amount of radioactive material:
#dX/dt=rX(1-X/K)
#where X(t) is the population size, and r and K are the model parameters.

def model(x,t):
    K=100
    if t>10:
        K=20
    print(str(t)+" and  "+str(K))
    dxdt = r*x*(1-x/K)
    return dxdt
# initial conditions for x0,r and 
x0,r,dt=1,1,0.1
#maximum time
tmax=20
numOfsamples=tmax/dt
# time points
t = np.linspace(0,tmax,num=int(numOfsamples))
print(t)
# solve ODE
x = odeint(model,x0,t)
# plot results
plt.plot(t,x)
plt.xlabel('time')
plt.ylabel('x(t)')
plt.show()
