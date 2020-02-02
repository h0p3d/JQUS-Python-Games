import turtle
import random
import time
#make turtles
turtle.tracer(1,0) #removes delay
turtle.bgcolor("black") #changes background color

#IMPORTANT VARIABLES 
fruits = [] # empty for now
spikes = [] # empty for now
#make player
player = turtle.Turtle()
player.color("white")
player.shape("square")
PLAYER_WIDTH = 30
player.turtlesize(PLAYER_WIDTH/20,PLAYER_WIDTH/20)
player.penup() 

#other variables that stay the same:
turtle.setup(.75, .8) # makes a screen 
WIDTH = 400
HEIGHT = 250
DISTANCE = 2 # how far the turtles move each time step (decrease to  move slower)
MAX_X = WIDTH - 10 # -10 so that falling items don't touch edges
MAX_Y = HEIGHT - 10 # -10 so that falling items don't touch edges
distance = 20 #how much player moves
TIME_STEP = 15 # 15 milliseconds (1000 ms = 1 s). What happens if you chabge this value?
max_rand = 100 #1/100 chance of blocks respawning what happens if you change this value?

#These variables change
score = 0
num_lives = 3

#STEP 1 - Make the game border
def make_border():
    '''
    makes a white border around the game screen
    using variables WIDTH and HEIGHT
    '''
    turtle.color("white")
    turtle.penup()
    turtle.hideturtle() #hides the arrow


#STEP 2 - Move the player around
def up():
    '''
    Turns player North and moves it up by distance amount
    '''
    player.setheading(90) # faces up
    player.forward(distance) #move turle forward by distance
    
turtle.onkeypress(up, "Up") # Create listener for Up key

##2. Make functions down(), left(), and right() that change direction
#####WRITE YOUR CODE HERE!!
def down():
    '''
    Turns player South and moves it down by distance amount
    '''
    #YOUR CODE HERE 

turtle.onkeypress(down, "Down")

def left():
    '''
    Turns player West and moves it left by distance amount
    '''
    #YOUR CODE HERE 

turtle.onkeypress(left, "Left")    
    
def right():
    '''
    Turns player East and moves it right by distance amount
    '''
    #YOUR CODE HERE 

turtle.onkeypress(right, "Right")   

#STEP 3 - Player stays in border - complete the can_move() function
def can_move(x,y):
    '''
    x - int, x coordinate of player
    y - int, y coordinate of player
    return True if position is inside the border, 
    False if it is outside the walls 
    '''
    result = True
    #your code here

    #end your code
    return result 

#STEP 4 - Check if player is touching falling objects
def isTouching(x,y):
    '''
    x - int, x coordinate of falling object
    y - int, y coordinate of falling object
    return True if position is inside the player, False otherwise
    '''
    player_x = player.xcor()
    player_y = player.ycor()

    result = False
    #your code here

    #end code
    return result

#STEP 5 - Subtract Lives & End the Game

#checks if player has been hit by falling spike
def check_player():
    '''
    For all blocks / spikes, check if player is touching it.
    If so, subtract a life from num_lives.
    If player reaches 0 lives, game is over.
    '''
    global num_lives
    for t in spikes:
        x,y = t.pos()
        if isTouching(x,y): #player is hit by blocks
            t.hideturtle()
            t.goto(x, -MAX_Y)
            #your code here

def game_over():
    '''
    When the game ends
    - change player color to red
    - pause for 5 seconds
    - and quit the screen
    '''
    #your code here
    quit()  #Exit screen

####################################################3
#        Other Functions for game:
#####################################################

# generates random x values for the falling items
def rand_x():
    return random.randint(-MAX_X, MAX_X)

def check_edge():
    '''
    Hides the turtle if it is below bottom edge
    This turtle will continue to fall until 1 is randomly selected.
    Think of it like rolling a 10 sided dice and waiting for a 10 to
    be rolled. This causes the items to fall at random times.
    '''
    global score
    for t in spikes + fruits:
        x,y = t.pos()
        if y == -MAX_Y:
            score += 1
        if y <= -MAX_Y:
            t.hideturtle()
            if random.randint(1,max_rand) == 1:
                t.goto(rand_x(),MAX_Y)
                t.showturtle()



def check_fruit():
    '''
    For all the fruit, check if player is touching it.
    If so, player gains points and fruit disappears.
    '''
    global score
    for f in fruits:
        x,y = f.pos() #get fruit position
        if isTouching(x,y): #player ate fruit
            score += 10 #increase score
            f.hideturtle() #hide food
            f.goto(0,-MAX_Y-50) #move it to the bottom of the screen so it randomly appears at the top


def make_spikes():
    '''
    Make blocks that subtract lives from the player.
    '''
    spike = turtle.Turtle()
    spike.shape("square")
    spike.color("red")
    spike.penup()
    spike.hideturtle()
    spikes = [spike] #this is a list, don't worry about it
    for i in range(25): #make 25 more spikes
        spikes.append(spike.clone())
    
    #move spikes to random locations at the top of the screen
    for t in spikes:
        t.goto(rand_x(),-MAX_Y-20)
    return spikes

def make_fruit():
    '''
    Make fruit that heals the player
    '''
    #make bonus fruit
    fruit = turtle.Turtle()
    fruit.shape("circle")
    fruit.color("green")
    fruit.penup()
    fruit.hideturtle()
    fruits = [fruit]
    for i in range(3): #repeat next line of code 3 times, makes total of 4 fruit
        fruits.append(fruit.clone())
    for t in fruits: #move fruit to random locations at bottom of screen
        t.goto(rand_x(),-MAX_Y-20)
    return fruits

#############################################################
#   Functions you should try to understand:
#############################################################

def update_score():
    '''
    Updates score after every move
    '''
    scoreWriter.undo() #unwrite previous score
    scoreWriter.write(score, font = ("Arial", 16, "normal")) #write new score

def game():
    '''
    This function controls the game!
    It moves the falling objects down, checks if the player has 
    been hit, and adds difficulty as the game progresses.
    '''
    for t in spikes + fruits:
        x = t.xcor()
        y = t.ycor()
        t.goto(x,y-DISTANCE) # move spikes and fruits down
    check_player() # check if player is hit by falling blocks
    check_fruit() #check if player ate fruit
    check_edge() # check if falling objects hit the bottom wall
    update_score() #write new score
    turtle.ontimer(game, TIME_STEP) #after TIME_STEP amount of time, repeat

#write score initially
scoreWriter = turtle.Turtle()
scoreWriter.hideturtle() #make arrow invisible
scoreWriter.color("white")
scoreWriter.penup()
scoreWriter.goto(WIDTH+10,0)
scoreWriter.write(score,font = ("Arial", 16, "normal"))

#make boarder and falling objects
make_border()
fruits = make_fruit()
spikes = make_spikes()
turtle.listen() #allows keyboard buttons to work
#start the game
game()
turtle.mainloop()
