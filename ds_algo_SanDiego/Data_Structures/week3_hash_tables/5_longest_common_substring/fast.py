# python3

import sys
from collections import namedtuple

Answer = namedtuple('answer_type', 'i j len')
class Solver:
	def __init__(self, s, t):
		self.s = s
		self.t = t
		self._prime1, self._prime2 = 10**9 + 7, 10**9 + 9
		self._multiplier = 257
		self.H1s = precompute_hashes(s, self._prime1, self._multiplier)
		self.H2s = precompute_hashes(s, self._prime2, self._multiplier)
		self.H1t = precompute_hashes(t, self._prime1, self._multiplier)
		self.H2t = precompute_hashes(t, self._prime2, self._multiplier)

def precompute_hashes(s, _prime, _multiplier):
	hash_table = [0 for _ in range(len(s) + 1)]
	for i in range(1, len(s) + 1):
		hash_table[i] = (hash_table[i-1] * _multiplier + ord(s[i - 1])) % _prime
	return hash_table

def HashValue(hash_table, _prime, _multiplier, start, length):
	y = pow(_multiplier, length, _prime)
	hash_value = (hash_table[start + length] - y * hash_table[start]) % _prime
	return hash_value

def AllHashValues(solver, start, length, bool):
	if bool:
		val1 = HashValue(solver.H1s, solver._prime1, solver._multiplier, start, length)
		val2 = HashValue(solver.H2s, solver._prime2, solver._multiplier, start, length)
	else:
		val1 = HashValue(solver.H1t, solver._prime1, solver._multiplier, start, length)
		val2 = HashValue(solver.H2t, solver._prime2, solver._multiplier, start, length)
	return (val1, val2)

def AreEqual(table1, table2, prime1, prime2, x, a, b, l):
    a_hash1 = HashValue(table1, prime1, x, a, l)
    a_hash2 = HashValue(table2, prime2, x, a, l)
    b_hash1 = HashValue(table1, prime1, x, b, l)
    b_hash2 = HashValue(table2, prime2, x, b, l)
    if a_hash1 == b_hash1 and a_hash2 == b_hash2:
        return True
    else:
        return False

def hash_checker(t_hash_tup, s_values):
	val1 = t_hash_tup[0] in s_values[0]
	val2 = t_hash_tup[1] in s_values[1]
	return val1 and val2

def get_hash_values(s, length, solver):
	hash1, hash2 = {}, {}
	for i in range(0, len(s) - length + 1):
		val1, val2 = AllHashValues(solver, i, length, True)
		hash1[val1], hash2[val2] = i, i
	return (hash1, hash2)

def get_possible_match(s, t, length, solver):
	#returns a tuple of 3 hashes tables.
	s_values = get_hash_values(s, length, solver)
	for i in range(0, len(t) - length + 1):
		hash_tup = AllHashValues(solver, i, length, False)
		if hash_checker(hash_tup, s_values):
			return Answer(s_values[0][hash_tup[0]], i, length)
	return Answer(0,0,0)


def solve(s, t):
	ans = Answer(0, 0, 0)
	high = len(s) if len(s) <= len(t) else len(t)
	low = 1
	solver = Solver(s,t)
	while low <= high:
		mid = (high + low)//2
		#what happens if there is a mutual substring of length mid
		temp_ans = get_possible_match(s, t, mid, solver)
		if temp_ans[2] != 0:
			ans = temp_ans
			low = mid + 1
		else:
			high = mid - 1
	return ans

for line in sys.stdin.readlines():
	s, t = line.split()
	ans = solve(s, t)
	print(ans.i, ans.j, ans.len)