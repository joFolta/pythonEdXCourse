# Gross Pay Calculator:
# A program to prompt the user for hours and rate per hour to compute gross pay

hours = input('How many hours do you work per week?')
print('*** You work '+str(hours)+' hours per week.')

rate = input('What is your hourly pay rate?')
print('*** Your hourly pay rate is $'+str(rate)+'/hr.')

pay = hours * rate
print('*** Your weekly gross pay is calculated to be $'+str(pay)+'.')