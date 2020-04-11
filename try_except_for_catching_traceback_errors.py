print('...initializing program...')

defined = input('Is x defined? Please enter True or False:')
if defined == True:
  x = "I'm real!"

# Dangerous Line (may blow up)
# if (x):
#   print("x is defined! x is '"+x+"'")

try:
  if (x):
    # Dangerous Line nested inside try/except block
    print("x is defined! x is '"+x+"'")
except:
  print('THE PROGRAM BLEW UP!!!')
  print('But whew! I (AKA the except of the try/except block) just saved you from getting stuck back there...')