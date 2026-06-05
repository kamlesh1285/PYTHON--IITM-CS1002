# Get age(int), dob(str of format "dd/mm/yy") and weight(float) from the standard input and print the tenth_month, fifth_birthday and last_birthday formatted as "day/month/year"(do not include the preceeding zero for single digit number) separated by comma and a space a single line and print the weight_readable(str formatted as "55 kg 200 grams")

#Note: while formatting dates you may have to convert back int to str using the type conversion. There is something called as "f-strings" or "formatted strings" that will help us format things by automatically doing type conversion. This will be covered in later weeks. But you can explore that (Google or ChatGPT) and compare the difference.

#Note: The last_birthday depends on the dob and age. For example if the dob is "20/02/2001" and the age is 5 the last birthday will be "20/02/2006".


age = int(input()) # int: Read a number as integer from standard input
dob = input() # str: Read a string of format dd/mm/yy from standard input
day, month, year = map(int, dob.split('/')) # int, int, int: Get the correct parts from dob as int

fifth_birthday = f"{day}/{month}/{year+5} " # str: fifth birthday formatted as day/month/year 

last_birthday = f"{day}/{month}/{year+age} " # str: last birthday formatted as day/month/year

tenth_month = f"{day}/{month+10}/{year} " # str: dob same day after 10 months formatted as day/month/year

# print tenth_month, fifth_birthday and last_birthday in same line separated by comma and a space
print(f"{tenth_month}, {fifth_birthday}, {last_birthday} ")

weight = float(input()) # float: Read a number as float from stdin(Standard input)

weight_readable = f"{int(weight)} kg {int((weight - int(weight))*1000 + 0.5 )} grams" # str: reformat weight of format 55 kg 250 grams

# print weight_readable 
print(weight_readable)

