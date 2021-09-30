# Uses python3
import sys
from collections import namedtuple

Segment = namedtuple('Segment', 'start end')

def optimal_points(segments):
    points = []
    #write your code here
    segments = sorted(segments, key=lambda x: x.end)
    index = 0
    while (index < len(segments)):
        points.append(segments[index].end)
        cur = index
        while (cur < len(segments) and segments[cur].start <= (segments[index].end) <= segments[cur].end):
            cur += 1
        index = cur

    return points

if __name__ == '__main__':
    input = sys.stdin.read()
    n, *data = map(int, input.split())
    segments = list(map(lambda x: Segment(x[0], x[1]), zip(data[::2], data[1::2])))
    points = optimal_points(segments)
    print(len(points))
    print(*points)
