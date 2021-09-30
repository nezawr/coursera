import sys, threading

sys.setrecursionlimit(10**7) # max depth of recursion
threading.stack_size(2**25)  # new thread will get stack of such size


def inOrder(tree):
    result = []
    # Finish the implementation
    # You may need to add a new recursive method to do that
    stack = []
    curr = 0
    while stack or curr != -1:
      if curr != -1:
        stack.append(curr)
        #left
        curr = tree[curr][1]
      else:
        curr = stack.pop()
        result.append(tree[curr][0])
        #right
        curr = tree[curr][2]
    return result


def IsBinarySearchTree(tree):
  # Implement correct algorithm here
  if len(tree) == 0:
    return True
  result = inOrder(tree)
  for i in range(1, len(result)):
    if result[i-1] >= result[i]:
      return False
  return True


def main():
  nodes = int(sys.stdin.readline().strip())
  tree = []
  for i in range(nodes):
    tree.append(list(map(int, sys.stdin.readline().strip().split())))
  if IsBinarySearchTree(tree):
    print("CORRECT")
  else:
    print("INCORRECT")

threading.Thread(target=main).start()
