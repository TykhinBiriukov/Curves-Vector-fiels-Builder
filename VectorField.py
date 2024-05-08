import matplotlib.pyplot as plt
import numpy as np


x,y = np.meshgrid(np.linspace(-10,10,10),np.linspace(-10,10,10))
u = x/np.sqrt(x**2 + y**2)
v = y/np.sqrt(x**2 + y**2)

plt.quiver(x,y,u,v)
plt.show()