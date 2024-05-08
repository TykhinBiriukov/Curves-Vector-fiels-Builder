from mpl_toolkits import mplot3d
import matplotlib.pyplot as plt
import numpy as np

fig = plt.figure()
ax = plt.axes(projection='3d')

t = np.linspace(0,50*np.pi, 400)
x = np.sin(2*t/3+np.pi/4)
y = np.sin(t)
z = t

ax.plot3D(x, y, z)
plt.show()