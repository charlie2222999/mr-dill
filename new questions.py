sport1 =['football','basketball']
ursport = input('enter your favourite sport')
sport1.append(ursport)
sport1.sort()
print(sport1)

subjects = ['maths','english','irish','science','geography','computer science']
print(subjects)
user = input('which subject do you dislike')
subjects.remove(user)
print('my new list:',subjects)

colors = ['red','yellow','orange','blue','navy','grey','brown','indigo','violet','purple']
start = int(input('enter a starting number between between 0 and 4'))
end = int(input('enter an ending number between 5 and 9'))
print(
