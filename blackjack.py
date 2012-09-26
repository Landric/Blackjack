from random import shuffle

def createDeck(shoes=1):
	suits = ["C", "D", "H", "S"]
	deck = []
	
	for s in suits:
		for i in range(9):
			deck.append(("{0}{1}".format(i+2, s), i+2))
		
		deck.append(("{0}{1}".format("J", s), 10))
		deck.append(("{0}{1}".format("Q", s), 10))
		deck.append(("{0}{1}".format("K", s), 10))
		deck.append(("{0}{1}".format("A", s), 1))
	
	for s in range(shoes):
		deck = deck + list(deck)
	
	shuffle(deck)
	
	return deck

def calculateHandValue(hand):
	total = 0
	ace = False
	for c in hand:
		total = total + c[1]
		if not ace and c[1] == 1:
			ace = True
			
	if ace and total + 10 <= 21:
		total = total + 10
		
	return total

def printCards(dealer_hand, player_hand, hide_dealer):
	print "###################################"
	if hide_dealer:
		print "Dealer's hand:"
		print dealer_hand[0][0]+" ##"
		print "Total: Unkown"
	else:
		print "Dealer's hand:"
		for c in dealer_hand:
			print c[0]+" ",
		print
		print "Total: "+str(calculateHandValue(dealer_hand))
	print
	print "###################################"
	print
	
	print "Your hand:"
	for c in player_hand:
		print c[0]+" ",
	print
	print "Total: "+str(calculateHandValue(player_hand))
	print "###################################"
	print
	
def hit():
	accepted_answers = ["h", "H", "s", "S"]
	answer = raw_input("Do you want to hit (h) or stick (s): ")
	print
	while answer not in accepted_answers:
		answer = raw_input("Please answer h or s: ")
		print
	return answer in ["h", "H"]
	
def shoes(message):
	answer = raw_input(message)
	print
	try:
		return int(answer)
	except ValueError:
		return shoes("Please enter an integer: ")

def newGame():	
	deck = createDeck(shoes("How many shoes would you like to play with: "))
	player_hand = []
	dealer_hand = []
	for i in range(2):
		player_hand.append(deck.pop())
		dealer_hand.append(deck.pop())
		
	printCards(dealer_hand, player_hand, True)
	
	if calculateHandValue(player_hand) == 21:
		print "Blackjack! You win!"
		print
	else:
		lose = False
		
		while(hit()):
			player_hand.append(deck.pop())
			printCards(dealer_hand, player_hand, True)
			if calculateHandValue(player_hand) > 21:
				lose = True
				printCards(dealer_hand, player_hand, False)
				print "You're bust! Better luck next time!"
				print
				break
				
		if not lose:
			player_hand_value = calculateHandValue(player_hand)
			
			dealer_hand_value = calculateHandValue(dealer_hand)
			while dealer_hand_value < 17 or dealer_hand_value < player_hand_value:
				dealer_hand.append(deck.pop())
				dealer_hand_value = calculateHandValue(dealer_hand)
				
			printCards(dealer_hand, player_hand, False)
			if 21 >= dealer_hand_value >= player_hand_value:
				print "The dealer beat you! Better luck next time!"
			else:
				print "You win! Well done!"
			print
	
def playAgain():
	accepted_answers = ["y", "Y", "n", "N"]
	answer = raw_input("Would you like to play again (y/n): ")
	print
	while answer not in accepted_answers:
		answer = raw_input("Please answer y or n: ")
		print
	return answer in ["y", "Y"]
	
if __name__ == '__main__':
	play = True
	while(play):
		newGame()
		play = playAgain()
	print "Goodbye!"