from mpl_toolkits import mplot3d
import matplotlib.pyplot as plt
import numpy as np


fig = plt.figure()
ax = plt.axes(projection='3d')

t = np.linspace(0,10*np.pi, 100)
x = 4*np.cos(t)+np.cos(4*t)
y = 4*np.sin(t)-np.sin(4*t)
z = t/5

ax.plot3D(x, y, z)
plt.show()