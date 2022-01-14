import sys

player1_choice = 'x'
player2_choice = 'o'
game_draw = 'DRAW'

# make grid
board = [cell for cell in range(9)] 
print()

def display_board():
# will display in a screen 
    print(f'{board[0]} {board[1]} {board[2]}') 
    print(f'{board[3]} {board[4]} {board[5]}')      
    print(f'{board[6]} {board[7]} {board[8]}')

# call display_board function
display_board()

# a function that will call check_winner function
#  and return the condition of the game
def game():
    winner = check_winner()
    if winner == 'x':
        print('Player 1 is the winner')
        sys.exit()
    elif winner == 'o':
        print('Player 2 is the winner')
        sys.exit()
    elif winner == game_draw:
        print('Game is a draw')
        sys.exit()

# function to check for winner and draw
def check_winner():
# check the rows
    if board[0] == board[1] == board[2]:
        return board[0]
    elif board[3] == board[4] == board[5]:
        return board[3]
    elif board[6] == board[7] == board[8]:
        return board[6]

# check columns
    elif board[0] == board[3] == board[6]:
        return board[0]
    elif board[1] == board[3] == board[7]:
        return board[1]
    elif board[2] == board[5] == board[8]:
        return board[2]

# check diagonally
    elif board[0] == board[4] == board[8]:
        return board[0]
    elif board[2] == board[4] == board[6]:
        return board[2]

# check for a draw
    else:
        for cell in board:
            if isinstance(cell, int):
                return
            return game_draw

# A function to check for correct input and to if the cell 
# is full to ask the player to try again
def update_board(choice, cell):
    if cell < 0 or cell > 9:
        print('Not a valid cell')
    if board[cell] == 'x' or board[cell] == 'o':
        print('Cell is already filled. Try again')
    else:
        board[cell] = choice

# main function, that calls the game and check_winner function
# and asks for player input
def main():
    player1_cell = int(input('Player 1, enter your choice of cell from numbers (0 - 8) ' ))
    update_board(player1_choice, player1_cell)
    game()
    display_board()
    player2_cell = int(input('Player 2, enter your choice of cell from numbers (0 - 8) ' ))
    update_board(player2_choice, player2_cell)
    game()
    display_board()


while True:
    main()

   
    