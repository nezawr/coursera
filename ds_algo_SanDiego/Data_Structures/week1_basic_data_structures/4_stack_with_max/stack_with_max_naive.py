#python3
import sys

class StackWithMax():
    def __init__(self):
        self.__stack = []

    def Push(self, a):
        self.__stack.append(a)

    def Pop(self):
        assert(len(self.__stack))
        self.__stack.pop()

    def Max(self):
        assert(len(self.__stack))
        return max(self._stack)


if __name__ == '__main__':
    stack = StackWithMax()
    max_stack = StackWithMax()

    num_queries = int(sys.stdin.readline())
    for _ in range(num_queries):
        query = sys.stdin.readline().split()

        if query[0] == "push":
            stack.Push(int(query[1]))
            if (len(max_stack._StackWithMax__stack) == 0):
                max_stack.Push(int(query[1]))
            else:
                if (max_stack._StackWithMax__stack[-1] < int(query[1])):
                    max_stack.Push(int(query[1]))
                else:
                    max_stack.Push(max_stack._StackWithMax__stack[-1])
        elif query[0] == "pop":
            stack.Pop()
            max_stack.Pop()
        elif query[0] == "max":
            print(max_stack._StackWithMax__stack[-1])
        else:
            assert(0)
