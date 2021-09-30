# python3
def max_element_logic(stack, element):
    if (len(stack) == 0):
        stack.append(element)
    else:
        if (stack[-1] < element):
            stack.append(element)
        else:
            stack.append(stack[-1])
    
def max_sliding_window_fast(sequence, m):
    
    stack1, max_stack1 = [], []
    stack2, max_stack2 = [], []
    window = []

    #initate 
    for i in range(m):
        stack1.append(sequence[i])
        max_element_logic(max_stack1, sequence[i])
    window.append(max_stack1[-1])
    
    for j in range(0, len(sequence) - m):
        if len(stack2) == 0:
            while (len(stack1) != 0):
                element = stack1.pop()
                max_stack1.pop()
                stack2.append(element)
                max_element_logic(max_stack2, element)

        # increase window
        # first by removing first element in window
        stack2.pop()
        max_stack2.pop()

        # adding new element
        stack1.append(sequence[m+j])
        max_element_logic(max_stack1,sequence[m+j])

        if len(stack2) == 0:
            while (len(stack1) != 0):
                element = stack1.pop()
                max_stack1.pop()
                stack2.append(element)
                max_element_logic(max_stack2, element)

        if len(max_stack1) != 0:
            window.append(max(max_stack1[-1], max_stack2[-1]))
        else:
            window.append(max_stack2[-1])
    
    return window


def max_sliding_window_naive(sequence, m):
    maximums = []
    for i in range(len(sequence) - m + 1):
        maximums.append(max(sequence[i:i + m]))
    return maximums

if __name__ == '__main__':
    n = int(input())
    input_sequence = [int(i) for i in input().split()]
    assert len(input_sequence) == n
    window_size = int(input())

    print(*max_sliding_window_fast(input_sequence, window_size))

