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
    print(b)
    print(r)
    dxdt = r -b*x
    return dxdt

# initial condition
x0 = 0
r=1
b=0.5
# time points
t = np.linspace(0,100)

# solve ODE
x = odeint(model,x0,t)

# plot results
plt.plot(t,x)
plt.xlabel('time')
plt.ylabel('x(t)')
plt.show()