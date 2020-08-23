class Node:
    def __init__(self, value, prev, next):
        self.value = value
        self.prev = prev
        self.next = next

class DoublyLinkedList:
    def __init__(self):
        self.head = None
        self.tail = None
        self.size = 0

    # returns node
    def at (self, index):
        if (index >= self.size):
            return None
        
        idx = 0
        current = self.head
        while (idx <= index):
            if (idx == index):
                return current
            current = current.next
            idx += 1
        
        return None
    
    # returns index where the node is located
    def find (self, node):
        index = 0
        current = self.head
        while (current != None):
            if (current.value == node.value and current.next == node.next):
                return index
            current = current.next
            index += 1
        
        return None

    def insert (self, index, node): 
        # insert at head's position
        if (index == 0): 
            self.head.prev = node
            node.prev = None
            node.next = self.head
            self.head = node
        # insert after tail -> push_back
        elif (index == self.size - 1):
            self.push_back(node)
            return
        else: # insert at the middle
            prev_node = self.at(index - 1)
            next_node = prev_node.next
            
            prev_node.next = node
            node.prev = prev_node
            node.next = next_node
            next_node.prev = node
        
        self.size += 1

    def remove (self, index):
        # remove when there's 1 elem left
        if (self.size == 1):
            self.head = None
            self.tail = None
        # remove head
        elif (index == 0): 
            (self.head.next).prev = None
            temp = self.head
            self.head = self.head.next
            temp.next = None
        # remove tail
        elif (index == self.size - 1):
            (self.tail.prev).next = None
            temp = self.tail
            self.tail = self.tail.prev
            temp.prev = None
        else: # remove middle elem
            remove = self.at(index)
            (remove.prev).next = remove.next
            (remove.next).prev = remove.prev
            remove.prev = None
            remove.next = None

        self.size -= 1

    def push_back (self, node):
        # when list is empty
        if (self.size == 0):
            node.prev = None
            node.next = None
            self.head = node
            self.tail = node
        elif (self.head.value == self.tail.value and self.head.next == self.tail.next):
            self.head.next = node
            node.prev = self.head
            node.next = None
            self.tail = node
        else: # otherwise
            self.tail.next = node
            node.prev = self.tail
            node.next = None
            self.tail = node

        self.size += 1

