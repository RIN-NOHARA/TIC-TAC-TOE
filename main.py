import random
def init_board():
    global current_player
    board=[['' for i in range(3)] for j in range(3)]
    pos=1
    for i in range(3):
        for j in range(3):
            board[i][j]=pos
            pos+=1
    board[1][1]='X'
    current_player='O'
    return board
    
def display_board(board):
    print("+-------"*3,'+',sep=' ')
    for i in range(3):
        print("|        "*3,'|',sep=' ')
        for j in range(3):
               print('|  ', str(board[i][j])+ '   ', end='')
        print('|')
        print('|       ' * 3, '|', sep='')
        print('+-------' * 3, '+', sep='')

def enter_move(board):
    turn_ok=False
    while(not turn_ok):
        move=input("Enter the move from 1-9")
        if(move<='0' or move>'9' or len(move)!=1):
            print("wrong move")
            continue
        move=(int(move))-10
        row=move//3
        col=move%3
        if(board[row][col] in ['O','X']):
            print("aldready occupied")
            continue
        turn_ok=not turn_ok
        board[row][col]='O'
        
    

def free_fields(board):
    free=[]
    for i in range(3):
       for j in range(3):
           if(board[i][j] not in ['O','X']):
               free.append((i,j))
    return free
               


def draw_move(board):
   free_square=free_fields(board)
   free_square_len=len(free_square)
   if(free_square_len>0):
       rand=random.randrange(free_square_len)
       row,col=free_square[rand]
       board[row][col]='X'
       
def victory_for(board, sign):
    for row in range(3):
        if board[row][0] == sign and board[row][0] == board[row][1] and board[row][1]==board[row][2]:
            return sign
    for column in range(3):
        if board[0][column] == sign and board[0][column] == board[1][column] and board[0][column]==board[2][column]:
            return sign
    if board[0][0] == sign and board[0][0] == board[1][1] and board[1][1] == board[2][2] or \
        board[0][2] == sign and board[0][2] == board[1][1] and board[1][1] == board[2][0]:
        return sign
    return None
    
def start_of_game():
    game_status = '0'
    while game_status != '-1':
        print('*-----------------------------*')
        print('* Welcome to TicTacToe game!', ' *')
        print('* Enter 0 to start the game.', ' *')
        print('* Enter -1 to end the game.', '  *')
        print('*-----------------------------*')

        game_status = input('Enter your choice : ')

        if type(game_status) != "<class 'str'>" and game_status not in ['0', '-1']:
            print('Please enter 0 or -1')
            continue

        if game_status == '-1':
            break
        
        # main program
        board = init_board()
        play(board)
        display_board(board)

        if winner != None :
            print()
            print('Yohoo ! The player', winner, 'won the game !')
            print()
        else:
            print('Tie game !')
def play(board):
    free_squares = len(free_fields(board))
    global winner
    global current_player
    
    while free_squares != 0:
        display_board(board)
        
        if current_player == 'O':
            # player turn
            enter_move(board)
        else:
            # computer turn
            draw_move(board)
        
        game_winner = victory_for(board, current_player)
        
        if game_winner != None:
            winner = game_winner
            break
        else:
            if current_player == 'O':
                current_player = 'X'
            else:
                current_player = 'O'

        free_squares = len(free_fields(board))

start_of_game()
        
        