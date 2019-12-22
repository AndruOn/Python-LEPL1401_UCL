#question 5

def create_dictionary(filename):
    txt = open(filename,"r")
    text= txt.read()
    l=text.split()
    txt.close()
    d={}
    for mot in l:
        d[mot]= d.get(mot,0) + 1
    return d

def occ(dictionary,word):
    return(dictionary.get(word,None))

    


f = open("text.txt","w")
f.write("avion caca avion caca\nbateau bateau avion\n bonjour caca bonjour avion")
f.close()


print(create_dictionary("text.txt"))
print(occ(create_dictionary("text.txt"),"avion"))