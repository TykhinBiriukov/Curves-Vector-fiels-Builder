from mpl_toolkits import mplot3d
import matplotlib.pyplot as plt
import numpy as np

fig = plt.figure()
ax = plt.axes(projection='3d')

t = np.linspace(0,12*np.pi, 1000)
x = np.sin(𝑡)*(np.exp(np.cos(𝑡))-2*np.cos(4*𝑡)-np.sin(𝑡/12)**5)
y = np.cos(𝑡)*(np.exp(np.cos(𝑡))-2*np.cos(4*𝑡)-np.sin(𝑡/12)**5)

ax.plot3D(x,y)
plt.show()