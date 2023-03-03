class Stack():
    def __init__(self):
        self.stack = []

    def add(self, element):
        self.stack.append(element)
    
    def pop(self):
        try:
            return(self.stack.pop())
        except IndexError:
            return "Stack is empty"
    
    def __len__(self):
        return len(self.stack)
    
    def peek(self):
        try:
            return(self.stack[-1])
        except IndexError:
            return "Stack is empty"
    
    def __str__(self):
        return f"{self.stack}"
    
obj = Stack()
obj.add(1)
obj.add(2)
print(obj)
print(obj.peek())
print(obj.pop())

