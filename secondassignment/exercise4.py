import numpy as np
from scipy.integrate import odeint
import matplotlib.pyplot as plt
#This ODE model represents the dynamics of the amount of radioactive material:
#dX/dt=rX(1-X/K)
#where X(t) is the population size, and r and K are the model parameters.

def model(x,t):
    dxdt = r*x*(1-x/K)
    return dxdt

# initial conditions
x0,r,K,dt,tmax=1,1,100,0.1,10
x0_100,r,K,dt,tmax=100,1,100,0.1,10
x0_200,r,K,dt,tmax=200,1,100,0.1,10
# time points
t = np.linspace(0,tmax,num=int(tmax/dt))
# solve ODE
x = odeint(model,x0,t)
x100=odeint(model,x0_100,t)
x200=odeint(model,x0_200,t)
# plot results
plt.plot(t,x)
plt.plot(t,x100)
plt.plot(t,x200)
plt.xlabel('time')
plt.ylabel('x(t)')
plt.legend(['x0=0','x0=100',"x0=200"],loc='lower right')
plt.show()