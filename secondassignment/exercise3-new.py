import numpy as np
import matplotlib.pyplot as plt
import math


def model(x):
    dxdt = dt*r*x*(1-x/K)
    return dxdt

# initial conditions
x0,r,K,dt=1,1,100,0.5
#maximum time
tmax=5
numOfsamples=int(tmax/dt)
# time points
t = np.linspace(0,tmax,num=int(numOfsamples))

#Solve the ODE
x05 = np.zeros(numOfsamples)
i=0
for j in t:
    if i==0:
        x05[i]=x0
    else:
        x05[i]=x05[i-1]+model(x05[i-1])
    i=i+1

#Exact solution
XE_05 = np.zeros(int(tmax/dt))
XE_05[0] = x0
for n in range(int(tmax/dt)-1):
    XE_05[n+1] = x0*K*math.exp(r*t[n])/(K+x0*(math.exp(r*t[n])-1))

#Calculate the Relative error
EXACT_SOLUTION = x0*K*math.exp(r*5)/(K+x0*(math.exp(r*5)))
ODE= r*XE_05[4]*(1-XE_05[4]/K)*dt
Relative_Error = 100 * ((EXACT_SOLUTION - ODE) / EXACT_SOLUTION)
print ("Retative error (dt=0.5): " +str(Relative_Error))

#plot results
plt.plot(t,x05,'r')
plt.plot(t,XE_05,'g',label='dt=0.1')
plt.xlabel('time')
plt.ylabel('x(t)')


# initial conditions
x0,r,K,dt=1,1,100,0.1
#maximum time
tmax=5
numOfsamples=int(tmax/dt)
# time points
t = np.linspace(0,tmax,num=numOfsamples)

#Solve the ODE
X01=np.zeros(numOfsamples)
i=0
for j in t:
    if i==0:
        X01[i]=x0
    else:
        X01[i]=X01[i-1]+model(X01[i-1])
    i=i+1

#Exact solution
XE_01 = np.zeros(int(tmax/dt))
XE_01[0] = x0
for n in range(int(tmax/dt)-1):
    XE_01[n+1] = x0*K*math.exp(r*t[n])/(K+x0*(math.exp(r*t[n])-1))

#Calculate the Relative error
EXACT_SOLUTION = x0*K*math.exp(r*5)/(K+x0*(math.exp(r*5)))
ODE= r*XE_01[4]*(1-XE_01[4]/K)*dt
Relative_Error = 100 * ((EXACT_SOLUTION - ODE) / EXACT_SOLUTION)
print ("Retative error (dt=0.1): " +str(Relative_Error))

#plot results
plt.plot(t,X01,'b')
plt.plot(t,XE_01,'y',label='dt=0.1')
plt.xlabel('time')
plt.ylabel('x(t)')
plt.legend(['ODE dt=0.1',"Exact Sol/dt=0.1",'ODE dt=0.5',"Exact Sol/dt=0.5"],loc='lower right')
plt.show()





