def create_dic(words):
    d={}
    for word in words:
        d[word]=d.get(word,0)+1
    return d

def top_k(words,k):
    d=create_dic(words)
    l=[]
    for key in d:
        l.append((d[key],key))
    print("l créé")
    l= sorted(l,reverse=True)
    ll=[]
    k2=0
    print("liste inversée")
    while k2 <= k:
        for occ,word in l:
            if occ == k2:
                ll.append(occ,word)
    return ll



lwords = ["while", "the", "congress", "of", "the", "republic", "endlessly", 
             "debates", "this", "alarming", "chain", "of", "events", "the", 
             "supreme", "chancellor", "has", "secretly", "dispatched", "two", 
             "jedi", "knights"]

print(top_k(lwords,2))
    
    
    
    

    
    
