def launchCountDown(startingNum):
  counterPrinter(startingNum)
  blastoff()

def counterPrinter(initialNumber):
  while initialNumber > 0:
    print(initialNumber)
    initialNumber = initialNumber - 1
  
def blastoff():
  print('********************')
  print('********************')
  print('********************')
  print('*****BLASTOFF!******')
  print('********************')
  print('********************')
  print('********************')

strInput = input('Enter the launch countdown number: ')
launchCountDown(strInput)