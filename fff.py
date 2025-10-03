fin = open('bob.txt','w')
fin.write('whats cooking good looking')
fin.write('\n')
fin.close()

fin = open('bob.txt','r')
for line in fin:
    print(line)
fin.close()
#1
duh = open('dumbers.txt','w')
duh.write('1,2,3,4,5')
duh.close()
#2
duh = open('names.txt','w')
duh.write('sanam')
duh.write('\n')
duh.write('charlie')
duh.write('\n')
duh.write('jamie')
duh.write('\n')
duh.write('Damien')
duh.write('\n')
duh.write('poopy head')
duh.write('\n')
duh.write('tun tun sakur')
duh.write('\n')
duh.close()

duh = open('names.txt','r')
for line in duh:
    print(line)
duh.close()

duh = open('names.txt','a')
rename = input('entr a new name')
duh.write(rename)
duh.close()

tur = open('menu','w')
print('1.Create a new file')
print('2. Display the file')
print('3. add a new item to the file')
print('Make a section 1,2 or 3')
user_input = int(input('Can u enter 1,2 or 3'))

if user_input == 1:
    subject = input('Enter a school subject')
    sub = open('Subject.txt','w')
    sub.write(subject)
    sub.close()
if user_input == 2:
    sub = open('Subject.txt','r')
    for i in sub:
        print(i)
    sub.close()
if user_input == 3:
    Subject = input('Enter a new school subject')
    sub = open('Subject.txt','a')
    sub.write(Subject)
    sub.close()
    sub = open('Subject.txt','r')
    for i in sub:
        print(i)
if user_input != 1 or 2 or 3:
    print('fella stoppppppp')
# sanam charlie jamie Damien poopy head  tun tun sakur  
#6
duh = open('name.txt','r')
which = input('type in one of the names exactly')
if which == 'sanam':
    
if which == 'charlie':
if which == 'jamie':
if which == 'poopy head':
if which == 'tun tun sakur':


    