from random import randint
import os
os.system('clear')

# todo: 
# - multiple battleships
# - battleships with different sizes
# - multiplayer


board = []

for x in range(5):
    board.append(["O"] * 5)

def print_board(board):
    for row in board:
        print " ".join(row)

print ""
print "Let's play Battleship!"
print ""
print_board(board)
print ""

def random_row(board):
    return randint(0, len(board) - 1)

def random_col(board):
    return randint(0, len(board[0]) - 1)

# init multiple battles
ship_row = []
ship_col = []
while len(ship_row) < 4:
    row = random_row(board) + 1
    col = random_col(board) + 1
    if row in ship_row:
    	rmatch = ship_row.index(row)
	if col in ship_col:
    		cmatch = ship_col.index(col)
		if rmatch == cmatch:
			continue
    ship_row.append(row)
    ship_col.append(col)

#ship_row = random_row(board) + 1
#ship_col = random_col(board) + 1
print ship_row
print ship_col



# Everything from here on should go in your for loop!
# Be sure to indent four spaces!
for turn in range(4):
    print "Turn", turn + 1
    guess_row = int(raw_input("Guess Row:"))
    guess_col = int(raw_input("Guess Col:"))

    if guess_row in ship_row and guess_col in ship_col:
    	print ship_row.index(guess_row)
    	print ship_col.index(guess_col)
	if ship_row.index(guess_row) == ship_col.index(guess_col):
            print "Congratulations! You sunk my battleship!"
            break
	else:
	    continue
    else:
        if (guess_row < 1 or guess_row > 5) or (guess_col < 1 or guess_col > 5):
            print "Oops, that's not even in the ocean."
        elif(board[(guess_row-1)][(guess_col-1)] == "X"):
            print "You guessed that one already."
        else:
            print "You missed my battleship!"
            board[(guess_row-1)][(guess_col-1)] = "X"
            if turn == 3:
                print "Game Over"
    # Print (turn + 1) here!
	print ""
        print_board(board)
	print ""




