print('x and o game')
print('player1 you are x you go ')
print('player2 you are y')
player1 = ['x']
print(player1)
player2 = ['y']
print(player2)
grid1 = ['1','2','3']
print(grid1)
grid2 = ['1','2','3']
print(grid2)
grid3 = ['1','2','3']
print(grid3)
turns = 9
while turn >= 1:
    player1_guess = input('enter grid1 grid2 or grid3 ensure you spell the same')
    if player1_guess == 'grid1':
        x_y = int(input('enter number 1 - 3'))
        grid1[x_y -1] = "x"
        turns = turns -1
        print(grid1)
    
    elif player1_guess == 'grid2':
        x_y = int(input('enter number 1 - 3'))
        grid2[x_y -1] = "x"
        turns = turns -1
        print(grid2)
    elif player1_guess == 'grid3':
        x_y = int(input('enter number 1 - 3'))
        grid3[x_y -1] = "x"
        turns = turns -1
        print(grid3)
break