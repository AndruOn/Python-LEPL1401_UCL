

def read(input1,file):
    """pre : /
       post : cherche quelle fonction l'utilisateur a introduit et l'appelle
    """
    try:
        
        l = (input1).split()
        numbers = (input1).split() [1:]
        if l[0] == "file":
            file = name(l[1])
            
        elif input1 == "info":
            info(file)

        elif input1 == "dictionary":
            file = dictionary(file)
           
        elif l[0] == "search":
            search(file,l[1])
      
        elif l[0] == "sum":
            sum_numb(numbers)
      
        elif l[0] == "avg":
            avg_numb(numbers)
            
        elif l[0] == "hyp":
            hyp(numbers)
        
        elif input1 == "help":
            help_ult()
        
            
        return file
    except:
        print("error")
        



def name(name):
    '''pre : un fichier doit être introduit en argument
       post : ouvre le fichier introduit en argument '''
    file = open( name ,"r")
    print( name, "chargé")                 
    return file



def info(file):
    '''pre : /
       post : affiche le nombre de lignes et de caractères contenus dans le fichier'''
    if file == None:
        print("vous n'avez pas encore choisi de fichier")
        return
    
    countl = 0
    countchar = 0
    for i in file:
        countl += 1
        for j in i:
            countchar += 1
    print("le fichier contient", countl, "ligne(s)")
    print("le fichier contient", countchar, "caractères")
    test_info





def dictionary(file):
    '''pre: fichier ne contenant que des lettres
       post : utilise ce fichier en tant que dictionnaire'''
    try:
        if not only_words(file):
            my_error = ValueError("{0} n'est pas un fichier valide car il contient des nombres".format(file))
            raise my_error
        file = sorted(file)
        print("lis le fichier comme un dictionnaire")
        return file
    except:
        print ("le fichier choisi (si fichier choisi il y a) n'est pas un dictionnaire valide car il contient des nombres")
    return file


def only_words(file):
    '''pre :/
       post : vérifie si le fichier ne contient que des lettres'''
    for line in file:
        word = line.split(",") [0]
        for a in word:
            if a not in "azertyuiopqsdfghjklmwxcvbnAZERTYUIOPQSDFGHJKLMWXCVBN ',0\n":
                return False
    return True


def search(file,word):
    '''pre: word n'est composé que de str
       post : recherche dans le dictionnaire le mot le plus proche de celui introduit '''
    try:
        if file == None:
            print("vous n'avez pas encore introduit de fichier")
            return
        
        for line in file:
            lst = line.split(",") [0]
            e = 1
            b = ""
            if word == lst:
                print(lst)
                
                   
            if len(word) > len(lst):
                
                c = word
                while e < len(lst):
                    for i in range(len(c)):
                        a = list(c)
                        del a[i: i + e]
                        b = "".join(a)
                        if b == lst:
                            print(lst)
                            return
                    e += 1 
            else:
                while e < len(lst):
                
                    for j in range(len(lst)):
                        d = list(lst)
                        del d[j:j+e]
                        b = "".join(d)
                        if b == word:
                            print(lst)
                            return
                    e += 1
            
    except:
        print("le fichier choisi n'est pas un dico")
        

def sum_numb(numbers):
    '''pre : numbers est une suite de nombres
       post : affiche la somme des nombres introduits'''
    try:
        numbers = [int(i) for i in numbers]
        print(sum(numbers))
    except:
        print("il est impossible de faire la somme de caractères différents de nombres")

def avg_numb(numbers):
    '''pre : numbers est une suite de nombre
       post : affiche la moyenne des nombres introduits'''
    try:
        numbers = [int(i) for i in numbers]
        tot = sum(numbers)
        avg = tot/len(numbers)
        print(avg)
    except:
        print("il est impossible de faire la moyenne de caractères différents de nombres")


def hyp(numbers):
    """ pre : numbers est 2 nombres (cotés d'un triangle)
        post : affiche l'hypoténuse de ce triangle
    """
    try:
        if len(numbers) == 2:
            numbers = [int(i) for i in numbers]
            a = numbers[0]
            b = numbers[1]
            c = (a**2 + b**2)**(1/2)
            print(c)
        else:
            raise ValueError
    except:
        print("il est impossible de trouver l'hypoténuse si 2 nombres ne sont pas introduits")
        

def help_ult():
    '''pre :/
       post : affiche toutes les infos pour utiliser les commandes de l'assistant'''
    print("pour utiliser l'assistant, veuillez tout d'abord introduire un fichier contenant un dictionnaire dans lequel il pourra travailler.")
    
    print("la commande info vous permet de connaître le nombre de lignes ainsi que le nombre de caractères contenus dans votre fichier.")
    
    print("la commande file + nom du fichier vous permet de choisir le fichier qui va être traité par l'assistant.")
    
    print("la commande search vous affiche si le mot recherché est dans le dictionnaire, si un mot ayant le même nombre de caractère mais qui possède une lettre qui diffère, la commande affichera le mot le plus similaire.")
    
    print("la commande avg affiche la moyenne des nombres introduits.")
    
    print("la commande sum affiche la somme de tous les nombres introduits.")
    
    print("la commande dictionnary vous permet de transformer le fichier chargé qui sera utilisé comme dictionnaire.")
    
    print("la commande hyp affiche l'hypoténuse d'un triangle rectangle si vous introduisez 2 cotés.")
    
    print("la commande exit vous permet de fermer le fichier et de stopper l'assistant.")


input1 = None
file = None
while input1 != "exit":
    input1 = input("rentrez une commande (pour connaître le detail des commandes, rentrez help): ")
    file = read(input1,file)
try:
    file.close
    
except:
    print("l'assistant s'est arrêter sans que vous ayez introduit de fichier, appuyer sur f5 pour le redémarrer")
    


