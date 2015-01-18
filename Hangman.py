import random
#Word Bank
things = ['Things','chair','book','building','thermometer','watch']
animals = ['Animals','fish','horse','kangaroo','lion','penguin']
countries = ['Countries','china','united states','canada','brazil','indonesia']
city_items = ['Things in the City','taxi','skyscraper','street','mall','university']
plants = ['Plants','garlic','bamboo','clover','lavender','mango']
word = [things,animals,countries,city_items,plants]
#Reused Variables
symbol = " >"

#Functions
def endGame(attempts):
	choice = '0'
	keepGoing = True
	while choice == '0':
		choice=raw_input("Continue? Y or N" + str(symbol)) or '0'
		if choice == '0':
			print "We need an input!"
		elif choice != 'Y' and choice != 'N':
			print "We need the correct input!"
			choice = '0'
	if choice == 'N':
		keepGoing = False
	choice = '0'
	if attempts == 0:
		print "You ran out of attempts! :("
		keepGoing = False
	return keepGoing;

def wordDisplayinitial(word,guessed):
	temp=[]
	for n in word:
		temp.append('_')
	return temp
		
def wordDisplaygame(word,guessed,unknown):
	temp=unknown
	counter = 0
	for n in word:
		for m in guessed:
			if n==m:
				temp[counter] = n
				break;
			else:
				temp[counter] = '_'
		counter=counter+1
	return temp

	
def printBoard (word):
	for n in word:
		print n,
	print "\n"
	
#main code	
playing = True
unknown = []
guessed = []
counter = 0
listChoice=random.randint(0, 4)
wordChoice=random.randint(1, 5)
legnth = len(word[listChoice][wordChoice])
unknown = wordDisplayinitial(word[listChoice][wordChoice],guessed)
attempts = legnth*2.5
print"Welcome to Hangman"
raw_input("Enter to Start" + str(symbol))
while playing:
	print "Catagory: ", word[listChoice][0]
	print word[listChoice][wordChoice]
	printBoard(unknown)
	print "Attempt Remaining: %d" %attempts
	guess = raw_input("What is your guess" + str(symbol))
	guessed.append(guess)
	unknown = wordDisplaygame(word[listChoice][wordChoice],guessed,unknown)
	counter = counter+1
	attempts = attempts-1
	playing = endGame(attempts)