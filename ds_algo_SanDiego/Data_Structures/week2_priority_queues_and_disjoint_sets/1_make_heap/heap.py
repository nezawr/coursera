#min heap

def parent(i):
    if i == 0:
        return 0
    return int((i-1)//2)

def leftChild(i):
    return 2*i + 1

def rightChild(i):
    return 2*(i+1)

def siftUp(i, H):
    while i > 0 and H[parent(i)] > H[i]:
        H[parent(i)], H[i] = H[i], H[parent(i)]

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

def buildHeap(H):
    n = len(H)
    swaps = [] 
    for i in range(int((n)//2),-1,-1):
        siftDown(i,H,swaps)

    return swaps

x = [3,4,5,7,18,2,1]
y = buildHeap(x)
print(x)
print(y)

