#Kyle Pullen
#This is a timer for poker tournaments. Blinds double each round.
import time
import os

print("This is the timer")

# Variables to keep track and display
round = 1
sec = 00
min = 10
small = 5
big = 10
nextMin = 60
nextSec = 00

def breakRound():

	min = 10 
	sec = 00
	while True:
		os.system('clear')

		print ("This is the break round\n ")
		print (str(min) + " Minutes " + str(sec) + " seconds remaining in the break ")
		time.sleep(1)
		sec = sec - 1
		if sec == -1:
			min = min - 1
			sec = 59

		if min == -1:
			min = 10
			sec = 00
			nextMin = 60
			nextSec = 00
			break
	return



while True:
	os.system('clear')
	print (str(min) + " Minutes " + str(sec) + " seconds remaining in round " + str(round))
	print ("\nSmall Blind: " + str(small) + "\t\t Big Blind: " + str(big))
	print ("\nNext break in " + str(nextMin) + " mins " + str(nextSec) + " seconds")

	time.sleep(1)

	nextSec = nextSec - 1
	if nextSec == -1:
		nextMin = nextMin - 1
		nextSec = 59

	sec = sec - 1
	if sec == -1:
		min = min - 1
		sec = 59

	if nextMin == -1:
		breakRound()

	if min == -1:
		min = 10
		sec = 0
		round = round + 1
		small = small * 2
		big = big * 2
	os.system('clear')
	




