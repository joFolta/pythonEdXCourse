# Exercise: Write a program which repeatedly reads numbers until the user enters 'done'. Once 'done' is entered, print out the total, count, and average of the numbers. If the user enters anything other than a number, detect their mistake using try and except and print an error message and skip to the next number. 

sum = 0.0
count = 0
while True:
  data = input('Enter a number: ')
  if data == 'done':
    break
  try:
    sum += data
    count += 1
  except:
    print('Invalid input')
print(sum, count, sum/count)