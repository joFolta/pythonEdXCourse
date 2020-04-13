# If function called with no arg, we get a traceback error.
# Thus, a default param value is set as None
def petSound(petType = None):
  if petType == 'dog':
    print('Woof!')
  elif petType == 'cat':
    print('Meow~')
  else:
    print('LOL!')



try:
  arg = input("Enter a pet name like dog, cat, or something else to hear it's sound: ")
except: 
  arg = None
petSound(arg)