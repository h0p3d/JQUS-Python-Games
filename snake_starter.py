"""
Snake Game Starter Code
Name:
Date:
Collaborators: 
"""
# Import packages
import turtle
import time
import random 

#Set up screen
turtle.tracer(1,0) #This helps the turtle move more smoothly
turtle.setup(.75, .75) #Make the game window 

# Game constants - variables that do not change
TIME_STEP = 200 # This is how many miliseconds between moving the snake. 
MAX_X = 340 #size of game border in the x-direction
MAX_Y = 220 #size of game border in the y-direction
SQUARE_SIZE = 20 # this is how much the snake moves and also the width of the square 
START_LENGTH = 5 
NUM_FOOD = 6     

#Other game variables - things that change during the course of the game
snake_pos = [] # positions [x,y] of each piece of the snake body
snake_ids = [] # ids of each piece of the snake body
food_pos = []  # positions [x,y] of each piece of food
food_ids = []  # ids of each piece of food

score = 0  # how many pieces of food has the snake eaten?

turtle.bgcolor("white") #set the background color
turtle.color("black") #set the border color

#Set up snake head
snake = turtle.Turtle()
snake.shape("square")
snake.color("black")
snake.penup()


#Set up food for snake to eat
food = turtle.Turtle()
food.shape("circle")
food.color("red") 
food.penup()
food.hideturtle() # so we don't see the food

##################################
#      STEP 1 - MAKE BORDER      #
##################################
def make_border():
    '''
    Using the variables MAX_X and MAX_Y, use turtle to draw a border
    for the snake game.
    '''
    ###YOUR CODE HERE


##################################
#  STEP 2 - MAKE SNAKE AND FOOD  #
##################################
#2A MAKE SNAKE
def make_snake():
    '''
    Draw a snake at the start of the game with a while loop
    to make START_LENGTH number of snake pieces.
    '''
    ###YOUR CODE HERE
    id = snake.stamp() #makes a stamp of a snake
    snake_ids.append(id) #adds stamp id to list
    snake_pos.append( [snake.xcor(), snake.ycor()] ) #adds location of stamp
    snake.forward(SQUARE_SIZE) #moves snake forward

#2B MAKE FOOD
def make_food():
    '''
    Make NUM_FOOD number of pieces of food for the snake 
    to eat at the start of the game using a while loop. 
    '''
    ###YOUR CODE HERE
    move_food() #moves food turtle to random location
    id = food.stamp() #makes a stamp of the food
    food_ids.append(id) #adds stamp id to list
    food_pos.append([food.xcor(), food.ycor()]) #adds location of stamp




##################################
#      STEP 3 - MOVE SNAKE       #
##################################
UP = "Up" # snake Movement directions
DOWN = "Down"
LEFT = "Left"
RIGHT = "Right"
direction = RIGHT #snake starts off moving right

def up():
    '''
    When up button is pressed, change 
    direction to UP
    '''
    global direction
    direction = UP

# 3A - Make functions down(), left(), and right() that change direction
#####WRITE YOUR CODE HERE!!


turtle.onkeypress(up, UP) # When UP key is pressed, call up() function.

# 3B - Do the same for the other arrow keys
#####WRITE YOUR CODE HERE!!


#3C - Move the snake to new position
def move_snake():
    '''
    Using the variable direction,
    find the new_x and new_y position
    of the snake and then goto that new
    position.
    '''
    new_x = snake.xcor()
    new_y = snake.ycor()

    if direction == UP:
        new_y = new_y + SQUARE_SIZE
    ### YOUR CODE HERE

    snake.goto(new_x, new_y)

##########################################
# STEP 4 - CHECK IF SNAKE EATS FOOD      #
##########################################
def check_eat_food():
    '''
    Using snake location and the list of food_pos,
    make a while loop that checks if the snake
    is in the same location as the food. If so,
    increase score by 1 and make a new piece of
    food 
    '''
    global score
    ### YOUR CODE HERE

##########################################
# STEP 5 - CHECK IF SNAKE HITS THE WALLS #
##########################################
def check_edges():
    '''
    Get the x and y coordinates of the snake
    If the snake is outside of the top, left
    right, or bottom walls, call game_over() function
    '''
    x = snake.xcor()
    y = snake.ycor()
    if y >= MAX_Y:
        print("You hit the top wall! Game over!")
        game_over()
    ### YOUR CODE HERE

##########################################
# STEP 6 - CHECK IF SNAKE EATS ITSELF    #
##########################################
def check_eat_self():
    '''
    Check if the snake's head is in the same location
    as the rest of the body of the snake. If it
    is, call the game_over() function
    '''
    ### YOUR CODE HERE


##################################
#      Code written for you      #
##################################
def game_over():
    '''
    When the game is over, change the color of the snake,
    wait 5 seconds and then close the game window
    '''
    snake.color("yellow")
    time.sleep(5) #pause for 5 seconds
    quit() #closes window

def move_body():
    '''
    Moves the rest of the snake forward
    by deleting the last stamp (piece) of the
    snake and adding a new stamp in the
    new location
    '''
    global snake_pos, snake_ids 

    #add new stamp (piece) of snake
    snake_ids.append(snake.stamp())
    snake_pos.append(snake.pos())

    snake_length = len(snake_pos) - START_LENGTH
    # if we haven't eaten food, we need to delete
    # the last stamp of the snake when we move 
    if  snake_length > score: 
        id = snake_ids.pop(0) #remove last id
        snake.clearstamp(id) #delete stamp
        snake_pos.pop(0) #remove last position
    


def move_food():
    '''
    If a piece of food is eaten, move to 
    a new random location without food
    or one of the snake pieces
    '''
    #But we need to make food pieces only on game squares
    # (locations the snake can move to)
    #So we cut up the game board into multiples of SQUARE_SIZE.
    max_x= int(MAX_X/SQUARE_SIZE) - 1
    max_y= int(MAX_Y/SQUARE_SIZE) - 1
    
    #Pick a position that is a random multiple of SQUARE_SIZE
    food_x = random.randint(-max_x,max_x)*SQUARE_SIZE
    food_y = random.randint(-max_y,max_y)*SQUARE_SIZE

    #If the location is already occupied by another food or by the snake,
    # get a new random position
    while (food_x, food_y) in snake_pos or (food_x, food_y) in food_pos:
        food_x = random.randint(-max_x,max_x)*SQUARE_SIZE
        food_y = random.randint(-max_y,max_y)*SQUARE_SIZE        

    # go to the random location
    food.goto(food_x,food_y)


def game():
    '''
    This function controls the
    game!
    '''
    move_snake() # 1. move snake forward in direction
    check_eat_self() # 2. check if the snake ate itself
    move_body() # 3. update the snake pieces
    check_edges() # 4. check if the snake hit an edge
    check_eat_food() # 5. check if snake ate food
        
    turtle.ontimer(game, TIME_STEP) 
    #wait TIME_STEP miliseconds, 
    #then call game function again and repeat the steps all over again


turtle.listen() # DO NOT DELETE - this allows the game to "listen" for user to press buttons
make_border()
make_snake()
make_food()
game()

turtle.mainloop()
