class MinHeap:
    def __init__ (self):
        self.heap = []
        self.size = 0

    # O(log(n))
    def push (self, element):
        if (self.size == 0):
            self.heap.append(element)
            self.size += 1
            return
        
        self.heap.append(element)
        self.size += 1
        parent_idx = self.compute_parent(self.size - 1)
        current_idx = (self.size - 1)

        while (current_idx > 0 and self.heap[parent_idx] > element):
            # swap
            self.heap[parent_idx], self.heap[current_idx] = self.heap[current_idx], self.heap[parent_idx]
            current_idx = parent_idx
            parent_idx = self.compute_parent(current_idx)
        

    # helper function
    def compute_parent (self, child):
        parent_idx = -1
        if ((child % 2) == 1):
            parent_idx = ((child - 1) // 2)
        else: # % 2 == 0
            parent_idx = ((child - 2) // 2)

        return parent_idx

    # O(log(n))
    def pop (self):
        if (self.size == 0): 
            return
        elif (self.size == 1):
            self.heap.pop(0)
            self.size -= 1
            return
        
        # swap
        self.heap[0], self.heap[self.size - 1] = self.heap[self.size - 1], self.heap[0]
        self.heap.pop(self.size - 1) # remove swapped root node
        self.size -= 1

        parent_idx = 0
        left_child_idx = (2 * parent_idx) + 1
        right_child_idx = (2 * parent_idx) + 2
        while (left_child_idx <= self.size - 1):
            if (self.heap[parent_idx] > self.heap[left_child_idx]): # left child
                self.heap[parent_idx], self.heap[left_child_idx] = self.heap[left_child_idx], self.heap[parent_idx]
        
            if (right_child_idx <= self.size - 1 and self.heap[parent_idx] > self.heap[right_child_idx]): # right child
                self.heap[parent_idx], self.heap[right_child_idx] = self.heap[right_child_idx], self.heap[parent_idx]

            parent_idx += 1
            left_child_idx = (2 * parent_idx) + 1
            right_child_idx = (2 * parent_idx) + 2
        
    # O(1)
    def top (self):
        return (self.heap[0])

    def is_empty (self):
        if (self.size > 0):
            return False
        return True

    def heap_size (self):
        return (self.size)
    
if __name__ == '__main__':
    mh = MinHeap()
    print ("When min heap has nothing, is it empty?:", mh.is_empty())
    # push
    mh.push(7)
    print ("After pushing 7, heap:", mh.heap)
    print ("Current size:", mh.size)
    print ("Current top:", mh.top())
    mh.push(4)
    print ("After pushing 4, heap:", mh.heap)
    print ("Current size:", mh.size)
    print ("Current top:", mh.top())
    mh.push(8)
    print ("After pushing 8, heap:", mh.heap)
    print ("Current size:", mh.size)
    print ("Current top:", mh.top())
    mh.push(2)
    print ("After pushing 2, heap:", mh.heap)
    print ("Current size:", mh.size)
    print ("Current top:", mh.top())
    mh.push(5)
    print ("After pushing 5, heap:", mh.heap)
    print ("Current size:", mh.size)
    print ("Current top:", mh.top())
    mh.push(3)
    print ("After pushing 3, heap:", mh.heap)
    print ("Current size:", mh.size)
    print ("Current top:", mh.top())
    mh.push(9)
    print ("After pushing 9, heap:", mh.heap)
    print ("Current size:", mh.size)
    print ("Current top:", mh.top())
    print ("When min heap has 7 elements, is it empty?:", mh.is_empty())

    # pop
    while (mh.size > 0):
        print ("After pop:", mh.top())
        mh.pop()
        print ("Current heap:", mh.heap)
        print ("Current size:", mh.size)
    print ("When min heap has nothing, is it empty?:", mh.is_empty())
