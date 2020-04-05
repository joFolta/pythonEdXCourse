# Elevator Floor Converter (European -> US)

# In European countries, the ground floor is the 0th floor, 
# But in the US it is the 1st floor.

inp = input('European floor?')
usf = int(inp) + 1
print('Equivalent US floor:', usf)