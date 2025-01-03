#1:
def int_to_bin(n):
    if n <= 0:
        return("Error: Input must be a positive integer.")
    return bin(n)[2:] #function that converts an integer to its binary representation as a string
number = int(input("Enter the number for conversion into binary: "))
print(int_to_bin(number)) 

#2:
def int_factors(n):
    if n <= 0:
        print("Error: Input must be a positive integer.")
        return []  # Return an empty list
    
    factors = []
    for i in range(1, n + 1):
        if n % i == 0:
            factors.append(i)
    
    return factors
#testing:
number = int(input("Enter the number for factorisation: "))
print(int_factors(number))  

#3:
from math import sqrt
def is_prime(n):
    if n <= 1:
        return "Please enter value greater than 1."

    for i in range(2, int(sqrt(n)) + 1):
        if n % i == 0:
            return False  # n is divisible by i, so it's not prime
    return True  # n is prime if no divisors were found

#testing:
prime = int(input("Enter a number for checking if its a prime number: "))
print(is_prime(prime))

#4:
def encrypt_message(message):
    # The replace(" ", "") method is used to remove all spaces from the string. This creates a new string no_spaces that contains the original message without any spaces.
    no_spaces = message.replace(" ", "")
    # The slicing operation [::-1] is used to reverse the string. This creates a new string encrypted that is the reverse of no_spaces.
    encrypted = no_spaces[::-1]
    return encrypted

message = input("Type string for encryption: ")
print(encrypt_message(message))

#5:
import random
import string

def encrypt_with_random_letters(message):
    # Generate a random interval between 2 and 20
    interval = random.randint(2, 20)
    
    # Create a list to hold the encrypted message
    encrypted_message = []
    key = []  #store all the original characters that are replaced
    
    # Iterate through the message and fill in the gaps
    for i in range(len(message)):
        if (i % interval) == 0:  # If the index is a multiple of the interval
            encrypted_message.append(message[i])  # Add the character from the message
        else:
            # Add a random letter from the alphabet
            random_letter = random.choice(string.ascii_lowercase)
            encrypted_message.append(random_letter)
    
    # Join the list into a single string
    encrypted_message_str = ''.join(encrypted_message)
    
    return encrypted_message_str, interval

#  testing
message = input("Enter the message for encryption: ")
encrypted_message, interval, key = encrypt_with_random_letters(message)

print(f"Original Message: {message}")
print(f"Encrypted Message: {encrypted_message}")
print(f"Interval: {interval}")
print(f"Key: {key}")

#6:
def decrypt_with_random_letters(encrypted_message, interval, key):
    decrypted_message = []
    key_index = 0

    for i in range(len(encrypted_message)):
        if i % interval == 0:
            decrypted_message.append(encrypted_message[i])  # Use the retained character
        else:
            decrypted_message.append(key[key_index])  # Use characters from the key
            key_index += 1

    return ''.join(decrypted_message)

encrypted_message = input("Enter the encrypted message: ")
interval = int(input("Enter the encryption interval: "))
key = input("Enter the key (comma-separated): ").split(',')

original_message = decrypt_with_random_letters(encrypted_message, interval, key)

print(f"Encrypted Message: {encrypted_message}")
print(f"Decrypted (Original) Message: {original_message}")



def unique_sorted_letters(input_string):
    # Convert the string to lowercase to ensure uniqueness is case-insensitive
    input_string = input_string.lower()
      # Use a set to get unique letters
    unique_letters = set(input_string)
    # Filter out non-letter characters and sort the result
    sorted_unique_letters = sorted([char for char in unique_letters if char.isalpha()])
    
    return sorted_unique_letters

print(unique_sorted_letters("uniqueness of a string"))
print(unique_sorted_letters("984157"))

#2:
def letters_in_either(word1, word2):
    """Return a sorted list of letters that appear in at least one of the two words."""
    return sorted(set(word1) | set(word2))

def letters_in_both(word1, word2):
    """Return a sorted list of letters that appear in both words."""
    return sorted(set(word1) & set(word2))

def letters_in_either_not_both(word1, word2):
    """Return a sorted list of letters that appear in either word, but not in both."""
    return sorted(set(word1) ^ set(word2))

print(letters_in_either("application", "aliases"))
print(letters_in_both("portability", "picsart"))
print(letters_in_either_not_both("hello", "worldd")) 

#3:
def main():
    # Dictionary to store countries and their capitals
    countries_capitals = {}

    while True:
        country = input("Enter the name of a country (or type 'exit' to quit): ").strip() #strip() method is used to remove any leading or trailing whitespace from the input.

        # Check if the user wants to exit
        if country.lower() == 'exit':
            print("Exiting the program")
            break

        # Check if the country is already in the dictionary
        if country in countries_capitals:
            print(f"The capital of {country} is {countries_capitals[country]}.")
        else:
            # If the capital is not known, ask the user to enter it
            capital = input(f"Enter the capital of {country}: ").strip()
            countries_capitals[country] = capital  # adds new entry to the countries_capitals dictionary
            print(f"Thank you!  {capital} has been added as the capital of {country}.")
main()

#4:
def frequency_analysis(message):
    # Normalize the message to lowercase
    message = message.lower()
    
    # Dictionary to store letter counts
    letter_count = {}
    
    # Count occurrences of each letter
    for char in message:
        if char.isalpha():  # Check if the character is a letter
            if char in letter_count:
                letter_count[char] += 1
            else:
                letter_count[char] = 1
    
    # Sort the letters by frequency (highest first) and then alphabetically
    sorted_letters = sorted(letter_count.items(), key=lambda item: (-item[1], item[0]))#tuple for sorting
    
    # Get the top six most common letters
    top_six = sorted_letters[:6]
    
    # Print the results
    print("The six most common letters are:")
    for letter, count in top_six:
        print(f"'{letter}': {count}")

# Example usage
message = "This is an example message to demonstrate frequency analysis."
frequency_analysis(message)
