# Complete the method/function so that it converts dash/underscore delimited words into camel casing. The first word within the output should be capitalized only if the original word was capitalized (known as Upper Camel Case, also often referred to as Pascal case).

# Examples
# "The_Stealth_Warrior" gets converted to "TheStealthWarrior"

# method1

def to_camel_case(text): 
    list = [x for x in text] 
    if len(list) != 0: 
        for i in range(len(list)): 
            if list[i] in ('-', '_'): 
                list = ''.join([i for i in list if i not in ('-', '_')]) 
                return list
            
print(to_camel_case("To_Camel_Case"))
