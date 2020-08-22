class Vector:
    def __init__(self):
        self.vector = [None] * 10
        self.iter_begin = -1
        self.iter_end = -1
        self.elem_size = 0
        self.store_size = 10

    def at (self, index):
        if (self.size() == 0):
            return None
        return (self.vector[index])

    def insert (self, index, element):
        if (self.elem_size == self.store_size):
            self.resize()
        
        for i in reversed (range(index, self.iter_end + 2)):
            self.vector[i + 1] = self.vector[i]
        self.vector[index] = element
        
        self.elem_size += 1
        self.iter_end += 1

        if (self.size() == 1):
            self.iter_begin = 0
    
    def remove (self, index):
        if (self.size() == 0):
            return None
        
        for i in range (index, self.iter_end):
            self.vector[i] = self.vector[i + 1]
        
        self.vector[self.iter_end] = None
        self.iter_end -= 1
        self.elem_size -= 1

        if (self.size() == 0):
            self.iter_begin = -1

    def index_of (self, element):
        if (self.size() == 0):
            return None

        for i in range (self.iter_begin, self.iter_end + 1):
            if (self.vector[i] == element):
                return i
        return None
    
    def push_back (self, element):
        if (self.elem_size == self.store_size):
            self.resize()

        self.vector[self.iter_end + 1] = element
        
        self.elem_size += 1
        self.iter_end += 1

        if (self.size() == 1):
            self.iter_begin = 0

    def resize (self):
        new_list = [None] * (10 + self.size())

        for i in range (self.iter_begin, self.iter_end + 1):
            new_list[i] = self.vector[i]

        self.vector = new_list
        self.store_size = (10 + self.size())

    def is_empty (self):
        if (self.size() == 0):
            return True
        return False

    def size (self):
        return self.elem_size


if __name__ == '__main__':
    v = Vector()

    print ("========== Array Initial Check ==========")
    print ("Original vector:", v.vector)
    print ("Is the vector empty?", v.is_empty())
    print ("Size of vector:", v.size())
    print ("vector[1]:", v.at(1), "\n")

    print ("========== Testing: push_back() ==========")
    for i in range (1, 11):
        v.push_back(i)
    print ("After appending int 0 to 10:", v.vector)
    print ("element size:", v.elem_size, "| store size:", v.store_size)
    print ("iter begin:", v.iter_begin, "| iter end:", v.iter_end, "\n")

    print ("========== Array Check After Append ==========")
    print ("Current vector:", v.vector)
    print ("Is the vector empty?", v.is_empty())
    print ("Size of vector:", v.size())
    print ("vector[1]:", v.at(1), "\n")

    print ("========== Testing: index_of() ==========")
    print ("Index of 7:", v.index_of(7))
    print ("Index of 100:", v.index_of(100), "\n")

    print ("========== Testing: push_back() w/ resizing ==========")
    v.push_back(11)
    print ("After push_back(11) & resizing:", v.vector)
    print ("element size:", v.elem_size, "| store size:", v.store_size)
    print ("iter begin:", v.iter_begin, "| iter end:", v.iter_end, "\n")

    print ("========== Testing: insert() ==========")
    v.insert(7, 100)
    print ("After insert(7, 100):", v.vector)
    v.insert(3, 200)
    print ("After insert(3, 200):", v.vector)
    v.insert(5, 300)
    print ("After insert(5, 300):", v.vector)
    v.insert(10, 400)
    print ("After insert(10, 400):", v.vector)
    print ("element size:", v.elem_size, "| store size:", v.store_size)
    print ("iter begin:", v.iter_begin, "| iter end:", v.iter_end, "\n")

    print ("========== Testing: push_back() ==========")
    for i in range (16, 21):
        v.push_back(i)
    print ("After appending int 16 to 20:", v.vector)
    print ("element size:", v.elem_size, "| store size:", v.store_size)
    print ("iter begin:", v.iter_begin, "| iter end:", v.iter_end, "\n")

    print ("========== Testing: remove() ==========")
    print ("Original vector:", v.vector)
    v.remove(4)
    print ("After remove(4):", v.vector)
    v.remove(7)
    print ("After remove(7):", v.vector)
    v.remove(0)
    print ("After remove(0):", v.vector)
    v.remove(19)
    print ("After remove(19):", v.vector)
    print ("element size:", v.elem_size, "| store size:", v.store_size)
    print ("iter begin:", v.iter_begin, "| iter end:", v.iter_end, "\n")

    print ("========== Testing: remove() all element ==========")
    print ("Original vector:", v.vector)
    print ("element size:", v.elem_size, "| store size:", v.store_size)
    print ("iter begin:", v.iter_begin, "| iter end:", v.iter_end)
    for i in range (0, 16):
        v.remove(i)
    print ("After removal:", v.vector)
    print ("element size:", v.elem_size, "| store size:", v.store_size)
    print ("iter begin:", v.iter_begin, "| iter end:", v.iter_end, "\n")
