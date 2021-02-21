class Stack:
    def __init__(self):
        self.__list = []

    def get_Stack(self):
        return self.__list

    def is_empty(self):
        return self.__list == []

    def size(self):
        return len(self.__list)

    def push(self, item):
        self.__list.append(item)

    def pop(self):
        try:
            return self.__list.pop()
        except IndexError:
            return "ERROR: The stack is empty!"

    def peek(self):
        try:
            return self.__list[-1]
        except IndexError:
            return "ERROR: The stack is empty!"

    def __len__(self):
        return len(self.__list)

    def clear(self):
        self.__list = []

    def __str__(self):
        return "Stack: " + str(self.__list)

    def push_list(self, a_list):
        for i in a_list:
            self.push(i)

    def multi_pop(self, number):
        if len(self.__list) < number:
            return False
        [self.pop() for i in range(number)]
        return True

    def copy(self):
        copy = Stack()
        [copy.push(i) for i in self.__list]
        return copy

    def __eq__(self, other):
        if not isinstance(other, Stack):
            return False
        return self.__list == other.__list

def reverse_sentence(sentence):
    obj = Stack()
    obj2 = []
    [obj.push(i) for i in sentence.split()]
    [obj2.append(obj.pop()) for i in range(obj.size())]
    return " ".join(obj2)

def is_balanced_brackets(text):
    stack1 = Stack()
    open_brack = ["(", "{", "["]
    closed_brack = [")", "}", "]"]
    combined = ['[]', '()', '{}']
    for i in text:
        if i in open_brack:
            stack1.push(i)
        elif i in closed_brack:
            if stack1.is_empty():
                return False
            check = stack1.pop()
            if check + i not in combined:
                return False
    if stack1.is_empty():
        return True
    return False

def evaluate_postfix(postfix_list):
    stack1 = Stack()
    plus = ['+']
    minus = ['-']
    div = ["/"]
    floor_div = ['//']
    mod = ['%']
    multi = ['*']
    exp = ['^']
    for i in postfix_list:
        if i.isdigit():
            stack1.push(int(i))
        else:
            if stack1.size() < 2:
                raise IndexError("Not enough elements")
            values = [stack1.pop() for i in range(2)]
            if i in plus:
                stack1.push(values[0] + values[1])
            elif i in minus:
                stack1.push(values[1] - values[0])
            elif i in div:
                stack1.push(values[1] / values[0])
            elif i in floor_div:
                stack1.push(values[1] // values[0])
            elif i in mod:
                stack1.push(values[1] % values[0])
            elif i in multi:
                stack1.push(values[0] * values[1])
            elif i in exp:
                stack1.push(values[1] ** values[0])
    if stack1.size() > 1:
        raise IndexError("End error")
    return stack1.pop()

class Stack:
    def __init__(self):
        self.__items = []

    def is_empty(self):
        return self.__items == []

    def push(self, item):
        self.__items.append(item)

    def pop(self):
        return self.__items.pop()

    def peek(self):
        return self.__items[len(self.__items) - 1]

    def size(self):
        return len(self.__items)

    def __str__(self):
        return 'Stack: {} <- top of the stack'.format(str(self.__items))

    def slice(self, start, stop, step=1):
        obj = Stack()
        copy_stack_list = [i for i in self.__items]
        copy_stack_list = copy_stack_list[start:stop:step]
        [obj.push(i) for i in copy_stack_list]
        return obj

    def copy_stack(self):
        stack1 = Stack()
        stack2 = Stack()
        stack3 = Stack()
        for i in range(self.size()):
            stack1.push(self.peek())
            stack2.push(self.pop())
        [stack3.push(stack2.pop()) for i in range(stack2.size())]
        [self.push(stack3.pop()) for i in range(stack3.size())]
        print(stack1)
        print(self)

def move_k_elements_to_bottom(a_stack, k):
    obj = Stack()
    obj2 = Stack()
    for i in range(k):
        obj.push(a_stack.pop())
    for i in range(a_stack.size()):
        obj2.push(a_stack.pop())
    for i in range(obj.size()):
        a_stack.push(obj.pop())
    for i in range(obj2.size()):
        a_stack.push(obj2.pop())
  
    
        
s = Stack()
s.push(1)
s.push(2)
s.push(3)
s.copy_stack()
    
    
