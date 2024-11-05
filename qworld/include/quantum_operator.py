import random, math, numpy
from quantum_state import random_qstate_by_value

# randomly create a 2x2-dimensional un,tary operator
def random_unitary_2x2():
    first_col = random_qstate_by_value()
    second_col = random_qstate_by_value()
    unitary = [[first_col[0], second_col[0]], 
               [first_col[1], second_col[1]]]
    return unitary

# randomly create a 4x4-dimensional un,tary operator
def random_unitary(qubit_num=2):
    N = int(numpy.ceil(2 ** qubit_num))
    unitary = numpy.array([[numpy.random.randint(0, 100) for _ in range(N)] for _ in range(N)], dtype="float64")
    for i in range(N):
        col = unitary[:, i]
        length = numpy.sqrt(sum([j ** 2 for j in col]))
        col /= length
        unitary[:, i] = col
    return unitary
