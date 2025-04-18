import numpy as np
import pandas as pd
import matplotlib.pyplot as plt


a = np.array([1, 2, 3])
b = np.array([[1, 2], [3, 4]])

z = np.zeros((3, 3))
o = np.ones((2, 4))

r = np.random.rand(2, 2)
rb = np.random.rand(5, 5)

i = np.eye(10)
print(i)

# ----------------------------------
print(b.shape, b.ndim, b.size, b.dtype)

print(r)
print(r[0,0], r[0,1], r[1,0], r[1,1])
print(r[1,:])
print(rb[1:3, 1:3])
print(rb[::2])


# Maths

a = np.array([1, 2, 3])
b = np.array([8, 9, 10])

print (a+b)
acarre = a**2
print(acarre)
print(np.sum(acarre))
print(np.sum(r))

# Stats
a = np.array([1, 2, 3, 4, 5,6,7,8,9,10])
print(np.mean(a))
print(np.median(a))
qt = np.percentile(a, 25)  # 1er quartile
print(qt)

# Produit matriciel

A = np.array([[1, 2], [3, 4]])
B = np.array([[2, 0], [1, 2]])

print(np.dot(A, B))
print(A @ B)

a = np.array([1, 2, 3, 4, 5])
print (a [a>2])
print (a %2 )
print (a %2 ==0)


x = np.linspace(0,2*np.pi,100)
y = np.sin(x) + 0.5 * np.cos(2*x)
print(y)


# reg lineaire
x = np.array([1, 2, 3, 4, 5]) # heures
y = np.array([2, 4, 6, 8, 10]) #notes
A = np.vstack([x, np.ones(len(x))]).T
m, c = np.linalg.lstsq(A, y, rcond=None)[0]


# reduct 10% line 1
prices = np.array([
    [89, 250, 120],
    [105, 270, 130],
    [95, 260, 125],
])

# Réduction de 10% sur business
print(prices[:, 1] * 0.9)