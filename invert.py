# Given a set of numbers, return the additive inverse of each. Each positive becomes negatives, 
# and the negatives become positives.
# invert([1,2,3,4,5]) == [-1,-2,-3,-4,-5] 
# invert([1,-2,3,-4,5]) == [-1,2,-3,4,-5] 
# invert([]) == []

def invert1(lst): 
    return [-x for x in lst]

def invert2(lst): 
    return list(map(lambda x: -x, lst))

print(invert1([1,2,3,4,5]))
print(invert2([1,-2,3,-4,5]))
print(invert1([]))