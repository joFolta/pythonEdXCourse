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


# "is" operator
# implies "is the same as"
# similar to, but strong than "=="
# there is also an "is not" operator
# us "is" for True False None

# ie. "is" checks to see if the object is the same object, while == just checks if they are equivalent.