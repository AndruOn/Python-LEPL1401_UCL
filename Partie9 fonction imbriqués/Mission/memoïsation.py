import time
import turtle



alreadyknown = {0: 0, 1: 1}
def fib(n):
    '''pre : n est un nombre entier positif
       post : retourne la n-ième valeur de la suite de fibonacci en utilisant la recursivité'''
    if n not in alreadyknown:
        new_value = fib(n-1) + fib(n-2)
        alreadyknown[n] = new_value
    return alreadyknown[n]


def fib_it(n):
    '''pre : n est un nombre entier positif
       post : retourne la n-ième valeur de la suite de fibonacci en utilisant une itération'''
    final_n = 1
    l = [0 for i in range(n+1)]
    l[1] = 1
    for i in range(2, len(l)):
        l[i] = l[i-1] + l[i-2]
    return l[n]

        
def test_time_fib(fct1,fct2, n1):
    '''pre: 2 fonctions et n1 est un nombre entier positif
       post: imprime les temps d'exécution des 2 fonctions'''
    t0 = time.clock()
    result = fct1(n1)
    t1 = time.clock()
    print("fct1({0}) = {1}, ({2:.10f} secs)".format(n1, result, t1-t0))
    
    t2 = time.clock()
    result = fct2(n1)
    t3 = time.clock()
    print("fct2({0}) = {1}, ({2:.10f} secs)".format(n1, result, t3-t2))        
    
test_time_fib(fib, fib_it, 200)


dict_mapping = {}

def memoisation(fct,n):
    '''pre: n est un nombre entier positif
       post: créer un dictionnaire contenant chaque fonction appelée, et les résultats retournés par ces fonctions pour chaque valeur de n'''
    if fct not in dict_mapping:
         dict_mapping[fct]={}
    if n in dict_mapping[fct]:
         return dict_mapping[fct][n]
    dict_mapping[fct][n] = fct(n)
    return dict_mapping[fct][n]


def fib_mem(n):
    '''pre : n est un nombre entier positif
       post : retourne la n-ième valeur de la suite de fibonacci en utilisant la mémoïsation'''
    dict_mapping[fib_mem]={}
    dict_mapping[fib_mem][0] = 0
    dict_mapping[fib_mem][1] = 1
    
    if n not in dict_mapping[fib_mem]:
        dict_mapping[fib_mem][n] = memoisation(fib_mem,n-1) + memoisation(fib_mem,n-2)
    return dict_mapping[fib_mem][n]


def test_time(fct, n1):
    '''pre: n1 est un nombre entier positif
       post: imprime et retourne le temps d'exécution d'une fonction'''
    t0 = time.clock()
    result = fct(n1)
    t1 = time.clock()
    print("fct({0}) = {1}, ({2:.10f} secs)".format(n1, result, t1-t0))
    return t1-t0

test_time(fib_mem, 200)

trf = turtle.Turtle()
trf.speed("fastest")
def draw_bar(t, height):
    """ pre: height est un nombre
        post: trace un histogramme sur turtle"""
    t.left(90)
    t.forward(height)     # Draw up the left side
    t.right(90)
    t.forward(5)         # Width of bar, along the top
    t.right(90)
    t.forward(height)     # And down again!
    t.left(90)            # Put the turtle facing the way we found it.
    t.forward(2)         # Leave small gap after each bar

def fib_it_graph(n):
    '''pre: n est un nombre entier positif
       post: retourne une liste contenant les n premiers termes de la suite de fibonacci'''
    final_n = 1
    l = [0 for i in range(n+1)]    #fonction créée pour dessiner le graphe des n premiers termes de fibonacci
    l[1] = 1
    for i in range(2, len(l)):
        l[i] = l[i-1] + l[i-2]
    return l

trf.penup()
trf.fd(-200)
trf.pendown()
for v in fib_it_graph(20):        #trace le graphe pour les 20 premiers termes en parcourant la liste retournée par fib_it_graph 
    draw_bar(trf, v)
    


alreadyknown1 = {0: 0, 1: 1}
def count_fib(n, count=[0]):
    '''pre: n est un nombre entier positif
       post: retourne la n-ième valeur de la suite de fibonacci en utilisant la recursivité'''
    count[0]+=1
    if n not in alreadyknown1:
        new_value = count_fib(n-1) + count_fib(n-2)
        alreadyknown1[n] = new_value                       #permet de connaitre le nombre d'appel de fonction en fonction de n
    count_fib.bye = count[0] 
    return alreadyknown1[n]
    
def count_fib_it(n, count=[0]):
    '''pre : n est un nombre entier positif
       post : retourne la n-ième valeur de la suite de fibonacci en utilisant une itération'''
    final_n = 1
    l = [0 for i in range(n+1)]
    count[0]+=1
    l[1] = 1
    for i in range(2, len(l)):
        l[i] = l[i-1] + l[i-2]                             #permet de connaitre le nombre d'appel de fonction en fonction de n
    count_fib_it.bye = count[0]
    return l[n]
    

