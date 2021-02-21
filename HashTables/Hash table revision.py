class SimpleHashTable:
    def __init__(self, size=7):
        self.__size = size
        self.__slots = [None] * size

    def get_hash_key(self, key):
        return key % len(self.__slots)

    def get_str_hash_key(self, word):
        total = 0
        for i in range(len(word)):
            total += (i+1) * ord(word[i])
        return total % len(self.__slots)

    def __str__(self):
        return str(self.__slots)

    def get_size(self):
        return self.__size

    def put(self, key):
        if len([i for i in self.__slots if i != None]) == self.get_size():
            raise IndexError("ERROR: The hash table is full")
        get_key = self.get_hash_key(key)
        if self.__slots[get_key] == None:
            self.__slots[get_key] = key
        else:
            linear_collision = self.get_new_hash_code_linear_probing(get_key)
            self.__slots[linear_collision] = key

    def __len__(self):
        return len([i for i in self.__slots if i != None])

    def get_new_hash_code_linear_probing(self, index):
        count = 1
        linear_key = (index + count) % len(self.__slots)
        while self.__slots[linear_key] != None:
            count += 1
            linear_key = (linear_key + count) % len(self.__slots)
        return linear_key

    def is_empty(self):
        return len([i for i in self.__slots]) == 0

    def clear(self):
        self.__slots = []

    def rehashing(self, new_size):
        elements = [i for i in self.__slots if i != None]
        self.__slots = [None] * new_size
        for i in elements:
            self.put(i)

    def search(self, item):
        if self.__slots[item%len(self.__slots)] == item:
            print(True)
        elif self.__slots[item%len(self.__slots)] == None:
            print(None)
        else:
            collision_search = self.get_new_hash_code_linear_probing(item%len(self.__slots), item)
            print(self.__slots[collision_search])
            if self.__slots[collision_search] == item:
                print(item)

    def probe(self, index):
        search = self.get_hash_key(index)
        count = 0
        var = []
        while self.__slots[search] != index:
            var.append(search)
            count += 1
            search = (index + count) % len(self.__slots)
        print(var)
        return count

def worst_index(size, values):
    new_table = SimpleHashTable(size)
    [new_table.put(i) for i in values]
    probe_number = [new_table.probe(i) for i in range(size)]
    print(probe_number)
    var = [i for i in range(len(probe_number)) if probe_number[i] == max(probe_number)]
    print(var)


class QuadraticHashTable:
    def __init__(self, size=7):
        self.__size = size
        self.__slots = [None] * size

    def get_hash_key(self, key):
        return key % len(self.__slots)

    def get_str_hash_key(self, word):
        total = 0
        for i in range(len(word)):
            total += (i+1) * ord(word[i])
        return total % len(self.__slots)

    def __str__(self):
        return str(self.__slots)

    def get_size(self):
        return self.__size

    def __len__(self):
        return len([i for i in self.__slots if i != None])

    def put(self, key):
        if len([i for i in self.__slots if i != None]) == self.get_size():
            raise IndexError("ERROR: The hash table is full")
        get_key = self.get_hash_key(key)
        if self.__slots[get_key] == None:
            self.__slots[get_key] = key
        else:
            quad_collision = self.get_new_hash_code_quadratic_probing(get_key,1)
            self.__slots[quad_collision] = key

    def get_new_hash_code_quadratic_probing(self, index, distance):
        quad = (index + distance**2) % len(self.__slots)
        while self.__slots[quad] != None:
            distance += 1
            quad = (index + distance**2) % len(self.__slots)
        return quad

    def is_empty(self):
        return len([i for i in self.__slots]) == 0

    def clear(self):
        self.__slots = []

    def rehashing(self, new_size):
        elements = [i for i in self.__slots if i != None]
        self.__slots = [None] * new_size
        for i in elements:
            self.put(i)

    def probe(self, index):
        search = self.get_hash_key(index)
        count = 0
        var = []
        while self.__slots[search] != index:
            var.append(search)
            count += 1
            search = (index + count**2) % len(self.__slots)
        print(var)
        return count

class DoubleHashTable:
    def __init__(self, size=7, second_hash_value=7):
        self.__size = size
        self.__second_hash_value = second_hash_value
        self.__slots = [None] * size
        
    def get_hash_key(self, key):
        return key % len(self.__slots)

    def get_str_hash_key(self, word):
        total = 0
        for i in range(len(word)):
            total += (i+1) * ord(word[i])
        return total % len(self.__slots)

    def __str__(self):
        return str(self.__slots)

    def get_size(self):
        return self.__size

    def __len__(self):
        return len([i for i in self.__slots if i != None])

    def put(self, key):
        if len([i for i in self.__slots if i != None]) == self.get_size():
            raise IndexError("ERROR: The hash table is full")
        get_key = self.get_hash_key(key)
        if self.__slots[get_key] == None:
            self.__slots[get_key] = key
        else:
            dub_collision = self.get_new_hash_code_double_hashing(key)
            self.__slots[dub_collision] = key

    def get_new_hash_code_double_hashing(self, key):
        second_hash = self.__second_hash_value - (key % self.__second_hash_value)
        new_key = (key + second_hash) % len(self.__slots)
        while self.__slots[new_key] != None:
            new_key = (new_key + second_hash) % len(self.__slots)
        return new_key

    def is_empty(self):
        return len([i for i in self.__slots]) == 0

    def clear(self):
        self.__slots = []

    def rehashing(self, new_size):
        elements = [i for i in self.__slots if i != None]
        self.__slots = [None] * new_size
        for i in elements:
            self.put(i)
