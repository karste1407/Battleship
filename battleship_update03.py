from random import randint


board = []

for x in range(5):
    board.append(["O"] * 5)

def print_board(board):
    for row in board:
        print " ".join(row)

print "Let's play Battleship!"
print "Attack ships: 2x2"
print_board(board)

def random_row(board):
    return randint(1, len(board[0]) - 1)

def random_col(board):
    return randint(1, len(board[0]) - 1)

init_attackShip_row = random_row(board)
init_attackShip_col = random_col(board)
attackShip_row = [init_attackShip_row, init_attackShip_row + 1]
attackShip_col = [init_attackShip_col, init_attackShip_col + 1]

#Debugging
print attackShip_row
print attackShip_col

# Everything from here on should go in your for loop!
# Be sure to indent four spaces!
for turn in range(6):
    max_turn = 5
    print "Turn", turn + 1
    guess_row = int(raw_input("Guess Row:")) -1
    guess_col = int(raw_input("Guess Col:")) -1

    if board[attackShip_row[0]][attackShip_col[0]] == "H" and board[attackShip_row[1]][attackShip_col[1]] == "H":
        print "You sunk my attack ship!"
        print "YOU WON!"
        break
    elif guess_row in attackShip_row and guess_col in attackShip_col:        
		board[guess_row][guess_col] = "H"
		print "You hit my attack ship!"
		print print_board(board)
    else:
        if (guess_row < 0 or guess_row > 4) or (guess_col < 0 or guess_col > 4):
            print "Oops, that's not even in the ocean."
        elif(board[guess_row][guess_col] == "M"):
            print "You guessed that one already."
        else:
            print "You missed my battleship!"
            board[guess_row][guess_col] = "M"
        # Print (turn + 1) here!
        print_board(board)
    if turn == max_turn:
        print "Game Over"
        break



raw_input()
