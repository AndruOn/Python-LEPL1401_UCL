import math as m
import numpy as np
import matplotlib.pyplot as plt



'''constante :  m = masse
                g = 9.81
                k = elsticité
                mu = coéfficient de friction
                N = normale 

E_tot = mv^2/2 + mgh + kx^2/2 + Iw^2/2
E_tot(d) = mv^2/2(d) + mgh(d) + kx^2/2 + Iw^2/2(d) - mu*cos(alpha)*mg*d'''


"Ces 3 valeurs peuvent etre changées au dernier moment"
"longueur du saut"
L= 800
"hauteur de la bosse"
hbosse= 100
"hauteur de la pente ajoutée"
hpente= 200
lpente= 180

"Ce sont les longueurs qui ne peuvent pas etre modifiées le jour du jury"
hpiste=20
htremplin=122
d1=lpente
d2=744 - d1
d3=600
d4=300
d5=353

"Variables pour énergies"
masse = 0.8
mu=0.03
k=0                                   # k de l'élastique
dressort=0
kdefrot=0.3
couple= (0.8)**(1/2)    
mvol=0.2
Rroue=0.5
Rvol=1
rapport= couple**2 * (mvol*Rvol)  / (masse*Rroue)        # rapport entre energie volant d'inertie et cinétiue de translation ( rapport * Ec = Evol)


step = 1  # pas de simulation [m]
end = 1997 + L

x = np.arange(0, end, step)           # distance parcourue [m]
l = np.zeros(len(x))                  # position x [m]
y = np.zeros(len(x))
y[0]= hpente + hpiste
l[0]=0
x[0]=0


f = np.zeros(len(x))
p = np.zeros(len(x))
ctot = np.zeros(len(x))
c = np.zeros(len(x))
evol = np.zeros(len(x)) 
elas = np.zeros(len(x))
frotx = np.zeros(len(x))
froty = np.zeros(len(x))
E = np.zeros(len(x))
vx = np.zeros(len(x))
vy = np.zeros(len(x))

f[0]=0
p[0]=masse*9.81* (hpente + hpiste)
ctot[0]=0
c[0]=0
evol[0]=0
elas[0]=0
E[0]= p[0]+10000



def pente1(x,y,l,lpente,hpente,hpiste):
    y[i] = -(hpente/lpente)*x[i] + hpente + hpiste
    l[i] = l[i-1] + m.sqrt((x[i]-x[i-1])**2+(y[i]-y[i-1])**2)
    return (y[i],l[i])

def plat(y,l,i,step,hpiste):
    y[i] = hpiste
    l[i] = l[i-1] + step
    return (y[i],l[i])
    
def bosse(x,y,l,i,debut,lbosse,hbosse,hpiste,step):
    y[i] = (hbosse/2) * (m.cos( (2*m.pi* (x[i] -debut+lbosse/2) ) /d3) + 1 ) + hpiste
    l[i] = l[i-1] + m.sqrt((x[i]-x[i-1])**2+(y[i]-y[i-1])**2)
    return (y[i],l[i])

def tremplin(x,y,l,i,debut,ltremplin,htremplin):
    y[i]= (htremplin/ltremplin)*(x[i]-debut) + hpiste
    l[i] = l[i-1] + m.sqrt((x[i]-x[i-1])**2+(y[i]-y[i-1])**2)
    return (y[i],l[i])
"""
defini saut(x,y,l,h,L,pente,debut):
    c = h
    b = pente
    a = (-h - pente*L)/L**2
    y[i] = a*(x[i]-debut)**2+b*(x[i]-debut)+c
    l[i] = l[i-1] + m.sqrt((x[i]-x[i-1])**2+(y[i]-y[i-1])**2)
    return (y[i],l[i])
"""

def vitx(angle,i,c):
    v= (c[i]*2/masse)**(1/2)
    vx[i]= ( m.cos(angle) * v )
    return vx[i]

