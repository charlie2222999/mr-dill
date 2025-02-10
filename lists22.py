a =[] #lists with no members,empty lists
print(a)
b = [1,2,3] # lists of integers
print(b)
c =[1,2.5,3.7,9]# list of numbers 
print(c)
d =['a','b','c']# lists of characters
print(d)
e = ['a',1,'b',3.5,'zero']#list of mixed value types 
print(e)

a = [2,4,6]
print(a)
b = ['abc','def']
print(a)
c = [1,2.0,3,4.0]
print(c)
d = []
print(d)

#The empty list,
l = list()

#the long list,
sqrs = [ 0,1,4,9,16,25,36,49,64,81,100,121,144,169,196,212]

#The neat lists
L1 = [3,4,[5,6],7]
print(L1)
#L1 is a neated list withfour elements: 3,4[5,6] and 7.L1[2] element is a list[5,6].
#Length of L4 is 4 as it counts [5,6] as one element. Also,as L1[2] is a list e.g[5,6]
#which means L1[2][0] will give 5 while L1[2][1] will give 6.

L1 = list('hello')
print(L1)

t = ('w','e','r','t','y')
L1 = list(t)
print(L1)

list = eval(input('Enter list to be added:'))
print('List you have entered:',list)

var1 = eval(input('enter value:'))
print(var1,type(var1))

vowels =['a','e','i','o','u']
print(vowels[0])
vowels[0]= 'A'
print(vowels)

L =['P','y','t','h','o','n']
for a in L:
    print(a)

L = ['q','w','e','r','t','y']
length= len(L)
for a in range(length):
    print('at indexes',a,'and',(a-length),'element:',L[a])
    
first = [10,12,14,20,22,24,30,32,34]
seq = first[3:-3]
print(seq)
seq[1]= 28
print(seq)


