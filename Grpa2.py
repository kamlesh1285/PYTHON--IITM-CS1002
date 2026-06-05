# Note this prefix code is to verify that you are not using any for loops in this exercise. This won't affect any other functionality of the program.
with open(__file__) as f:
    content = f.read().split("# <eoi>")[2]
if "while " in content:
    print("You should not use while loop or the word while anywhere in this exercise")

# your code should not use more than 7 for loops 
# assuming one for loop per problem
if content.count("for ")>7:
    print("You should not use more than 7 for loops")

# This is the first line of the exercise
task = input()
# <eoi>

if task == 'factorial':
    n = int(input())
    result = 1
    i = 1
    while i <= n:
        result *= i
        i += 1

    print(result)
elif task == 'even_numbers':
    n = int(input())
    while i < n+1:
        print(i)
        i+=2

elif task == 'power_sequence':
    n = int(input())
    result = 1
    while i<n:
        print(result)
        result*=2
        i+=1

elif task == 'sum_not_divisible':
    n = int(input())
    total = 0
    i = 1
    while i < n:
        if i % 4 != 0 and i % 5 != 0:
            total += i 
        i += 1 
    print(total)

elif task == 'from_k':
    line = input()
    n = int(line[0])
    k = int(line[1])
    i = 100 
    count = 0 
    while count < n:
        if i < k:
            break 
        valid = True 
        if i % 2 == 0:
            valid = False
        else:
            digits = str(i) 
            if '5' in digits or '9' in digits:
                valid = False 
        if valid:
            rev_num = int(str(i)[::-1])
            print(rev_num)
            count += 1 
        i -= 1 

elif task == 'string_iter':
    s = input().strip() 
    prev = 1 
    i = 0 
    while i < len(s):
        digit = int(s[i]) 
        print(digit*prev, end=' ')
        if i < len(s) - 1:
            print(' ', end=' ')
        prev = digit

elif task == 'list_iter':
    lst = eval(input()) # this will load the list from input

else:
    print("Invalid")
