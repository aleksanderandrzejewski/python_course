from scipy.integrate import odeint
import numpy as np
import matplotlib.pyplot as plt

t=np.linspace(0,1,100)
def rhs(y0, t): # funkcja prawych stron
    return y0

y = odeint(rhs, 1, t )

plt.figure()
plt.plot(t, y)
plt.show()