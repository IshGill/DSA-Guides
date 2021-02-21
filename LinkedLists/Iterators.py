##numbers = [1,2,3,4,5,6,7]
####Simple list of numbers. List is an iterable data structure
##numbers_iterator = numbers.__iter__()
####Variable which takes our list object and sends it iterator method
##print((numbers_iterator))
###We can see the variable is a iterator object 
##print(next(numbers_iterator))
###By doing next on the iterator object we are iterating through the list
##print(next(numbers_iterator))
##print(next(numbers_iterator))
##print(next(numbers_iterator))
##print(next(numbers_iterator))
##print(next(numbers_iterator))
##print(next(numbers_iterator))
###One the list is out of elements a StopIteration Error is raised
##print(next(numbers_iterator))

##FOR LOOP EXAMPLE
##numbers = [1,2,3,4,5,6,7]
##numbers_iterator = numbers.__iter__()
##while True:
##    try:
##        item = next(numbers_iterator)
##        print(item)
##    except StopIteration:
##        break


class Iterator:
    def __init__(self, start_point, end_point):
        #Start_point = Beginning range, where to start iteration from
        self.__start_point = start_point
        #End_point = End range, where to end iteration
        self.__end_point = end_point

    def __iter__(self):
        #ALL THIS METHOD DOES IS TAKE OUR OBJECT/INSTANCE VARIABLE AND RETURN IT AS AN ITERABLE OBJECT!
        return self

    def __next__(self):
        if self.__start_point >= self.__end_point:
            #Check that we are not at the end of the range, so we do not have anymore elements left
            #in object to iterate. If the starting range is >= the ending range that means we have reached
            #the end of the number of elements in the object, or the end of the specified range. Raise
            #StopIteration Error
            raise StopIteration("End of object reached")
        else:
            #If we are not at the end of the object or end of the specified range yet then we can continue to iterate
            current = self.__start_point
            #Make a variable to hold the current element in the object
            self.__start_point += 1
            #Increment the range so we eventually stop
            return current
            #Return the variable

numbers = Iterator(10, 15)
#This object gives us a start and end point to iterate thorugh, OUR RANGE

for i in numbers:
    print(i)

    

