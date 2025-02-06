
lives = 7
secret_word = 'deputy'
place_holder = '_'*len(secret_word)
string = ''
completed_man = '''
 +---+
 | |
 O |
/|\|
/ \|
'''
man1=  '''
 +---+
 | |
   |
   |
   |
'''
man2 = string1 = '''
 +---+
 | |
 O |
   |
   |
'''
man3='''
 +---+
 | |
 O |
 | |
   |
'''
man4 ='''
 +---+
 | |
 O |
 |\|
   |
'''
man5 ='''
 +---+
 | |
 O |
/|\|
   |
'''
man6 ='''
 +---+
 | |
 O |
/|\|
  \|
'''

while game == 'yes':
    while lives > 0:
        user_input = input('Enter a letter')
        if user_input in secret_word:
            string = string + user_input
            z = string.count(user_input)
            if z==2:
                print('you have entered the same number twice')
            x = secret_word.count(user_input)
            y = secret_word.find(user_input)
            place_holder = place_holder[0:y]+user_input+place_holder[y+1:]
            print('u guessed right',place_holder)
            if place_holder ==secret_word:
                print('Well done')
                break
        else:
            lives = lives - 1
        if lives == 6 :
            print('wrong, try again:',man1)
        if lives == 5:
            print('wrong,try again:',man2)
        if lives ==4:
            print('wrong,try again:',man3)
        if lives == 3:
            print('wrong,try again:',man4)
        if lives == 2:
            print('wrong,try again:',man5)
        if lives == 1:
            print('wrong, try again:',man6)
        if lives == 0 :
            print('GAME OVER',completed_man)
            break
    game = input(' do you wanna play the game again: yes or no')

    
    

