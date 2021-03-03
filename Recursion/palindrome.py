def palindrome_filter(sentence):
    locate_full = sentence.rfind(".")
    locate_space = sentence.rfind(" ")
    locate_question = sentence.rfind("?")
    if locate_full == -1 and locate_space == -1 and locate_question == -1:
        return sentence
    else:
        if sentence[0].isalpha():
            return sentence[0].lower() + palindrome_filter(sentence[1:])
        else:
            return palindrome_filter(sentence[1:])
            
def is_palindrome(sentence):
    #Base Case: If we hit this then we haven't returned False yet, implying that
    #Uptill now the first and last letters of each recursive step have been matching thus fulfilling plaindrome 
    if len(sentence) <= 1:
        return True
    elif sentence[0] != sentence[-1]:
    #If we ever reach a point where first and last letter are not equal then this is not a palindrome, return False
        return False
    else:
        #Recursivley cut the problem down from both ends.
        return is_palindrome(sentence[1:len(sentence)-1])

print(is_palindrome(palindrome_filter("Able was I ere I saw Elba.")))
print(is_palindrome(palindrome_filter("Ebla was I ere I saw Elba.")))
print(is_palindrome(palindrome_filter("Are we not drawn onward, we few, drawn onward to new era?")))
