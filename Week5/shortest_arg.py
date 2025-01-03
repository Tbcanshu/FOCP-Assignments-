#'''Write a program that takes a bunch of command-line arguments, and then prints out the shortest. If there is more than one of the shortest length, any will do. Hint: Don't overthink this. A good way to find the shortest is just to sort them'''
import sys
args = sys.argv[1:]

if args:
    shortest_arg = min(args, key=len) # finds the shortest argument in the args list by using the min() function with key=len, which compares the lengths of the arguments.
    print(f"The shortest argument is: '{shortest_arg}'")
else:
    print("No arguments provided.")