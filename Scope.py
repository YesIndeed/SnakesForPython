import pygame, sys
from random import randint

# This file is where we're going to learn about scope, before we start digging around in the main game
# Here is a great place to make changes and experiment

# Part 1: Global Variables
# Q 1.1: What happens if we get rid of the global keyword? Will that happen no matter where we use global?
global scores

# Part 2: Variables in Loops
for i in range(0,20):
    scores[i] = randint

# Q 2.1: We're outside of our loop. What happens if we print i?

# Part 3: Variables in functions
def check_high_score(oldScore, newScore):
    #Q 3.1: We're inside our function. What value does newScore have?
    if oldScore < newScore:
        return newScore
    else:
        return oldScore
# Q 3.2: We're outside of our function. What value does newScore have?

# Part 4: Variables in Classes
class Player(object):
    # This is how we create an object in Python
    def __init__(self, name):
        # declare and initialize an instance variable
        # Q 4.1 We use self in Python like we use this in Java. Something very different about the two. What?
        self.name = name
        self.score = 0

    # Q 4.2: Can we use the same name "newScore" from Part 3 here? Why or why not?
    def new_score(self, newScore):
        self.score = check_high_score(self.score, newScore)

# Q 4.3: Why do we only have one parameter here, our function had two? What's going on?
exampleUser = Player("Mr. Chuah")
exampleUser.score = new_score(999999999999)
print exampleUser.name, exampleUser.score

# Part 5: Show what you've got
# Q 5.1: Make two new players, name them after you and your partner.

# Q 5.2: Give the players new highscores from our list #

