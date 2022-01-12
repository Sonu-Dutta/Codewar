# Your team is writing a fancy new text editor and you've been tasked with implementing the line numbering.
# Write a function which takes a list of strings and returns each line prepended by the correct number.
# The numbering starts at 1. The format is n: string. Notice the colon and space in between.
# Examples:
# number([]) # => []
# number(["a", "b", "c"]) # => ["1: a", "2: b", "3: c"]
def number(lines):
    return ["{}: {}".format(i + 1, lines[i]) for i in range(len(lines))]
    # return ["{}: {}".format(*line) for line in enumerate(lines, start=1)]
    # return ["%d: %s" %line for line in enumerate(lines, 1)]
print(number(["a", "b", "c"]))