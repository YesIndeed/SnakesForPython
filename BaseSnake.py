# These are import statements, just like in Java!
# They help us so we don't have to rewrite code someone else has already written
import pygame, sys
from random import randint
from pygame.locals import *
from Helpers import *
from Constants import *

# This is the head of the snake.
# What color is the snake head?
snakeHead = Block(Rect(blockSize, blockSize, blockSize, blockSize), Color(50, 50, 50))

# This is the body of the snake.
# These brackets mean that the body is a list;
# In other words, there might be many parts to the body.
snakeBody = []

# This is the apple.
# Calling randomRect starts the apple off in a random place on the screen.
# How does the Color() affect the apple?
apple = randomBlock(Color(60, 60, 60))

# A block contains a color, block.color.
# We can modify an existing color's RGB values by setting block.color.r, block.color.g, block.color.b.
# Think about what this method does right now, but feel free to change it!
# Right now, our program doesn't call this method. Where can we use this function?
def changeColor(block):
    if (block.color.r < 255 and block.color.g < 255 and block.color.b < 255):
        block.color.r = block.color.r + 1
        block.color.g = block.color.g + 1
        block.color.b = block.color.b + 1

# Set up the screen. Don't worry about this code - it tells python that we want a screen of a certain size
pygame.init()
scrHeight = yBound * blockSize
scrWidth = xBound * blockSize
screen = pygame.display.set_mode((scrHeight, scrWidth))
initWalls(screen)
clock = pygame.time.Clock()

# This loop is very interesting. When will it stop running?
# (hint- when is the while condition false?)
while True:
    clock.tick(10)
    changeColor(snakeHead)
    # This gets the keyboard input. Don't worry too much about the first couple lines.
    for keypress in pygame.event.get():
        if keypress.type == QUIT:
            quitGame()

        # This is where we switch directions based on which key is pressed.
        # What do you think elif means? Does it sound like anything you've heard before?
        # Why do we check direction != UP, direction != DOWN, etc. ?
        elif keypress.type == KEYDOWN:
            # Check for the up arrow key
            if keypress.key == K_UP and direction != DOWN:
                direction = UP
            # Check for the down arrow key
            elif keypress.key == K_DOWN and direction != UP:
                direction = DOWN
            # Check for the left arrow key
            elif keypress.key == K_LEFT and direction != RIGHT:
                direction = LEFT
            # Check for the right arrow key
            elif keypress.key == K_RIGHT and direction != LEFT:
                direction = RIGHT

    # Copy the head for later use.
    oldPiece = snakeHead.rect.copy()
    # Move the head in the direction we are facing.
    snakeHead.moveInDir(direction)

    # Update the snake's body (excluding the head).
    # This piece of code takes each piece in the body and shifts it to where the next piece is
    # so it looks like the snake is moving!
    for i in range(0, len(snakeBody)):
        temp = snakeBody[i].rect.copy()
        snakeBody[i].rect = moveBody(oldPiece, snakeBody[i].rect)
        oldPiece = temp

    # These are variables that are True or False depending on conditions.
    # What do we call these kinds of variables?
    hasHitWall = snakeHead.rect.collidelist(walls) != -1
    hasHitBody = snakeHead.collideList(snakeBody)
    hasEaten = snakeHead.rect.colliderect(apple)

    # Checks if the head collides with the wall.
    if(hasHitWall or hasHitBody):
        quitGame()

    # Checks if the head collides with the apple.
    if (hasEaten):
        apple = randomBlock(Color(40, 40, 40))
        snakeBody.append(Block(oldPiece, Color(80, 80, 80)))

    #Graphically draws all the updates we just made.
    draw(oldPiece, snakeHead, snakeBody, apple, hasEaten, screen)
    pygame.display.flip()






