from doubly_linked_list import *

class Deque:
    def __init__ (self):
        self.deque = DoublyLinkedList()
        self.size = 0
    
    def add_first (self, element):
        e = Node(element, None, None)
        self.deque.insert(0, e)
        self.size += 1
    
    def add_last (self, element):
        e = Node(element, None, None)
        self.deque.push_back(e)
        self.size += 1

    def remove_first (self):
        if (self.size == 0):
            return None
        self.deque.remove(0)
        self.size -= 1

    def remove_last (self):
        if (self.size == 0):
            return None
        self.deque.remove(self.size - 1)
        self.size -= 1

    def first_top (self):
        if (self.size > 0):
            return (self.deque.head.value)
        return None

    def last_top (self):
        if (self.size > 0):
            return (self.deque.tail.value)
        return None

    def is_empty (self):
        if (self.size > 0):
            return False
        return True
    
    def deque_size (self):
        return (self.size)

    # print function to make result more intuitive
    def print_deque (self):
        result = []
        current = self.deque.head
        while (current != None):
            result.append(current.value)
            current = current.next
        
        return result

if __name__ == '__main__':
    d = Deque()

    # is_empty, add left and right
    print ("When deque has nothing, is it empty?:", d.is_empty())
    d.add_first(1)
    print ("Add 1 into first:", d.print_deque(), "\t\tCurrent size:", d.deque_size(),
            "\nLeft first element:", d.first_top(), "\t\tRight first element:", d.last_top())
    d.add_last(3)
    print ("Add 3 into last:", d.print_deque(), "\tCurrent size:", d.deque_size(),
            "\nLeft first element:", d.first_top(), "\t\tRight first element:", d.last_top())
    d.add_first(5)
    print ("Add 5 into first:", d.print_deque(), "\tCurrent size:", d.deque_size(),
            "\nLeft first element:", d.first_top(), "\t\tRight first element:", d.last_top())
    d.add_last(2)
    print ("Add 2 into last:", d.print_deque(), "\tCurrent size:", d.deque_size(),
            "\nLeft first element:", d.first_top(), "\t\tRight first element:", d.last_top())
    print ("When deque has elements, is it empty?:", d.is_empty())

    # remove first and last
    d.remove_first()
    print ("Remove left:", d.print_deque(), "\tCurrent size:", d.deque_size(),
            "\nLeft first element:", d.first_top(), "\t\tRight first element:", d.last_top())
    d.remove_last()
    print ("Remove right:", d.print_deque(), "\tCurrent size:", d.deque_size(),
            "\nLeft first element:", d.first_top(), "\t\tRight first element:", d.last_top())
    d.remove_first()
    print ("Remove left:", d.print_deque(), "\tCurrent size:", d.deque_size(),
            "\nLeft first element:", d.first_top(), "\t\tRight first element:", d.last_top())
    d.remove_last()
    print ("Remove right:", d.print_deque(), "\tCurrent size:", d.deque_size(),
            "\nLeft first element:", d.first_top(), "\t\tRight first element:", d.last_top())
    print ("When deque has elements, is it empty?:", d.is_empty())