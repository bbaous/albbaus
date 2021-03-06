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
x0,r,K,dt,tmax=1,1,100,0.5,10
# time points
t = np.linspace(0,tmax,num=int(tmax/dt))
print(t)
# solve ODE
x = odeint(model,x0,t)
# plot results
plt.plot(t,x)
plt.xlabel('time')
plt.ylabel('x(t)')
plt.legend(['dt=0.5'], loc='lower right')
plt.show()