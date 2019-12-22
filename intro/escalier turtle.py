import turtle


Amine = turtle.Turtle()      # Create turtle

def escalier(T,marches,longueur,color):
   '''T nom du turtle, marches-> nombre de marches,
         longueur-> longueur des marcheurs'''
   
   T.color(color)
   for i in range(marches):
       T.forward(longueur)
       T.right(90)
       T.forward(longueur)
       T.left(90)
    
    
escalier(Amine,4,20,"blue")
