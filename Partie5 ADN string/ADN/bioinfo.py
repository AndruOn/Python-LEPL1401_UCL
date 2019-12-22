import sys
#import test


def is_adn(s):
    
    """pre: s est un string
       post: retourne True si s est composé exclusivement de a , c, t, g
    """
    if len(s) == 0 :
        return False
    for i in s:
        if i not in ("actgATCG"):
            return False
    return True
        
        
def positions(s,p):
    
    """pre: s et p sont deux chaines de caractères. s en majuscules p en minuscules
       post: retourne une liste des positions de p dans s
    """
    
    l=[]
    p = p.upper()
    if p in s:
        for i in range(len(s)):
            if s[i:i+len(p)] == p:          
                l.append(i)
    return l    


def distance_h(s,p):
    """ pré: s et p sont deux string de même longueur.
        post: calcule la distance de Hamming entre s et p.
        En théorie de l'information, cette distance est définie comme
        étant le nombre de positions où les deux chaînes de caractères diffèrent
    """
    if len(s) != len(p):
        return
    sum = 0
    for i in range(len(s)):
        if s[i] != p[i]:
            sum += 1
    return sum


def inverse(s):
    """ pré: s est un string ou une liste
        post: fonction renvoie le string ou la liste lu de droite à gauche
    """
    return s[::-1]


def plus_long_palindrome(s):
    """ pré: s est un string
        post: retourne le plus long palindrome de s
    """
    if len(s) == 1:
        return s
    for c in inverse( range((len(s)//2)+2) ):
       
        for i in range(len(s)):
            if s[i:i+c] == inverse(s[i+c:i+2*c]):          #palindrome style TAGGAT = longueur paire
                return s[i:i+2*c]
        for i in range(len(s)):
            if s[i:i+c] == inverse(s[i+c-1:i+2*c-1]):       #palindrome type kayak = longueur impaire
                return s[i:i+2*c-1]
    
    return 
        
