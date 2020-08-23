class Node:
    def __init__(self, value, next):
        self.value = value
        self.next = next

class SinglyLinkedList:
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
            node.next = self.head
            self.head = node
        # insert after tail -> push_back
        elif (index == self.size - 1):
            self.push_back(node)
            return
        else: # insert at the middle
            prev_node = self.at(index - 1)
            node.next = prev_node.next
            prev_node.next = node
        
        self.size += 1

    def remove (self, index):
        # remove head
        if (index == 0): 
            temp = self.head
            self.head = self.head.next
            temp.next = None
        # remove tail
        elif (index == self.size - 1):
            tail_prev = self.at(index - 1)
            tail_prev.next = None
            self.tail = tail_prev
        else: # remove middle elem
            remove_prev = self.at(index - 1)
            remove = remove_prev.next
            remove_prev.next = remove.next
            remove.next = None

        self.size -= 1

    def push_back (self, node):
        # when list is empty
        if (self.size == 0):
            self.head = node
            self.tail = node
        elif (self.head.value == self.tail.value and self.head.next == self.tail.next):
            self.head.next = node
            self.tail.next = node
            self.tail = node
        else: # otherwise
            self.tail.next = node
            self.tail = node

        self.size += 1

if __name__ == '__main__':
    sll = SinglyLinkedList()

    # push_back
    print ("========== Testing: push_back() when list is empty ==========")
    n1 = Node (1, None)
    sll.push_back(n1)
    print ("Head node value:", sll.head.value, "\nHead node next:", sll.head.next)
    print ("Tail node value:", sll.tail.value, "\nTail node next:", sll.tail.next)
    print ("Current SLL size:", sll.size)

    print ("\n========== Testing: push_back() when list has 1 element ==========")
    n2 = Node (2, None)
    sll.push_back(n2)
    print ("Head node value:", sll.head.value, "\nHead node next:", sll.head.next.value)
    print ("Tail node value:", sll.tail.value, "\nTail node next:", sll.tail.next)
    print ("Current SLL size:", sll.size)

    print ("\n========== Testing: push_back() when list has multiple elements ==========")
    n3 = Node (3, None)
    sll.push_back(n3)
    print ("Head node value:", sll.head.value, "\nHead node next:", sll.head.next.value)
    print ("Tail node value:", sll.tail.value, "\nTail node next:", sll.tail.next)
    print ("Current SLL size:", sll.size)

    print ("\n========== Test: print current nodes by sequence ==========")
    current = sll.head
    while (current != None):
        print ("Node value:", current.value)
        current = current.next

    # find
    print ("\n========== Test: find() non-existing node ==========")
    n4 = Node (4, None)
    print ("Index:", sll.find(n4))

    print ("\n========== Test: find() head node ==========")
    print ("Index:", sll.find(n1))

    print ("\n========== Test: find() middle node ==========")
    print ("Index:", sll.find(n2))

    print ("\n========== Test: find() tail node ==========")
    print ("Index:", sll.find(n3))

    # at
    print ("\n========== Test: at() head node ==========")
    print ("Node value:", (sll.at(0)).value)

    print ("\n========== Test: at() middle node ==========")
    print ("Node value:", (sll.at(1)).value)

    print ("\n========== Test: at() tail node ==========")
    print ("Node value:", (sll.at(2)).value)

    # insert
    print ("\n========== Testing: insert() element into head ==========")
    n0 = Node (0, None)
    sll.insert(0, n0)
    print ("Head node value:", sll.head.value, "\nHead node next:", sll.head.next.value)
    print ("Tail node value:", sll.tail.value, "\nTail node next:", sll.tail.next)
    print ("Current SLL size:", sll.size)

    print ("\nCurrent SLL:")
    current = sll.head
    while (current != None):
        print ("Node value:", current.value)
        current = current.next

    print ("\n========== Testing: insert() element into tail (=push_back) ==========")
    sll.insert(3, n4)
    print ("Head node value:", sll.head.value, "\nHead node next:", sll.head.next.value)
    print ("Tail node value:", sll.tail.value, "\nTail node next:", sll.tail.next)
    print ("Current SLL size:", sll.size)

    print ("\nCurrent SLL:")
    current = sll.head
    while (current != None):
        print ("Node value:", current.value)
        current = current.next

    print ("\n========== Testing: insert() element into middle ==========")
    n100 = Node (100, None)
    sll.insert(2, n100)
    print ("Head node value:", sll.head.value, "\nHead node next:", sll.head.next.value)
    print ("Tail node value:", sll.tail.value, "\nTail node next:", sll.tail.next)
    print ("Current SLL size:", sll.size)

    print ("\nCurrent SLL:")
    current = sll.head
    while (current != None):
        print ("Node value:", current.value)
        current = current.next
    
    # remove
    print ("\n========== Testing: remove() head ==========")
    sll.remove(0)
    print ("Head node value:", sll.head.value, "\nHead node next:", sll.head.next.value)
    print ("Tail node value:", sll.tail.value, "\nTail node next:", sll.tail.next)
    print ("Current SLL size:", sll.size)

    print ("\nCurrent SLL:")
    current = sll.head
    while (current != None):
        print ("Node value:", current.value)
        current = current.next
    
    print ("\n========== Testing: remove() tail ==========")
    sll.remove(4)
    print ("Head node value:", sll.head.value, "\nHead node next:", sll.head.next.value)
    print ("Tail node value:", sll.tail.value, "\nTail node next:", sll.tail.next)
    print ("Current SLL size:", sll.size)

    print ("\nCurrent SLL:")
    current = sll.head
    while (current != None):
        print ("Node value:", current.value)
        current = current.next

    print ("\n========== Testing: remove() middle ==========")
    sll.remove(1)
    print ("Head node value:", sll.head.value, "\nHead node next:", sll.head.next.value)
    print ("Tail node value:", sll.tail.value, "\nTail node next:", sll.tail.next)
    print ("Current SLL size:", sll.size)

    print ("\nCurrent SLL:")
    current = sll.head
    while (current != None):
        print ("Node value:", current.value)
        current = current.next