from Eliminate import *
import random
import time

def randomMatrix(n, e):
	# Create matrix R (nxn) filled with zeros
	R = np.zeros(n*n).reshape(n, n)
	# For every line
	for i in range(len(R)):
		# For every column
		for j in range(len(R[i])):
			# Replace R[i,j] with a random variable from a uniform(-epsilon, epsilon)
			R[i][j] = random.uniform(-e, e)

	# Return the matrix
	return R


times_eliminate = []
for k in range(2, 13):
	times_eliminate.append([])
	n = 2**k
	e = 0.5

	A = np.arange(1, n*n+1)
	A = A.reshape((n, n))
	b = np.ones(n)

	for i in range(10):
		R = randomMatrix(n, e)
		B = A + R

		start = time.clock()
		eliminate(B, b) 
		times_eliminate[k-2].append(time.clock() - start)
		print "n = %d\nFor %d runs (eliminate): %f" %(n, i+1, np.mean(times_eliminate[k-2]))

