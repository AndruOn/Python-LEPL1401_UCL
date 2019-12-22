#question 5

def create_dictionary(filename):
    with open(filename,"r") as txt:
        text= txt.read()
        l=text.split()
        d={}
        for mot in l:
            d[mot]= d.get(mot,0) + 1
        return d

def occ(dictionary,word):
    return(dictionary.get(word,None))