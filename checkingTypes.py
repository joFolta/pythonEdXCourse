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