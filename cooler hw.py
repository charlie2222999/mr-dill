print('''
1
 2
  3
''')

test = 'test.\nNext line.'
print(test)

print('One', 'Two' * 2)
print('One' + 'Two' * 2)
print(len('0123456789'))

s ='0123456789'
print(s[3],',',s[0:3],'-',s[2 : 5])
print(s[:3],'-',s[3:],',',s[3:100])
print(s[20:],s[2:1],s[1:1])

s = '987654321'
print(s[-1],s[-3])
print(s[-3:],s[:-3])
print(s[-100:-3],s[-100:3])

y = str(123)
x ='Hello'*3
print(x,y)
x = 'Hello' + 'world'
y = len(x)
print(y,x)

x = 'hello'+\
'to python'+\
'world'
for char in x:
    y = char
    print(y,':', end ='')
    
x = 'hello world'
print(x[:2],x[:-2],x[-2:])
print(x[6],x[2:4])
print(x[2:-3], x[-4:-2])

theStr = 'This is a test'
inputInt = int(input('enter an integer:'))
testStr = theStr
while inputInt >= 0:
    testStr = testStr[1:-1]
    inputInt = inputInt -1
testBool = 't' in testStr
print(theStr)
print(testStr)
print(inputInt)
print(testBool)

teststr ='abcdefghi'
inputint = int(input('Enter an integer'))
count = 2
newstr =''
while count<= inputint:
    newstr = newstr + teststr[0 : count]
    teststr = teststr[2:]
    count = count + 1
print(newstr)
print(teststr)
print(count)
print(inputint)

inputstr = input('give me a string')
bigint = 0
littleint = 0
otherint = 0
for ele in inputstr:
    if ele>='a' and ele <='m':
        littleint = littleint + 1
    elif ele > 'm' and ele <= 'z':
        bigint = bigint + 1
    else:
        otherint = otherint + 1
print(bigint)
print(littleint)
print(otherint)
print(inputint.isdigit())


