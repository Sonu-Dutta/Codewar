# An anagram is the result of rearranging the letters of a word to produce a new word (see wikipedia).
# Note: anagrams are case insensitive
# Complete the function to return true if the two arguments given are anagrams of each other; return false otherwise.
# Examples
# "foefet" is an anagram of "toffee"
# "Buckethead" is an anagram of "DeathCubeK"

from collections import Counter
def is_anagram(test, original):
    # return Counter(test.lower()) == Counter(original.lower())
    return sorted(original.lower()) == sorted(test.lower())

print(is_anagram("sonus","unoss"))