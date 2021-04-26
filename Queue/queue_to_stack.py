"""
Queue to stack converter. - https://github.com/Adeon18/Queue-Stack_Convertion
"""
import copy
from arrayqueue import ArrayQueue  # or from linkedqueue import LinkedQueue
from arraystack import ArrayStack  # or from linkedstack import LinkedStack


def queue_to_stack(queue):
    """
    Convert a queue to a stack using another stack
    """
    input_queue = copy.deepcopy(queue)
    output_stack = ArrayStack()
    converter_stack = ArrayStack()
    # Get the queue items
    while True:
        try:
            converter_stack.push(input_queue.pop())
        except KeyError:
            break
    # Reverse the queue
    while True:
        try:
            output_stack.push(converter_stack.pop())
        except KeyError:
            break

    return output_stack


if __name__ == "__main__":
    queue = ArrayQueue()
    for i in range(10):
        queue.add(i)
    stack = queue_to_stack(queue)
    print(queue)
    print(stack)
    print(stack.pop())
    print(queue.pop())

    stack.add(11)
    queue.add(11)
    print(queue)
    print(stack)
