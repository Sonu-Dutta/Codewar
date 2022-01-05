# You probably know the "like" system from Facebook and other pages. People can "like" blog posts, pictures or other items. 
# We want to create the text that should be displayed next to such an item.

# Implement the function which takes an array containing the names of people that like an item. 
# It must return the display text as shown in the examples:

# [] --> "no one likes this" 
# ["Peter"] --> "Peter likes this" 
# ["Jacob", "Alex"] --> "Jacob and Alex like this" 
# ["Max", "John", "Mark"] --> "Max, John and Mark like this" 
# ["Alex", "Jacob", "Mark", "Max"] --> "Alex, Jacob and 2 others like this"

# nethod1
def likes(names): 
    if len(names) == 0: 
        return 'no one likes this' 
    elif len(names) == 1: 
        return str(names[0]+' likes this') 
    elif len(names) == 2: 
        return str(names[0]+' and '+names[1]+' like this') 
    elif len(names) == 3: 
        return str(names[0]+', '+names[1]+' and '+names[2]+' like this') 
    else: 
        return str(names[0]+', '+names[1]+' and '+str(len(names)-2)+' others like this')
    
print(likes(["Jacob", "Alex"]))

# method2
def like(names): 
    n = len(names) 
    return { 
            0: 'no one likes this', 
            1: '{} likes this', 
            2: '{} and {} like this', 
            3: '{}, {} and {} like this', 
            4: '{}, {} and {others} others like this' 
            }[min(4, n)].format(*names[:3], others=n-2)
print(like(["Alex", "Jacob", "Mark", "Max"]))