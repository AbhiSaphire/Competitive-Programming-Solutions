# ~~Abhishek K. Singh~~
# Solved in 2 days 16 hours
# A simple problem if you know about Markov Chains and Absorbing Markov Chain Probabilities, certainly I didn't even have a clue.
# It took me 5 to 6 hours just understand what the question really is and what is needed to be returned.
# I spend a whole day learning about Finite mathematics, Markov Chains and absorbing Markov chains.
# I recommend watching markov chains from edureka(Youtube), Absorbing Markov chain from PatrickJMT(Youtube) and absorbing markov chain lecture14 from Dartmouth Mathematics Lecture series(math.dartmouth.edu).
# 
# After that the approach is very simple you just have to follow the steps of AMC to find probabilties.
# ~~~Steps:~~~
# --> Disect the matrix to get terminal elements and non terminal elements, arrange matrix to get fractional elements
# --> Calculate F matix by (I - Q)^(-1)
# 			--> I is identity matrix (same size of Q)
# 			--> Q is submatrix of P(original matrix given i.e, m)
# --> Calculate F*R
# 			--> Previously obtained matrix
# 			--> R is submatrix of P(original matrix given i.e, m)
# --> Select first row of F*R matrix which is the individual probabilities (append numerators in returner list)
# --> Calculate the common denominator of probabilities (append common denominator in returner list)
# --> Return returner

from fractions import Fraction, gcd

def convert_to_fractions(m):
	for i, row in enumerate(m):
		sum_row = sum(row)
		if sum_row == 0:
			m[i][i] = 1
		else:
			for j, col in enumerate(row):
				m[i][j] = Fraction(col, sum_row)

def create_Q_and_R(m, rows, cols):
	matrix = []
	for row in rows:
		current_row_values = []
		for col in cols:
			current_row_values.append(m[row][col])
		matrix.append(current_row_values)
	return matrix

def creatematrix(row, col):
	matrix = []
	for row in range(0, row):
		matrix += [[0] * col]
	return matrix

def subtract_from_I(q, non_terminal):
	identity = creatematrix(len(non_terminal), len(non_terminal))

	for i in range(0, len(identity)):
		identity[i][i] = Fraction(1, 1)

	for i in range(0, len(identity)):
		for j in range(0, len(identity)):
			q[i][j] = identity[i][j] - q[i][j]

def transposeMatrix(m):
    return map(list,zip(*m))

def getMatrixMinor(m,i,j):
    return [row[:j] + row[j+1:] for row in (m[:i]+m[i+1:])]

def getMatrixDeternminant(m):
    if len(m) == 2:
        return m[0][0]*m[1][1]-m[0][1]*m[1][0]

    determinant = 0
    for c in range(len(m)):
        determinant += ((-1)**c)*m[0][c]*getMatrixDeternminant(getMatrixMinor(m,0,c))
    return determinant

def invertmatrix(m):
    determinant = getMatrixDeternminant(m)
    #special case for 2x2 matrix:
    if len(m) == 2:
        return [[m[1][1]/determinant, -1*m[0][1]/determinant], [-1*m[1][0]/determinant, m[0][0]/determinant]]

    #find matrix of cofactors
    cofactors = []
    for r in range(len(m)):
        cofactorRow = []
        for c in range(len(m)):
            minor = getMatrixMinor(m,r,c)
            cofactorRow.append(((-1)**(r+c)) * getMatrixDeternminant(minor))
        cofactors.append(cofactorRow)
    cofactors = transposeMatrix(cofactors)
    for r in range(len(cofactors)):
        for c in range(len(cofactors)):
            cofactors[r][c] = cofactors[r][c]/determinant
    return cofactors

def multiplymatrices(y, x):
	if len(x) == len(y[0]):
		c = creatematrix(len(y), len(x[0]))
		for row in xrange(len(y)):
			for col in xrange(len(x[0])):
				dot_product = Fraction(0, 1)
				for i in xrange(len(y[0])):
					dot_product += y[row][i]*x[i][col]
				c[row][col] = dot_product
	return c

def lcm(lst):
	lcm = lst[0].denominator
	for i in lst[1:]:
		lcm = lcm*i.denominator/gcd(lcm, i.denominator)
	return lcm

def solution(m):
	terminal = []
	non_terminal = []
	returner =[]
	for i, row in enumerate(m):
		if sum(row) == 0:
			terminal.append(i)
		else:
			non_terminal.append(i)

	if len(terminal) == 1:
		return [1, 1]

	convert_to_fractions(m)
	q = create_Q_and_R(m, non_terminal, non_terminal)
	r = create_Q_and_R(m, non_terminal, terminal)

	subtract_from_I(q, non_terminal)
	inverse = invertmatrix(q)
	inverse_multiply_r = multiplymatrices(inverse, r)
	common_denominator = lcm(inverse_multiply_r[0])

	returner = [item.numerator * common_denominator / item.denominator for item in inverse_multiply_r[0]]
	returner.append(common_denominator)
	return returner

print(solution([
			[0, 1, 0, 0, 0, 1],
			[4, 0, 0, 3, 2, 0],
			[0, 0, 0, 0, 0, 0], 
			[0, 0, 0, 0, 0, 0], 
			[0, 0, 0, 0, 0, 0], 
			[0, 0, 0, 0, 0, 0]
		]))

print(solution([
			[0, 2, 1, 0, 0], 
			[0, 0, 0, 3, 4], 
			[0, 0, 0, 0, 0], 
			[0, 0, 0, 0,0], 
			[0, 0, 0, 0, 0]
		]))

print(solution([
			[0, 0, 0, 0], 
			[1, 1, 1, 1],
			[1, 1, 1, 1],
			[1, 1, 1, 1]
		]))

print(solution([
            [1, 1, 0, 1],
            [1, 1, 0, 0],
            [0, 0, 0, 0],
            [0, 0, 0, 0]
        ]))

print(solution([
            [0, 1, 0, 0, 0, 1],
            [1, 0, 0, 1, 1, 0],
            [0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0]
        ]))

print(solution([
            [0, 2, 1, 0, 0],
            [0, 0, 0, 3, 4],
            [0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0]
        ]))
