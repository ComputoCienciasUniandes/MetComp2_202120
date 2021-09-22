import numpy as np
import matplotlib.pyplot as plt
import imageio

data = np.loadtxt("adveccion.dat")
print(np.shape(data))

n_times = np.shape(data)[0]
n_space = np.shape(data)[1]

x = np.linspace(0.0, 1.0, n_space)
t = np.linspace(0.0, 2.0, n_times)

for i in range(n_times):
    filename = "snap_{}.png".format(i)
    fig = plt.figure(figsize=(3,3))
    plt.plot(x, data[i,:])
    plt.title("Tiempo {:.2f} segundos".format(t[i]))
    plt.xlabel("Posicion [metros]")
    plt.ylabel("U")
    plt.ylim(-0.05,0.05)
    plt.xlim(0.0, 1.0)
    plt.grid()
    plt.savefig(filename, bbox_inches="tight")
    plt.close(fig)
    
with imageio.get_writer('adveccion.gif', mode='I') as writer:
    for i in range(n_times):
        print(i, n_times)
        filename = "snap_{}.png".format(i)
        image = imageio.imread(filename)
        writer.append_data(image)
    
    

    
    
    
    
    
    
    
    
    