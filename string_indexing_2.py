
number = "9,223,372,036,854,775,807"
print(number[1::4])  # print all commas


number_two = "9,223;372:036 854,775;807"
print(number_two[1::4])  # print all separators

seperators = number_two[1::4]
print(seperators)

values = "".join(char if char not in seperators else " " for char in number_two ).split()
print(values) # extract numbers from the above string

# convert the string to int and print the values
list_of_numbers = [int(i) for i in values]
print(list_of_numbers)

print("".join(str(i) for i in list_of_numbers))
