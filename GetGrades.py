# Complete the function so that it finds the average of the three scores passed to it and returns the letter value associated with that grade.
# Numerical Score Letter Grade
# 90 <= score <= 100 'A'
# 80 <= score < 90 'B'
# 70 <= score < 80 'C'
# 60 <= score < 70 'D'
# 0 <= score < 60 'F'

def get_grade(s1, s2, s3):
    m = (s1 + s2 + s3) / 3.0
    if 90 <= m <= 100:
        return 'A'
    elif 80 <= m < 90:
        return 'B'
    elif 70 <= m < 80:
        return 'C'
    elif 60 <= m < 70:
        return 'D'
    return "F"
print(get_grade(90,89,97))