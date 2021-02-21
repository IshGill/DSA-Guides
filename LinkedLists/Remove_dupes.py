def remove_dupes(linked_list):
    current = linked_list.get_head()  # Current will point to head node of linked list
    runner = linked_list.get_head()  # Runner also points at head node of linked list
    while current != None:  # Iterate while current != None
        while runner.get_next() != None:  # While the element after the head element also does not equal None
            if current.get_data() == runner.get_next().get_data():  # If the current data in the linked list is present in the next node of the linked list
                runner.remove_after()  # Remove that node
            else:
                runner = runner.get_next()  # Else increment runner
        runner = current.get_next()  # Reset runner to the next element of the linked list
        current = current.get_next()  # Reset current to the next element of the linked list