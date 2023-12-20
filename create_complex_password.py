import string
import random

# Function for creating a password, pass a number as an argument, but you can also pass a number as a string - F]`DO93.Gk!3vR*G{T!P`P#yQzrh+@vC
def create_complex_password(length):
    length = int(length)
    # Checking for the existence of a variable
    if type(length) == int:
        characters = string.ascii_letters + string.digits + string.punctuation
        password = ''.join(random.choice(characters) for _ in range(length))
        return password
    else:
        return 'Enter variable length'

# 
if __name__ == "__main__":
    print ("Start programm play!\n")
    print (create_complex_password("12"))
    print ("\nEnd programm play!")
else: 
    print ("An error has occurred! Unable to start")