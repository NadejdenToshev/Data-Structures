class Queue:
    def __init__(self):
        self.items = []

    def enqueue(self, item):
        self.items.append(item)

    def dequeue(self):
        if not self.is_empty():
            return self.items.pop(0)
        else:
            raise IndexError("dequeue from empty queue")

    def peek(self):
        if not self.is_empty():
            return self.items[0]
        else:
            raise IndexError("peek from empty queue")

    def is_empty(self):
        return len(self.items) == 0

    def size(self):
        return len(self.items)

    def display(self):
        print(self.items)

# Example usage
if __name__ == "__main__":
    queue = Queue()

    # Enqueue items into the queue
    queue.enqueue(1)
    queue.enqueue(2)
    queue.enqueue(3)

    # Display the queue
    print("Queue after enqueues:")
    queue.display()

    # Peek at the front item
    print("Front item is:", queue.peek())

    # Dequeue an item from the queue
    print("Dequeued item:", queue.dequeue())

    # Display the queue after dequeuing
    print("Queue after dequeue:")
    queue.display()

    # Check if the queue is empty
    print("Is queue empty?", queue.is_empty())

    # Get the size of the queue
    print("Queue size:", queue.size())





