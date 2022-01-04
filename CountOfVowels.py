# Return the number (count) of vowels in the given string.
# We will consider a, e, i, o, u as vowels for this Kata (but not y).
# The input string will only consist of lower case letters and/or spaces.

# method1
def getCount1(inputStr): 
    # for let in inputstr:
    #     if let in "aeiou":
    return sum(1 for a in inputStr if a in "aeiouAEIOU")

# method2
def getCount2(s): 
    #for c in "aeiou": 
    #   if c in inputstr:
    return sum(c in 'aeiouAEIOU' for c in s)  

# method3 
inputstr="Hello Sonu"
a=0
for let in inputstr:
    if let in "aeiou":
        a+=1
print(a)
        
print(getCount1("Hello everyone"))
print(getCount2("Good Morning"))

