# Quasi-infinite loop
# ie. infinite loop with break
# Exit with 'done'
# while True:
#   line = input('> ')
#   if line == 'done':
#     break
#   print(line)

# print('Done!')

# 'break' skips out of the loop
# 'continue' skips to the top of the loop (skips anything below the continue and keeps looping)

while True:
  line = input('> ')
  # if list character is '#', then skip the print and loop again
  if line[0] == '#':
    continue
  if line == 'done':
    break
  print(line)

print('Done!')