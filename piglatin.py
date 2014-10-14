#Pig Latin
#Pig Latin is a game of alterations played on the English language game. 
#To create the Pig Latin form of an English word the initial consonant sound is transposed to the end of the word and an ay is affixed 
#(Ex.: "banana" would yield anana-bay). Read Wikipedia for more information on rules.
#For words that begin with vowel sounds or silent letter, you just add "way" (or "wa") to the end.

#isalpha
def pigLatin (original):
    #original = raw_input("please input:")
    word = original.lower()
    vowel = "way"
    consonant = "ay"
    first = word[0]
    if len(word) > 0:
        if first.isalpha() == True:
            if first in "aeiou":
                #newWordVowel = str(word) + str(vowel)
                newWordVowel = word + vowel
                print newWordVowel
            else:
                #newWordConsonant = str(word[1:]) + str(first) + str(consonant)
                newWordConsonant = word[1:] + first + consonant
                print newWordConsonant
        else:
            print "character only"
    else:
        print "Empty"

original = raw_input("please input:")
pigLatin (original)
    
    
"""
    
    if len(word) > 0 and first.isalpha() == TRUE:
        if first in "aeiou":
            #newWordVowel = str(word) + str(vowel)
            newWordVowel = word + vowel
            print newWordVowel
        else:
            #newWordConsonant = str(word[1:]) + str(first) + str(consonant)
            newWordConsonant = word[1:] + first + consonant
            print newWordConsonant
            
    elseif len(word) > 0 and first.isalpha() == FALSE:
        print "character only"
        
    else:
        print "Empty"
        
        # not alpha
        
"""    
        
