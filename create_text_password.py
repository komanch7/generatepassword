import string
import random

# Default value register= ['lower', 'upper', 'mix']
def create_text_password(length, register='lower'):
    length = int(length)
    if type(length) == int and type(register) == str:
        if register == 'lower':
            letters = string.ascii_lowercase
            return ''.join(random.choice(letters) for i in range(length))
        elif register == 'upper':
            letters = string.ascii_uppercase
            return ''.join(random.choice(letters) for i in range(length))
        elif register == 'mix':
            letters = string.ascii_letters
            return ''.join(random.choice(letters) for i in range(length))
    else:
        return 'Enter variable length or register'

# 
if __name__ == "__main__":
    print ("Start programm play!\n")
    print (create_text_password("14", register='mix'))
    print ("\nEnd programm play!")
else: 
    print ("An error has occurred! Unable to start")