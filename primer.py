import os
import numpy as np
import matplotlib.pyplot as plt

plt.figure(1, figsize=(8,4))

plt.subplot(1,2,2)
data = np.loadtxt("primer.dat")

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
            
plt.savefig("resultado.png")

#Apoyado mi ejercicio 14
x=[2.031331588946557076e+00, 5.886777538940683563e+00, 2.195744759275823021e+00, 6.821886748452244298e+00, 8.793952398085184141e-01, 2.951577398416659559e+00, 4.454332895499525158e+00, -1.804396045394615955e+00, -5.841925974092386120e+00, -1.113495627653518838e+00]

listax=[]
listay=[]

for i in range(100000):
    sigma=1.0
    ang=np.random.uniform(0,2*np.pi)
    y3=-np.log(np.random.uniform(0,1))
    r=sigma*np.sqrt(2*y3)
    xn=r*np.cos(ang)
    yn=r*np.sin(ang)
    listax.append(xn)
    listay.append(yn)

def proba(sigma, x):
    return 1/(sigma*np.sqrt(2*np.pi))*np.exp(-0.5*(x**2/sigma**2))


def like(x,sigma):
    p=1.0/9
    for i in x:
        p = p * proba(sigma, i)
    return p

sigma=np.linspace(1,10,1000)
p=like(x,sigma)
plt.figure(2)
plt.plot(sigma,p)
plt.xlabel("sigma")
plt.ylabel("probabilidad")
plt.title("SIGMA")
plt.savefig('sigma.png')
