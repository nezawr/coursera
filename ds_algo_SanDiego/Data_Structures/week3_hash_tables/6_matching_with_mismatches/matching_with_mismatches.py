# python3

import sys
from collections import deque

class Solver:
	def __init__(self, s, t):
		self.s = s
		self.t = t
		self._prime1, self._prime2 = 10**9 + 7, 10**9 + 9
		self._multiplier = 257
		self.H1s = precompute_hashes(s, self._prime1, self._multiplier)
		#self.H2s = precompute_hashes(s, self._prime2, self._multiplier)
		self.H1t = precompute_hashes(t, self._prime1, self._multiplier)
		#self.H2t = precompute_hashes(t, self._prime2, self._multiplier)

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
		#val2 = HashValue(solver.H2s, solver._prime2, solver._multiplier, start, length)
	else:
		val1 = HashValue(solver.H1t, solver._prime1, solver._multiplier, start, length)
		#val2 = HashValue(solver.H2t, solver._prime2, solver._multiplier, start, length)
	#return (val1, val2)
	return val1

def hash_equality_check(solver, text_start, pattern_start, length):
	#t_1, t_2 = AllHashValues(solver, text_start, length, True)
	#p_1, p_2 = AllHashValues(solver, pattern_start, length, False)
	t_1 = AllHashValues(solver, text_start, length, True)
	p_1= AllHashValues(solver, pattern_start, length, False)
	return True if t_1 == p_1 else False

def find_mismatches(k, solver, text_segment ,pattern ,text_loc_index):
	# Assume len(t) == len(p)
	count = 0
	low = 0
	for i in range(k+1):
		high = len(text_segment) - 1
		while low<=high:
			mid = (high + low)//2
			if text_segment[mid] == pattern[mid]:
				if hash_equality_check(solver, text_loc_index + low, low, mid - low + 1):
					low = mid + 1
				else: 
					high = mid - 1
			elif text_segment[mid] != pattern[mid]:
				if hash_equality_check(solver, text_loc_index + low, low, mid - low):
					count += 1
					low = mid + 1
				else:
					high = mid - 1

	return True if count <= k else False
    	

def find_mismatches_naive(s, t, k):
    low = 0
    count = 0
    for i in range(k+1): 
        high = len(s) - 1
        while low <= high:
            mid = (low + high)//2
            if s[mid] == t[mid]:
                if s[low:mid+1] == t[low:mid+1]:
                    low = mid + 1
                else:
                    high = mid - 1
            elif s[mid] != t[mid]:
                if s[low:mid] == t[low:mid]:
                    count += 1
                    low = mid + 1
                else:
                    high = mid - 1
    return True if count <= k else False

def solve(k, text, pattern):

	results = []
	solver = Solver(text, pattern)

	for i in range(len(text) - len(pattern) + 1):

		if find_mismatches(k, solver, text[i:i+len(pattern)], pattern, i):
		#if find_mismatches_naive(text[i:i+len(pattern)], pattern, k):
			results.append(i)
	
	return results


for line in sys.stdin.readlines():
	k, t, p = line.split()
	ans = solve(int(k), t, p)
	print(len(ans), *ans)