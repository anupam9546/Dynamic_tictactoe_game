import itertools

def win(current_game):
    def same(l):
        if l.count(l[0])==len(l) and l[0]!=0:
            return True
        else:
            return False

    #horizonatal
    for row in game:
        print(row)
        if same(row):
            print(f"Player{row[0]} winner horizonal (---)")
            return True

    #diag

    daigs=[]
    for col, row in enumerate(reversed(range(len(game)))):
        daigs.append(game[row][col])
    if same(daigs):
        print(f"Player{daigs[0]} winner daigonally (/)")
        return True

    for i in range(len(game)):
        daigs.append(game[i][i])
    if same(daigs):
        print(f"Player{daigs[0]} winner daigonally (\\)")
        return True

    
    #vertical

    for i in range(len(game)):
        check=[]
        for row in game:
            check.append(row[i])
        if same(check):
            print(f"Player{check[0]} winner vertically (|)")
            return True
    return False


def game_board(game_map,player=0, row=0, column=0,just_display=False):
    try:
        if game_map[row][column] !=0:
            print("This place is occipied dont cheat ;-)")
            return game_map,False
        print("   "+"  ".join([str(i) for i in range(len(game_map))]))
        if not just_display:
            game_map[row][column]=player
        for count,i in enumerate(game_map):
            print(count,i)
        print()
        return game_map,True
    except IndexError as e:
        print("E44o4: ",e)
    except Exception as e:
        print("Sonthing went wrong : ",e)
        return game_map,False


play=True
player=[1,2]
while play:
    game_size=int(input("What game size of tic tac toe u wannna play? "))
    game=[[0 for i in range(game_size)] for i in range(game_size)]
    game_won=False
    game,_=game_board(game,just_display=True)
    player_choice=itertools.cycle([1,2])
    while not game_won:
        current_player=next(player_choice)
        print(f"Current player : {current_player}")
        played=False

        while not played:
            column_choice=int(input("What col do you wanna play? (0,1,2): "))
            row_choice=int(input("What row do you wanna play? (0,1,2): "))
            game,played=game_board(game,current_player,row_choice,column_choice)
        if win(game):
            game_won=True
            again=input("The game is over , would you like to play again? (y/n) ")
            if again.lower() == "y":
                print("Restating")
            elif again.lower() == "n":
                print()
                print("Byeeeee")
                play= False
            else:
                print("Whats that anyways byeeee")
                play= False

