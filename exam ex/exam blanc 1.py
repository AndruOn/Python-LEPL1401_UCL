def plus_frequent(l):
    d={}
    for i in l:
        if i not in d:
            d[i]=0
            for truc in l:
                if i == truc:
                    d[i]= d[i]+1
    print(d)
    nbremax=(None,0)
    for i in d:
        if nbremax[1] < d[i]:
            nbremax= (i,d[i])
            
            

    return nbremax[0]


print(plus_frequent([1,2,3,1,2,2]))


def rainfall(l):
    listavt=[]
    for nbre in l:
        if nbre >= 9999:
            break
        elif nbre < 0:
            listavt.append(0)
        else:
            listavt.append(nbre)
    total= sum(listavt)
    try:
        return total/len(listavt)
    except:
        return ("liste vide")

print(rainfall([100,50,50,250,200,9999]))


def load_matrix(filename):
    list=[]
    with open(filename,"r") as file:
        for line in file:
            list.append(line)
        m= int(list[0])
        n= int(list[1])
        matrix= [[0.0 for j in range(n)]for i in range(m)]
        del list[0:2]
        print("lis= ",list)
        
        listpos=[]
        for line in list:
            i=line
            i= i.strip("\n").split(",")
            
            i= [i[0] , i[1].split(" ")[0], i[1].split(" ")[1]]
            print(i)
            listpos.append(i)
        print("listpos= ",listpos)
        
        for element in listpos:
            i=int(element[0])
            j=int(element[1])
            matrix[i][j]=float(element[2])
            
        return matrix
    
f = open("mat.txt", "w")
f.write("""\
3
3
0,0 10
1,1 20
0,2 30
""")
f.close()
print(load_matrix("mat.txt"))    # [[10.0, 0.0, 30.0], [0.0, 20.0, 0.0], [0.0, 0.0, 0.0]]
    
    
class Client:
    """
    Un client. Chaque client a un nom d'utilisateur (supposé unique,
    par exemple adresse email) et un code pin qui est stocké comme un entier.
    """
    def __init__(self, name, pin):
        self.userName = name
        self.pin = pin

    def getUserName(self):
        return self.userName

    def getPin(self):
        return self.pin

    def setPin(self, pin):
        self.pin = pin

    def __str__(self):
        return self.userName + "(" + str(self.pin) + ")"

class ClientList:
    """Une liste de clients"""

    # un noeud de la liste
    class Node:
        def __init__(self, client, prev):
            self.data = client
            self.link = prev

    def __init__(self):
        self.last = None

    def __str__(self):
        list=[]
        last= self.last
        while True:
            if last == None:
                break
            list.append(str(last))
            last= last.link
        return list

    def update(self, name, pin):
        """
        pre: name != None, la liste contient au plus un élément dont le username
             est `name`.
        post: Si un client dont le username est name est déjà présent, met à jour
              son code pin, sinon ajoute à la liste un nouveau client ayant `name`
              comme username et `pin` comme code pin.
        """
        if self.last == None:
            self.last = Node( Client(name,pin),None )

        else:
            last= self.last
            is_in=True
            while True:
                if last.getUserName == name:
                    break
                last= last.link
                if last == None:
                    is_in=False
                    break
                    
            if not is_in:
                self.last = Node(Client(name,pin),self.last)
                
            if is_in:
                last.data = Client(name,pin)



cl = ClientList()
cl.update("alice", 1234)
print(cl)                # [alice(1234)]