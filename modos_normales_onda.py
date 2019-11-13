# Author: Jesus A. Rodriguez Henao
import numpy as np
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation

def init():
	ax.set_xlim(-2*np.pi, 2*np.pi)
	ax.set_ylim(-1.2, 1.2)
	return ln,

def update(time):
	A = [] # amplitud
	A = np.sin(T - (time/4))
	B = np.sin(T + (time/4))
	C = A + B
	ax.clear()
	ax.set_ylim(-2.1, 2.1)
	ln = plt.plot(T, A, 'r-')	
	ln = plt.plot(T, B, 'b-')	
	ln = plt.plot(T, C, 'g-')	
	return ln,

# ani = FuncAnimation(fig, update, frames=T, init_func=init, blit=True)
fig, ax = plt.subplots()
xdata, ydata = [], []
# ln, = plt.plot([], [], 'r-')
L = 2*np.pi
T = np.linspace(-2*np.pi, 2*np.pi, 128) # periodo
n = 0
t = np.arange(0, 1, 0.01)
fps = 10 # frame per sec
frn = 100 # frame number of the animation
ani = FuncAnimation(fig, update, frn, fargs=t.all())
plt.show()