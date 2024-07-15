class Stack:
    def __init__(self):
        self.items = []

    def push(self, item):
        self.items.append(item)

    def pop(self):
        if not self.is_empty():
            return self.items.pop()
        else:
            raise IndexError("pop from empty stack")

    def peek(self):
        if not self.is_empty():
            return self.items[-1]
        else:
            raise IndexError("peek from empty stack")

    def is_empty(self):
        return len(self.items) == 0

    def size(self):
        return len(self.items)

    def display(self):
        print(self.items)

# Example usage
if __name__ == "__main__":
    stack = Stack()

    # Push items onto the stack
    stack.push(1)
    stack.push(2)
    stack.push(3)
    stack.push(4)

    # Display the stack
    print("Stack after pushes:")
    stack.display()

    # Peek at the top item
    print("Top item is:", stack.peek())

    # Pop an item off the stack
    print("Popped item:", stack.pop())

    # Display the stack after popping
    print("Stack after pop:")
    stack.display()

    # Check if the stack is empty
    print("Is stack empty?", stack.is_empty())

    # Get the size of the stack
    print("Stack size:", stack.size())

