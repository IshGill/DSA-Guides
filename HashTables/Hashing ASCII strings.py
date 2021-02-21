def hash_string(word_string, table_size):
    total = 0
    for i in range(len(word_string)):
        #i + 1 is the weight we add as the position of the
        #character in the string
        total += (i+1) * ord(word_string[i]) 
    return total % table_size

print(hash_string("paul", 13))
print(hash_string("dose", 13))  
print(hash_string("does", 13)) 
