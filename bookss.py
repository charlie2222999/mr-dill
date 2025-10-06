#csv - comma seperated values
#numbers.txt number.csv
#12 13 14 15 12,13,14,15
chart = open('books.csv','w')
chart.write(',book,author,year,released\n')
chart.write('0,to kill a mockingbird,harper lee,1960\n')
chart.write('1,brief history of time,stephen hawking,1988\n')
chart.write('2,the man who mistook his wife for a hat,f.scotts fitzgerald,1922\n')
chart.write('3,pride and prejudge,oliver sacks,1985\n')
chart.write('4,the great gatsby,jane austin,1813\n')
chart.close()
#2
chart = open('books.csv','a')
line = input('enter in a number line')
name = input('enter in a name line')
author = input('enter in an author line')
date = input('enter in a date line')
string_out= line+','+name+','+author+','+date+'\n'
chart.write(string_out)
chart.close()
#3
chart = open('books.csv','a')


