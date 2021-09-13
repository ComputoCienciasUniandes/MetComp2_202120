import numpy as np
import matplotlib.pyplot as plt

data = np.loadtxt("salida.dat")

plt.figure()
plt.plot(data[:,0],data[:,2])
plt.xlabel("tiempo")
plt.ylabel("y")
plt.savefig("plot_1.jpg")

plt.figure()
plt.plot(data[:,1],data[:,2])
plt.xlabel("x")
plt.ylabel("y")
plt.savefig("plot_2.jpg")

plt.figure()
plt.plot(data[:,0],np.sqrt(data[:,3]**2 + data[:,4]**2))
plt.xlabel("t")
plt.ylabel("v")
plt.savefig("plot_3.jpg")