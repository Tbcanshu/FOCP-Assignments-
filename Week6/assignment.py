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



