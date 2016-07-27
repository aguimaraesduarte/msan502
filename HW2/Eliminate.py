import numpy as np
import sys

# Function that will perform the elimination algorithm to solve A_*x = b_
def eliminate(A_, b_):
	# perform checks to see if we can proceed with the algorithm
	if not checks(A_, b_):
		sys.exit(0)

	# Make a copy of A and b, so as to not modify the original matrices
	A, b = makeCopy(A_, b_)

	# for consistency, transform the first row values to floats
	A[0] = np.dot(1.0, A[0])

	# n is the number of rows
	n = A.shape[0]
	# m is the number of columns
	m = A.shape[1]

	# save the pivots if we need them
	# we will save a tuple (x, y) where x=pivot value, y=pivot index
	pivots = []

	# save the free variables (col number)
	free = []

	# i will go through the rows
	i = 0
	# while we haven't reached the bottom of A
	while i < n:
		# expectedPivot is the element on the diagonal for the current row
		expectedPivot = A[i][i]
		# firstNonZero is the actual first non-zero value on the current row
		firstNonZero = findFirstNonZero(A[i])

		# if all the values are 0, we will try permutation
		if not firstNonZero:
			# first, check solvability
			checkSolvability(b, i)
			# j = number of the row to permute
			j = findPermutationRow(A, i, n)
			# if no possible permutation rows
			if not j:
				# do nothing with this row and go to the next one
				i += 1
				continue
			# if we found a permutation row
			else:
				# method to switch rows i and j
				# two arrays because n and m may differ
				perm_array_A = np.array(range(n))
				perm_array_A[i], perm_array_A[j] = j, i
				perm_array_b = np.array(range(m))
				perm_array_b[i], perm_array_b[j] = j, i
				A = A[perm_array_A,:]
				b = b[perm_array_b]
				# we need to go through the row again, so we don't increment i
				continue
		# if firstNonZero found a value
		else:
			# if it's the same as expectedPivot
			if expectedPivot == firstNonZero:
				pivot = expectedPivot
				# add the pivot to the pivots list
				# (value, row_number)
				pivots.append((pivot, i))
				# for all other rows, perform elimination
				for ii in range(i+1, n):
					# calculate the multiplier
					multiplier = 1.0*A[ii][i]/pivot
					# replace the row (don't forget to update matrix b too!)
					A[ii] = A[ii] - np.dot(multiplier, A[i])
					b[ii] = b[ii] - np.dot(multiplier, b[i])
					# replace with 0.0 to prevent issues with approximations
					A[ii][i] = 0.0
				# go to the next row
				i += 1
				continue
			# if it's not the same as expectedPivot
			else:
				# j = number of the row to permute
				j = findPermutationRow(A, i, n)
				# if no possible permutation rows
				if not j:
					# add i to the free variables array
					free.append(i)
					# keep this row, and pivot=firstNonZero
					pivot = firstNonZero
					# find the index of the pivot
					k = np.where(A[i] == pivot)[0][0]
					# add the pivot to the pivots list
					pivots.append((pivot, k))
					# for all other rows, perform elimination
					for ii in range(i+1, n):
						# calculate the multiplier
						multiplier = 1.0*A[ii][k]/pivot
						# replace the row (don't forget to update matrix b too!)
						A[ii] = A[ii] - np.dot(multiplier, A[i])
						b[ii] = b[ii] - np.dot(multiplier, b[i])
						# replace with 0.0 to prevent issues with approximations
						A[ii][i] = 0.0
					# go to the next row
					i += 1
					continue
				# if we found a permutation row
				else:
					# method to switch rows i and j
					# two arrays because n and m may differ
					perm_array_A = np.array(range(n))
					perm_array_A[i], perm_array_A[j] = j, i
					perm_array_b = np.array(range(m))
					perm_array_b[i], perm_array_b[j] = j, i
					A = A[perm_array_A,:]
					b = b[perm_array_b]
					# we need to go through the row again, so we don't increment i
					continue
	
	# If we got to this point, we have an upper triangular matrix.

	# ss: number of special solutions
	ss = m-len(pivots)
