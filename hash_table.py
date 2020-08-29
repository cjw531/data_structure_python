# Separate Chaining
class HashTableChain:
    def __init__ (self):
        self.element_size = 0
        self.capacity = 10
        self.hash_table = [None] * self.capacity
        self.threshold = 0.5
    
    def insert (self, key, value):
        index = self.hash(key)
        
        # space empty -> simply insert
        if (self.hash_table[index] == None):
            self.hash_table[index] = []
            self.hash_table[index].append([key, value])
            self.element_size += 1
        # if key exists already -> update value field
        elif (self.find(key) != None):
            self.find(key)[1] = value
        # space not empty -> bucket insert
        else: 
            self.hash_table[index].append([key, value])
            self.element_size += 1

        # whether to rehash or not
        if ((self.element_size / self.capacity) > self.threshold):
            self.rehash()

    def remove (self, key):
        # remove non-existing key -> fail
        if (self.find(key) == None):
            return False
        else:
            index = self.hash(key)
            for i in range (0, len(self.hash_table[index])):
                if (self.hash_table[index][i][0] == key):
                    self.hash_table[index].pop(i)
                    self.element_size -= 0
                    return True

    def find (self, key):
        index = self.hash(key)
        if (self.hash_table[index] == None):
            return None

        for i in self.hash_table[index]:
            if (i[0] == key):
                return i
        return None

    def hash (self, key):
        return (key % self.capacity)

    def rehash (self):
        temp = self.hash_table
        self.capacity *= 2
        self.hash_table = [None] * self.capacity
        self.element_size = 0
        
        for i in temp:
            if (i != None):
                for j in range (0, len(i)):
                    self.insert(i[j][0], i[j][1])

    def is_empty (self):
        if (self.size > 0):
            return False
        return True

if __name__ == '__main__':
    htc = HashTableChain()
    htc.insert(5, "Five")
    htc.insert(15, "Fiftheen")
    print ("After inserting 5 and 15, bucket:", htc.hash_table[5])

    htc.insert(5, "New Five")
    print ("After inserting 5, update:", htc.hash_table[5])
    
    print ("Searching non-existing key:", htc.find(6))
    print ("Remove non-existing key:", htc.find(6))
    
    htc.remove(15)
    print ("Remove 15 from hash table:", htc.hash_table[5])

    htc.insert(1, "One")
    htc.insert(2, "Two")
    htc.insert(3, "Three")
    htc.insert(4, "Four")
    print ("Rehash:", htc.hash_table)
    htc.insert(6, "Six")
    print ("Current:", htc.hash_table)
    htc.remove(3)
    print ("Current:", htc.hash_table)
    htc.insert(3, "New Three")
    print ("Current:", htc.hash_table)

