import turtle

def set_backgroun():
    window = turtle.Screen()
    window.bgcolor("black")
    
def draw_square():
    brad = turtle.Turtle()

    brad.color("yellow")
    brad.shape("turtle")
    #brad.speed("slow")
    brad.speed("fast")


    for j in range(1,37):
       brad.right(10)
       for i in range(4):
           brad.forward(100)
           brad.right(90)
    
    window.exitonclick()

set_backgroun()
draw_square()