class LinkedList:
    def __init__(self, data=None):
        self.__head = data

    def get_head(self):
        return self.__head

    def set_head(self, value):
        self.__head = value

    def add(self, value):
        self.__head = Node(value, self.__head)

    def size(self):
        count = 0
        nodes_in_list = self.get_head()
        while nodes_in_list != None:
            count += 1
            nodes_in_list = nodes_in_list.get_next()
        return count

    def clear(self):
        self.set_head(None)

    def is_empty(self):
        return self.size() == 0

    def __len__(self):
        return self.size()

    def __str__(self):
        current = self.get_head()
        list_string = ""
        while current != None:
            list_string += str(current.get_data()) + ", "
            current = current.get_next()
        return "[{}]".format(list_string[:-2])

    def __contains__(self, search_value):
        current = self.get_head()
        while current != None:
            if current.get_data() == search_value:
                return True
            current = current.get_next()
        return False

    def __getitem__(self, index):
        count = 0
        current = self.get_head()
        while count != index:
            count += 1
            current = current.get_next()
        return current.get_data()

##    def __getitem__(self, index):
##        count = 0
##        current = self.__head
##        while current != None:
##            if count == index:
##                return current.get_data()
##            count += 1
##            current = current.get_next()

    def append(self, data):
        new_node = Node(data)

        if self.__head == None:
            self.__head = new_node
            return

        get_last_node = self.__head
        while get_last_node.get_next() != None:
            get_last_node = get_last_node.get_next()
        get_last_node.set_next(new_node)

    def add_all(self, a_list):
        for i in a_list:
            self.add(i)

    def get_min_odd(self):
        mins_list = []
        current = self.get_head()
        while current != None:
            if current.get_data() % 2 != 0:
                mins_list.append(current.get_data())
            current = current.get_next()
        mins_list.sort()
        return mins_list[0] if len(mins_list) >= 1 else 999

    def reverse(self):
        previous = None
        current = self.get_head()
        while current != None:
            next_node = current.get_next()
            current.set_next(previous)
            previous = current
            current = next_node
        self.__head = previous

    def add_sorted_order(self, item):
        previous = None
        obj = Node(item)
        current = self.get_head()
        while current != None:
            if item < current.get_data():
                break
            else:
                previous = current
                current = current.get_next()
        if previous == None:
            self.__head = Node(item, self.__head)
        else:
            previous.set_next(obj)
            obj.set_next(current)

    def remove(self, key):
        current = self.__head 
        previous = None
        if current.get_data() == key:
            self.__head = current.get_next()
            current = None
            return
        while current != None:
            if current.get_data() == key:
                previous.set_next(current.get_next())
                return
            previous = current
            current = current.get_next()
        print("ERROR: Data not in LinkedList")

    def deleting_from_index(self, index):
        current = self.get_head()
        previous = None
        count = 1
        if index == 0:
            self.__head = current.get_next()
            current = None
            return
        while current != None:
            previous = current
            current = current.get_next()
            if count == index:
                previous.set_next(current.get_next())
                
                return
            count += 1
        print("ERROR: DNE")
                
            
    def comparing_two_lists(self, other):
        self_list = []
        other_list = []
        self_ref = self.get_head()
        other_ref = other.__head
        if not self.size() == other.size():
            return False
        while self_ref != None:
            self_list.append(self_ref.get_data())
            other_list.append(other_ref.get_data())
            self_ref = self_ref.get_next()
            other_ref = other_ref.get_next()
        return sorted(self_list) == sorted(other_list)

    def compared_to_linked_listed_check(self, other):
            if not self.size() == other.size():
                return False
            else:
                self_ref = self.get_head()
                matched_counter = 0
                outer_loop_counter = 0
                while outer_loop_counter < self.size():
                    other_ref = other.get_head()
                    inner_loop_counter = 0
                    while inner_loop_counter < other.size():
                        if other_ref.get_data() == self_ref.get_data():
                            matched_counter += 1
                        other_ref = other_ref.get_next()
                        inner_loop_counter += 1
                    outer_loop_counter += 1
                    self_ref = self_ref.get_next()
            return matched_counter == self.size()

    def comparing_two_lists_linked_only(self, list2):
        if not self.size() == list2.size():
            return False
        else:
            matched_count = 0 #Counter to hold number of matched elements
            current_of_self = self.get_head() #Reference to head of self linkedlist head
            outer_loop_counter = 0 #Hold the range of the outer loop, when this == size of the linked list this means all elements visited
            
            while outer_loop_counter < self.size(): #Outer loop which runs through the element of the linked list one at a time
                current_of_list2 = list2.get_head() #Reference to list2 linkedlist head, Note that in the inner loop we increment the head of list2
                inner_loop_counter = 0 #Resets the inner loop counter
                
                while inner_loop_counter < list2.size(): #Loop thorugh the enitre second linkedlist and visit each element it contains every loop
                    if current_of_self.get_data() == current_of_list2.get_data(): #Take one element of our outer loop and check that with every element of the second linkedlist to see if it is contained in the second linked list also.
                        matched_count += 1 #If it is contained the matched count is incremented
                    inner_loop_counter += 1 #Increment the count, this is akin to incrementing the range for a for loop
                    current_of_list2 = current_of_list2.get_next() #Increment list2 so we can visit all of it's elements
            
                outer_loop_counter += 1 #Increment counter 1 so we eventually finish our loop
                current_of_self = current_of_self.get_next() #Get the next element of the linked list
                
            if matched_count == self.size() and matched_count == list2.size(): #If the matched count is == to the size of the linkedlists then they both contain matching elements so return True, else False
                return True
            else:
                return False
    #General idea here is:
    #To iterate through to linked lists and compare their elements we use nested while loops.
    #1: Set reference variables for each linked list object
    #2: Set a outer loop counter, a matched elements counter and a inner loop reset counter
    #3: Iterate any list with the outer loop counter < self.size()
    #4: Nested while loop with inner_loop_counter < other.size()
    #5: During this while loop check if the current data of the current linked list is equal to the one current data in the self linked list, if it is then add 1 to the counter, if not the increment the outer loop counter and do other = other.get_next()
    #6: Finally just check if the matched counter is == size of both linked lists

