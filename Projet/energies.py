

def alpha(x,y,i):
    return m.atan(y[i]/x[i])
    
def fric(f,x,y,l,i,mu,masse):
    f[i]= mu*m.cos(alpha(x,y,i))*masse*9.81 * (l[i])
    return f[i]

def pot(p,y,i,masse):
    p[i]= masse*9.81*y[i]
    return p[i]

def cin(c,x,y,l,i,masse):
    pass

def vol(evol,x,y,l,i,I,omega):
    evol[i]= I* (omega**2)/2      #a revoir pcq gros zbeul
    return evol[i]

def elas(elas,x,y,l,i,k,dressort):
    elas[i] = k* (dressort**2)/2
    return elas[i]

def potint(petitpoids,h):
    potint= petitpoids*h*9.81
    return potint

def frot(frot,x,y,l,i):
    pass

def etot(E,x,y,l,f,p,c,elas,evol):
    etot[i]= p[i] + c[i] + elas[i] + evol[i] - f[i]
    return etot[i]



        f[i]= fric(f,x,y,l,i,mu,masse)
        p[i]= pot(p,y,i,masse)
        c[i]= cin(c,x,y,l,i,masse)
        evol[i]= vol(evol,x,y,l,i,I,omega)
        elas[i]= elas(elas,x,y,l,i,k,dressort)
        frot[i]= frot(frot,x,y,l,i)
        etot[i]= etot(E,x,y,l,f,p,c,elas,evol)