'''
Estimates pi using Monte Carlo simulation

Virtual Dartboard has area 2 X 2 to accommodate unit circle
Total area is 4
Therefore, since area of unit circle = pi * radius^2 (and radius of 1 squared
  is 1), ratio of area of unit circle to area of board should be pi/4
  Theoretically, if you fill the entire board with darts, counting
  the number of darts that fall within the circle divided by the
  total number of darts thrown should give us that ratio (i.e., 1/4 * pi)
  Therefore, multiplying that result by 4 should give us an approx. of pi

Output to monitor:
  approximation of pi (float)
Output to window:
  colored dots that simulate unit circle on 2x2 square
Functions you must implement:
  drawSquare(myturtle=None, width=0, top_left_x=0, top_left_y=0) - to outline dartboard
  drawLine(myturtle=None, x_start=0, y_start=0, x_end=0, y_end=0) - to draw axes
  drawCircle(myturtle=None, radius=0) - to draw the circle
  setUpDartboard(myscreen=None, myturtle=None) - to set up the board using the above functions
  isInCircle(myturtle=None, circle_center_x=0, circle_center_y=0, radius=0) - determine if dot is in circle
  throwDart(myturtle=None)
  playDarts(myturtle=None) - a simulated game of darts between two players
  montePi(myturtle=None, num_darts=0) - simulation algorithm returns the approximation of pi
'''
import turtle
import random
import time

#########################################################
#                   Your Code Goes Below                #
#########################################################
#making dartboard
def drawSquare(myturtle, width, top_left_x, top_left_y):
    myturtle.goto(0, 0)
    myturtle.penup()
    myturtle.goto(top_left_x, top_left_y)
    myturtle.pendown()
    myturtle.goto(-(width / 2), -(width / 2))
    myturtle.goto((width / 2), -(width / 2))
    myturtle.goto((width / 2), (width / 2))
    myturtle.goto(-(width / 2), (width / 2))

#drawing axis
def drawLine(myturtle, x_start, y_start, x_end, y_end):
    myturtle.penup()
    myturtle.goto(x_start, y_start)
    myturtle.pendown()
    myturtle.goto(x_end, y_end)

def drawCircle(myturtle, radius):
    ''' Draws circle
    Returns dartboard, axis, and circle '''
    myturtle.goto(0, -1)
    myturtle.circle(radius)

def setUpDartboard(myscreen, myturtle):
    myturtle.color('black')
    myturtle.penup()
    myturtle.goto(0, 0)
    myturtle.pendown()
    turtle.setworldcoordinates(-1, -1, 1, 1)
    drawSquare(myturtle, 2, -1, 1)
    drawLine(myturtle, -1, 0, 1, 0)
    drawLine(myturtle, 0, -1, 0, 1)
    drawCircle(myturtle, 1)

def  isInCircle(myturtle, circle_center_x, circle_center_y, radius):
    if myturtle.distance(circle_center_x, circle_center_y) < radius:
        return True
    else:
        return False

def throwDart(myturtle):
    myturtle.penup()
    myturtle.goto(float(random.randrange(-100, 101) / 100), float(random.randrange(-100, 101) / 100))
    myturtle.pendown()
    if isInCircle(myturtle, 0, 0, 1) == True:
        myturtle.color('green')
    else:
        myturtle.color('red')
    myturtle.dot()

def playDarts(myturtle):
    player1 = 0
    player2 = 0
    for i in range(10):
        throwDart(myturtle)
        if isInCircle(myturtle, 0, 0, 1) == True:
            player1 += 1
        throwDart(myturtle)
        if isInCircle(myturtle, 0, 0, 1) == True:
            player2 += 1
    if player1 > player2:
        print('Player 1 Wins!', player1, '-', player2)
    elif player2 > player1:
        print('Player 2 Wins!', player2, '-', player1)
    else:
        print("It's a tie!", player1, '-', player2)

def montePi(myturtle, num_darts):
    inside_count = 0
    for i in range(num_darts):
        throwDart(myturtle)
        if isInCircle(myturtle, 0, 0, 1) == True:
            inside_count += 1
    return inside_count * 4

#########################################################
#         Do not alter any code below here              #
#       Your code must work with the main proivided     #
#########################################################
def main():
    # Get number of darts for simulation from user
    # Note continuation character <\> so we don't go over 78 columns:
    print("This is a program that simulates throwing darts at a dartboard\n" \
        "in order to approximate pi: The ratio of darts in a unit circle\n"\
        "to the total number of darts in a 2X2 square should be\n"\
        "approximately  equal to pi/4")
    print("=========== Part A ===========")

    #Create window, turtle, set up window as dartboard
    window = turtle.Screen()
    darty = turtle.Turtle()
    darty.speed(0) # as fast as it will go!
    setUpDartboard(myscreen=window, myturtle=darty)

    # Loop for 10 darts to test your code
    for i in range(10):
        throwDart(darty)
        if isInCircle(myturtle=darty, radius=1):
          print("You hit the dartboard!")
    print("\tPart A Complete...")
    print("=========== Part B ===========")
    darty.clear()
    setUpDartboard(myscreen=window, myturtle=darty)
    playDarts(myturtle=darty)
    print("\tPart B Complete...")
    # Keep the window up until dismissed
    print("=========== Part C ===========")
    darty.clear()
    setUpDartboard(myscreen=window, myturtle=darty)
    
    # Includes the following code in order to update animation periodically
    # instead of for each throw (saves LOTS of time):
    BATCH_OF_DARTS = 5000
    window.tracer(BATCH_OF_DARTS)

    # Conduct simulation and print result
    number_darts = int(input("\nPlease input the number of darts to be thrown in the simulation:  "))
    approx_pi = montePi(myturtle=darty, num_darts=number_darts)
    print("\nThe estimation of pi using "+str(number_darts)+" virtual darts is " + str(approx_pi))
    print("\tPart C Complete...")
    # Don't hide or mess with window while it's 'working'
    window.exitonclick()

main()
