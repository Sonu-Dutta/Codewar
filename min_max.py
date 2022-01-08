# Ben has a very simple idea to make some profit: he buys something and sells it again. 
# Of course, this wouldn't give him any profit at all if he was simply to buy and sell it at the same price. 
# Instead, he's going to buy it for the lowest possible price and sell it at the highest.
# Task
# Write a function that returns both the minimum and maximum number of the given list/array.

# Examples
# min_max([1,2,3,4,5])   == [1,5]
# min_max([2334454,5])   == [5, 2334454]
# min_max([1])           == [1, 1]

def min_max(lst):
  lst.sort()
  temp = [lst[0],lst[-1]]
  return temp
print(min_max([4,6,2,3,8,1]))