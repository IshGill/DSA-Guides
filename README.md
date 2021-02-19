# DSA and Leetcode walkthroughs 
My walkthroughs, designed to help build solid fundamentals and understanding for concepts in data structures and algorithms, and how to identify patterns and efficiently solve various leetcode problems.  

# Strings
## License Key Formatting 
All we need to do with this question is firstly clean up the given string S by making it uppercase and replacing all instances of - with empty strings.
Now, the main trick to solving this problem is the fact that the first grouping can have any number of elements, hence this is why we need to work FROM THE END of the string. As all we really need to do is split the string into groups of size K, however the first group can be any size aslong as the rest are size K, meaning the first group is like the leftovers which we get from splitting the string into K units! Therefore, all we need to do to solve this problem is run a simple string splitting for loop, BUT FIRST REVERSE THE LIST, because we want to our leftovers which are not a full K units to be the first alphanumeric characters in the string. Finally, after completing the splitting process return the string reversed again, hence in the original order. 

    def licenseKeyFormatting(self, S, K):
        S = S.replace('-','').upper()[::-1]
        #Replace the dashes, go uppercase, reverse the string
        new_S = []
        #Break the string into K units append each unit to new list
        for i in range(0, len(S), K):
            new_S.append(S[i:i+K])
        #Join the new list and return in after reversing! 
        return "-".join(new_S)[::-1]
# Arrays
# LinkedLists
# Sorting & Searching
# Stacks
# Queues
# Priority Queues/Heaps
# Trees
# Hash tables
# Dynamic Programming 
