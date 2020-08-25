class Queue ():
    def __init__(self):
        self.queue = []
        self.size = 0

    def enqueue (self, element):
        self.queue.append(element)
        self.size += 1
    
    def dequeue (self):
        result = self.queue[0]
        if (self.size > 0):
            self.queue.pop(0)
            self.size -= 1
            return
        return result

    def first (self):
        if (self.size == 0):
            return None
        return (self.queue[0])

    def is_empty (self):
        if (self.size > 0):
            return False
        return True
    
    def queue_size (self):
        return (self.size)

def queue_functionality_test():
    q = Queue()
    print ("When queue has nothing, is it empty?:", q.is_empty())
    q.enqueue(5)
    print ("Enqueue 5 into queue:", q.queue, "\nCurrent size:", q.queue_size())
    q.enqueue(3)
    print ("Enqueue 3 into queue:", q.queue, "\nCurrent size:", q.queue_size())
    q.enqueue(1)
    print ("Enqueue 1 into queue:", q.queue, "\nCurrent size:", q.queue_size())
    q.dequeue()
    print ("Dequeue from queue:", q.queue, "\nCurrent size:", q.queue_size())
    q.dequeue()
    print ("Dequeue from queue:", q.queue, "\nCurrent size:", q.queue_size())
    q.dequeue()
    print ("Dequeue from queue:", q.queue, "\nCurrent size:", q.queue_size())
    print ("Queue is now empty, is it empty?:", q.is_empty())

if __name__ == '__main__':
    queue_functionality_test()