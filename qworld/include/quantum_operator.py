import numpy as np
from scipy.linalg import qr

# randomly create a 2x2-dimensional un,tary operator
def random_unitary(n=2):    
    H = np.random.randn(n, n)
    Q, R = qr(H)
    unitary = list(Q.dot(Q.T))
    return unitary


