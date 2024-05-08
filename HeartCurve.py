from mpl_toolkits import mplot3d
import matplotlib.pyplot as plt
import numpy as np

fig = plt.figure()
ax = plt.axes(projection='3d')

t = np.linspace(0,2*np.pi, 100)
x = 16*np.sin(t)**3
y = 13*np.cos(t)-5*np.cos(2*t)-2*np.cos(3*t)-np.cos(4*t)

ax.plot3D(x,y)
plt.show()