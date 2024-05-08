from mpl_toolkits import mplot3d
import matplotlib.pyplot as plt
import numpy as np

fig = plt.figure()
ax = plt.axes(projection='3d')

t = np.linspace(0,20*np.pi, 100)
x = 11*np.cos(𝑡)-np.cos(11*𝑡/10)
y = 11*np.sin(𝑡)-np.sin(11*𝑡/10)

ax.plot3D(x,y, lw = 1)
plt.show()