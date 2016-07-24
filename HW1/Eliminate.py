import numpy as np
import sys

# Function that will perform the elimination algorithm to solve A_x = b_
def eliminate(A_, b_):
	# perform checks to see if we can proceed with the algorithm
	if not checks(A_, b_):
		sys.exit(0)

	# Make a copy of A and b, so as to not modify the original matrices
	A, b = makeCopy(A_, b_)

	# for consistency, transform the first row values to floats
	A[0] = np.dot(1.0, A[0])

	# n is the number of rows and columns
	n = len(A)

	# for every row
	for i in range(n):
		# A[i] = current row
		#print A[i]
		#print "Current row: %d" %i

		# expectedPivot is the element on the diagonal for the current row
		expectedPivot = A[i][i]
		# firstNonZero is the actual first non-zero value on the current row
		firstNonZero = findFirstNonZero(A[i], i)
		# if these two values are different, then we have a temporary failure.
		# A permutation algorithm should be written here to try to solve this failure.
		# For now, we will just quit the algorithm.
		if expectedPivot != firstNonZero:
			print "Temporary failure. Expected pivot, found 0 on row %d." % i
			#print A[i]
			#print expectedPivot, firstNonZero
			sys.exit(0)

		# If we got here, the expected pivot is the actual pivot	
		pivot = expectedPivot
		#print "Pivot = %f\n" %pivot

		# for all other rows, perform elimination
		for ii in range(i+1, n):
			# calculate the multiplier
			multiplier = 1.0*A[ii][i]/pivot
			# replace the row (don't forget to update matrix b too!)
			A[ii] = A[ii] - np.dot(multiplier, A[i])
			b[ii] = b[ii] - np.dot(multiplier, b[i])
			# replace with 0.0 to prevent issues with approximations
			A[ii][i] = 0.0

	# If we got to this point, we have an upper triangular matrix.
	# Now, we have to do back-substitution
	res = backsubstitution(A, b)

	# Print the original matrix, upper triangular matrix and the solution vector
	#print "Original matrix:\n", A_
	#print "\nUpper triangular matrix:\n", A
	#print "\nSolution vector:\n", res

	# return the vector with the solution (x)
	return res

# Function that performs backward substitution. T is an upper triangular matrix
def backsubstitution(T, b):
	# n is the number of rows and columns
	n = len(T)
	# define the vector of solutions (x). It is filled with 0s to begin
	sol = np.zeros(n)
	# for every row, starting from the last one
	for i in range(n-1, -1, -1):
		# T[i] = current row
		# sol = fact1 * fact2
		fact1 = (1.0/T[i][i])
		fact2 = b[i]
		# define a j to decrement fact2
		j = i + 1
		while j < n:
			# decrement fact2 by a certain amount while the condition stands true
			fact2 -= T[i][j] * sol[j]
			j += 1
		# update sol[i] with its value	
		sol[i] = fact1 * fact2
	# we return a vector with the solution (x)
	return sol


# Function that finds the first non-zero value in a given row
def findFirstNonZero(row, index):
	# for every value in the row
	for value in row:
		# if the current value is not 0
		if not np.isclose(value, 0):
		#if abs(value) > 1.0e-3:
			# return the first non-zero value
			return value
	# if we run through all values in the row and cannot find a 0,
	# there are no non-zero values in the row, which leads to a failure.
	# There are either no or infinitely many solutions, and the program exits.		
	print "Failure. Could not find a pivot in this row (%d). No solutions or infinite solutions." %index
	sys.exit(0)

# Function that makes copies of two matrices A and b
def makeCopy(A_, b_):
	if isinstance(A_, np.ndarray):
		A = A_.copy()
	if isinstance(b_, np.ndarray):
		b = b_.copy()
	if isinstance(A_, list):
		A = [row[:] for row in A_]
	if isinstance(b_, list):
		b = b_[:]
	return A, b

# Function that groups several checks before proceding with the elimination algorithm
def checks(A, b):
	# check if A and b are arrays (matrices)
	if not ((isinstance(A, np.ndarray) and isinstance(b, np.ndarray)) or (isinstance(A, list) and isinstance(b, list))):
		print "Matrices should be arrays of same type (np.array or list)"
		return False
	# check if matrix A is square
	if not isSquare(A):
		print "Matrix A is not square (nxn)."
		return False
	# check if matrix b is (nx1)
	if not isVector(b):
		print "Matrix b is not a vector (nx1)."
		return False
	# check if the dimensions of A and b match
	if len(A) != len(b):
		print "Dimensions of A and b do not match!"
		return False
	# if all checks pass, we can continue
	return True

# Function that returns a boolean to check whether matrix A is square
def isSquare(A):
	# for every row in A
	for i in A:
		# if the length of the row is different than the number of rows
		if len(i) != len(A):
			# A is not square
			return False
	# if every row is the same length as the number of rows, A is square
	return True

# Function that returns a boolean to check whether matrix b is a vector (nx1)
def isVector(b):
	# for every row in b
	for i in b:
		# if b[i] is an array
		if (isinstance(i, np.ndarray) or isinstance(i, list)):
			# b is not a vector
			return False
	# if every row has only one element (ie is not an array), b is a vector
	return True

'''
# Compare this algorithm to the work done on Problem 1
A = np.arange(1, 101)
A = A.reshape((10, 10))
v = np.arange(1, 11)
b = np.ones(10)

x1 = np.linalg.solve(A, b)
x2 = np.linalg.solve(A, v)

x1_eliminate = eliminate(A, b) # no solutions or infinitely many solutions
x2_eliminate = eliminate(A, v) # no solutions or infinitely many solutions
# row 3 = 2*row 2
'''

# Tests
'''
# Simple (3x3) test
A = [[2,3,1],[4,7,5],[0,-2,2]]
b = [8,20,0]
eliminate(A,b)
#[2,1,1]
#'''
'''
# Verify function isSquare
A = np.arange(1, 101)
A = A.reshape((10, 10))
print isSquare(A)
B = np.arange(1, 81)
B = B.reshape((8, 10))
print isSquare(B)
'''
'''
# Verify isVector
A = np.ones(10)
print isVector(A)
B = np.arange(1, 101)
B = B.reshape((10, 10))
print isVector(B)
'''
'''
# Verify checks
A = np.arange(1, 101)
A = A.reshape((10, 10))
b = np.ones(10)
print checks(A, b)
B = np.arange(1, 81)
B = B.reshape((8, 10))
print checks(B, b)
c = np.ones(5)
print checks(A, c)
print checks(A, B)
'''
'''
# Verify the call to checks()
A = np.arange(1, 101)
A = A.reshape((10, 10))
b = np.ones(10)
B = np.arange(1, 81)
B = B.reshape((8, 10))
c = np.ones(5)
# uncheck the one to test
eliminate(A, b)
#eliminate(B, b)
#eliminate(A, c)
#eliminate(A, B)
'''





