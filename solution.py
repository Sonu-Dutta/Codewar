# Complete the solution so that the function will break up camel casing, using a space between words.
# Example
# "camelCasing" => "camel Casing" 
# "identifier" => "identifier" 
# "" => ""

def solution1(s): 
    st = "" 
    for c in s: 
        if c.upper() == c: 
            st += " " + c 
        else: 
            st += c 
    return st

def solution2(s): 
    return ''.join(' ' + c if c.isupper() else c for c in s)

import re 
def solution3(s): 
    return re.sub('([A-Z])', r' \1', s)

print(solution1('sonuDutta'))
print(solution2('camelCasing'))
print(solution3('hello'))