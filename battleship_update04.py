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
    state = False
    while state == False:
        try:
            get_row = int(raw_input("enter ship row between 1 and 5: "))
        except ValueError:
            print "Invalid input. Try again..."
        else:
            state = True
    return int(get_row)

def user_col():
    state = False
    while state == False:
        try:
            get_col = int(raw_input("enter ship col between 1 and 5: "))
        except ValueError:
            print "Invalid input. Try again..."
        else:
            state = True
    return int(get_col)
    
#/////////////////////////Intro//////////////////////////////////////////////////////

print "PLAYER 1!"
print "Place your ship..."
print ""
print "PLAYER 2 LOOK AWAY!"
raw_input("press enter to proceed...")

#Not shure if this will call the two functions chronologic and store them as index 0 and 1 in my array. That is what I want it to do
user1_ship = [user_row(), user_col()]

if (user1_ship[0] < 1 or user1_ship[0] > 5) or (user1_ship[1] < 1 or user1_ship[1] > 5):
    print "Your trying to place your ship outside of the ocean!!!"
    user1_ship = [user_row(), user_col()]


print "////////////////////////////////////////////////////////"
print "////////////////////////////////////////////////////////"
print "////////////////////////////////////////////////////////"
print "////////////////////////////////////////////////////////"
print "////////////////////////////////////////////////////////"
print "////////////////////////////////////////////////////////"
print "////////////////////////////////////////////////////////"
print "////////////////////////////////////////////////////////"
print "////////////////////////////////////////////////////////"
print "////////////////////////////////////////////////////////"
print "////////////////////////////////////////////////////////"
print "////////////////////////////////////////////////////////"
print "////////////////////////////////////////////////////////"
print "////////////////////////////////////////////////////////"
print "////////////////////////////////////////////////////////"

print "PLAYER 2"
print "Place your ship..."
print ""
print "PLAYER 1 LOOK AWAY!"
raw_input("press enter to proceed...")


user2_ship = [user_row(), user_col()]

if (user2_ship[0] < 1 or user2_ship[0] > 5) or (user2_ship[1] < 1 or user2_ship[1] > 5):
    print "Your trying to place your ship outside of the ocean!!!"
    user2_ship = [user_row(), user_col()]


print "////////////////////////////////////////////////////////"
print "////////////////////////////////////////////////////////"
print "////////////////////////////////////////////////////////"
print "////////////////////////////////////////////////////////"
print "////////////////////////////////////////////////////////"
print "////////////////////////////////////////////////////////"
print "////////////////////////////////////////////////////////"
print "////////////////////////////////////////////////////////"
print "////////////////////////////////////////////////////////"
print "////////////////////////////////////////////////////////"
print "////////////////////////////////////////////////////////"
print "////////////////////////////////////////////////////////"
print "////////////////////////////////////////////////////////"
print "////////////////////////////////////////////////////////"
print "////////////////////////////////////////////////////////"

#///////////////////////guesswork?//////////////////////////////////////////////////
#Maybe while loops inside while loops is not the best way of running the code over and over until someone sinks the other persons ship
#What Im expecting is the first inside while loop to raise an error if the player wins (same with second inner-while loop) and then the outer while loop catches that error and then breaks the entire while loop.
while True:
    try:
        while True:
            print "Player 1 your turn"
            user1_guess = [user_row(), user_col()]
            if user1_guess == user2_ship:
                board[user1_guess[0]][user1_guess[1]] == "H"
                print "PLAYER 1 WINS!"
                raise
                break
            else:
                board[user1_guess[0]][user1_guess[1]] == "M"
                print "You missed"
            break

        while True:
            user2_guess = [user_row(), user_col()]
            print "Player 2 your turn"
            if user2_guess == user1_ship:
                board[user2_guess[0]][user2_guess[1]] == "H"
                print "PLAYER 2 WINS!"
                raise
            	break
            else:
                board[user2_guess[0]][user2_guess[1]] == "M"
                print "You missed"
            break
    except:
        break


