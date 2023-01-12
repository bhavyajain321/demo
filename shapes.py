#####################################
# MAIN WINDOW
# import turtle

# # creating turtle screen
# root = turtle.getscreen()
# # mainloop
# turtle.mainloop()


########################################
# FORWARD METHOD
# import turtle
# root = turtle.getscreen()
# # to move forward
# turtle.forward(200)

# # main loop
# turtle.mainloop()

#####################################
# BACKWARD 
# import turtle
# root = turtle.getscreen()
# # to move forward
# turtle.backward(200)

# # main loop
# turtle.mainloop()


################################# 
# RIGHT
# import turtle 
# # root = turtle.getscreen()
# t = turtle.Turtle()

# # to move forward
# t.right(90) # angle
# t.forward(100)

# # main loop
# turtle.mainloop()


##################################

# LEFT
# import turtle 
# # root = turtle.getscreen()
# t = turtle.Turtle()

# # to move forward
# t.left(35) # angle
# t.forward(100)

# # main loop
# turtle.mainloop()

######################################### 
# GOTO

# import turtle 
# # root = turtle.getscreen()
# t = turtle.Turtle()
#  # move turtle with coordinates
# t.goto(100,500)

# # main loop
# turtle.mainloop()


###########################
# shape

# import turtle 
# # root = turtle.getscreen()
# t = turtle.Turtle()

# # shape
# t.fd(150)
# t.rt(90)
# t.fd(150)
# t.rt(90)
# t.fd(150)
# t.rt(90)
# t.fd(150)

# # main loop
# turtle.mainloop()


################################
# circle
# import turtle 
# # root = turtle.getscreen()
# t = turtle.Turtle()

# # circle
# t.circle(150)
# t.end_fill("red")


# # main loop
# turtle.mainloop()

###################################
# DOT

# import turtle 
# # root = turtle.getscreen()
# t = turtle.Turtle()

# # DOT
# t.dot(50)

# # main loop
# turtle.mainloop()

####################
# changing the screen color

# import turtle
# t = turtle.Turtle()

# turtle.bgcolor("red")

# turtle.mainloop()


#############################
# import turtle


# t = turtle.Turtle()

# turtle.bgpic("img.png")
# # alternative of bgpic

# turtle.mainloop()



########################

# import turtle


# t = turtle.Turtle()

# t.shapesize(3,3,3)
# t.fillcolor("red")
# t.pencolor("blue")

# turtle.mainloop()


###########################

# import turtle
# t = turtle.Turtle()


# t.begin_fill()
# t.speed(1)

# t.fd(150)
# t.rt(90)
# t.fd(150)
# t.rt(90)
# t.fd(150)
# t.rt(90)
# t.fd(150)
# t.end_fill()

# turtle.mainloop()


# import turtle  
# # Creating turtle turtle  
# t = turtle.Turtle()  
  
# # Increase the turtle size  
# t.shapesize(3,3,3)  
  
# # fill the color  
# t.fillcolor("blue")  
  
# # Change the pen color  
# t.pencolor("yellow")  
  
# turtle.mainloop()


# import turtle  
# # Creating turtle turtle  
# t = turtle.Turtle()  
  
# t.shapesize(3,3,3)  
  
# t.begin_fill()  
# t.fd(100)  
# t.lt(120)  
# t.fd(100)  
# t.lt(120)  
# t.fd(100)  
# t.end_fill()  
  
# turtle.mainloop() 


# import turtle  
# # Creating turtle  
# t = turtle.Turtle()  
  
# t.pencolor("red")  
# t.fillcolor("orange")  
# t.pensize(10)  
# t.speed(7)  
# t.begin_fill()  
# t.circle(75)  
# turtle.bgcolor("blue")  
# t.end_fill()  
  
# turtle.mainloop()


# # Creating turtle  
# t = turtle.Turtle()  
# t.stamp()  
  
# t.fd(200)  
# t.stamp()  
  
# t.fd(100)  
  
# turtle.mainloop() 

#################################################

# cloning of a turtle

# import turtle

# t = turtle.Turtle()

# # clone 
# c = t.clone() # cloning variable
# t.color("red")
# c.color("orange")
# t.circle(30) # r = 30
# c.circle(40) # c = 40 

# for i in range(50, 120, 20):  #40, 50, 70, 90, 110
#     c.circle(i)

# turtle.mainloop()

# range(start,stop,step)

#################################
# for loop

# import turtle

# t = turtle.Turtle()

# for i in range(4):
#     t.fd(100)
#     t.rt(90)


# turtle.mainloop()

#########################################
# import turtle

# t = turtle.Turtle()

# n = 10

# while n<=70:  # 10,20,30,40,50,60,70
#     t.circle(n)
#     n+=10

# turtle.mainloop()


#################################

# Example 1

import turtle

t= turtle.Turtle()

turtle.bgcolor("black")
turtle.pensize(2)
turtle.speed(0)

while True:  # infinte loop
    for i  in range(6): #  6 circle
        for colors in ["red","yellow","green","pink","blue","white"]:
            turtle.color(colors)
            turtle.circle(100)
            turtle.left(10)

turtle.hideturtle()
turtle.mainloop()