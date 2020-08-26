from vector import *
from doubly_linked_list import *

class VectorPriorityQueue:
    def __init__ (self):
        self.vpq = Vector()
        self.size = 0

    # amortized O(1)
    def push (self, element):
        self.vpq.push_back(element)
        self.size += 1

    # O(n), act as a selection sort
    def pop (self):
        if (self.size == 0):
            return None

        min = self.vpq.at(0)
        remove_index = 0
        for i in range (1, self.size):
            if (min > self.vpq.at(i)):
                min = self.vpq.at(i)
                remove_index = i
        
        self.vpq.remove(remove_index)
        self.size -= 1
        return min

    # O(n)
    def top (self):
        if (self.size == 0):
            return None

        min = self.vpq.at(0)
        for i in range (1, self.size):
            if (min > self.vpq.at(i)):
                min = self.vpq.at(i)
        
        return min

    def is_empty (self):
        if (self.size == 0):
            return True
        return False

    def vpq_size (self):
        return (self.size)

class LinkedListPriorityQueue:
    def __init__ (self):
        self.dllpq = DoublyLinkedList()
        self.size = 0

    # O(n), act as an insertion sort
    def push (self, element):
        node = Node(element, None, None)

        if (self.size == 0):
            self.dllpq.push_back(node)
        else:
            index = 0
            current = self.dllpq.head
            while (current != None):
                if (current.value >= element):
                    self.dllpq.insert(index, node)
                    break
                current = current.next
                index += 1

            if (index == self.size):
                self.dllpq.push_back(node)
        
        self.size += 1

    # O(1)
    def pop (self):
        if (self.size == 0):
            return None

        removal = (self.dllpq.at(0)).value
        self.dllpq.remove(0)
        self.size -= 1
        return removal

    # O(1)
    def top (self):
        if (self.size == 0):
            return None
        
        return (self.dllpq.head.value)

    def is_empty (self):
        if (self.size == 0):
            return True
        return False

    def dllpq_size (self):
        return (self.size)

    # print function to make result more intuitive
    def print_pq (self):
        result = []
        current = self.dllpq.head
        while (current != None):
            result.append(current.value)
            current = current.next
        
        return result

def priority_queue_functionality_test(pq):
    print ("When PQ has nothing, is it empty?:", pq.is_empty())

    # push, top, size test
    pq.push(5)
    print ("After pusing 5, unordered PQ:\n", pq.vpq.vector)
    print ("Current size:", pq.size)
    print ("Current top:", pq.top())
    pq.push(9)
    print ("After pusing 9, unordered PQ:\n", pq.vpq.vector)
    print ("Current size:", pq.size)
    print ("Current top:", pq.top())
    pq.push(2)
    print ("After pusing 2, unordered PQ:\n", pq.vpq.vector)
    print ("Current size:", pq.size)
    print ("Current top:", pq.top())
    pq.push(7)
    print ("After pusing 7, unordered PQ:\n", pq.vpq.vector)
    print ("Current size:", pq.size)
    print ("Current top:", pq.top())
    print ("When PQ has 4 elements, is it empty?:", pq.is_empty())

    # pop test
    print("Pop from PQ:", pq.pop())
    print ("After pop, unordered PQ:\n", pq.vpq.vector)
    print ("Current size:", pq.size)
    print ("Current top:", pq.top())

    print("Pop from PQ:", pq.pop())
    print ("After pop, unordered PQ:\n", pq.vpq.vector)
    print ("Current size:", pq.size)
    print ("Current top:", pq.top())

    print("Pop from PQ:", pq.pop())
    print ("After pop, unordered PQ:\n", pq.vpq.vector)
    print ("Current size:", pq.size)
    print ("Current top:", pq.top())

    print("Pop from PQ:", pq.pop())
    print ("After pop, unordered PQ:\n", pq.vpq.vector)
    print ("Current size:", pq.size)
    print ("Current top:", pq.top())
    print ("When PQ has nothing, is it empty?:", pq.is_empty())

def linked_list_priority_queue_functionality_test(pq):
    print ("When PQ has nothing, is it empty?:", pq.is_empty())

    # push, top, size test
    pq.push(5)
    print ("After pusing 5, ordered PQ:\n", pq.print_pq())
    print ("Current size:", pq.size)
    print ("Current top:", pq.top())
    pq.push(9)
    print ("After pusing 9, ordered PQ:\n", pq.print_pq())
    print ("Current size:", pq.size)
    print ("Current top:", pq.top())
    pq.push(2)
    print ("After pusing 2, ordered PQ:\n", pq.print_pq())
    print ("Current size:", pq.size)
    print ("Current top:", pq.top())
    pq.push(7)
    print ("After pusing 7, ordered PQ:\n", pq.print_pq())
    print ("Current size:", pq.size)
    print ("Current top:", pq.top())
    pq.push(4)
    print ("After pusing 4, ordered PQ:\n", pq.print_pq())
    print ("Current size:", pq.size)
    print ("Current top:", pq.top())
    print ("When PQ has 5 elements, is it empty?:", pq.is_empty())

    # pop test
    print("Pop from PQ:", pq.pop())
    print ("After pop, ordered PQ:\n", pq.print_pq())
    print ("Current size:", pq.size)
    print ("Current top:", pq.top())

    print("Pop from PQ:", pq.pop())
    print ("After pop, ordered PQ:\n", pq.print_pq())
    print ("Current size:", pq.size)
    print ("Current top:", pq.top())

    print("Pop from PQ:", pq.pop())
    print ("After pop, ordered PQ:\n", pq.print_pq())
    print ("Current size:", pq.size)
    print ("Current top:", pq.top())

    print("Pop from PQ:", pq.pop())
    print ("After pop, ordered PQ:\n", pq.print_pq())
    print ("Current size:", pq.size)
    print ("Current top:", pq.top())

    print("Pop from PQ:", pq.pop())
    print ("After pop, ordered PQ:\n", pq.print_pq())
    print ("Current size:", pq.size)
    print ("Current top:", pq.top())
    print ("When PQ has nothing, is it empty?:", pq.is_empty())

if __name__ == '__main__':
    vpq = VectorPriorityQueue()
    print ("========== TEST: Priority Queue based on vector (list) ==========")
    priority_queue_functionality_test(vpq)

    dllpq = LinkedListPriorityQueue()
    print ("========== TEST: Priority Queue based on Doubly Linked List ==========")
    linked_list_priority_queue_functionality_test(dllpq)