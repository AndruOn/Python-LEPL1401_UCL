"""p dans s avec des ? dans p"""


def match(p,s,list):
    """test si s = p"""
    for i in range(len(p)) :
        if i in list:
            pass
        else:
            if p[i] != s[i]:
                return False
    return True
        
def position_int(p):
    """posisions des ?"""
    l=[]
    for i in range(len(p)):
        if p[i] == "?" :
            l.append(i)
    return l
            
            
def chaines(p,s):
    """ rends toutds les chaines de s de longueur p"""
    l=[]
    for i in range(len(s)-len(p)+1):
        l.append( s[i:i+len(p)] )
    return l



def p_dans_s(p,s):
    """trouve les position de p avec un caractère "?"(inconnu) dans s"""
    list=position_int(p)
    rep=[]
    ch=chaines(p,s)
    for i in ch:
        if match(p,i,list):
            rep.append(ch.index(i))
    print(rep)
            
    
p_dans_s("AB?B","ABCBGDFZGABFBGD")
#print(position_int("AB?B"))
#print(chaines("AB?B","ABCBGDFZGABFBGD"))