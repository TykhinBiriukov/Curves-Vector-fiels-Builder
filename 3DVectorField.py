from mpl_toolkits.mplot3d import axes3d
import matplotlib.pyplot as plt
import numpy as np

fig = plt.figure()
axes1 = fig.add_subplot(projection = '3d')

x, y, z = np.meshgrid(np.arange(-0.8, 1, 0.2), np.arange(-0.8, 1, 0.2), np.arange(-0.8, 1, 0.8))
u = x
v = y
w = z

plt.quiver(x,y,z,u,v,w, color = "red", length=0.1, normalize=True)
plt.show()