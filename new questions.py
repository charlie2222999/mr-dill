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

counts={} #create a dictionary 1-3
counts2 = dict({})
counts3 = dict()
print(counts)
print(counts2)
#To add a key value pair
counts["games"] = 24
print(counts)
counts["players"] = 200
print(counts)
#To find how many items are in a dictionary
print(len(counts))
#To check if a key is in a dictionary
if "players" in counts: #Boolean check
    print("players found")
if "managers" not in counts: #returns true or false
    print("managers not found")
#To print a value
print(counts["games"]) #returns game value - error
print(counts)
print(counts.get("games")) #returns game value - none
print(counts)
print(counts.pop("games")) #returns game value - error
print(counts)
 
for key in counts.keys():
    print(key)
for key in counts: #Will print the keys in the dictionary
    print(key)
for values in counts.values(): #Will print the values
    print(values)
for key,value in counts.items(): #will return key-value
    print(f'{key} -- {value}')
