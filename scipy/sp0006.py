#线性代数
import scipy.linalg as la
import numpy as np
A=np.array([[1,2],[3,4]])
l,v=la.eig(A)
print(l)
print(v)

a,b=np.linalg.eig(A)
print(a)
print(b)

#奇异值分解(svd)
a = np.random.randn(3, 2) + 1.j*np.random.randn(3, 2)
U, s, Vh = la.svd(a)
print (U, Vh, s)
