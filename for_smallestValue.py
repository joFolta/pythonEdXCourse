# nums = [5, 2, 6, 1, -3, 2]
# smaller = nums[0]
# for num in nums:
#   if num < smaller:
#     smaller = num
# smallest = smaller
# print('The smallest number is '+ str(smallest))

nums = [5, 2, 6, 1, -3, 2]
smaller = None
for num in nums:
  if smaller is None:
    smaller = num
  elif num < smaller:
    smaller = num
smallest = smaller
print('The smallest number is '+ str(smallest))