if __name__ == '__main__':
    dll = DoublyLinkedList()

    # push_back
    print ("========== Testing: push_back() when list is empty ==========")
    n1 = Node (1, None, None)
    dll.push_back(n1)
    print ("Head node value:", dll.head.value, 
            "\nHead node prev:", dll.head.prev, 
            "\nHead node next:", dll.head.next)
    print ("Tail node value:", dll.tail.value, 
            "\nTail node prev:", dll.tail.prev,
            "\nTail node next:", dll.tail.next)
    print ("Current SLL size:", dll.size)

    print ("\n========== Testing: push_back() when list has 1 element ==========")
    n2 = Node (2, None, None)
    dll.push_back(n2)
    print ("Head node value:", dll.head.value, 
            "\nHead node prev:", dll.head.prev, 
            "\nHead node next:", dll.head.next.value)
    print ("Tail node value:", dll.tail.value, 
            "\nTail node prev:", dll.tail.prev.value,
            "\nTail node next:", dll.tail.next)
    print ("Current SLL size:", dll.size)

    print ("\n========== Testing: push_back() when list has multiple elements ==========")
    n3 = Node (3, None, None)
    dll.push_back(n3)
    print ("Head node value:", dll.head.value, 
            "\nHead node prev:", dll.head.prev, 
            "\nHead node next:", dll.head.next.value)
    print ("Tail node value:", dll.tail.value, 
            "\nTail node prev:", dll.tail.prev.value,
            "\nTail node next:", dll.tail.next)
    print ("Current SLL size:", dll.size)

    print ("\n========== Test: print current nodes by sequence ==========")
    current = dll.head
    while (current != None):
        print ("Node value:", current.value)
        current = current.next

    # find
    print ("\n========== Test: find() non-existing node ==========")
    n4 = Node (4, None, None)
    print ("Index:", dll.find(n4))

    print ("\n========== Test: find() head node ==========")
    print ("Index:", dll.find(n1))

    print ("\n========== Test: find() middle node ==========")
    print ("Index:", dll.find(n2))

    print ("\n========== Test: find() tail node ==========")
    print ("Index:", dll.find(n3))

    # at
    print ("\n========== Test: at() head node ==========")
    print ("Node value:", (dll.at(0)).value)

    print ("\n========== Test: at() middle node ==========")
    print ("Node value:", (dll.at(1)).value)

    print ("\n========== Test: at() tail node ==========")
    print ("Node value:", (dll.at(2)).value)

    # insert
    print ("\n========== Testing: insert() element into head ==========")
    n0 = Node (0, None, None)
    dll.insert(0, n0)
    print ("Head node value:", dll.head.value, 
            "\nHead node prev:", dll.head.prev, 
            "\nHead node next:", dll.head.next.value)
    print ("Tail node value:", dll.tail.value, 
            "\nTail node prev:", dll.tail.prev.value,
            "\nTail node next:", dll.tail.next)
    print ("Current SLL size:", dll.size)

    print ("\nCurrent SLL:")
    current = dll.head
    while (current != None):
        print ("Node value:", current.value)
        current = current.next

    print ("\n========== Testing: insert() element into tail (=push_back) ==========")
    dll.insert(3, n4)
    print ("Head node value:", dll.head.value, 
            "\nHead node prev:", dll.head.prev, 
            "\nHead node next:", dll.head.next.value)
    print ("Tail node value:", dll.tail.value, 
            "\nTail node prev:", dll.tail.prev.value,
            "\nTail node next:", dll.tail.next)
    print ("Current SLL size:", dll.size)

    print ("\nCurrent SLL:")
    current = dll.head
    while (current != None):
        print ("Node value:", current.value)
        current = current.next

    print ("\n========== Testing: insert() element into middle ==========")
    n100 = Node (100, None, None)
    dll.insert(2, n100)
    print ("Head node value:", dll.head.value, 
            "\nHead node prev:", dll.head.prev, 
            "\nHead node next:", dll.head.next.value)
    print ("Tail node value:", dll.tail.value, 
            "\nTail node prev:", dll.tail.prev.value,
            "\nTail node next:", dll.tail.next)
    print ("Current SLL size:", dll.size)

    print ("\nCurrent SLL:")
    current = dll.head
    while (current != None):
        print ("Node value:", current.value)
        current = current.next
    
    # remove
    print ("\n========== Testing: remove() head ==========")
    dll.remove(0)
    print ("Head node value:", dll.head.value, 
            "\nHead node prev:", dll.head.prev, 
            "\nHead node next:", dll.head.next.value)
    print ("Tail node value:", dll.tail.value, 
            "\nTail node prev:", dll.tail.prev.value,
            "\nTail node next:", dll.tail.next)
    print ("Current SLL size:", dll.size)

    print ("\nCurrent SLL:")
    current = dll.head
    while (current != None):
        print ("Node value:", current.value)
        current = current.next
    
    print ("\n========== Testing: remove() tail ==========")
    dll.remove(4)
    print ("Head node value:", dll.head.value, 
            "\nHead node prev:", dll.head.prev, 
            "\nHead node next:", dll.head.next.value)
    print ("Tail node value:", dll.tail.value, 
            "\nTail node prev:", dll.tail.prev.value,
            "\nTail node next:", dll.tail.next)
    print ("Current SLL size:", dll.size)

    print ("\nCurrent SLL:")
    current = dll.head
    while (current != None):
        print ("Node value:", current.value)
        current = current.next

    print ("\n========== Testing: remove() middle ==========")
    dll.remove(1)
    print ("Head node value:", dll.head.value, 
            "\nHead node prev:", dll.head.prev, 
            "\nHead node next:", dll.head.next.value)
    print ("Tail node value:", dll.tail.value, 
            "\nTail node prev:", dll.tail.prev.value,
            "\nTail node next:", dll.tail.next)
    print ("Current SLL size:", dll.size)

    print ("\nCurrent SLL:")
    current = dll.head
    while (current != None):
        print ("Node value:", current.value)
        current = current.next

    print ("\n========== Testing: remove() 2 more ==========")
    dll.remove(0)
    dll.remove(1)
    print ("Head node value:", dll.head.value)
    print ("Tail node value:", dll.tail.value)
    print ("Current SLL size:", dll.size)

    print ("\nCurrent SLL:")
    current = dll.head
    while (current != None):
        print ("Node value:", current.value)
        current = current.next

    print ("\n========== Testing: remove() the last node ==========")
    dll.remove(0)
    print ("Head node:", dll.head)
    print ("Tail node:", dll.tail)
    print ("Current SLL size:", dll.size)

    print ("\nCurrent SLL:")
    current = dll.head
    while (current != None):
        print ("Node value:", current.value)
        current = current.next