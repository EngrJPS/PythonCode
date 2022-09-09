#This project creates a mini game using python. The game
#we will create is called madlibs. Madlibs is a word
#game where one player prompts another word for a list
#of words to subsititute for blanks in a story

class Story:
    def __init__(self, username, food, name, adjective, noun, verb, verb2, verb3):
        self.username = username
        self.food = food
        self.name = name
        self.adjective = adjective
        self.noun = noun
        self.verb = verb
        self.verb2 = verb2
        self.verb3 = verb3

    def madlibs(abc):
        print ("Hi {}! Welcome to the minigame called madlibs.".format(abc.username))
        print ("Lets play shall we?")
        print ("It was {} day at school, and {} was super {} for lunch".format(abc.food, abc.name, abc.adjective))
        print ("But when she went outside to eat, a {} stole her {}!".format(abc.noun, abc.name))
        print ("{} chased the {} all over the school.".format(abc.name, abc.noun))
        print ("She {},{}, and {} through the playground.".format(abc.verb, abc.verb2, abc.verb3))
        print ("Then she tripped on her {} and the {} escaped!".format(abc.noun, abc.noun))
        print ("Luckily, {}'s friends were willing to share their {} with her.".format(abc.name, abc.food))


username = input("Enter user name: ")
food = input("Food: ")
name = input("Name: ")
adjective = input("Adjective: ")
noun = input("Noun: ")
verb = input("Verb: ")
verb2 = input("Verb: ")
verb3 = input("Verb: ")

madlibs1 = Story(username, food, name, adjective, noun, verb, verb2, verb3)

#First create a story to and fill the sentences some blanks

madlibs1.madlibs()