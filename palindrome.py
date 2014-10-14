#Check if Palindrome
#Checks if the string entered by the user is a palindrome. 
#That is that it reads the same forwards as backwards like racecar

def palindrome(original):
    reversedString = original[::-1]
    if reversedString == original:
        print "It is palindrome!"
    else:
        print "It is not palindrome!"
    
'''    print reversedString
    return reversedString
'''    
#def palindrome(original):
    
    

original = raw_input('What is your string?')
palindrome(original)

