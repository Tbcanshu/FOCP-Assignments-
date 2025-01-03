#1:
name = input("Hello, what is your name? ")
print(f"Hello {name}   Nice to meet you" )

#2:
temp = float(input("Enter the tempertaure in celsius:"))
Fahrenheit = temp*(9/5)+32
print(f"The temperature in Fahrenheit is: {Fahrenheit}")

#3:
total_stds = int(input("Total number of students "))
group_size = int(input("Required group size "))

groups = total_stds // group_size
leftover = total_stds % group_size

group_word = "group" if groups == 1 else "groups"
student_word = "student" if leftover == 1 else "students"

print(f"There will be {groups} {group_word} with {leftover} {student_word} left over.")

#4:
total_pupils = int(input("Total number of pupils "))
sweets = int(input("tub of sweets"))

sweet_per_pupil = total_pupils // sweets
remaining = total_pupils% sweets

group_word = "group" if groups == 1 else "groups"
student_word = "student" if leftover == 1 else "students"

print(f"There will be {sweet_per_pupil}  with {remaining} left over.")