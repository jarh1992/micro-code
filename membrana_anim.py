#Author Jesus Rodriguez

from math import pi, pow, cos, sin, sqrt
import matplotlib.pyplot as plt
import mpl_toolkits.mplot3d.axes3d as p3
import numpy as np
from matplotlib.ticker import LinearLocator, FormatStrFormatter
from matplotlib import cm
import matplotlib.animation as animation

fig = plt.figure()
ax = fig.gca(projection='3d')

# Customize the z axis.
#ax.zaxis.set_major_locator(LinearLocator(10))
#ax.zaxis.set_major_formatter(FormatStrFormatter('%.02f'))

plot_args = {'cmap':cm.coolwarm, 'linewidth':0, 'antialiased':False}
a = b = 4
X = np.arange(0, a + 0.25, 0.25)
X, Y = np.meshgrid(X, X)
zero_array = np.zeros((len(X),len(Y)))
#surf = ax.plot_surface(X, Y, zero_array, **plot_args)
n = m = 1
t = np.arange(0, 1, 0.01)
fps = 10 # frame per sec
frn = 100 # frame number of the animation

def update(time):
	z2 = []
	for x in X[0]:
	    z1 = []
	    for y in Y:
	        l1 = float(n * pi / a)
	        l2 = float(m * pi / b)
	        Amn = -16 * pow(a * b, 2) * (pow(-1, m) - 1) * (pow(-1, n) - 1) / (pow(m * n * pi,3))
	        z1.append(Amn * cos(3 * sqrt(pow(l1, 2) + pow(l2, 2)) * time) * sin(l1 * x) * sin(l2 * y[0]))
	    z2.append(z1)
	Z = np.array(z2)
	ax.clear()
	ax.set_zlim3d(-510.00, 510.00)
	surf = ax.plot_surface(X, Y, Z, **plot_args)
	return surf,

ani = animation.FuncAnimation(fig, update, frn, fargs=t.all())
plt.show()