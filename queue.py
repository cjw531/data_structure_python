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

class TwoStackQueue ():
    def __init__ (self):
        self.inbox = []
        self.outbox = []
        self.size = 0

    def enqueue (self, element):
        self.inbox.append(element)
        self.size += 1
    
    def dequeue (self):
        if (self.size > 0):
            # inbox -> outbox: now outbox's top is first of the queue
            while (len(self.inbox) > 0):
                self.outbox.append(self.inbox[len(self.inbox) - 1])
                self.inbox.pop(len(self.inbox) - 1)
            
            result = self.outbox[len(self.outbox) - 1]
            self.outbox.pop(len(self.outbox) - 1)

            # outbox -> inbox: re-assign
            while (len(self.outbox) > 0):
                self.inbox.append(self.outbox[len(self.outbox) - 1])
                self.outbox.pop(len(self.outbox) - 1)

            self.size -= 1
            return result

        return None

    def first (self):
        if (self.size == 0):
            return None
        
        # inbox -> outbox: now outbox's top is first of the queue
        while (len(self.inbox) > 0):
            self.outbox.append(self.inbox[len(self.inbox) - 1])
            self.inbox.pop(len(self.inbox) - 1)
        
        result = self.outbox[len(self.outbox) - 1]

        # outbox -> inbox: re-assign
        while (len(self.outbox) > 0):
            self.inbox.append(self.outbox[len(self.outbox) - 1])
            self.outbox.pop(len(self.outbox) - 1)

        return result

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
    print ("Enqueue 5 into queue:", q.queue, 
            "\nCurrent size:", q.queue_size(),
            "\nFirst:", q.first())
    q.enqueue(3)
    print ("Enqueue 3 into queue:", q.queue, 
            "\nCurrent size:", q.queue_size(),
            "\nFirst:", q.first())
    q.enqueue(1)
    print ("Enqueue 1 into queue:", q.queue, 
            "\nCurrent size:", q.queue_size(),
            "\nFirst:", q.first())
    q.dequeue()
    print ("Dequeue from queue:", q.queue, 
            "\nCurrent size:", q.queue_size(),
            "\nFirst:", q.first())
    q.dequeue()
    print ("Dequeue from queue:", q.queue, 
            "\nCurrent size:", q.queue_size(),
            "\nFirst:", q.first())
    q.dequeue()
    print ("Dequeue from queue:", q.queue, 
            "\nCurrent size:", q.queue_size(),
            "\nFirst:", q.first())
    print ("Queue is now empty, is it empty?:", q.is_empty())

def two_stack_queue_functionality_test():
    q = TwoStackQueue()
    print ("When queue has nothing, is it empty?:", q.is_empty())
    q.enqueue(5)
    print ("Enqueue 5 into queue:", q.inbox, 
            "\nCurrent size:", q.queue_size(),
            "\nFirst:", q.first())
    q.enqueue(3)
    print ("Enqueue 3 into queue:", q.inbox, 
            "\nCurrent size:", q.queue_size(),
            "\nFirst:", q.first())
    q.enqueue(1)
    print ("Enqueue 1 into queue:", q.inbox, 
            "\nCurrent size:", q.queue_size(),
            "\nFirst:", q.first())
    q.dequeue()
    print ("Dequeue from queue:", q.inbox, 
            "\nCurrent size:", q.queue_size(),
            "\nFirst:", q.first())
    q.dequeue()
    print ("Dequeue from queue:", q.inbox, 
            "\nCurrent size:", q.queue_size(),
            "\nFirst:", q.first())
    q.dequeue()
    print ("Dequeue from queue:", q.inbox, 
            "\nCurrent size:", q.queue_size(),
            "\nFirst:", q.first())
    print ("Queue is now empty, is it empty?:", q.is_empty())

if __name__ == '__main__':
    print ("========== TEST: Queue based on list ==========")
    queue_functionality_test()
    print ("========== TEST: Queue based on 2 Stack ==========")
    two_stack_queue_functionality_test()