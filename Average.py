# Write a function which calculates the average of the numbers in a given list.
# Note: Empty arrays should return 0.

def find_average(array): 
    try: 
        return sum(array) / len(array) 
    except ZeroDivisionError: 
        return 0
    
print(find_average([2,3,4]))