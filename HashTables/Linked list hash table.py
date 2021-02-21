class LinkedListHashTable:
    def __init__(self, size=7):
        self.__size = size
        self.__slots = [LinkedList() for i in range(size)]
        #Take note this is the LinkedList equivalent of [None] * size. Note this is actually making a list which contains Linked List objects.
    
    def get_hash_code(self, key):
        return key % len(self.__slots)
    
    def __str__(self):
        container = ""
        for i in self.__slots:
            container += str(i)+"\n"
            #Remember to add in new line characters when you want to make the elements all on on new lines!
            #Remember to slice [:-1] as there is always an extra variable at the end when you add strings this way!!!
        return container[:-1]

    
    def put(self, key):
        hash_key = self.get_hash_code(key)
        self.__slots[hash_key].add(key)
        #Remember the append for LinkedList is .add(item)
    
    def __len__(self):
        return sum([i.size() for i in self.__slots])
        #Remember the len for linked list is self.size()
    
        
