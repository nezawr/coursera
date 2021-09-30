# python3

def read_input():
    return (input().rstrip(), input().rstrip())

def print_occurrences(output):
    print(' '.join(map(str, output)))

def get_occurrences(pattern, text):
    return [
        i 
        for i in range(len(text) - len(pattern) + 1) 
        if text[i:i + len(pattern)] == pattern
    ]

def _hash_func(s, _prime, _multiplier):
        ans = 0
        for c in reversed(s):
            ans = (ans * _multiplier + ord(c)) % _prime
        return ans 

def precompute_hashes(text, pattern_len, _prime, _multiplier):
    H = [-1 for i in range(len(text) - pattern_len + 1)]
    S = text[len(text) - pattern_len:]
    H[-1] = _hash_func(S, _prime, _multiplier)
    y = 1
    for i in range(pattern_len):
        y = (y * _multiplier) % _prime
    for i in range(len(text) - pattern_len - 1, -1, -1):
        H[i] = (_multiplier*H[i+1] + ord(text[i]) - y*ord(text[i+pattern_len])) % _prime
    return H

def Rabin_Karp(pattern, text):
    _prime, _multiplier = 1000000007, 263
    result = []
    pattern_hash = _hash_func(pattern, _prime, _multiplier)
    H = precompute_hashes(text, len(pattern),_prime, _multiplier)
    for i in range(len(text) - len(pattern) + 1):
        if H[i] != pattern_hash:
            continue
        if text[i:i+len(pattern)] == pattern:
            result.append(i)
    return result



if __name__ == '__main__':
    print_occurrences(Rabin_Karp(*read_input()))

