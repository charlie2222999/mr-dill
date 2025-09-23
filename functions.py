#function to calculate the length of the line
#using pythagrom theorm

import math
def calculatelinelenght(a,b):
#    a = 3
 #   b = 4
    lengthOfSide = math.sqrt(a**2 +b**2)
    return lengthOfSide

print(calculatelinelenght(3,4))


def addun(a):
    b='un'
    adduning= ('un' + a)
    return adduning
a = input('give me a word ')
print(addun(a))

def adds(a):
    b = 's'
    addsing= (a+'s')
    return addsing
a = input('gimmie a word')
print(adds(a))

import math
def calculatearea(a):
    r =(a/2)
    areas = (math.pi*r**2)
    return areas
a = float(input('gimmie a number'))
print(calculatearea(a))

import math 
def ans(a,b):
    area =(a*b)
    return area

a= float(input('enter the height'))
b = float(input('enter the width'))
c = ans(a,b)
print((c))

print('menu')
print('1. Area of Circle')
print('2. Permimeter of circle')
print('3. Area of rectangle')
print('4. Perimeter of rectangle')
a = float(input('enter 1 or 2 or 3 or 4'))
if a == 1 :
    import math
    def calculatearea(a):
        r =(a/2)
        areas = (math.pi*r**2)
        return areas
    a = float(input('gimmie a number'))
    print(calculatearea(a))
if a == 2:
    def ans(a,b):
        area =(a*b)
        return area
    a= float(input('enter the height'))
    b = float(input('enter the width'))
    c = ans(a,b)
    print((c))
if a == 3:
    def permcirlce(a):
        r = (a/2)
        perimeter = (2*math.pi*r)
        return perimeter
    a= float(input('gimmie a number'))
    c = permcirlce(a)
    print((c))
if a == 4:
    def permrectangle(a,b,c,d):
        perimeter = (a+b+c+d)
        return perimeter
    a = float(input('enter 1 of the sides'))
    b = float(input('enter 1 0f the sides '))
    c = float(input('enter 1 0f the sides '))
    d = float(input('enter 1 0f the sides '))
    c = permrectangle(a,b,c,d)
    print((c))

def middle_

    
    



    
