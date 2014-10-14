#Random Gift Suggestions
#Enter various gifts for certain people when you think of them. 
#When its time to give them a gift (xmas, birthday, anniversary) 
#it will randomly pick one and perhaps places you can get it.
import random
def randomGift(gift, people):
    #gifts = gift.split(",")
    print people,"'s gift is", (random.choice(gift))     
#    print (random.choice(gift))
    
    
 # http://stackoverflow.com/questions/306400/how-do-i-randomly-select-an-item-from-a-list-using-python
 
    
gift = raw_input("Please input the gift options: \n").split()
people = raw_input("Please input people's name: \n")
randomGift(gift,people)
