import time, os, sys
from random import randint

os.system('clear')

		
print('Welcome!')
print('Loading')
print('-------')
time.sleep(0.2)
os.system('clear')

print('Welcome!')
print('Loading')
print('+------')
time.sleep(0.2)
os.system('clear')

print('Welcome!')
print('Loading')
print('++-----')
time.sleep(0.2)
os.system('clear')

print('Welcome!')
print('Loading')
print('+++----')
time.sleep(0.2)
os.system('clear')

print('Welcome!')
print('Loading')
print('++++---')
time.sleep(0.2)
os.system('clear')

print('Welcome!')
print('Loading')
print('+++++--')
time.sleep(0.2)
os.system('clear')

print('Welcome!')
print('Loading')
print('++++++-')
time.sleep(0.2)
os.system('clear')

print('Welcome!')
print('Loading')
print('+++++++')
time.sleep(0.2)
os.system('clear')


restart = 1
while restart == 1:
	os.system('clear')
	print('Choose a difficulty')
	print('1 - A number between 1 and 10')
	print('2 - A number between 1 and 20')
	print('3 - A number between 1 and 50')
	print('4 - A number between 1 and 100')
	print('5 - A number between 1 and 1000')
	difficulty = input('>> ')
	if difficulty == 1:
		lower = 0
		upper = 10
	elif difficulty == 2:
		lower = 0
		upper = 20
	elif difficulty == 3:
		lower = 0
		upper = 50
	elif difficulty == 4:
		lower = 0
		upper = 100
	elif difficulty == 5:
		lower = 0
		upper = 1000
	else:
		print('Sorry, I didn\'t understand. Setting difficulty to 3')
		lower = 0
		upper = 50
	time.sleep(1)
	os.system('clear')	
	randNum = randint(lower, upper)

	print('I\'m thinking of a number!')
	print('What do you think it is?')
	numberOfTries = 0
	reset = 1
	while reset == 1:
		guess = input('>> ')
		numberOfTries = numberOfTries + 1

		if guess == randNum:
			reset = 0
		
		elif guess > randNum:
			print('Lower')

		elif guess < randNum:
			print('Higher')	
	
	print('Correct! It took you ' + str(numberOfTries) + ' tries')
	print('Press 1 to go again or 2 to exit')
	choice = input('>>')
	restart = choice
	
sys.exit()
	
	
	
	
	
	
	
	