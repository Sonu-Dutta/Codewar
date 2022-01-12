# Write a function that will return the count of distinct case-insensitive alphabetic characters and numeric digits that occur more than once in the input string. 
# The input string can be assumed to contain only alphabets (both uppercase and lowercase) and numeric digits.
# Example
# "abcde" -> 0 # no characters repeats more than once
# "aabbcde" -> 2 # 'a' and 'b'
# "aabBcde" -> 2 # 'a' occurs twice and 'b' twice (b and B)
# "indivisibility" -> 1 # 'i' occurs six times
# "Indivisibilities" -> 2 # 'i' occurs seven times and 's' occurs twice
# "aA11" -> 2 # 'a' and '1'
# "ABBA" -> 2 # 'A' and 'B' each occur twice

from re import findall

def duplicate_count(text):
# method1
    # count = 0
    # for c in set(text.lower()):
    #     if text.lower().count(c) > 1:
    #         count += 1
    # return count

# method2
    # seen = set()
    # dupes = set()
    # for char in text:
    #     char = char.lower()
    #     if char in seen:
    #         dupes.add(char)
    #     seen.add(char)
    # return len(dupes)
# method3   
    return len([c for c in set(text.lower()) if text.lower().count(c)>1])

print(duplicate_count("aabBcccdde"))