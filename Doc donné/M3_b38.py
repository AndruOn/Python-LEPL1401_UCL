"""========================================================================
* Monfichier.py: Description of what the program does (generally speaking).
* Auteurs: Mr & Mrs Smith
* Groupe: 42
* Local: Ba48
========================================================================"""

# Libraries
import turtle

# Initialisation
w = turtle.Turtle()
w.speed("fastest")
w.shape("blank")
r= turtle.Screen()
r.bgcolor("purple")


def rectangle(length, width, color):
    """
    pre: To be completed
    post:To be completed
    """
    w.color(color)
    w.begin_fill()
    for x in range(2):
        w.fd(width)
        w.rt(90)
        w.fd(length)
        w.rt(90)
    w.end_fill()
    
def space_between_rectangle(width):
    """
    pre: To be completed
    post:To be completed
    """
    w.pu()
    w.backward(width)
    w.pd()
    
def space_between_rectangle_bis(length):
    """
    pre: To be completed
    post:To be completed
    """
    w.pu()
    w.lt(180)
    w.backward(length)
    w.pd()

def centré(length, width):
    """
    pre: To be completed
    post:To be completed
    """
    w.pu()
    w.backward(width/2)
    w.right(90)
    w.forward(length/2)
    w.rt(90)
    w.pd()
    
def centré_bis(length, width):
    """
    pre: To be completed
    post:To be completed
    """
    w.pu()
    w.lt(90)
    w.forward(length/2)
    w.lt(90)
    w.backward(width/2)
    w.pd()
    
def three_color_flag(length, width, color1, color2, color3):
    """
    pre: To be completed
    post:To be completed
    """
    centré(length, width)
    rectangle(length, width, color1)
    space_between_rectangle(width)
    rectangle(length, width, color2)
    space_between_rectangle(width)
    rectangle(length, width, color3)

def three_color_flag_bis(lengthb, widthb, color1, color2, color3):
    """
    pre: To be completed
    post:To be completed
    """
    centré_bis(lengthb, widthb)
    rectangle(lengthb, widthb, color1)
    space_between_rectangle_bis(widthb)
    rectangle(lengthb, widthb, color2)
    w.pu()
    w.rt(90)
    w.forward(lengthb)
    w.lt(90)
    w.pd()
    rectangle(lengthb, widthb, color3)

def european_flag(length, width):
    """
    pre: To be completed
    post:To be completed
    """
    w.forward(width/2)
    w.right(90)
    w.forward(length/2)
    w.right(90)
    rectangle(length, width, "blue")

    #étoiles
    n=0
    
    # Add a few comments
    # to explain 
    # the algorithm
    for x in range(12):
        w.penup()
        w.home()
        w.left(n+120)
        w.forward(width/4)
        w.right(n+30)
        w.pendown()
        #étoile
        w.color("yellow")
        w.begin_fill()
        w.forward(width/24)
        w.left(162)
        w.forward(width/12)
        for x in range(5):
            w.left(144)
            w.forward(width/12)
        w.end_fill()
        n = n+30
            
        

def belgium_flag(length, width):    
    three_color_flag(length, width, "black", "yellow", "red")
    
def france_flag(length, width):
    three_color_flag(length, width, "blue", "white", "red")
    
def italia_flag(length, width):
    three_color_flag(length, width, "green", "white", "red")
    
def germany_flag(lengthb, widthb):
    three_color_flag_bis(lengthb, widthb, "black", "red", "yellow")

def nederland_flag(lengthb, widthb):
    three_color_flag_bis(lengthb, widthb, "red", "white", "darkblue")
    
def luxembourg_flag(lengthb, widthb):
    three_color_flag_bis(lengthb, widthb, "red", "white", "cyan")
    
def bulgaria_flag(lengthb, widthb):
    three_color_flag_bis(lengthb, widthb, "white", "green", "red")
    
def romania_flag(length, width):
    three_color_flag(length, width, "blue", "yellow", "red")
    
def irland_flag(length, width):
    three_color_flag(length, width, "green", "white", "orange")
    
def estonia_flag(lengthb, widthb):
    three_color_flag_bis(lengthb, widthb, "blue", "black", "white")

def austria_flag(lengthb, widthb):
    three_color_flag_bis(lengthb, widthb, "red", "white", "red")
    
def lithuania_flag(lengthb, widthb):
    three_color_flag_bis(lengthb, widthb, "yellow", "green", "red")

def deplacement(length, angle):
    """
    pre: To be completed
    post:To be completed
    """
    w.penup()
    w.home()
    w.left(angle)
    w.forward(length*5)
    w.right(angle)
    w.pendown()

def placement_drapeau(length, width, lengthb, widthb):
    """
    pre: To be completed
    post:To be completed
    """
    deplacement(length, 90)
    belgium_flag(length, width)
    deplacement(length, 120)
    france_flag(length, width)
    deplacement(length, 150)
    italia_flag(length, width)
    deplacement(length, 180)
    germany_flag(lengthb, widthb)
    deplacement(length, 210)
    nederland_flag(lengthb, widthb)
    deplacement(length, 240)
    luxembourg_flag(lengthb, widthb)
    deplacement(length, 270)
    bulgaria_flag(lengthb, widthb)
    deplacement(length, 300)
    romania_flag(length, width)
    deplacement(length, 330)
    irland_flag(length, width)
    deplacement(length, 0)
    estonia_flag(lengthb, widthb)
    deplacement(length, 30)
    austria_flag(lengthb, widthb)
    deplacement(length, 60)
    lithuania_flag(lengthb, widthb)
    
    
european_flag(60, 100)
placement_drapeau(20, 11.11, 6.67, 33.33)
    
    







