#Hi! Welcome to python programming language

#This is how you input variables
#Python will automatically identify your variables as a string or integer
msg = "Hello World"

print(msg)

#This is how python receives input from users

userName = input("Enter your name: ")
print("Welcome to Python programming Mr./Ms. " + userName)

#This is how python create class and object
class NameAndAge:
    ##__init__ is a special function, also known as Constructor, is
    ##used to initialize the class Name and Age
    def __init__(self, name, age):
        self.name = name
        self.age = age
        

    def myObject(abc):
        print("Welcome to the family " + abc.name ,  abc.age)

var1 = NameAndAge("Jimson", 23)
var2 = NameAndAge("Nikka",20)
var3 = NameAndAge("Ismael",50)
var4 = NameAndAge("Monica", 47)

var1.myObject()
var2.myObject()
var3.myObject()
var4.myObject()

userAge = input("What is your age? ")
print("The users age is: " + userAge)

#This is how python make if statement

class Arguments:
    def __init__(self, a, b):
        self.a = a
        self.b = b

    def state(self):
        if self.a < self.b:
            print(self.a + " is less than " + self.b)
        elif self.a > self.b:
            print(self.a + " is greater than "+ self.b)
        else:
            print(self.a + " is equal to "+ self.b)

first = input("Enter the first value: ")
second = input("Enter the second value: ")

arg1 = Arguments(first, second)
arg1.state()

#This is how python writes for loops

x = input("State your goal: ")

for y in range(6):
    print(x)

def same_init(wd1, wd2):
    if wd1[0].lower() == wd2[0].lower():
        return True
    else:
        return False

same_init('leona', 'lemon')
