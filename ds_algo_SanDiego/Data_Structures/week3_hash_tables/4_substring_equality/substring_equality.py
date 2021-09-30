# python3

import sys

class Solver:
	def __init__(self, s):
		self.s = s
		self._prime1, self._prime2 = 10**9 + 7, 10**9 + 9
		self._multiplier = 257
		self.H1 = precompute_hashes(s, self._prime1, self._multiplier)
		self.H2 = precompute_hashes(s, self._prime2, self._multiplier)
		
	def ask(self, a, b, l):
		return AreEqual(self.H1, self.H2, self._prime1, self._prime2, self._multiplier, a, b, l)

def precompute_hashes(s, _prime, _multiplier):
	hash_table = [0 for _ in range(len(s) + 1)]
	for i in range(1, len(s) + 1):
		hash_table[i] = (hash_table[i-1] * _multiplier + ord(s[i - 1])) % _prime
	return hash_table

def HashValue(hash_table, _prime, _multiplier, start, length):
	y = pow(_multiplier, length, _prime)
	hash_value = (hash_table[start + length] - y * hash_table[start]) % _prime
	return hash_value


def AreEqual(table1, table2, prime1, prime2, x, a, b, l):
    a_hash1 = HashValue(table1, prime1, x, a, l)
    a_hash2 = HashValue(table2, prime2, x, a, l)
    b_hash1 = HashValue(table1, prime1, x, b, l)
    b_hash2 = HashValue(table2, prime2, x, b, l)
    if a_hash1 == b_hash1 and a_hash2 == b_hash2:
        return True
    else:
        return False

s = sys.stdin.readline()
q = int(sys.stdin.readline())
solver = Solver(s)
for i in range(q):
	a, b, l = map(int, sys.stdin.readline().split())
	print("Yes" if solver.ask(a, b, l) else "No")
