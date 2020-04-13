# Quasi-infinite loop
# ie. infinite loop with break
# Exit with 'done'
while True:
  line = input('> ')
  if line == 'done':
    break
  print(line)

print('Done!')