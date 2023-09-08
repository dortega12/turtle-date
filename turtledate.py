#Daniel Ortega Rubio
#My program add 2 extra turtles. the second turtle moves 10 units forward and moves 5 times for every 1 time the first turtle moves.
#Additionally, my third turtle stay in the center of the screen and does not move but instead writes a message for whenever a turtle is out of bounds.

import random
import turtle    

#This function 'move' takes in 3 turtles and the screen. in it, called the other function to check if a turtle is still in the screen.
#once a turtle is out of bounds, it saves the Y coordinate for each one and compares them to write out which turtle is higher.
def move(t1, t2, t3, w):
    while isInScreen(w,t1, t2): 
        coin = random.randrange(0, 2)
        if coin == 0:
            t1.left(90)
        else:
            if coin == 1:
                t1.right(90)
                t1.forward(50)
                for five in range(5):
                    t2move = random.randrange(-360, 360, 90)
                    t2.right(t2move)
                    t2.forward(10)
    t1Ypos = t1.ycor()
    t2Ypos = t2.ycor()
    
    if t1Ypos > t2Ypos:
        t3.write("Black turtle is on top", align='center', font=("Arial", 25, "italic"))
    if t2Ypos > t1Ypos:
        t3.write("Blue turtle is on top", align='center', font=("Arial", 25, "italic"))

#This function checks if a turtle is within the boundaries
def isInScreen(win,turt1, turt2):
    leftBound = -win.window_width() / 2
    rightBound = win.window_width() / 2
    topBound = win.window_height() / 2
    bottomBound = -win.window_height() / 2

    turtleX1 = turt1.xcor() #set x and y coordinates in order to make a check later
    turtleY1 = turt1.ycor()
    
    turtleX2 = turt2.xcor()
    turtleY2 = turt2.ycor()
   
    stillIn = True
    if turtleX1 > rightBound: #originally i had nested if statements but changed them to elif per instructions
        stillIn = False
    elif turtleX1 < leftBound:
        stillIn = False
        
    if turtleY1 > topBound:
        stillIn = False
    elif turtleY1 < bottomBound:
        stillIn = False
        
    if turtleX2 > rightBound:
        stillIn = False
    elif turtleX2 < leftBound:
        stillIn = False
        
    if turtleY2 > topBound:
        stillIn = False
    elif turtleY2 < bottomBound:
        stillIn = False

    return stillIn #This returns the status of stillIn, we first set it as true but once a turtle gets out of bounds then it becomes false

#This function creates 3 turtles and calls my 'move' function which then calls my 'isInScreen' function
#I also moved my black and blue turtles away from each other on the x-axis but having an even y-coordinate.
def main():
    wn = turtle.Screen()
    june = turtle.Turtle() #First turtle named June w/ parameters
    june.shape('turtle')
    june.penup()
    june.goto(-100,0) #moved starting position away from second turtle
    june.pendown()
    
    anri = turtle.Turtle() #Second turtle named anri w/ paramters
    anri.shape('turtle')
    anri.color('blue')
    anri.penup()
    anri.goto(100,0) #moved starting position away from first turtle
    anri.pendown()
    anri.speed(10)
    
    hidden = turtle.Turtle() #created third turtle and hid it. this one will write on the screen using the write() function
    hidden.hideturtle()
    
    move(june, anri, hidden, wn)

    wn.exitonclick()

main()