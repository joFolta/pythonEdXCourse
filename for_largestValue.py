# my attempt at finding largestValue with a for loop
nums = [5, 2, 6, 1, -3, 2]
larger = 0
for i in nums:
  if i > larger:
    larger = i
largest = larger
print('The largest number is '+ str(largest))

