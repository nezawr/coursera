def fast_count_segments(starts, ends, points):
    cnt = {}
    segments_num = 0

    listpoints = [(x,'l') for x in starts]
    listpoints += [(x,'p') for x in points]
    listpoints += [(x, 'r') for x in ends]

    listpoints.sort()

    for p in listpoints:
        if p[1] == 'l':
            segments_num += 1
        elif p[1] == 'r':
            segments_num -= 1
        else:
            cnt[p[0]] = segments_num

    return [cnt[x] for x in points]
    
    return cnt

assert fast_count_segments([], [], [1]) == [0]

assert fast_count_segments([-1000], [1000], [-100,100,0]) == [1,1,1]

assert fast_count_segments([0,-3,7], [5,2,10], [1,6]) == [2,0]

print(fast_count_segments([0,1,2],[10,10,10], [1,2,10]))
