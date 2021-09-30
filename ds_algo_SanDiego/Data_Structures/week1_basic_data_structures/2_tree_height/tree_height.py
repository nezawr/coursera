# python3

import sys
import threading

class QueueNode:
    def __init__(self, data):
        self.data = data 
        self.next = None

class Queue:
    def __init__(self):
        self.front = self.rear = None
        self.count = 0

    def isEmpty(self):
        return self.front == None
    
    def enQueue(self, data):
        temp = QueueNode(data)
        self.count += 1
        if self.rear == None:
            self.front = self.rear = temp
            return
        self.rear.next = temp
        self.rear = temp

    def deQueue(self):

        if self.isEmpty():
            return None
        self.count -= 1
        temp = self.front
        self.front = temp.next
        

        if (self.front == None):
            self.rear = None

        return temp.data

    
class Node:
    def __init__(self, children ,val):
        self.children = []
        self.val = val

def build_tree(n, parents):
    nodes = [Node(None, i) for i in range(n)]
    root = None
    for i in range(n):
        if parents[i] == -1:
            root = nodes[i]
        else:
            nodes[parents[i]].children.append(nodes[i])
    return root
        


def compute_height(n, parents):
    # Replace this code with a faster implementation
    root = build_tree(n, parents)

    if (root is None):
        return 0

    q = Queue()
    q.enQueue(root)
    height = 0

    while (True):

        node_count = q.count
        if node_count == 0:
            return height
        
        height += 1

        while (node_count > 0):
            node = q.deQueue()
            for i in range(len(node.children)):
                q.enQueue(node.children[i])

            node_count -= 1


def main():
    n = int(input())
    parents = list(map(int, input().split()))
    print(compute_height(n, parents))


# In Python, the default limit on recursion depth is rather low,
# so raise it here for this problem. Note that to take advantage
# of bigger stack, we have to launch the computation in a new thread.
sys.setrecursionlimit(10**7)  # max depth of recursion
threading.stack_size(2**27)   # new thread will get stack of such size
threading.Thread(target=main).start()
