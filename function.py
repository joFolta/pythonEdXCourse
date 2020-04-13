# If function called with no arg, we get a traceback error.
# Thus, a default param value is set as None
def petSound(petType = None):
  if petType == 'dog':
    print('Woof!')
  elif petType == 'cat':
    print('Meow~')
  else:
    print('LOL!')


# Use try/except block as input() crashes if nothing is entered
try:
  arg = input("Enter a pet name like dog, cat, or something else to hear it's sound: ")
except: 
  arg = None
petSound(arg)

# Variation of function by using return
def returnPetSound(petType = None):
  if petType == 'dog':
    return 'woof!'
  elif petType == 'cat':
    return 'meow~'
  else:
    return 'LOL!'

def printSentence(petType = None):
  print("The "+petType+" goes "+returnPetSound(petType)+". ")
  
try:
  newArg = input("To get a sentence, enter a pet type: ")
except:
  newArg = 'blank'
printSentence(newArg)