class Node:
    def __init__(self,data,next=None):
        self.__data = data
        self.__next = next 
    
    def __str__(self):
        return "%s" % self.__data
        
    def get_data(self):
        return self.__data
    
    def get_next(self):
        return self.__next
    
    def set_data(self, new_data):
        self.__data = new_data
    
    def set_next(self, new_next):
        self.__next = new_next
        
    #Add node directly after current node
    def add_after(self, value):
        node_to_add = Node(value)
        #Make a node object which contains data of the new value we want to add.
        temp = self.get_next()
        #Get the next node and the chain of all its children. This is important because we need to add this back after we add the new node.
        self.set_next(node_to_add)
        #Set the next node to the node object which we initalised before which contains the data we want to add.
        self.get_next().set_next(temp)
        #Set the node after the node which we just added to the node which was there before. This keeps our linked list chain of nodes in place

    #Remove node after the current node in linked list
    def remove_after(self):
        children = self.get_next().get_next()
        #Get the children of the node which we want to remove. Remember we just want to remove the one node we don't want to remove
        #all of its children nodes in the linked list.
        current = Node(self.__data,children)
        #Initialise a new node object which will hold the current node and the children nodes of the node which we are removing.
        #Remember the node object takes data and a next parameter, the next parameter is just a link in memory to the next node
        #If we provide that link in memory we can link wherever we want, if we don't provide anything it just links to None.
        self.set_next(current.get_next())
        #Set the element which we want to remove to the node object which we initialised.
        #What is happening is we initialised a new node object which holds data of the current node that the linked list is pointing at
        #and has links to all the nodes in the linked list asides from the node which we want to remove which is the node which is directly
        #after the current node in the linked list. Thus it pretty much is a node which holds the current nodes data and the links of all
        #the nodes from the next next node till the end.
        #Thus if we set the next node in our current linked list to the next node of the object we initialised then we are setting the next
        #node in the linked list to be the chain of nodes after the element which we wanted to remove. Thus we have removed the node and kept all the links.

    def __contains__(self, value):
        #REMEMBER WE SEARCH THE ENTIRE LINKED LIST NODES FOR OUR GIVEN VALUE, IF IT IS AVAILABLE IN ANY NODE THEN WE RETURN TRUE!
        #Want to search for a given value in our linked list nodes, if the value is IN ANY OF THE NODES WE RETURN TRUE AS THEY ARE ALL LINKED!
        current = Node(self.__data, self.__next)
        #Initialise a new node object
        while current != None:
        #While loop whihc will iterate until we get to the last node which contains None as a reference
            if current.get_data() == value:
            #If the current node contains the value return True
                return True
            else:
                current = current.get_next()
                #Move on to the next node if it does not contain the value
        return False

#GIVEN A LIST OF ELEMENTS WE WANT TO APPEND MAKE EACH ELEMENT INTO A NODE THE CONNECT THE NODES IN ORDER
def create_node_chain(values):
    #Edge case if list contains only 1 element
    if len(values) == 1:
        #Set the head node to that element, NONE is set by default to the next node
        head = Node(values[0])
        return head
    else:
        #Make a child node which will hold a reference to the remaining elements in the list, set it to first element in list initially.
        children = Node(values[1])
        #Head node which will connect itself to the child node which will contain all of the nodes which have the list elements as data.
        head = Node(values[0])
        #A temporary assignment variable, this will hold a reference to the children node. If this updates the children updates and vice versa
        temp = children
        for i in range(2, len(values)):
            #By doing temp.set_next() we are doing children.set_next() as temp holds a reference to the children node.
            #WHENEVER WE set_next() THE DATA MUST BE A NODE OBJECT!
            temp.set_next(Node(values[i]))
            #Now make temp equal to the next node which it just set.
            temp = temp.get_next()
        #So what is happening here is:
        #Make a reference variable to hold a reference to the children node
        #Initialise to set the next node in the temp variable to get given list value thus setting the next node in the children node reference to this value also
        #Update temp to move forward to the node which we just set
        #This means children node will continue to hold its reference to it's base nodes + all the nodes which are added and temp node will continue to add new references
        #to itself therefore adding new references to the children node.
        head.set_next(children)
        #Finally at the end we set the children node the be the direct reference of the head node.
        return head

#GIVEN A LINKED LIST OR CHAIN OF NODES CONVERT EACH NODE ELEMENT INTO A PYTHON LIST AND RETURN
def convert_to_list(first_node):
    node_list = []
    #If the data in the node is None then stop iteration as cannot append that
    while first_node != None:
        #Add the nodes data to the list
        node_list.append(first_node.get_data())
        #Iterate through the linked list
        first_node = first_node.get_next()
    return node_list

def get_consecutive_sum(first_node):
    node_list = convert_to_list(first_node)
    for i in range(len(node_list)):
        node_list[i] = node_list[i] + sum(node_list[i+1:])
    return node_list



        
