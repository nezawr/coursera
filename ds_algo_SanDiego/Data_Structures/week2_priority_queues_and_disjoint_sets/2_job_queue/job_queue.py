# python3

from collections import namedtuple

AssignedJob = namedtuple("AssignedJob", ["worker", "started_at"])


def assign_jobs_naive(n_workers, jobs):
    # TODO: replace this code with a faster algorithm.
    result = []
    next_free_time = [0] * n_workers
    for job in jobs:
        next_worker = min(range(n_workers), key=lambda w: next_free_time[w])
        result.append(AssignedJob(next_worker, next_free_time[next_worker]))
        next_free_time[next_worker] += job

    return result


def parent(i):
    if i == 0:
        return 0
    return int((i-1)//2)

def leftChild(i):
    return 2*i + 1

def rightChild(i):
    return 2*(i+1)

def siftDown(i, H):
    n = len(H)
    minIndex = i

    l = leftChild(i)
    if l < n and H[l][1] < H[minIndex][1]:
        minIndex = l
    if l < n and H[l][1] == H[minIndex][1] and H[l][0] < H[minIndex][0]:
        minIndex = l

    r = rightChild(i)
    if r < n and H[r][1] < H[minIndex][1]:
        minIndex = r
    if r < n and H[r][1] == H[minIndex][1] and H[r][0] < H[minIndex][0]:
        minIndex = r

    if i != minIndex:
        H[i], H[minIndex] = H[minIndex], H[i]
        siftDown(minIndex, H)

def siftUp(i, H):
    while i > 0 and H[parent(i)][1] > H[i][1]:
        H[i], H[parent(i)] = H[parent(i)], H[i]
        i = parent(i)

    while i > 0 and H[parent(i)][1] == H[i][1] and [parent(i)][0] > H[i][0]:
        H[i], H[parent(i)] = H[parent(i)], H[i]
        i = parent(i)

def insert(element, H):
    H += [element]
    siftUp(len(H) - 1, H)

def extractMin(H):
    result = H[0]
    H[0] = H[-1]
    H.pop()
    siftDown(0, H)
    return result
    
def build_heap(n):
    heap = []
    for i in range(n):
        heap.append((i,0))
    return heap

def assign_jobs(n_workers, jobs):
    heap = build_heap(n_workers)
    count = 0
    assigned = []
    while count != len(jobs):
        thread, start_time = extractMin(heap)
        assigned.append((thread, start_time))
        insert((thread, start_time + jobs[count]), heap)
        count += 1
    return assigned
        

def main():
    n_workers, n_jobs = map(int, input().split())
    jobs = list(map(int, input().split()))
    assert len(jobs) == n_jobs

    assigned_jobs = assign_jobs(n_workers, jobs)

    for job in assigned_jobs:
        print(job[0], job[1])


if __name__ == "__main__":
    main()
