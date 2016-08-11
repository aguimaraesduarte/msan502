import numpy as np

n = 6
alpha = .15

A = [[0, 0, .5, .5, 0, .2],
     [1.0/3, 0, 0, 0, 0, .2],
     [1.0/3, .5, 0, .5, 1, .2],
     [1.0/3, .5, 0, 0, 0, .2],
     [0, 0, .5, 0, 0, .2],
     [0, 0, 0, 0, 0, 0]]

B=[[1.0/n for i in range(n)] for j in range(n)]

M = np.dot(1-alpha, A) + np.dot(alpha, B)

e_vals_A, e_vecs_A = np.linalg.eig(A)

e_val_A1 = e_vals_A[0]
e_vec_A1 = np.dot(1.0/sum(e_vecs_A[:,0]), e_vecs_A[:,0])

e_vals_M, e_vecs_M = np.linalg.eig(M)

e_val_M1 = e_vals_M[0]
e_vec_M1 = np.dot(1.0/sum(e_vecs_M[:,0]), e_vecs_M[:,0])

print "lamba (A) =", e_val_A1
print "vec (A) =", e_vec_A1
print "lamba (M) =", e_val_M1
print "vec (M) =", e_vec_M1