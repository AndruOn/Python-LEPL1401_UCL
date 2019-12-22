import turtle
a = turtle.Turtle()
a.speed("fastest")           #set turtle and screen
wn = turtle.Screen()
wn.title("Drapeau Européen")


def etoile(l):
    '''dessine une étoile avec une longoeur de bras de l'''
    a.fillcolor("yellow") 
    a.begin_fill()
    
    for i in range(5):
        a.right(72)
        a.forward(l)         #dessin etoile + remplir
        a.left(72)
        a.forward(l)
        a.right(72)
        
    a.end_fill()


def rectangle(L,l):
    '''dessine un rectangle centré(de longueur L et de largeur l) bleu et revenient a (0;0)'''
    a.penup()
    a.left(90)
    a.fd(l/2)
    a.left(90)               #amener turtle au coin gauche supérieur du rectangle
    a.fd(L/2)
    a.left(180)
    
    a.fillcolor("blue")
    a.begin_fill()
    for i in range(2):       #dessine le carré et le colorie en bleu
        a.forward(L)
        a.right(90)
        a.forward(l)
        a.right(90)
    a.end_fill()
    
    a.fd(L/2)
    a.right(90)
    a.fd(l/2)                #revient a (0;0)
    a.left(90)
    a.pendown()

--------------------------------------------------------------------------------------------------------------------------

    #On lance le dessin de turtle

rectangle(1000,500)         #dessin du rectangle

a.penup()
a.fd(22)
a.left(90)
a.fd(145)                   #déplacer les étoiles
a.right(90)
a.fd(50)
a.pendown()

for i in range(12):
    b = 15 +30+ i*30        #dessin cercle des étoiles
    a.penup()
    a.right(b)
    a.forward(75)                      #distance entre etoiles
    a.left(b)
    etoile(14)                         #taille etoiles
    a.pendown()
    
    
a.shape("blank")            #faire disparaitre la petite flèche de turtle
    