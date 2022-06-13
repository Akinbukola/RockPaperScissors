import random



computer_wins=0
player_wins=0
while True:
    choices = ['R','P','S']

    computer = random.choice(choices)
    player = None

    while player not in choices:
        player=input('R, P, or S?:')

    if player==computer:
            print('computer:', computer)
            print('player',player)
            print('It is a tie!')
        

    elif player=='R':
        if computer=='P':
            print('computer:', computer)
            print('player',player)
            print('You Lose, Try Again!')
            computer_wins += 1

        if computer=='S':
            print('computer:', computer)
            print('player',player)
            print('You Win, Good Job!')
            player_wins +=1

    elif player=='S':
        if computer=='R':
            print('computer:', computer)
            print('player',player)
            print('You Lose, Try Again!')
            computer_wins += 1

        if computer=='P':
            print('computer:', computer)
            print('player',player)
            print('You Win, Good Job!')
            player_wins +=1


    elif player=='P':
        if computer=='scissors':
            print('computer:', computer)
            print('player',player)
            print('You Lose, Try Again!')
            computer_wins += 1

        if computer=='R':
            print('computer:', computer)
            print('player',player)
       
            print('You Win, Good Job!')
            player_wins +=1

    print ('')
    print('player wins: '+ str(player_wins))
    print('computer wins: '+ str(computer_wins))
    print('')        


    play_again=input('Play Again?(yes/no):'). lower()

    if play_again!='yes':
        break

print('Bye')
     

print('computer:',computer)
print('player:',player)