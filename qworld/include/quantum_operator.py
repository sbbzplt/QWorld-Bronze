import numpy as np
from scipy.linalg import qr

# randomly create a 2x2-dimensional un,tary operator
def random_unitary(n=2):    
    N = int(2 ** n)    
    H = np.random.randn(N, N)
    Q, R = qr(H)
    unitary = list(Q.dot(Q.T))
    return unitary