def vity(angle,i,c):
    v= (c[i]*2/masse)**(1/2)
    vy[i]= ( m.sin(angle) * v )
    return vy[i]


    
"""
x y l sont des listes tres speciales de numpy.Si jms une seule position de la liste
n'est pas assignée alors la liste part en couilles et met ds valeurs aleatoires
c'est pour ca que jai mis des valeur nulles qu'il faut remplacer quon aura
fait les fct
"""


for i in range(len(x)):
    if 0 < x[i] < d1:
        y[i] = pente1(x,y,l,d1,hpente,hpiste)[0]
        l[i] = pente1(x,y,l,d1,hpente,hpiste)[1]
    if d1 <= x[i] < d1+d2:
        y[i] = plat(y,l,i,step,hpiste)[0]
        l[i] = plat(y,l,i,step,hpiste)[1]
    if d1+d2 <= x[i] < d1+d2+d3:
        debut= d1+d2
        y[i]= bosse(x,y,l,i,debut,d3,hbosse,hpiste,step)[0]
        l[i]= bosse(x,y,l,i,debut,d3,hbosse,hpiste,step)[1]  
    if d1+d2+d3 <= x[i] < d1+d2+d3+d4:
        y[i] = plat(y,l,i,step,hpiste)[0]
        l[i] = plat(y,l,i,step,hpiste)[1]
    if d1+d2+d3+d4 <= x[i] <= d1+d2+d3+d4+d5:
        debut= d4+d3+d2+d1
        y[i] = tremplin(x,y,l,i,debut,d5,htremplin)[0]
        l[i] = tremplin(x,y,l,i,debut,d5,htremplin)[1] 

    if d1+d2+d3+d4+d5 <= x[i] < d1+d2+d3+d4+d5+L:
        y[i]=0
        l[i]=0
"""        debut= d5+d4+d3+d2+d1
        y[i] = saut(x,y,l,htremplin+hpiste,L, htremplin/d5 ,debut)[0]
        l[i] = saut(x,y,l,htremplin+hpiste,L, htremplin/d5 ,debut)[1]   
"""

dl = np.empty(len(l))
dl[0]=1
for i in range(1,len(l)):
    dl[i]=(l[i]-l[i-1])/(x[i]-x[i-1]) 

"""
LES ENERGIES
"""



def alpha(x,y,i):
    return m.atan( (y[i]-y[i-1]) / (x[i]-x[i-1]) )
    
def fric(f,x,y,l,i,mu,masse):
    f[i]= mu * m.cos(alpha(x,y,i))*masse*9.81 * (l[i])
    return f[i]

def pot(p,y,i,masse):
    p[i]= masse*9.81*y[i]
    return p[i]

def elast(elas,x,y,l,i,k,dressort):
    elas[i] = k* (dressort**2)/2
    return elas[i]

def potint(petitpoids,h):
    potint= petitpoids*h*9.81
    return potint

def cintot(ctot,x,y,l,i):
    ctot[i] = E[i-1] - (p[i] + elas[i])
    return ctot[i]

def cin(c,ctot,x,y,l,i,rapport):
    if x[i] < d1+d2+d3+d4+d5:
        c[i]= ctot[i] / (1 + rapport)                   #A REVOIR        
    else:
        c[i]= ( vx[i]**2 + vy[i]**2 ) *masse/2
    return c[i]

def vol(evol,x,y,l,i,rapport):    
    evol[i]= c[i] * rapport                    #A REVOIR
    return evol[i]

def etot(E,x,y,l,f,p,c,elas,evol):
    if x[i] < d1+d2+d3+d4+d5:
        E[i]= p[i] + ctot[i] + elas[i] - (f[i]-f[i-1])
    else:
        E[i]= p[i] + c[i] - frotx[i]+ froty[i]
    return E[i]

def long(x,y,l,i):
    l[i]= m.sqrt( (x[i]-x[i-1])**2 + (y[i]-y[i-1])**2 )
    return l[i]

