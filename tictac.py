import random


def player_input():
    symbol=''
    while symbol!='x' and symbol!='o':
        symbol=input("choose your symbol: ")
    if symbol=='x' or symbol=="X":
        return  ('X','O')
    else:
        return('O','X') 

def toss():
	player = random.randint(1, 2)
	if player == 1:
		return 'player 1'
	else:
		return 'player 2'
        
def board(game_board):
    print(" "*20,"-"*9)
    print(" "*20,"|",game_board[7]+"|"+game_board[8]+"|"+game_board[9],"|")
    print(" "*20,"|","-"*5,"|")
    print(" "*20,"|",game_board[4]+"|"+game_board[5]+"|"+game_board[6],"|")
    print(" "*20,"|","-"*5,"|")
    print(" "*20,"|",game_board[1]+"|"+game_board[2]+"|"+game_board[3],"|")
    print(" "*20,"-"*9)


def choose_position(game_board,symbol):
    position=0    
    position=int(input("choose position :"))
    if game_board[position]==" " :
        game_board[position]=symbol
        print()
        board(game_board)
    else:
        print("you choose wrong posittion choose agian ")
        choose_position(game_board,symbol)


def Win(game_board,symbol):
    return( (game_board[7]==game_board[8]==game_board[9]==symbol) or
            (game_board[4]==game_board[5]==game_board[6]==symbol) or
            (game_board[1]==game_board[2]==game_board[3]==symbol) or
            (game_board[7]==game_board[4]==game_board[1]==symbol) or
            (game_board[8]==game_board[5]==game_board[2]==symbol) or
            (game_board[9]==game_board[6]==game_board[3]==symbol) or
            (game_board[7]==game_board[5]==game_board[3]==symbol) or
            (game_board[9]==game_board[5]==game_board[1]==symbol)
    )
    
def game_tie(game_board):
    for i in range(1,10):
        if game_board[i]==' ':
            return False
    return True
  
        
def play_again():
    play_again=input("do you want to play again [Y/N] :")
    if play_again=="Y" or play_again=='y':
        return True



def computer(game_board,symbol):
    position=0    
    position=random.randint(1,7)
    if game_board[position]==" " :
        game_board[position]=symbol
        print()
        board(game_board)
    else:
        computer(game_board,symbol)
    


    



