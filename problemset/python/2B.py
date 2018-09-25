n = int(input())

A = [[int(x) for x in input().split()] for i in range(n)]

zx, zy = -1,-1

# note that the only way to get a zero is if we multiply by a number
# that has at least one factor of 2 and 5, so we will want to count
# these with count_facs(mat[i][j], 2) or count_facs(mat[i][j], 5)
def count_facs(x,f):
	count = 0
	while x > 0 and x % f == 0:
		x /= f
		count += 1
	return count

def print_results(counts):
	print(counts[n-1][n-1])

	pos = max(1,(n-1)**2 - 1)
	path = [''] * (pos + 1)
	i,j = n-1, n-1
	while i + j > 0:
		if i > 0 and j > 0:
			if counts[i][j-1] < counts[i-1][j]:
				path[pos] = "R"
				j -= 1
			else:
				path[pos] = "D"
				i -= 1
		elif i == 0:
			path[pos] = "R"
			j -= 1
		else:
			path[pos] = "D"
			i -= 1
		pos -= 1
	print(''.join(path))


# the following function will find for each i and j the path in which
# the number f shows up in the product the least amount of times
# we will call it twice for 2 and 5, since these are the only ways
# we can get 10, the better of these two paths will be the winner
def dp(f):
	counts = [[None for _ in range(n)] for _ in range(n)]

	for i in range(n):
		for j in range(n):
			curr_count = count_facs(A[i][j], f)
			if i == 0 and j > 0:
				counts[i][j] = counts[0][j-1] + curr_count
			elif i > 0 and j == 0:
				counts[i][j] = counts[i-1][0] + curr_count
			elif i > 0 and j > 0:
				counts[i][j] = min(counts[i][j-1], counts[i-1][j]) + curr_count
			else:
				counts[0][0] = curr_count

	return counts

counts2 = dp(2)
counts5 = dp(5)
if counts2[n-1][n-1] < counts5[n-1][n-1]:
	print_results(counts2)
else:
	print_results(counts5)
