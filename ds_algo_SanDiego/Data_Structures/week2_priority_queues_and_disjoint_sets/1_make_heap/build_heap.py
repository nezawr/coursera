# python3

def parent(i):
    if i == 0:
        return 0
    return int((i-1)//2)

def leftChild(i):
    return 2*i + 1

def rightChild(i):
    return 2*(i+1)

def siftDown(i, H, swaps):
    n = len(H)
    minIndex = i
    l = leftChild(i)
    if l < n and H[l] < H[minIndex]:
        minIndex = l
    r = rightChild(i)
    if r < n and H[r] < H[minIndex]:
        minIndex = r
    if i != minIndex:
        swaps.append((i, minIndex))
        H[i], H[minIndex] = H[minIndex], H[i]
        siftDown(minIndex, H, swaps)


def build_heap(H):
    n = len(H)
    swaps = [] 
    for i in range(int((n)//2),-1,-1):
        siftDown(i,H,swaps)

    return swaps


def main():
    n = int(input())
    data = list(map(int, input().split()))
    assert len(data) == n

    swaps = build_heap(data)

    print(len(swaps))
    for i, j in swaps:
        print(i, j)


if __name__ == "__main__":
    main()
