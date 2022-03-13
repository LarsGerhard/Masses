from numpy import eye, sqrt

from numpy.linalg import eig

# Constructing tridiagonal matrix

N = 5

A = -2 * eye(N) + 1 * eye(N,N,1) + 1 * eye(N,N,-1)

# Finding eigensystem

w,v = eig(A)

# Verify that system matches given website (it does)

print(w)

print(v.T)

# Calculate frequency

omega = sqrt(abs(w))

# Verify that frequencies matches given website (they do)

print(omega)

vtest = v[1] + v[2]
