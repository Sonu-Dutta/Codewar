# You are going to be given a word. Your job is to return the middle character of the word. If the word's length is odd, return the middle character. 
# If the word's length is even, return the middle 2 characters.
#Examples:

# getMiddle("test") should return "es" 
# getMiddle("testing") should return "t" 
# getMiddle("middle") should return "dd" 
# getMiddle("A") should return "A" 

import math 
def get_middle(s): 
    x = len(s) 
    y = int(x/2) 
    if x%2==0: 
        return s[y-1:y+1] 
    else: 
        return s[y:y+1]
    
print(get_middle("Sonu"))
print(get_middle("Dutta"))
print(get_middle("A"))