a = 1
print(a, type(a))

b = 98.6
print(b, type(b))

c = 'hello world'
print(c, type(c))

d = 120
print(d, type(d))
# float() does not appear to "reassign" value of d; just RETURNS a floating point value for d
print('using float function to return floating point value of d:')
print(d, float(d), type(float(d)))


# python2 vs python3

# PYTHON3
# print(9/2)
# 4.5 (automatically returns floating point)


# PYTHON2
# print(9/2)
# 4 (stays as integer and loses 0.5)

# thus, solution was to divide floats not integers: 
# print(9.0/2.0)
# 4.5

# OR

# print(99/100)
# 0 (stays as integer and loses 0.99)

# thus, solution was to divide floats not integers: 
# print(99.0/100.0)
# 0.99