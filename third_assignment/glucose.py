
import numpy as np
import matplotlib.pyplot as plt
from scipy.integrate import odeint

# define a function containing the derivatives, i.e. the ODE
def glucose(x,t,params):
    X,I = x    
    k, alpha, beta, gamma_X, gamma_I = params
    derivs = [k - gamma_X * X - beta * I * X,
             alpha * X - gamma_I * I]
    return derivs

# define parameters
k = 5.625
alpha = 1.111
beta = 0.2
gamma_X = 0.25
gamma_I = 1.0


# bundle parameters for the solver
params = [k, alpha, beta, gamma_X, gamma_I]
# initial values
X = 6
I = 5
x0 = [X,I]

# Make time array for the solution
maxt = 12.0
tstep = 0.05

t = np.arange(0,maxt,tstep)
glucose_out = odeint(glucose, x0, t, args=(params,))
plt.plot(t,glucose_out)
plt.show()