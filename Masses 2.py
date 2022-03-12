from numpy import eye

from numpy.linalg import eig

N = 5

A = -2 * eye(N) + 1 * eye(N,N,1) + 1 * eye(N,N,-1)

d,v = eig(A)

print(d)

print(v.T)