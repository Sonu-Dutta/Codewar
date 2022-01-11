
# There was a test in your class and you passed it. Congratulations!
# But you're an ambitious person. You want to know if you're better than the average student in your class.
# You receive an array with your peers' test scores. Now calculate the average and compare your score!
# Return True if you're better, else False!
# Your points are not included in the array of your class's points. For calculating the average point you may add your point to the given array!

import statistics
def better_than_average(class_points, your_points):
    # return your_points > statistics.mean(class_points)
    average = (sum(class_points) + your_points) / (len(class_points) + 1)
    return your_points > average

print(better_than_average([23,34,54,53],95))