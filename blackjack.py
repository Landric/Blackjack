from random import shuffle

def createDeck(shoes=1):
	suits = ["C", "D", "H", "S"]
	deck = []
	
	for s in suits:
		for i in range(2, 11):
			deck.append(("{0}{1}".format(i, s), i))
		
		deck.append(("{0}{1}".format("J", s), 10))
		deck.append(("{0}{1}".format("Q", s), 10))
		deck.append(("{0}{1}".format("K", s), 10))
		deck.append(("{0}{1}".format("A", s), 1))
	
	new_deck = []
	for s in range(shoes):
		new_deck = new_deck + list(deck)
	
	shuffle(new_deck)
	
	return new_deck

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
	print "###################################"
	
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
	player_cash = 200
	dealer_cash = 200

	s = shoes("How many shoes would you like to play with: ")
	
	while player_cash > 0 and dealer_cash > 0:
		player_cash, dealer_cash = newRound(createDeck(s),  player_cash, dealer_cash)
		
	return player_cash > 0
	
def printCash(player_cash, dealer_cash):
	print
	print "###################################"
	print "Dealer's cash: $"+str(dealer_cash)
	print "Your cash: $"+str(player_cash)
	
def newRound(deck, player_cash, dealer_cash):
	BET_AMOUNT = 50 #Global bet amount for testing

	printCash(player_cash, dealer_cash)
	
	player_hand = []
	dealer_hand = []
	for i in range(2):
		player_hand.append(deck.pop())
		dealer_hand.append(deck.pop())
		
	printCards(dealer_hand, player_hand, True)
	
	if calculateHandValue(player_hand) == 21:
		player_cash = player_cash + BET_AMOUNT
		dealer_cash = dealer_cash - BET_AMOUNT
		print "Blackjack!"
		print
	else:
		lose = False
		
		while(hit()):
			player_hand.append(deck.pop())
			printCards(dealer_hand, player_hand, True)
			if calculateHandValue(player_hand) > 21:
				lose = True
				printCards(dealer_hand, player_hand, False)
				player_cash = player_cash - BET_AMOUNT
				dealer_cash = dealer_cash + BET_AMOUNT
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
				player_cash = player_cash - BET_AMOUNT
				dealer_cash = dealer_cash + BET_AMOUNT
				print "The dealer beat you! Better luck next time!"
			else:
				player_cash = player_cash + BET_AMOUNT
				dealer_cash = dealer_cash - BET_AMOUNT
				print "You win! Well done!"
			print
			
	return player_cash, dealer_cash

def playAgain():
	accepted_answers = ["y", "Y", "n", "N"]
	answer = raw_input("Would you like to play again (y/n): ")
	print
	while answer not in accepted_answers:
		answer = raw_input("Please answer y or n: ")
		print
	return answer in ["y", "Y"]
	
if __name__ == '__main__':
	
	games_played = 0
	games_won = 0
	
	play = True
	while(play):
		if(newGame()):
			games_won = games_won + 1
		games_played = games_played + 1
		
		print "Won {0} of {1} games".format(games_won, games_played)
		
		play = playAgain()
	print "Goodbye!"