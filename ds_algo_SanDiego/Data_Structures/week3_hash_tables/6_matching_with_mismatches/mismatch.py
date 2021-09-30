def find_mismatches(s, t, k):
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
    if count <= k:
        return True
    return False


print(find_mismatches('12345', '13265', 3))



for line in sys.stdin.readlines():
	k, t, p = line.split()
	ans = solve(int(k), t, p)
	print(len(ans), *ans)