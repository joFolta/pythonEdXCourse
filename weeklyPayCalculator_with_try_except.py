print('***Welcome to Weekly Pay Calculator***')
print('This program can calculate weekly pay including overtime pay (1.5x)')
print('For normal mode, type "normal"')
print('For error-catch or advanced mode, type "advanced"')

try:
  modeSelection = input('Please select a mode: ')
except:
  print('Oops! Please enter a either "normal" or "advanced" typed w/in quotes.')
  try:
    modeSelection = input('One more try. Please select a mode: ')
  except:
    print('WARNING: Invalid mode entered')
    print('...shutting down program...')
    exit()

if modeSelection != 'normal' and modeSelection != 'advanced':
    print('Oops! Please enter a either "normal" or "advanced" typed w/in quotes.')
    modeSelection = input('One more try. Please select a mode: ')


if modeSelection == 'normal':
  # Normal Mode: Calculate weekly pay with overtime
  print('...entering NORMAL MODE...')
  hours = input('Enter Hours:')
  rate = input('Enter Rate:')
  regHours = hours
  overtimeHours = 0
  overtimeRate = rate * 1.5
  if hours > 40:
    overtimeHours = hours-40
    hours = 40
  pay = hours * rate + overtimeHours * overtimeRate
  print("Pay: "+str(pay))

elif modeSelection == 'advanced':
  # Advanced Mode: Normal mode plus error catching with try/except blocks
  print('...entering ADVANCED MODE...')
  try:
    hours = input('Enter Hours:')
  except: 
    print('Error: Please enter a number next time. ')
    print('...terminating program...')
    exit()
  try:  
    rate = input('Enter Rate:')
  except:
    print('Error: Please enter a number next time. ')
    print('...terminating program...')
    exit()
  regHours = hours
  overtimeHours = 0
  try:
    overtimeRate = rate * 1.5
  except:
    print('Error: Cannot multiply non-numeric values. ')
    print('Error: Please enter numbers next time. ')
    print('...terminating program...')
    exit()
  if hours > 40:
    try:
      overtimeHours = hours-40
    except:
      print('Error: Hours must be a number. ')
      print('...terminating program...')
      exit()
    hours = 40
  pay = hours * rate + overtimeHours * overtimeRate
  print("Pay: "+str(pay))

else:
  print('WARNING: Invalid mode entered')
  print('...shutting down program...')
  exit()