#Write a program that takes a URL as a command-line argument and reports whether or not there is a working website at that address. Hint: You need to get the HTTP response code. Another Hint: StackOverflow is your friend
import sys
import requests

# Get the URL from command-line arguments
url = sys.argv[1] if len(sys.argv) > 1 else None

# Check if a URL is provided
if not url:
    print("Please provide a URL.")
    sys.exit(1)

try:
    # Send a GET request to the specified URL
    response = requests.get(url)
    # Raise an exception for HTTP error status codes
    response.raise_for_status()  
    print("Website is working.")
except requests.exceptions.RequestException as e:
    # Catch any request-related exceptions and print the error message
    print(f"Error accessing the website: {e}")