# python3

from collections import namedtuple

Bracket = namedtuple("Bracket", ["char", "position"])


def are_matching(left, right):
    return (left + right) in ["()", "[]", "{}"]


def find_mismatch(text):
    opening_brackets_stack = []
    index_stack = []
    for i, next in enumerate(text):
        if next in "([{":
            opening_brackets_stack.append(next)
            index_stack.append(i)

        if next in ")]}":
            if (len(opening_brackets_stack) == 0):
                return i + 1
            top = opening_brackets_stack.pop()
            index_stack.pop()
            if not are_matching(top,next):
                return i + 1
    bol = len(opening_brackets_stack) == 0
    if bol:
        return 'Success'
    else:
        return index_stack.pop() + 1


def main():
    text = input()
    mismatch = find_mismatch(text)
    # Printing answer, write your code here
    print(mismatch)

if __name__ == "__main__":
    main()
