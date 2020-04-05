# Python2 
# input(): evaluates the string entered (eg. converts to integer); has security issues
# vs 
# raw_input(): does not evaluate the string entered; equivalent to input() in Python3

# Code emulated from https://stackoverflow.com/a/21122817:

# PYTHON2 INPUT() EVALUATES THE STRING ENTERED
print('*****PYTHON2 INPUT() EVALUATES THE STRING ENTERED*****')
theOneWhoMustNotBeNamed = "Voldemort"
yourName = input('Enter your name (do not enter theOneWhoMustNotBeNamed...shudder): ')
print("AHHHH!!!!!!! $#$#! It's "+yourName+'!!!!')

# Security considerations with Python 2.7's input:
# User can call a function
print('*****SECURITY CONSIDERATIONS WITH PYTHON 2 INPUT()*****')
print('User can call a function within the input(eg. delete system files)')
print('call another input() within the "Enter your name:" input prompt, for example, input("Enter your MasterCard Info Here: ")')
yourName = input('Enter your name: ')
print("I've taken your MastCard Info. MUHAHAHAHA!!!!")