def count_fib_mem(n, count=[0]):
    '''pre : n est un nombre entier positif
       post : retourne la n-ième valeur de la suite de fibonacci en utilisant la mémoïsation'''
    count[0]+=1
    dict_mapping[count_fib_mem]={}
    dict_mapping[count_fib_mem][0] = 0
    dict_mapping[count_fib_mem][1] = 1
    
    if n not in dict_mapping[count_fib_mem]:
        dict_mapping[count_fib_mem][n] = memoisation(count_fib_mem,n-1) + memoisation(count_fib_mem,n-2)       #permet de connaitre le nombre d'appel de fonction en fonction de n
    count_fib_mem.bye = count[0] 
    return dict_mapping[count_fib_mem][n]
    


tr = turtle.Turtle()
tr1 = turtle.Turtle()
tr2 = turtle.Turtle()                                             #initialisation des 6 turtle pour créer les 6 graphes
tr3 = turtle.Turtle()
tr4 = turtle.Turtle()
tr5 = turtle.Turtle()
tr.speed("fastest")
tr1.speed("fastest")
tr2.speed("fastest")
tr3.speed("fastest")
tr4.speed("fastest")
tr5.speed("fastest")


tr.penup()
tr.fd(-600)
tr.pendown()
for y in range(1,50):                                 #dessine le graphe du nombre d'appel de fonction dans fib(n) en fonction de n
    count_fib(y)
    draw_bar(tr, count_fib.bye - y)

tr1.penup()
tr1.fd(-600)
tr1.left(90)
tr1.fd(250)
tr1.right(90)
tr1.pendown()
tr1.color("red")
for w in range(1,50):
    count_fib_it(w)
    draw_bar(tr1, count_fib_it.bye - w+1 )          #dessine le graphe du nombre d'appel de fonction dans fib_it(n) en fonction de n
    

tr2.penup()
tr2.fd(-600)
tr2.right(90)
tr2.fd(250)
tr2.left(90)
tr2.pendown()                    
tr2.color("blue")
for z in range(1,50):
    count_fib_mem(z)
    draw_bar(tr2, count_fib_mem.bye - z)            #dessine le graphe du nombre d'appel de fonction dans fib_mem(n) en fonction de n
    


def exec_time(f):
    '''pre: f est une fonction
       post: retourne une fonction qui pour une certaine valeur de n, retourne le temps d'exécution de la fonction'''
    return lambda n : test_time(f,n)                                      #fonction d'ordre supérieur qui prend une fonction en paramètre et retourn une autre fonction qui pour une certaine valeur de n,
                    #donne le temps d'exécution de cette fonction


def test_time_ohigher(n):
    pass
    t0 = time.clock()
    result = f(n)
    t1 = time.clock()
    print("f({0}) = {1}, ({2:.10f} secs)".format(n, result, t1-t0))
    return t1-t0

tr3.penup()
tr3.fd(100)
tr3.left(90)
tr3.fd(250)
tr3.right(90)
tr3.pendown()
tr3.color("red")
for x in range(1,50):
    draw_bar(tr3, test_time(fib, x))                 #dessine le graphe du temps d'exécution de fib(n) en fonction de n

    
    
tr4.penup()
tr4.fd(100)
tr4.pendown()
tr4.color("blue")
for f in range(1,50):    
    draw_bar(tr4, test_time(fib_it, f))              #dessine le graphe du temps d'exécution de fib_it(n) en fonction de n

tr5.penup()
tr5.fd(100)
tr5.right(90)
tr5.fd(250)
tr5.left(90)
tr5.pendown()
tr5.color("green")
for z in range(1,50):
    draw_bar(tr5, test_time(fib_mem, z))             #dessine le graphe du temps d'exécution de fib_mem(n) en fonction de n
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
a= (d1+d2+d3+d4+d5)//step +1
print(a)
for i in range(a):
        f[i]= fric(f,x,y,l,i,mu,masse)
        p[i]= pot(p,y,i,masse)
        elas[i]= elast(elas,x,y,l,i,k,dressort)            # Circuit
        ctot[i]= cintot(ctot,x,y,l,i)
        c[i]= cin(c,ctot,x,y,l,i,rapport)
        evol[i]= vol(evol,x,y,l,i,rapport)
        E[i]= etot(E,x,y,l,f,p,c,elas,evol)
        vx[i]= vitx(alpha(x,y,i),i,c)
        vy[i]= vity(alpha(x,y,i),i,c)
for i in range(a,len(x)):
        y[i]= saut(i,x,y,vx,vy,frotx,froty)[0]
        l[i]= long(x,y,l,i)
        vx[i]= saut(i,x,y,vx,vy,frotx,froty)[1]                #saut
        vy[i]= saut(i,x,y,vx,vy,frotx,froty)[2]
        frotx[i]= frotairx(frotx,vx,i,kdefrot)
        froty[i]= frotairy(froty,vy,i,kdefrot)
        c[i]= cin(c,ctot,x,y,l,i,rapport)
        
        
        
        
        