import sys

#////////////////////////////Setting up board////////////////////////////////////
board = []

for x in range(5):
    board.append(["O"] * 5)

def print_board(board):
    for row in board:
        print " ".join(row)


#///////////////////////////Getting input//////////////////////////////////////////
def user_row():
	get_row = raw_input("Enter ship row between 1 and 5")
	if int(get_row) == False:
		print "You must enter an integer between 1 and 5"
		get_row = raw_input("Enter ship row...")
		if int(get_row) == False:
			sys.exit()

def user_col():
    get_col = raw_input("Enter ship col between 1 and 5")
    if int(get_col) == False:
        print "You must enter an integer between 1 and 5"
        get_col = raw_input("Enter ship col...")
        if int(get_col) == False:
        	sys.exit()

#/////////////////////////Intro//////////////////////////////////////////////////////
print "Let's play Battleship!"
print "This is your ocean"
print_board(board)


#////////////////////////Placing ships//////////////////////////////////////////////
print "Player 1 your up!"
print "Player 2 look away!"
print "Place your ship..."

user1_ship = [user_row(), user_col()]

print_board(board)
print "Player 2 your up!"
print "Player 1 look away!"
print "Place your ship..."

user_2 = [user_row(), user_col()]


#///////////////////////guesswork?//////////////////////////////////////////////////
print "Player 1 your turn..."
user1_guess = [user_row(), user_col()]

if user1_guess == user2_ship:
	board[user1_guess[0]][user1_guess[1]] == "H"
	print "You won!"
	print "PLAYER 1 slayed PLAYER 2!"
else:
	board[user1_guess[0]][user1_guess[1]] == "M"
	print "You missed!"

print_board(board)

print "Player 2 your turn..."
user2_guess = [user_row(), user_col()]

if user2_guess == user1_ship:
	board[user2_guess[0]][user_guess[1]] == "H"
	print "You won!"
	print "PLAYER 2 slayed PLAYER 1!"
else:
	board[user2_guess[0]][user_guess[1]] == "M"
	print "You missed!"




