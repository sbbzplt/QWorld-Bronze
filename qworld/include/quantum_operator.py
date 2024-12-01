import numpy as np
from scipy.linalg import qr

# randomly create a NxN-dimensional unitary operator
def random_unitary(num_qubit=1, dtype="float"):
    if dtype == "float":
        N = int(2 ** num_qubit)    
        H = np.random.randn(N, N)
        Q, R = qr(H)
    elif dtype == "complex":
        N = int(2 ** num_qubit)    
        H_real = np.random.randn(N, N)
        H_imag = np.random.randn(N, N)
        Q, R = qr(H_real + 1j*H_imag)
    else:
        raise AttributionError(f"dtype should be either 'float' or 'complex', not {dtype}")
    return Q
