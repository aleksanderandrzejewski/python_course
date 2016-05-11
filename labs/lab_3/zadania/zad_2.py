from scipy.integrate import odeint
import numpy as np
import matplotlib.pyplot as plt
mport matplotlib.animation as FuncAnimation

k=10
g=[0,-9.81]
x10=[0,0]
x20=[-10,0]
l0=10
u10=[0,5]
u20=[-3,3]

def rhs(Y0, t):

    r=x2-x1
    dlr=np.linalg


time=np.linspace(0,1,100)


def rhs(Y0, t): # funkcja prawych stron
    x1=Y[2:4]
    u1=y[]

    r=x1-x20

    dYdt[5]=-r*k/2*(1.-;0/dlr)
    dYdt[1]
    dYdt[6:]=u2




    return Y0

y = odeint(rhs, 1, t )

fig = figure()

plt.plot(t, y)
plt.show()