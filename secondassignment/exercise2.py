import numpy as np
from scipy.integrate import odeint
import matplotlib.pyplot as plt
import math

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

X = np.zeros(int(tmax/dt))
X[0] = x0
for n in range(int(tmax/dt)-1):
    print(str(n)+" and  "+str(X[n]) + "  "+str(t[n]))
    X[n+1] = X[n]*K*math.exp(r*t[n])/(K+X[n]*(math.exp(r*t[n])-1))

plt.plot(t,x)
plt.plot(t,X)
plt.xlabel('time with dt=0.5')
plt.ylabel('x(t)')
plt.legend(['ODE','ExactSolution'],loc='upper left')
plt.show()



