class Stack:
    def __init__(self):
        self.__items = []
    def is_empty(self):
        return self.__items == []
    def push(self, item):
        self.__items.append(item)
    def pop(self):
        try:
            return self.__items.pop()
        except IndexError:
            return "ERROR: The stack is empty!"
    def peek(self):
        try:
            return self.__items[len(self.__items) - 1]
        except IndexError:
            return "ERROR: The stack is empty!"
    def __str__(self):
        return "Stack: {}".format(self.__items)
    def __len__(self):
        return len(self.__items)
    def clear(self):
        self.__items = []
    def push_list(self, a_list):
        self.__items = self.__items + a_list
    def multi_pop(self, number):
        if len(self.__items) >= number:
            for i in range(number):
                self.pop()
            return True
        else:
            return False
    def copy(self):
        #To copy a class object, create a new instance of that object
        copy_obj = Stack()
        #Pass that object to a method in the class which will return to you the exact same object 
        copy_obj.push_list(self.__items)
        return copy_obj
    def __eq__(self, other):
        if type(other) != Stack:
            return False
        return self.__items == other.__items

def evaluate_postfix(postfix_list):
    tokens = postfix_list
    add = ["+"]
    minus = ["-"]
    multi = ["*"]
    div = ["/"]
    exp = ["**"]
    mod = ["%"]
    postfix_stack = Stack()
    for i in tokens:
        if i.isdigit():
            postfix_stack.push(int(i))
        else:
            if len(postfix_stack) >= 2:
                val1 = postfix_stack.pop()
                val2 = postfix_stack.pop()
                if i in minus:
                    product = val2 - val1
                    postfix_stack.push(product)
                elif i in add:
                    product = val1 + val2
                    postfix_stack.push(product)
                elif i in multi:
                    product = val1 * val2
                    postfix_stack.push(product)
                elif i in div:
                    product = val2 // val1
                    postfix_stack.push(product)
                elif i == "^":
                    product = val2 ** val1
                    postfix_stack.push(product)
                elif i in mod:
                    product = val2 % val1
                    postfix_stack.push(product)  
    if len(postfix_stack) == 1:
        return postfix_stack.pop()
    else:
        print("ERROR")

print(evaluate_postfix(['2', '10', '^']))
##1024
print(evaluate_postfix(['2', '4', '3', '*', '^']))
##4096
print(evaluate_postfix(['10', '4', '2', '-', '5', '*', '+', '3', '%']))

def infixToPostfix(infixexpr):
    prec = {}
    prec["*"] = 3
    prec["/"] = 3
    prec["+"] = 2
    prec["-"] = 2
    prec["("] = 1
    opStack = Stack()
    postfixList = []
    tokenList = infixexpr.split()

    for token in tokenList:
        if token in "ABCDEFGHIJKLMNOPQRSTUVWXYZ" or token in "0123456789":
            postfixList.append(token)
        elif token == '(':
            opStack.push(token)
        elif token == ')':
            topToken = opStack.pop()
            while topToken != '(':
                postfixList.append(topToken)
                topToken = opStack.pop()
        else:
            while (not opStack.is_empty()) and \
               (prec[opStack.peek()] >= prec[token]):
                  postfixList.append(opStack.pop())
            opStack.push(token)

    while not opStack.is_empty():
        postfixList.append(opStack.pop())
    return " ".join(postfixList)

print(infixToPostfix("6 - (5 + 4) * (1 - 2)"))
                
            


