# Solve all the below tasks related to indexing and slicing.

# Keep in mind 🧠 The concept of indexing and slicing will come again in later weeks with list and tuple which are also sequences like string.

# This exercise gives you practice in different indexing and slicing methods.

# Sample inputs (# note: The values given in the prefix code(grey) will be changed by the autograder according to the testcase while running them.

s = "hello pyhton"
course_code = "24t2cs1002" # 24 - year, t2 - term 2, cs1002 - course id
# <eoi>

output1 = s[2] # str: get the third character of s

output2 = s[-4] # str: get the fourth last character of s

output3 = s[:3] # str: get the first 3 characters of s

output4 = s[::2] # str: get every second character of s

output5 = s[-3:] # str: get the last 3 characters of s

output6 = s[::-1] # str: get the reverse of s

course_term = ... #int: get the term of the year as number from course_code
course_year = ...  # int: get the year as two digit number from course_code
course_id = ... # str: get the course id from course_code
course_term = int(course_code[2:4][1]) # term is the second character of the term part
course_year = int(course_code[:2]) # year is the first two characters of the course code
course_id = course_code[6:] # course id is the part after the first 6 characters (year and term)


