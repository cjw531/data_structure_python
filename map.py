class Map:
    def __init__ (self):
        self.keys = []
        self.values = []
        self.size = 0

    def put (self, key, value):
        if (self.get(key) == None): # new entry
            self.keys.append(key)
            self.values.append(value)
            self.size += 1
        else: # update entry
            for i in range (0, self.size):
                if (self.keys[i] == key):
                    self.values[i] = value
                    break

    def remove (self, key):
        success = False
        for i in range (0, self.size):
            if (self.keys[i] == key):
                self.keys.pop(i)
                self.values.pop(i)
                success = True
                break
        
        return success

    def get (self, key):
        value = None
        for i in range (0, self.size):
            if (self.keys[i] == key):
                value = self.values[i]
                break
                
        return value

    def key_set (self):
        return self.keys

    def value_set (self):
        return self.values
    
    def entry_set (self):
        entry = []
        for i in range (0, self.size):
            entry.append([self.keys[i], self.values[i]])

        return entry

    def is_empty (self):
        if (self.size > 0):
            return False
        return True

    def map_size (self):
        return self.size

if __name__ == '__main__':
    map = Map()
    print ("When map has nothing, is it empty?:", map.is_empty())
    print ("===============================================")
    map.put("Jim", 647)
    print ("Insert Jim into map, size:", map.map_size())
    print ("Key Set:", map.key_set())
    print ("Value Set:", map.value_set())
    print ("K, V pair set:", map.entry_set())
    print ("===============================================")
    map.put("John", 416)
    print ("Insert John into map, size:", map.map_size())
    print ("Key Set:", map.key_set())
    print ("Value Set:", map.value_set())
    print ("K, V pair set:", map.entry_set())
    print ("===============================================")
    print ("Remove Alan which is not existing:", map.remove(597))
    print ("===============================================")
    map.put("John", 716)
    print ("Update John into map, size:", map.map_size())
    print ("Key Set:", map.key_set())
    print ("Value Set:", map.value_set())
    print ("K, V pair set:", map.entry_set())
    print ("===============================================")
    print ("Remove Jim from the map:", map.remove(647))
    print ("Key Set:", map.key_set())
    print ("Value Set:", map.value_set())
    print ("K, V pair set:", map.entry_set())