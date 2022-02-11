import random
from turtle import Turtle, Screen


#background setup
screen = Screen()
screen.setup(width=800, height=600)
screen.bgpic('road.gif')

#all turtles will start from the same x position but always keep the same y position
y_positions = [-260, -172, -85, 2 , 85, 172, 260]
#turtle colors, one for each
colors = ["white", "red", "orange", "pink", "tomato", "dodgerblue", "yellow"]
#turtle list
list_of_turtles = []
#variables for printing the winner message
ALIGN = "right"
FONT = ("Courier", 28, "bold")
#race status
race_status = True


#create 7 different instances of a turtle
for i in range(0,7):
	tur = Turtle(shape="turtle")
	tur.color(colors[i])
	tur.shapesize(2)
	tur.penup()
	tur.goto(x=-350, y=y_positions[i])
	list_of_turtles.append(tur)

#while race is still on
while race_status:
	#each turtle should move at a random pace 
	for turtle in list_of_turtles:
		#check if turtle passed the crossing line
		if turtle.xcor() > 330:
			#spinning because is the winner
			for w in range(0, 3):
				turtle.circle(10)
			winner = turtle.pencolor()
			#message to identify the winner
			turtle.write(f"Winner is the {winner} turtle!!!", font=FONT, align=ALIGN)
			#update race status and break from the loop
			race_status = False
			break
		#get a random pace for the move
		pace = random.randint(0, 25)
		#move the turtle
		turtle.forward(pace)

screen.exitonclick()