# Create a multi-functional program that performs different tasks based on the user input. The program should support the following tasks:

#Permutation (permutation): Given a string s, print all the possible two-letter permutations(without repitition) of the letters in the string.


task = input()

if task == "permutation":
    s = input()
    for i in range(len(s)):
        for j in range(len(s)):
            if i != j:
                print(s[i] + s[j])
elif task == "sorted_permutation":
    s = input()
    for i in range(len(s)):
        for j in range(len(s)):
            if i != j and s[i] < s[j]:
                print(s[i] + s[j] )
            
elif task == "repeat_the_repeat":
    n = int(input()) 
    for i in range(n):
        for j in range(1, n+1):
            print(j, end='')
        print() 
elif task =="repeat_incrementally":
    n = int(input())
    for i in range(1, n+1):
        for j in range(1, i+1):
            print(j, end='')
        print()
        
elif task == "increment_and_decrement":
    n = int(input()) 
    for i in range(1, n+1):
        for j in range(1, i+1):
            print(j, end='')
        for j in range(i-1, 0, -1):
            print(j, end='')
        print()
                

