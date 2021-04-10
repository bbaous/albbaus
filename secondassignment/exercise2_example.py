import numpy as np
from scipy.integrate import odeint
import matplotlib.pyplot as plt
import math
#This ODE model represents the dynamics of the amount of radioactive material:
#dX/dt=rX(1-X/K)
#where X(t) is the population size, and r and K are the model parameters.
#/(K+x(math.exp(r*time)-1))

def exactSolution(x,time):
    return x*K*math.exp(r*time)/(K+x)

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
plt.figure()
plt.plot(t,x)
plt.xlabel('time')
plt.ylabel('x(t)')

x=0.0
#for  n in range(0,int(tmax/dt),):
for n in [float(j) / 2 for j in range(0, 200, 1)]:
    plt.plot(n,x)
    print("n is "+str(n)+ "and x is"+str(x))
    if n==0:
        x= exactSolution(x0,n)
        plt.plot(n,x)
    else:
       x=x+exactSolution(x,n)
       plt.plot(n,x)


plt.xlabel('time')
plt.ylabel('x(t)')
plt.show()

