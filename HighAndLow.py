# In this little assignment you are given a string of space separated numbers, and have to return the highest and lowest number.
# Examples
# highAndLow("1 2 3 4 5") // return "5 1" 
# highAndLow("1 2 -3 4 5") // return "5 -3" 
# highAndLow("1 9 3 4 -5") // return "9 -5"

#method1
def high_and_low1(numbers): 
    n = [int(s) for s in numbers.split(" ")]
    return "%i %i" % (max(n),min(n))
  
print(high_and_low1("1 2 3 4 5"))
