import sys


with open("streets.txt","w") as f:
    f.write("""omg trop stylé omg omg omg 
pleins de lignes
yeessssssss allooooooo
mdkcjziocjize xppzczdpoce
omg
omg
omg
omg
""")

def readfile(filename):
    '''pre : filename est un fichier
       post : retourne une liste comprenant tous les lignes du fichier'''
    with open(filename,"r") as f:
        text= f.read()
        l=text.split("\n")
        return l
        

def get_words(line):
    '''pre : line est une chaîne de caractères
       post : retourne une liste comprenant chaque mot de la chaîne sans aucune ponctuation'''
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
       post : cherche le le nombre d'occurences du mot word dans la chaîne line'''
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


"""
----------------------------------------------------------------------------------------------------------------------------------------------------
--------------------------------------------------------------------------------------------------------------------------------------------------------
"""


def test(did_pass):                                    #On définit d'abord une fonction "did_pass" que l'on va utiliser dans les autres fonctions test.
  
    """  Print the result of a test."""
    
    linenum = sys._getframe(1).f_lineno
    if did_pass:
        msg = "Test at line {0} ok.".format(linenum)
    else:
        msg = ("Test at line {0} FAILED.".format(linenum))
    print(msg)
    
    
    
    
    
    
def test_readfile():
    test(readfile("streets.txt") == ['omg trop stylé omg omg omg ', 'pleins de lignes', 'yeessssssss allooooooo', 'mdkcjziocjize xppzczdpoce', 'omg', 'omg', 'omg', 'omg', ''])
    
def test_get_words():

    test(get_words("l'otarie est une espece marine tres violente, le viol est courant chez cette espece") == ['l', 'otarie', 'est', 'une', 'espece', 'marine', 'tres', 'violente', 'le', 'viol', 'est', 'courant', 'chez', 'cette', 'espece'])
    test(get_words("j'adore la vie aujourd'hui")==['j', 'adore', 'la', 'vie', 'aujourd', 'hui'])
    test(get_words("Turmoil has engulfed the Galactic Republic.")==["turmoil", "has", "engulfed", "the", "galactic", "republic"])


def test_occ():
    test(occ("viol","l'otarie est une espece marine tres violente, le viol est courant chez cette espece")==1)
    test(occ("omg",'omg trop stylé omg omg omg ')==4)
    test(occ("gentillesse","la loutre est une espece marine tres violente, le viol est courant chez cette espece")==0)
    
def test_create_dict():
    test(create_dict([("avion",(1,0)),("avion",(2,2))])=={'avion': {1: 0, 2: 2}})



def test_create_index():
    test(create_index("streets.txt")=={'omg': {0: 4, 4: 1, 5: 1, 6: 1, 7: 1}, 'trop': {0: 1}, 'styl': {0: 1}, 'pleins': {1: 1}, 'de': {1: 1}, 'lignes': {1: 1}, 'yeessssssss': {2: 1}, 'allooooooo': {2: 1}, 'mdkcjziocjize': {3: 1}, 'xppzczdpoce': {3: 1}})
    

def test_get_lines():
    test(get_lines(["omg"],create_index("streets.txt"))==[0, 4, 5, 6, 7])
    test(get_lines(["programme"],create_index("READ ME.txt"))==[4])
    test(get_lines(["andru","amine"],create_index("READ ME.txt"))==[1])
    


test_readfile()
test_get_words()
test_occ()
test_create_dict()
test_create_index()
test_get_lines()