def remove_dupes(linked_list):
    current = linked_list.get_head() # Current will point to head node of linked list
    runner = linked_list.get_head() # Runner also points at head node of linked list
    while current != None: # Iterate while current != None
        while runner.get_next() != None: # While the element after the head element also does not equal None
            if current.get_data() == runner.get_next().get_data(): # If the current data in the linked list is present in the next node of the linked list
                runner.remove_after() #Remove that node
            else:   
                runner = runner.get_next() # Else increment runner
        runner = current.get_next() # Reset runner to the next element of the linked list
        current = current.get_next() # Reset current to the next element of the linked list

#Ok so how does this work?
# All we are doing is we have two references to the head of the linked list we are given, current and runner.
# We set up a nested loop structure. Our outer loop will be run until the end of current which just means it will be run till the end of the linked list we are given.
# The inner loop is a nested loop. So it will iterate from the element infront of the head node pointer element each iteration and run until the next element in the linked list is referncing None
# Then in current.get_data() for the enitre inner loop we hold the same Node data which the head is currently pointing to. We then check that with the next node in the linked list and it's data
# If they match this means that we have a duplicate, as the data in current is in a eariler index than the data in next, so if this is true we have a repeat of the same element.
# In this case we use .remove_after() this will remove the node infront of the current node, Now we use this on runner because runner points at the node.   


class LinkedListHashTable:
    def __init__(self, size=7):
        self.__slots = [LinkedList() for i in range(size)]

    def get_hash_code(self, key):
        return key % len(self.__slots)

    def __str__(self):
        container = ""
        for i in self.__slots:
            container += str(i) + "\n"
        return container[:-1]

    def put(self, key):
        get_key = self.get_hash_code(key)
        self.__slots[get_key].add(key)

    def __len__(self):
        return sum([i.size() for i in self.__slots])

class HashTable:
    def __init__(self, size):
        self.__items = size*[None]
        self.__size = size
        self.__count = 0

    def put(self, value):
        if self.__count < self.__size:
            h = value % self.__size
            while self.__items[h] != None:
                h = (h + 1) % self.__size
            self.__items[h] = value
            self.__count += 1

    def __str__(self):
        result = ''
        for i in range(self.__size):
            result = result + str(i) + ', '
        return "["+result[:-2]+"]"

    def probe1(self, index):
        count = 0
        while self.__items[index] != None:
            count += 1
            index = (index + 1) % len(self.__items)
        return count
        
def worst_index(size, values):
    new_table = HashTable(size)
    [new_table.put(i) for i in values]
    probe_number = [new_table.probe(i) for i in range(size)]
    print(new_table)
    print(probe_number)
    return [i for i in range(len(probe_number)) if probe_number[i] == max(probe_number)]


def largest(list1):
    return [i for i in range(len(list1)) if list1[i] == max(list1)]



obj = HashTable(7)
obj_list = [40,20,12,50,26]
[obj.put(i) for i in obj_list]
print(obj)


    
    
    


        



