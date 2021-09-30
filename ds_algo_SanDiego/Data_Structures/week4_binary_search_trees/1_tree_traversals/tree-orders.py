# python3

import sys, threading
sys.setrecursionlimit(10**6) # max depth of recursion
threading.stack_size(2**27)  # new thread will get stack of such size

class TreeOrders:
  def read(self):
    self.n = int(sys.stdin.readline())
    self.key = [0 for i in range(self.n)]
    self.left = [0 for i in range(self.n)]
    self.right = [0 for i in range(self.n)]
    for i in range(self.n):
      [a, b, c] = map(int, sys.stdin.readline().split())
      self.key[i] = a
      self.left[i] = b
      self.right[i] = c

  def inOrder(self):
    self.result = []
    # Finish the implementation
    # You may need to add a new recursive method to do that
    stack = []
    curr = 0
    while stack or curr != -1:
      if curr != -1:
        stack.append(curr)
        curr = self.left[curr]
      else:
        curr = stack.pop()
        self.result.append(self.key[curr])
        curr = self.right[curr]
    return self.result

  

  def preOrder(self):
    self.result = []
    # Finish the implementation
    # You may need to add a new recursive method to do that
    stack = []
    stack.append(0)
    
    while stack:
      curr = stack.pop()
      self.result.append(self.key[curr])

      if self.right[curr] != -1:
        stack.append(self.right[curr])

      if self.left[curr] != -1:
        stack.append(self.left[curr])
                   
    return self.result

  def postOrder(self):
    self.result = []
    # Finish the implementation
    # You may need to add a new recursive method to do that
    stack = []
    out = []
    stack.append(0)
    while stack:
      curr = stack.pop()
      out.append(self.key[curr])
 
        # push the left and right child of the popped node into the stack
      if self.left[curr] != -1:
            stack.append(self.left[curr])
 
      if self.right[curr] != -1:
            stack.append(self.right[curr])
    
    while out:
        self.result.append(out.pop())
        
    return self.result

def main():
	tree = TreeOrders()
	tree.read()
	print(" ".join(str(x) for x in tree.inOrder()))
	print(" ".join(str(x) for x in tree.preOrder()))
	print(" ".join(str(x) for x in tree.postOrder()))

threading.Thread(target=main).start()
