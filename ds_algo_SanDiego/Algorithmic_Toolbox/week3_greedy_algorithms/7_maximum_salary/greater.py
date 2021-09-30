def isGreaterOrEqual(n, m):
    if (len(n) == len(m)):
        for i in range(len(n)):
            if int(n[i]) > int(m[i]):
                return False
            elif int(n[i]) < int(m[i]):
                return True
            else:
                continue
        return True
    elif (len(n) > len(m)):
        for i in range(len(m)):
            if int(n[i]) > int(m[i]):
                return False
            elif int(n[i]) < int(m[i]):
                return True
            else:
                continue
        for i in range(len(n) - len(m)):
            if int(n[i + len(m)]) > int(m[-1]):
                return False
            elif int(n[i + len(m)]) < int(m[-1]):
                return True
            else:
                continue
        return True
    else:
        for i in range(len(n)):
            if int(n[i]) > int(m[i]):
                return False
            elif int(n[i]) < int(m[i]):
                return True
            else:
                continue
        for i in range(len(m) - len(n)):
            if int(n[-1]) > int(m[i + len(n)]):
                return False
            elif int(n[-1]) < int(m[i + len(n)]):
                return True
            else:
                continue
        return True