    
st = """0.345.67
                hello
                -543.0
                500.0 1000.0 2000.0
                10.0
                3.1416"""
lis=st.split("    ")
for line in lis:
    line+="\n"
    

with open("AD","w") as file:
    for line in lis:
        file.write(line)
    
def get_max(filename):
    """
        pre:    filename est une chaîne de caractères
        post:   Renvoie le plus grand nombre réel >= 0 trouvé dans le fichier de nom
                filename.
                Les lignes ne représentant pas un seul nombre réel >= 0 sont ignorées.
                Si le fichier n'existe pas ou si une erreur d'entrée/sortie survient,
                la fonction renvoie la valeur -1, et imprime un message d'erreur.
                Si le fichier ne contient aucune ligne valide, renvoie
                la valeur -1.

                Par exemple, la méthode retourne 10.0 pour le fichier de contenu suivant:
                0.345.67
                hello
                -543.0
                500.0 1000.0 2000.0
                10.0
                3.1416
    """
    try:    
        l=[]
        with open(filename,"r") as file:
            for line in file:
                l.append( line.rstrip("\n") )
        max=-1.0
        for i in range(len(l)):
            try:
                if float(l[i]) > max:
                    max= float(l[i])
            except:
                pass
        return max
    except:
        print("Fichier introuvable")
        return -1
    
    
print(get_max("AD"))

l=["a",["b","6"],"e",["5",["g","h"]],"i"]


def deep_concat(l):
    s=""
    for i in l:
        if isinstance(i,str):
            s+= i
        else:
            s+=deep_concat(i)
    return s

    
def fib(n):
    memo = {0: 0, 1: 1}
    def fib_mem(n,memo):
        if n not in memo:
            new_value = fib_mem(n-1,memo) + fib_mem(n-2,memo)
            memo[n] = new_value
        return memo[n]
    return fib_mem(n,memo)

print(fib(150))


def winning_house(scroll):
    students = {'gryffindor': ['Harry', 'Hermione', 'Ron', 'Ginny', 'Fred', ' Georges', 'Neville'],
            'ravenclaw': ['Cho', 'Luna', 'Sybill', 'Marcus', 'Marietta', 'Terry', 'Penelope'],
            'hufflepuff': ['Pomona', 'Zacharias', 'Teddy', 'Cedric', 'Nymphadora', 'Newton', 'Justin'],
            'slytherin': ['Malfoy', 'Severus', 'Dolores', 'Horace', 'Blaise', 'Pansy', 'Bellatrix']}
    
    with open(scroll,"r") as file:
        for line in file:
            l.append( ( line.split[0], line.split[1].rstrip("\n") ) )
        print(l)
        
    houses_points= {}
    for house in students.keys():    
        for student,points in l:
            if student in students[house]:
                houses_points[house]= houses_points.get(house,0) + points
                
    l=[("losers",0)]
    for house in houses_points:
        if houses_points[house] > l[0][1]:
            l= [ (house,houses_points[house]) ]
        elif houses_points[house] > l[0][1]:
            l.append( (house,houses_points[house]) )
            
    return [l[1] for i in l]


class Item :

    def __init__(self,author,title,serial):
        """
        Méthode d'initialisation.
        @pre  author et title sont des valeurs de type String
              serial est un entier > 0
        @post Une instance de la classe est créée, et représente un objet ayant
              comme auteur author, comme titre title et comme numéro de série serial
        """
        self.__author = author
        self.__title = title
        self.__serial = serial

    def __str__(self):
        """
        Méthode de conversion en string.
        @pre  -
        @post le string retourné contient une représentation de cet objet sous la
              forme: [num série] Auteur, Titre
        """
        return "[{}] {}, {}".format(self.__serial,self.__author,self.__title)
    
class CD(Item):
    serial= 100000
    
    def __init__(self,author,title,time):
        super().__init__(author,title,CD.serial)
        self.time= time
        CD.serial+=1
        
    def __str__(self):
        return (super().__str__()+ " ({} s)".format(self.time))
        
        
        
        
