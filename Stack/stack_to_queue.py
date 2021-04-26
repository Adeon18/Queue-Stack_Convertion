"""
Stack to queue converter. - https://github.com/Adeon18/Queue-Stack_Convertion
"""
import copy

from arraystack import ArrayStack  # or from linkedstack import LinkedStack
from arrayqueue import ArrayQueue  # or from linkedqueue import LinkedQueue


def stack_to_queue(stack):
    """
    Convert queue to a stack
    """
    input_stack = copy.deepcopy(stack)
    output_queue = ArrayQueue()

    while True:
        try:
            output_queue.add(input_stack.pop())
        except KeyError:
            break

    return output_queue


if __name__ == "__main__":
    stack = ArrayStack()
    for i in range(10):
        stack.add(i)
    queue = stack_to_queue(stack)
    print(queue.pop())
    print(stack.pop())

    stack.add(11)
    queue.add(11)
    print(queue)
    print(stack)
