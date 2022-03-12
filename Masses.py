from numpy import linspace,array,arange, log,exp,sin,cos,sqrt, pi, zeros, ones, eye, matmul
import numpy as np
from numpy.linalg import eig,inv
from matplotlib.pyplot import plot,xlabel,ylabel,legend,show, figure, subplot, title, tight_layout, stem

#  set the time array
T = 10
dt = 0.01

# 1) Fill in t array using arange
t = arange(0,T,dt)

# 2) Create the Matrix M and find the eigenvalues and eigenvectors
k1 = 1
k2 = 1

beta = k1 + k2
alpha = k2
M = array([[-beta,alpha],[alpha,-beta]])


# 3) use eig(M) to store eigen values in array w and eigen vectors in matrix v
w,v = eig(M)

w = abs(w)


# 4) Create the time series of the motion of each mass as cosines
#     for the first eigenvalue/eigenvector
#  What is omega for the selected mode?
#  What is v1 and v2?
omega = sqrt(w)

x0 = [1,1]

def twoMass(omegain,vin,x0in,tin):
    gamma = matmul(inv(vin), x0in)

    v1 = vin[0] * gamma[0]
    v2 = vin[1] * gamma[1]

    x1out = v1[0] * cos(omegain[0] * tin) + v2[0] * cos(omegain[1] * tin)
    x2out = v1[1] * cos(omegain[0] * tin) + v2[1] * cos(omegain[1] * tin)
    return x1out, x2out

x1,x2 = twoMass(omega,v,x0,t)

plot(t,x1, t,x2)

show()

#5 Now superpose a mix of both eigen values, 0.5 each. Plot the motion of the two masses.
#   What would the initial conditions be to get that mix?

x0 = [0,1]

x1,x2 = twoMass(omega,v,x0,t)

plot(t,x1, t,x2)

show()
