#1:
def int_value(num):
    # takes in an integer as parameter and returns true if the parameter is in given range 
    if num in range(0, 101):
        return True  
    else:
        return False  
test_numbers = [45,90, 786,100,900]
for value in test_numbers:
    result = int_value(value)
    print(result)
    
#2:
def case_checker(string):
    """This function takes in a string and counts the number of uppercase and lowercase letters in it."""
    uppercase_no= 0
    lowercase_no = 0
    for char in string:
        if char.isupper(): #checks if current character is uppercase using .isupper() method
            uppercase_no += 1 
        elif char.islower():
            lowercase_no += 1
    print(f"Uppercase letters: {uppercase_no}")
    print(f"Lowercase letters: {lowercase_no}")

# Testing  the function
case_checker("MEDical DIAgnosiS")

#3:


#4:
def remove_char(str): 
    """This function takes in a string as a parameter and removes the last character of the string if its length is longer than 1."""
    if len(str) > 1:
        return str[:-1]
    else:
        return "no changes"

string = input("Enter a word: ")
result = remove_char(string)  
print(result) 


#5:
def cel_to_fht(celsius):
    """Converts Celsius to Fahrenheit."""
    fahrenheit = celsius * (9 / 5) + 32
    return fahrenheit

def fht_to_cel(fahrenheit):
    """Converts Fahrenheit to Celsius."""
    celsius = (fahrenheit - 32) * 5 / 9
    return celsius

# Convert Celsius to Fahrenheit
celsius_temp = float(input("Enter temperature in Celsius: "))
print(f"{celsius_temp}C is equivalent to {cel_to_fht(celsius_temp):.2f}F")

# Convert Fahrenheit to Celsius
fahrenheit_temp= float(input("Enter temperature in Fahrenheit: "))
print(f"{fahrenheit_temp}F is equivalent to {fht_to_cel(fahrenheit_temp):.2f}C")# 2f formats result to 2 decimal places

#6:
def to_fahrenheit(temp):
    """converts celsius to fahrenheit."""
    celsius = float(temp[:-1])  # Extract the numeric part
    fahrenheit = celsius * 9 / 5 + 32  # Convert to Fahrenheit
    return f"{fahrenheit:.2f}F"

given_temp = input("Enter your temperature in Celsius: ")
if given_temp[-1].lower() == 'c':  # Check if input ends with 'C' or 'c'
    print(f"{given_temp} is equivalent to {to_fahrenheit(given_temp)}")
else:
    print("Invalid input! Please enter a temperature ending with 'C'.")

#7:
from statistics import mean


def read_temperatures():
    """
    Reads 6 temperatures from the user, calculates and displays the maximum, minimum,
    and mean of these temperatures.
    """
    temperatures = []
    for i in range(6):
        temp = float(input(f"Enter temperature {i+1}: "))
        temperatures.append(temp)

    max_temp = max(temperatures)
    min_temp = min(temperatures)
    mean_temp = mean(temperatures)

    return max_temp, min_temp, mean_temp


max_temp, min_temp, mean_temp = read_temperatures()


print(f"The max temperature is: {max_temp},\nThe min temperature is: {
      min_temp},\nThe mean temperature is: {mean_temp}")

#8:
from statistics import mean

def read_temperatures():
    """
    Reads temperatures from the user until an empty input is given,
    then calculates and displays the maximum, minimum, and mean of these temperatures.
    """
    temperatures = []
    i = 0

    while True:
        entered_temp = input(f"Enter temperature {i + 1} (or press Enter to exit): ")
        
        if len(entered_temp) == 0:
            break  # Exit the loop if the user presses Enter without input
        
        
        temp = float(entered_temp) 
        temperatures.append(temp)  
        i += 1  # Increment the counter only if a valid temperature is entered
        

    if temperatures: 
        max_temp = max(temperatures)
        min_temp = min(temperatures)
        mean_temp = mean(temperatures)

        return max_temp, min_temp, mean_temp
    

# Call the function and unpack the results
max_temp, min_temp, mean_temp = read_temperatures()

print(f"The max temperature is: {max_temp},\nThe min temperature is: {min_temp},\nThe mean temperature is: {mean_temp:.2f}")

