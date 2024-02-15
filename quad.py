import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D


fig = plt.figure()
plot = fig.add_subplot(111, projection='3d')

def fx(x, y):
    return np.cos(x) + np.sin(y)

def quad(x, y, x0, y0):
    A = fx(x0, y0)
    J = np.array([-np.sin(x0), np.cos(y0)])
    H = np.array([[-np.cos(x0), 0], [0, -np.sin(y0)]])
    Z = []
    for i in range(len(x)):
        temp = []
        for j in range(len(x[0])):
            X = np.array([x[i][j], y[i][j]])
            Xh = np.array([x0, y0])
            Y = A + J.dot(X - Xh) + 0.5*(X - Xh).T.dot(H.dot(X - Xh))
            temp.append(Y)
        Z.append(temp)
    return np.array(Z)

def gradient(xa=3, ya=3, lr=0.05):
    dx = lambda u: -np.sin(u)
    dy = lambda u: np.cos(u)
    for i in range(30):
        yield xa, ya
        xa -= lr*dx(xa)
        ya -= lr*dy(ya)

dx = np.pi/32
domain = np.arange(0, 2*np.pi+dx, dx)
x, y = np.meshgrid(domain, domain)
z = fx(x, y)

for x0, y0 in gradient():
    plot.cla()
    plot.plot_surface(x, y, z, color='red', edgecolor='black', linewidth=0.5)
    z2 = quad(x, y, x0, y0)
    plot.plot_surface(x, y, z2, color='blue')
    plt.pause(0.001)
    

plt.show()









