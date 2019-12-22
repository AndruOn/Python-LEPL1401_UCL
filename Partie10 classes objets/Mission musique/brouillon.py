

class Duree:
    
    def __init__(self,h,m,s):
        h= int(h)
        m= int(m)
        s= int(s)
        if m >= 60 and m < 60 or s >= 0 and s < 0:
            print("Minutes ou secondes non valides")
            return
            
        self.h=h
        self.m=m
        self.s=s
    
    
    def toSeconds(self) :
        """
        Retourne le nombre total de secondes de cette instance de Duree (self).
        """
        return ( self.s + 60*( self.m + 60*self.h ) )

    def delta(self,d) :
        """
        Retourne la différence entre cette instance de Duree (self) et la Duree d passée en paramètre,
        en secondes (positif si ce temps-ci est plus grand).
        """
        return ( self.toSeconds()- d.toSeconds() )

    def apres(self,d):
        """
        Retourne True si cette instance de Duree (self) est plus grand que la Duree d passée en paramètre;
        retourne False sinon.
        """
        if delta(self,d) > 0:
            return True
        return False

    def ajouter(self,d):
       """
       Ajoute une autre Duree d à cette instance de Duree (self).
       Corrige de manière à ce que les minutes et les secondes soient dans l'intervalle [0..60[,
       en reportant au besoin les valeurs hors limites sur les unités supérieures
       (60 secondes = 1 minute, 60 minutes = 1 heure).
       """
       totsec= self.toSeconds() + d.toSeconds()
       toth= totsec//3600
       totmin= totsec//60 - toth*60
       totsec= totsec - toth*3600 - totmin*60
       return Duree(toth,totmin,totsec)

    def __str__(self):
        """
        Retourne cette durée sous la forme de texte "heures:minutes:secondes".
        Astuce: la méthode "{:02}:{:02}:{:02}".format(heures, minutes, secondes)
        retourne le String désiré avec les nombres en deux chiffres en ajoutant
        les zéros nécessaires.
        """
        return "{0:02}:{1:02}:{2:02}".format(self.h, self.m, self.s)


class Chanson:
    
    def __init__(self, t, a, d):
        if str(t) != t or str(a)!= a or not isinstance(d,Duree) :
            print("mal entré")
            return
        
        self.titre= t
        self.auteur= a
        self.duree= d
        
    def __str__(self):
        """
        Retourne un String décrivant cette chanson sous le format "TITRE - AUTEUR - DUREE".
        Par exemple: "Let's_Dance - David_Bowie - 00:04:05"
        """
        return ( self.titre +" - "+ self.auteur +" - "+ str(self.duree) )

class Album:
    
    def __init__(self,nom,list=[]):
        self.list=list
        self.nom=nom
        
    def add(self,chanson):
        if len(self.list) >= 100 or sum( chanson.duree.toSeconds() for chanson in self.list ) > 4500:
            return False
        
        listalbum= self.list
        listalbum+= [chanson]
        self.list = listalbum
        return True
        
    def __str__(self):
        dureetot= Duree(0,0,0)
        for chanson in self.list:
            dureetot= dureetot.ajouter(chanson.duree)
            
        text= "Album {0} ({1} chansons, {2})\n".format( self.nom,len(self.list), dureetot )
        for chanson in range(len(self.list)):
            text += "{0:02}: {1}\n".format( chanson+1,str(self.list[chanson]) )
        return text
        

with open("music-db.txt","r") as txt:
    album= Album("1",[])
    n=1
    for line in txt:
        lch= line.strip("\n").split()
        chanson= Chanson( lch[0], lch[1] , Duree(0,lch[2],lch[3]) )
        if not album.add(chanson):
            print(album)
            n += 1
            album = Album("{0}".format(n),[])
  
    
with open("music-db.txt","r") as txt:
    line= txt.readline()
    lch= line.strip("\n").split()
    chanson= Chanson( lch[0], lch[1] , Duree(0,lch[2],lch[3]) )
    print(chanson)
    album= Album("YAAH")
    print(album)
    listalb = album.list
    listalb += [chanson]
    print(listalb)
    
    line= "Relax Frankie_Goes_To_Hollywood 3 54\n"
    lch= line.strip("\n").split()
    chanson= Chanson( lch[0], lch[1] , Duree(0,lch[2],lch[3]) )
    print(chanson)
    listalb += [chanson]
    print(listalb)
    
    album.list= listalb
    print(album)
