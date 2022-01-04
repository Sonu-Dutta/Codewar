# Replace all vowel to exclamation mark in the sentence. aeiouAEIOU is vowel.

# Examples
# replace("Hi!") === "H!!"
# replace("!Hi! Hi!") === "!H!! H!!"
# replace("aeiou") === "!!!!!"
# replace("ABCDE") === "!BCD!"

def replace1(s):
    return ''.join('!' if c in 'aeiouAEIOU' else c for c in s)

import re 
def replace2(s): 
    return re.sub('[aeiouAEIOU]', '!', s)

print(replace1("Hello"))
print(replace1("Good Morning"))