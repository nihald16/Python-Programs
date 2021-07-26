from tictac import *

while True:
    print("__________WELCOME TO MY GAME ________")
    game=[' ']*10

    player_1,player_2=player_input()

    print(player_1,"is player_1 sign")
    print(player_2,"is player_2 sign")

    play_game=input("are you ready to play[Y/N]:")
    if play_game=='Y' or play_game=='y':
        print("lets start the game ")
        board(game)
        game_on=True
                
    else:
        game_on=False

    play=toss()
    while game_on:
        if play==player_1 :
            print("player 1 turn your sign is ",player_1,end=" ")
            choose_position(game,player_1)
            
            if Win(game,player_1):
                print("ohh yeyeye player_1 win the game ")
                game_on=False

            else:
                if game_tie(game):
                    print("game tie")
                    game_on=False
                else:
                    play=player_2

        else:
            print("player 2 turn and your sign is ",player_2,end=" ")
            choose_position(game,player_2)
            
            if  Win(game,player_2):
                print("ohh yehyehyeh player_2 win the game ")
                game_on=False

            else: 
                if game_tie(game):
                    print("game tie")
                    game_on=False
                else:
                    play=player_1

    if not play_again():
        break


