import numpy as np
import matplotlib.pyplot as plt

data = np.loadtxt("tmp.dat")

plt.figure()
plt.scatter(data[:,0], data[:,1], c=data[:,2])
plt.savefig("fig05.png")