from builtins import int
from math import *

name = input('Hello! What\'s your name? ') ##Asks your name
print('Welcome to coding ' + name) ##Welcomes you to coding and prints your name
age = int(input('What\'s your age? '))
print(age)
print(name.lower() + ' name is in lower case ' + name.upper() + ' name is in upper case') ##Prints the name in lower and upper case
print(name[0] + " " + name[1] + " " + name[2] + " " + name[3] + " " + name[4] + " " + name[5] + " ") ##Prints the character of the strings
print(sqrt(9))
print(9 ** (1 / 2))
add1 = input('Enter a number: ')
add2 = input('Enter a second number: ')
eq = int(add1) + int(add2) #adds the numbers
print(eq)

region = ["Davao Del Sur", 54, 548, 862 ,84]
place = ["Davao", "Digos " , "Mati " , "Cateel " , "Lanao " , "Butuan "]
region.extend(place)
place.sort()
print(region + place)
print(len(place[0]))

print("You will be " + str(age+1) + " in a year")

if name == 'Mike':
    print("Hi Mike!")
elif age > 12:
    print('You\'re already an adult')
else:
    print("Hello " + name + "!")

while name != 'your name':
    print('Please enter your name' + '\n')
    name = input()
print('Thank you')

num = int(input('Please enter a number: '))
if num == 5:
    print('The number is equal')
    if num > 5:
        print('Bigger than 5')
        if num <= 50:
            print('Between 5 and 50')
else:
    print('Not in range')

print(1 == 1 and 2 == 2)
