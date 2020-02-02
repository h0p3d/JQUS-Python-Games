#Name:
#Collaborator:
#Date:
#Description: Make an Etch-A-Sketch

import turtle
#Setup turtle and screen
turtle.tracer(1,0) #This helps the turtle move more smoothly
turtle.setup(.75, .75) #It's the turtle window size. 

#Make variables
CANVAS_WIDTH = 250
distance = 10
isPendown = True
draw = turtle.Turtle()

#Functions that do stuff

#STEP ONE: Complete this function to draw a box around your canvas
def draw_canvas(canvas_width):
    '''
    canvas_width - int, the width of the canvas that we are going to draw on
    Draw a square using the canvas width variable
    returns - nothing
    '''
    box = turtle.Turtle()
    box.width(20)
    #Your code here!


#STEP TWO: Move the pen around the canvas using the arrow keys

def up():
    '''
    Turns draw North and moves it up by distance amount
    '''
    check_border()
    draw.setheading(90) # faces up
    draw.forward(distance) #move turle forward by distance
    
turtle.onkeypress(up, "Up") # Create listener for Up key

##2. Make functions down(), left(), and right() that change direction
#####WRITE YOUR CODE HERE!!
def down():
    '''
    Turns draw South and moves it down by distance amount
    '''
    #your code here

turtle.onkeypress(down, "Down")

def left():
    '''
    Turns draw West and moves it left by distance amount
    '''
    #your code here

turtle.onkeypress(left, "Left")
    
def right():
    '''
    Turns draw East and moves it right by distance amount
    '''
    #your code here

turtle.onkeypress(right, "Right")

# STEP 3: Penup / pendown
def change_pen():
    '''
    When the spacebar is pressed, switch the pen to be up if it is down
    or down if the pen is currently up.
    '''
    global isPendown


turtle.onkeypress(change_pen, "space")

#STEP 4: change color!!
def change_color():
    new_color = turtle.textinput("Color", "New pen color:")
    #your code here

    turtle.listen()# DO NOT REMOVE

turtle.onkeypress(change_color, "c")

#STEP 5: Don't go off the screen!
def check_border():
    '''
    if the pen touches the border, move it to the opposite border
    Ex. pen touching right wall moves to the left wall.
    Should make it impossible to draw outside of the canvas
    '''
    x = draw.xcor()
    y = draw.ycor()
    if x > CANVAS_WIDTH: #outside right wall
        draw.penup()
        draw.goto(-CANVAS_WIDTH, y) #move to left wall
    #your code here

    if isPendown:
        draw.pendown()

#STEP 6: Add your own features here!!!



#Call functions to start program running -- DO NOT CHANGE
draw_canvas(CANVAS_WIDTH)
turtle.listen() #DO NOT REMOVE!!!
turtle.mainloop() #DO NOT REMOVE!!!