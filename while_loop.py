def launchCountDown(initialNumber):
  while initialNumber > 0:
    print(initialNumber)
    initialNumber = initialNumber - 1
  print('********************')
  print('********************')
  print('********************')
  print('*****BLASTOFF!******')
  print('********************')
  print('********************')
  print('********************')

strInput = input('Enter the launch countdown number: ')
launchCountDown(strInput)