import random
rolls = int(input("How many rolls? "))
num1 = 0
num2 = 0
num3 = 0
num4 = 0
num5 = 0
num6 = 0
for i in range(rolls):
	diceRoll = int(random.randint(1,6))
	if diceRoll == 0:
		pass
	elif diceRoll == 1:
		num1 = num1 + 1
	elif diceRoll == 2:
		num2 = num2 + 1
	elif diceRoll == 3:
		num3 = num3 + 1
	elif diceRoll == 4:
		num4 = num4 + 1
	elif diceRoll == 5:
		num5 = num5 + 1
	elif diceRoll == 6: 
		num6 = num6 + 1
	else:
		pass
print("1s - " + str(num1))
print("2s - " + str(num2))
print("3s - " + str(num3))
print("4s - " + str(num4))
print("5s - " + str(num5))
print("6s - " + str(num6))
print( )
print("1s - " + str(num1 * 100 / rolls) + "%")
print("2s - " + str(num2 * 100 / rolls) + "%")
print("3s - " + str(num3 * 100 / rolls) + "%")
print("4s - " + str(num4 * 100 / rolls) + "%")
print("5s - " + str(num5 * 100 / rolls) + "%")
print("6s - " + str(num6 * 100 / rolls) + "%")