class Queue:
    def __init__(self, array=[]):
        self.queue = array
    
    def push(self, element):
        self.queue.append(element)
    
    def pop(self):
        try:
            return(self.queue.pop(0))
        except IndexError:
            return "Queue is empty"
    
    def peek(self):
        try:
            return(self.queue[0])
        except IndexError:
            return "Queue is empty"
    
    def __len__(self):
        return len(self.queue)

    def size(self):
        return len(self.queue)

    def __str__(self):
        return f"{self.queue[::-1]}"

obj = Queue([1,2,3,4])
print(obj)
print(obj.size())
print(obj.pop())
print(obj.peek())