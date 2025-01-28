
lives = 7
secret_word = 'deputy'
secret_word1 = '_____'
while lives>0:
    user_input = input('Enter a letter')
    if user_input in secret_word:
        x = secret_word.count(user_input)
        y = secret_word.find(user_input)
        secret_word1 = secret_word1[0:y]+user_input+secret_word1[6:]
    else:
        lives = lives - 1
    if lives == 0 :
        print('GAME OVER')
    if secret_word1 =='deputy':
        print('Well done')
        
    
    

