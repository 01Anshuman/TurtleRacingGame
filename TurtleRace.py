from turtle import Turtle, Screen
from tkinter import messagebox
import random

is_race_on = False
screen = Screen()
screen.setup(width=500,height=400)
user_bet = screen.textinput(title="Make your bet",prompt = "which turtle will win the race? Enter a color: ")

#deciding color/y_position to choose from lists
color = ["red","orange","blue","yellow","black"]
y_position = [-70,-40,0,40,70]
all_turtles= []

#setting up the turle to the starting postions: 
for turtle_index in range(5):
    turt = Turtle(shape="turtle")
    turt.color(color[turtle_index])
    turt.penup()
    turt.goto(x=-230,y=y_position[turtle_index])
    all_turtles.append(turt)

#starting game: 
if user_bet:
    is_race_on = True

while is_race_on:
    for turtle in all_turtles:
        rand_distance = random.randint(0,10)
        turtle.forward(rand_distance)


        if turtle.xcor() >230:
            is_race_on = False
            winning_color = turtle.pencolor()
            if winning_color == user_bet:
                # print(f"You've won!, The {winning_color} turtle is winner!")
                messagebox.showinfo(f"You've won!, The {winning_color} turtle is winner!")
            else:
                messagebox.showinfo(f"you've lost! The {winning_color} turtle is the winner!")
                # print(f"you've lost! The {winning_color} turtle is the winner!")


#setting for turtles
screen.exitonclick()
screen.mainloop()
