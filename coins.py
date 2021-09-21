# name of student: tycho hartingsveld
# number of student: 99062718
# purpose of program: 
# function of program:
# structure of program: 

coinsReturnedList = [] # here we create a list called coinsReturnedList

toPay = int(float(input('Amount to pay: '))* 100) # fill the given amount the user needs to pay. then converts that to cents
payed = int(float(input('Payed amount: ')) * 100) # fill the given amount the user has payed. then converts that to cents
change = payed - toPay # calculate the amount of change the user needs to be given

if change > 0: # checks if the change is more than 0 cents
  coinValue = 500 # makes the value of coins 5 euros
  
  while change > 0 and coinValue > 0: # this will keep on running as long as change and coinvalue are more than 0
    nrCoins = change // coinValue # this will device change by coinvalue and round the answer to the nearest number. that number will then by stored in nrCoins

    if nrCoins > 0: # if nrcoins is greater than 0 this piece of code will run
      print('return maximal ', nrCoins, ' coins of ', coinValue, ' cents!' ) # this will print the maximum amount of coins allowed to be returned by the user
      nrCoinsReturned = int(input('How many coins of ' + str(coinValue) +  ' cents did you return? ')) # this will ask the user to input how many coins they have returned. the answer will be stored inside nrCoinsReturned
      change -= nrCoinsReturned * coinValue # the amount of user returned coins will be multiplied by the current coinvalue. then it will be subtracted off of change
      coinsReturnedList.append([nrCoinsReturned, coinValue]) # here we attach the coins returned and coinvalue of the current loop at the end of the coinsreturnedlist list

# comment on code below: here the coinvalue will be made lower every loop until it reaches 0
    if coinValue == 500:
      coinValue = 300
    elif coinValue == 300:
      coinValue = 200
    elif coinValue == 200:
      coinValue = 50
    elif coinValue == 50:
      coinValue = 20
    elif coinValue == 20:
      coinValue = 10
    elif coinValue == 10:
      coinValue = 5
    elif coinValue == 5:
      coinValue = 2
    elif coinValue == 2:
      coinValue = 1
    else:
      coinValue = 0

if change > 0: # if the change is higher than 0 at the end of the loop this piece of code will execute
  print('Change not returned: ', str(change) + ' cents')
else:
  print('done')

print("--------------------------")
for x in coinsReturnedList: # this piece of code here prints a summery of all coins that have been returned by the user
  print("You have returned " + str(x[0]) + " coins of " + str(x[1]) + " cents")
print("--------------------------")