#	print "There are %d special solutions.\n" % ss

	# if no special solutions, then the system is perfect
	# we can do back substitution
	if ss == 0:
#		print "There is only one solution.\n"
		res = backsubstitution(A, b)
	# if there are special solutions, since the program would have exited
	# if there were no solutions, then we must have infinitely many solutions
	else:
		print "There are infinitely many solutions.\n"
		# calculate solutions here
# TODO: find particular solution
# TODO: find special solutions
		res = []

	# Print the original matrix, upper triangular matrix and the solution vector
	
#	print "Original matrix A:\n", A_
#	print "Original matrixb:\n", b_
#	print "\nUpper triangle R:\n", A
#	print "New matrix d:\n", b
#	print "\nPivots matrix D:\n", pivots
#	print "Free veriables:\n", free
#	print "\nSolution vector X:\n", res

	# return the vector with the solution (x)
	return res

# Function that checks if the system is solvable (no 0=c)
def checkSolvability(b, i):
	# if b[i] is not 0, then there are no solutions
	if b[i] != 0:
		print "Failure! There are no solutions."
		sys.exit(0)

# Function that finds a suitable row for permutation
def findPermutationRow(A, i, n):
	# we don't need to look for rows above or == i
	for row_index in range(i+1, n):
		# get the first non-zero value
		value = findFirstNonZero(A[row_index])
		# if 0 or False
		if not value:
			# go to the next row
			continue
		# if not, get the index of the element. If it's at the position we want, keep it
		else:
			if np.where(A[row_index] == value)[0][0] == i:
				return row_index
			# if it's not at the position we want, go to the next row
			else:
				continue
	# if we reached the last row and found no candidate, return False
	return False

# Function that performs backward substitution. T is an upper triangular matrix
def backsubstitution(T, b):
	# n is the number of rows
	n = T.shape[0]
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
def findFirstNonZero(row):
	# for every value in the row
	for value in row:
		# if the current value is not 0
		if not np.isclose(value, 0):
		#if abs(value) > 1.0e-3:
			# return the first non-zero value
			return value
	# if we run through all values in the row and cannot find a 0,
	# there are no non-zero values in the row. 
	return False

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
	# check if matrix b is (nx1)
	if not isVector(b):
		print "Matrix b is not a vector (nx1)."
		return False
	# check if ncol of A and nrow of b are equal
	if A.shape[1] != b.shape[0]:
		print "Dimensions of A and b do not match!"
		return False
	# if A has less rows than columns, verify that all entries after n in b are 0
	if not isSolvable(A, b):
		print "Failure! There are no solutions."
		return False
	# if all checks pass, we can continue
	return True

# Function that returns a boolean to check whether the system is solvable when n<m
def isSolvable(A, b):
	# n is the number of rows
	n = A.shape[0]
	# m is the number of columns
	m = A.shape[1]
	# if there are "not enough" rows
	if n < m:
		# for the indexes after n
		for i in range(n, m):
			# if b[i] is not zero, the system is not solvable
			if b[i] != 0:
				return False
	# all values of b after n are 0, we can continue
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
A = np.array([[1,3,0,2],
	           #[0,0,1,4],
	           [1,3,0,3],
	           [1,4,1,6]])
b = np.array([1,6,7,0])
#A = np.array([[1,1,2,3],
#	          [2,2,8,10],
#	          [3,3,10,13]])
#b = np.array([0,0,0,0])
eliminate(A, b)
'''
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
A = np.array([[2,3,1],[4,7,5],[-4,3,1]])
b = np.array([8,20,2])
print eliminate(A,b)
#[2,1,1]
#'''
'''
# Verify isVector
A = np.ones(10)
print isVector(A)
B = np.arange(1, 101)
B = B.reshape((10, 10))
print isVector(B)
#'''
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
#'''
'''
# Verify the call to checks()
A = np.arange(1, 101)
A = A.reshape((10, 10))
b = np.ones(10)
B = np.arange(1, 81)
B = B.reshape((8, 10))
c = np.ones(5)
# uncheck the one to test
eliminate(A, b) #infinitely many solutions
#eliminate(B, b) #no solutions
#eliminate(A, c) #dimensions don't match
#eliminate(A, B) #b is not a vector
#'''