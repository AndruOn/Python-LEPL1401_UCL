
def readfile(filename):
    '''pre : filename est un fichier
       post : retourne une liste comprenant tous les lignes du fichier'''
    with open(filename,"r") as f:
        text= f.read()
        l=text.split("\n")
        return l
        

def get_words(line):
    '''pre : line est une chaîne de caractères
       post : retourne une liste comprenant chaque mot de la chaîne sans aucune ponctuation(qu'il transforme en espaces)'''
    l = list(line)
    a = " "
    for i in range(len(l)):
       if l[i] not in "azertyuiopmlkjhgfdsqwxcvbnAZERTYUIOPMLKJHGFDSQWXCVBN":
           l.insert(i, " ")
           del l[i+1]
       a += l[i]
    return a.lower().split()
    
def occ(word,line):
    '''pre : word et line sont des chaînes de caractères, word est un seul mot
       post : cherche le nombre d'occurences du mot word dans la chaîne line'''
    words = get_words(line)
    occ = 0
    for i in words:
        if i == word:
            occ += 1
    return occ
        
    
def create_dict(l):
    '''pre : l est une liste comprenant des mot, leur position (ligne) et leur occurence dans le fichier
       post : retourne un dictionnaire comprenant les mots et un autre dictionnaire des position et des occurences'''
    dict={}
    d= {}
    
    for word,pos_occ in l:
        if word not in d:
            d[word] = [pos_occ]     
        else:
            d[word].append(pos_occ)

    for word in d:
        a ={}
        for pos,occ in d[word]:    
            a[pos] = occ
        dict[word] = a
    
    return dict    

def create_index(filename):
    '''pre : filename est un fichier
       post : retourne un index : un dictionnaire comprenant tous les mots du fichier, leurs(s) position(s) et leur occurence'''
    txt = readfile(filename)
    l = []
    for line_numb in range(len(txt)):
        line = txt[line_numb]      
        for word in get_words(line):
            l.append((word,(line_numb,occ(word,line))))
    return create_dict(l)
        

def get_lines(words, index):
    ''' pre : words est une liste de mot(s), index est un dictionnaire comprenant des mots, leurs(s) position(s) et leur occurence
        post : retourne une liste des positions des lignes dans lesquels tous les mots de la liste words sont présents'''
    l = []
    for line_word1 in index[words[0]].keys():
        count = 0
        for word in words:
            if line_word1 in index[word]:
                count += 1
        if count == len(words) and line_word1 not in l:
            l.append(line_word1)
    return l


input1 = None
input2 = None
f = True
while True:
    input1 = input("veuillez rentrer le nom de votre fichier: ")
    if input1 == "exit":
        break
    try:
        filename = input1
        readfile(filename)
        while f:
            try:
                input2 = input("veuillez rentrer une liste de mots: ")
                if input2 == "exit":
                    f = False
                    continue
                create_index(filename)
                for line in get_lines(input2.split(), create_index(filename)):
                    print(readfile(filename)[line])
                if get_lines(input2.split(), create_index(filename)) == []:
                    print("vos mots ne se retrouvent jamais tous dans la même ligne")
            except:
                print("vous n'avez pas introduit une liste de mot valide")
        break
    except:
        print("vous n'avez pas introduit un fichier valide ")
    
print("l'assistant s'est arreté, appuyez sur f5 pour le redémarrer")