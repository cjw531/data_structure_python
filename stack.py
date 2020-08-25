class Stack ():
    def __init__ (self):
        self.stack = []
        self.size = 0
    
    def push (self, element):
        self.stack.append(element)
        self.size += 1
    
    def pop (self):
        if (self.size > 0):
            self.stack.pop(self.size - 1)
            self.size -= 1
            return 
        return None
    
    def top (self):
        if (self.size > 0):
            return self.stack[self.size - 1]
        return None

    def is_empty (self):
        if (self.size > 0):
            return False
        return True

    def stack_size (self):
        return self.size

def stack_functionality_test():
    s = Stack()
    print ("When stack has nothing, is it empty?:", s.is_empty())
    s.push(5)
    print ("Push 5 into stack:", s.stack, "\nCurrent size:", s.stack_size())
    s.push(3)
    print ("Push 3 into stack:", s.stack, "\nCurrent size:", s.stack_size())
    s.push(1)
    print ("Push 1 into stack:", s.stack, "\nCurrent size:", s.stack_size())
    print ("Current stack's top:", s.top())
    s.pop()
    print ("Pop from stack:", s.stack, "\nCurrent size:", s.stack_size())
    s.pop()
    print ("Pop from stack:", s.stack, "\nCurrent size:", s.stack_size())
    s.pop()
    print ("Pop from stack:", s.stack, "\nCurrent size:", s.stack_size())
    print ("Stack is now empty, is it empty?:", s.is_empty())

def reverse_array(array):
    s = Stack()
    for i in range (0, len(array)):
        s.push(array[i])

    result = []
    while not (s.is_empty()):
        result.append(s.top())
        s.pop()
    
    print ("Initial array:", array)
    print ("Reversed array:", result)

def delimiter_matching(array):
    print ("Initial delimiter:", array)

    s = Stack()
    for i in range(0, len(array)):
        if (is_opening(array[i])):
            s.push(array[i])
        elif (not is_opening(array[i])):
            if (is_matching(s.top(), array[i])):
                s.pop()
            else:
                return False
    
    if (s.stack_size() == 0):
        return True
    return False

# delimiter_matching helper function 1
def is_opening(element):
    if (element == '(' or element == '{' or element == '['):
        return True
    elif (element == ')' or element == '}' or element == ']'):
        return False
    return ("Neither opening nor closing parentheses")

# delimiter_mathcing helper function 2
def is_matching (open, close):
    if (open == '(' and close == ')'):
        return True
    elif (open == '{' and close == '}'):
        return True
    elif (open == '[' and close == ']'):
        return True
    else:
        return False

def is_palindrome (array):
    print ("Input str:", array)
    s = Stack()

    if (len(array) % 2 == 0): # even length
        middle_index = len(array) // 2
        for i in range (0, middle_index):
            s.push(array[i])
        for i in range (middle_index, len(array)):
            if (s.top() == array[i]):
                s.pop()
            else:
                return False
    else: # odd length
        middle_index = len(array) // 2 # int division
        for i in range (0, middle_index):
            s.push(array[i])
        for i in range (middle_index + 1, len(array)):
            if (s.top() == array[i]):
                s.pop()
            else:
                return False

    return True

if __name__ == '__main__':
    stack_functionality_test()
    reverse_array(['a','p','p','l','e'])
    print ("Delimiter result:", delimiter_matching(['(', '{', '[', ']', ')', ']', '}', ')']))
    print ("Delimiter result:", delimiter_matching(['(', ')', '(', '(', ')', ')', '{', '(', '[', '(', ')', ']', ')', '}']))
    print ("Palindrome result:", is_palindrome(['r', 'a', 'a', 'r']))
    print ("Palindrome result:", is_palindrome(['r', 'a', 'c', 'e', 'c', 'a', 'r']))
    print ("Palindrome result:", is_palindrome(['r', 'a', 'c', 'e']))