def saut(i,x,y,vx,vy,frotx,froty):
    D=0.3
    g=9.81
    parcours= d1+d2+d3+d4+d5 
    C1= vx[a] * ((-masse)/D)
    C2= (vy[a] + masse*g/D) * ((-masse)/D)
    #print("C1=",C1,"C2=",C2,"x[a]=",x[a])
    
    t = np.log( ( (x[i]-parcours+C1) /C1)**((-masse)/D) )             #temps en fct de x
    
    vx[i]= C1 * ((-D)/masse) * m.exp((-D)*t/masse)
    if vx[i]<0 :                                             #vitesse en x
        vx[i]=0
    
    vy[i]= C2 * ((-D)/masse) * m.exp((-D)*t/masse) - masse*g/D
    y[i]= C2 * m.exp((-D)*t/masse) - (htremplin-C2) - (masse*g/D)*t  
   
    if vy[i]<0:                                                        #vitesse en y 
        C2= (vy[a] - masse*g/D) * ((-masse)/D)
        vy[i]= C2 * ((-D)/masse) * m.exp((-D)*t/masse) + masse*g/D       
        y[i]= C2 * m.exp((-D)*t/masse) - (htremplin-C2) + (masse*g/D)*t
        
    return y[i],vx[i],vy[i]


a= (d1+d2+d3+d4+d5)//step +1

for i in range(a):
    if 0 < x[i] < d1+d2+d3+d4+d5:
        f[i]= fric(f,x,y,l,i,mu,masse)
        p[i]= pot(p,y,i,masse)
        elas[i]= elast(elas,x,y,l,i,k,dressort)            # Circuit
        ctot[i]= cintot(ctot,x,y,l,i)
        c[i]= cin(c,ctot,x,y,l,i,rapport)
        evol[i]= vol(evol,x,y,l,i,rapport)
        E[i]= etot(E,x,y,l,f,p,c,elas,evol)
        vx[i]= vitx(alpha(x,y,i),i,c)
        vy[i]= vity(alpha(x,y,i),i,c)

vx[a]=vx[a-1]
vy[a]=vy[a-1]
y[a]=y[a-1]
print("vxa=",vx[a],"vya=",vy[a])

for i in range(a+1,len(x)):
        y[i]= saut(i,x,y,vx,vy,frotx,froty)[0]
        vx[i]= saut(i,x,y,vx,vy,frotx,froty)[1]                #saut
        vy[i]= saut(i,x,y,vx,vy,frotx,froty)[2]
        l[i]= long(x,y,l,i)
        c[i]= cin(c,ctot,x,y,l,i,rapport)


#print(x,"\n",y,"\n",l,"\n",dl) 
#print(x,"\n",p,"\n",f,"\n",c,"\n",evol,"\n",elas,"\n",frot,"\n",E)
print("l=",l,"\n","x=",x,"\n","y=",y,"\n","vx=",vx,"\n","vy=",vy,"\n","\n","c=",c)


plt.subplot(411)   # grille 4x1, 1er graphique
plt.plot(x, dl,"green", label="dérivée de l")
plt.xlabel("x")
plt.ylabel("dl")
plt.legend()

plt.subplot(412)  # grille 2x1, 2e graphique
plt.plot(x, y, 'red', label="trajectoire")
plt.xlabel("x")
plt.ylabel("y")
plt.legend()

plt.subplot(212)   # grille 4x1, 2e graphique
plt.plot(x, f, "blue",label="travail de la friction")
plt.plot(x, p, "green",label="potentielle")
plt.plot(x, vy*10, "red",label="vy")
plt.plot(x, evol, "cyan",label="volant d'inertie")
plt.plot(x, vx*10, "magenta",label="vx")
plt.plot(x, E, "black",label="energie totale")
plt.ylabel("Energies")
plt.legend()

#help(plt.plot)
plt.show()
