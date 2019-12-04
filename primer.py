import os
import numpy as np
import matplotlib.pyplot as plt

plt.figure(1, figsize=(8,4))

plt.subplot(1,2,2)
data = np.loadtxt("Ejercicio29.dat")

plt.plot(data[:,0], data[:,1])
plt.plot(data[:,0], data[:,2])
plt.plot(data[:,0], data[:,3])
plt.plot(data[:,0], data[:,4])
plt.plot(data[:,0], data[:,5])
plt.plot(data[:,0], data[:,6])
plt.plot(data[:,0], data[:,7])
plt.title("condicion")
plt.xlabel('X')
plt.ylabel('Y')


plt.subplot(1,2,1)           
            
plt.savefig("Ejercicio29.png")
