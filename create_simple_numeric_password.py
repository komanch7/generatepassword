from random import randint

# Only Numeric
def create_simple_numeric_password(length):
    length = int(length)

    if type(length) == int:
        password = [randint(0, 9) for i in range(length)]
        passwordres = ''
        for i in password:
            passwordres += str(i)
        return passwordres
    else:
        return 'Enter variable length'

# 
if __name__ == "__main__":
    print ("Start programm play!\n")
    print (create_simple_numeric_password("12"))
    print ("\nEnd programm play!")
else: 
    print ("An error has occurred! Unable to start")