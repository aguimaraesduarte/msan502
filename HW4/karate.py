import numpy as np

f = open("karate.csv")
lines = f.readlines()
f.close()

n = 34

A = [[0.0 for i in range(n)] for j in range(n)]

for line in lines:
	source, target = line.strip().split(",")
	source = int(source)
	target = int(target)
	A[target-1][source-1] = 1.0

# Make A column stochastic
A_trans = np.transpose(A) # easier to work on rows
multipliers = [sum(A_trans[i]) for i in range(n)] # by how much we must divide each row

for row in range(n):
	if multipliers[row] != 0.0:
		A_trans[row] = A_trans[row]/multipliers[row]
	else:
		A_trans[row][row] = 1.0 # node is isolated

A = np.transpose(A_trans) # get A back
A = A.tolist() # coerce to list

for alpha in [0, .15, .5, .75, .99999999]:

	B=[[1.0/n for i in range(n)] for j in range(n)]

	M = np.dot(1-alpha, A) + np.dot(alpha, B)

	e_vals_A, e_vecs_A = np.linalg.eig(A)
	e_val_A1 = e_vals_A[0]
	e_vec_A1 = np.dot(1.0/sum(e_vecs_A[:,0]), e_vecs_A[:,0])

	e_vals_M, e_vecs_M = np.linalg.eig(M)
	e_val_M1 = e_vals_M[0]
	e_vec_M1 = np.dot(1.0/sum(e_vecs_M[:,0]), e_vecs_M[:,0])

	# get the indices of M sorted by importance according to pagerank
	sorted_indices = sorted(range(len(e_vec_M1)), key=lambda k: e_vec_M1[k], reverse = True)

	print "alpha =", alpha
	print "lamba (A) =", e_val_A1
	print "vec (A) =", e_vec_A1
	print "lamba (M) =", e_val_M1
	print "vec (M) =", e_vec_M1
	for i in sorted_indices:
		print "value of node %d = %f" %(i, e_vec_M1[i])
	print "\n\n\n"
