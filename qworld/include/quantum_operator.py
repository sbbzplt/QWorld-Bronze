import numpy as np
from scipy.linalg import qr

# randomly create a 2x2-dimensional un,tary operator
def random_unitary(n=2):    
    N = int(2 ** n)    
    H = np.random.randn(N, N)
    Q, R = qr(H)
    return Q

def random_complex_unitary(eps=0.0001):
    alpha = np.random.random() * 2 * np.pi
    beta = np.random.random() * 2 * np.pi
    theta = np.random.random() * 2 * np.pi
    u = np.array([[np.exp(1j*alpha)*np.cos(theta), np.exp(1j*beta)*np.sin(theta)], 
                  [-np.exp(-1j*beta)*np.sin(theta), np.exp(-1j*beta)*np.cos(theta)]])
    res = np.matmul(u, np.conjugate(np.transpose(u)))
    while not (abs(res[0, 0] - 1) < eps and abs(res[1, 1] - 1) < eps and abs(res[0, 1]) < eps and abs(res[1, 0]) < eps):
        alpha = random() * 2 * np.pi
        beta = random() * 2 * np.pi
        theta = random() * 2 * np.pi
    
        u = np.array([[np.exp(1j*alpha)*np.cos(theta), np.exp(1j*beta)*np.sin(theta)], 
                    [-np.exp(-1j*beta)*np.sin(theta), np.exp(-1j*beta)*np.cos(theta)]])
    
        res = np.matmul(u, np.conjugate(np.transpose(u)))
    return u


