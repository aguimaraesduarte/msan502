import numpy as np
import random

# Create matrix A (10x10) with integers 1:100
A = np.arange(1, 101)
A = A.reshape((10, 10))

# Create matrix v (10x1) with integers 1:10
v = np.arange(1, 11)

# Create matrix b (10x1) with ones
b = np.ones(10)

# Compute Av
Av = np.dot(A, v)
#print Av

# Solve Ax1 = b and Ax2 = v
x1 = np.linalg.solve(A, b)
x2 = np.linalg.solve(A, v)
#print x1
#print x2

# Verify that Ax1 = b and Ax2 = v
Ax1 = np.dot(A, x1) # == b
Ax2 = np.dot(A, x2) # == v
#print Ax1
#print Ax2
print np.isclose(Ax1, b)
print np.isclose(Ax2, v)

def randomMatrix(e):
	# Create matrix R (10x10) filled with zeros
	R = np.zeros(100).reshape(10, 10)
	# For every line
	for i in range(len(R)):
		# For every column
		for j in range(len(R[i])):
			# Replace R[i,j] with a random variable from a uniform(-epsilon, epsilon)
			R[i][j] = random.uniform(-e, e)

	# Return the matrix
	return R

##################################
# Create matrix R (10x10) with random noise
e = 0.01
R = randomMatrix(e)

# New matrix A+R
B = A + R

# Solve Bx1 = b and Bx2 = v
x11 = np.linalg.solve(B, b)
x21 = np.linalg.solve(B, v)

# Verify that Bx1 = b and Bx2 = v
Bx11 = np.dot(B, x11) # == b
Bx21 = np.dot(B, x21) # == v
#print Bx11
#print Bx21
print "e =", e
print np.isclose(Bx11, b)
print np.isclose(Bx21, v)

##################################
e = 0.1
R = randomMatrix(e)

# New matrix A+R
B = A + R

# Solve Bx1 = b and Bx2 = v
x11 = np.linalg.solve(B, b)
x21 = np.linalg.solve(B, v)

# Verify that Bx1 = b and Bx2 = v
Bx11 = np.dot(B, x11) # == b
Bx21 = np.dot(B, x21) # == v
#print Bx11
#print Bx21
print "e =", e
print np.isclose(Bx11, b)
print np.isclose(Bx21, v)

##################################
e = 0.5
R = randomMatrix(e)

# New matrix A+R
B = A + R

# Solve Bx1 = b and Bx2 = v
x11 = np.linalg.solve(B, b)
x21 = np.linalg.solve(B, v)

# Verify that Bx1 = b and Bx2 = v
Bx11 = np.dot(B, x11) # == b
Bx21 = np.dot(B, x21) # == v
#print Bx11
#print Bx21
print "e =", e
print np.isclose(Bx11, b)
print np.isclose(Bx21, v)

##################################
e = 1
R = randomMatrix(e)

# New matrix A+R
B = A + R

# Solve Bx1 = b and Bx2 = v
x11 = np.linalg.solve(B, b)
x21 = np.linalg.solve(B, v)

# Verify that Bx1 = b and Bx2 = v
Bx11 = np.dot(B, x11) # == b
Bx21 = np.dot(B, x21) # == v
#print Bx11
#print Bx21
print "e =", e
print np.isclose(Bx11, b)
print np.isclose(Bx21, v)