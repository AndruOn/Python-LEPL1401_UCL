from random import randint, seed

bienvenue= "Bienvenue au Puissance 4"
niv= "Veuillez choisir le niveau de l'IA (1-4) : "
messseed= "Veuillez entrer votre graine : "

messtour= "Dans quelle colonne souhaitez-vous jouer ? "
messtriche= "Pas possible, recommencez : "

utilgagne= "Félicitations, vous avez gagné la partie !"
ordigagne= "L'intelligence artificielle vous a battu."
finégalité= "Partie nulle"

requestion= "Voulez-vous rejouer? (oui - non) : "
fermerprog= "Merci d'avoir jouer avec nous. No hard feelings :)"


def niv1(list):
    """Ordi joue au hasard
        """
    lignechoisie = test_lines() [randint( 1 , len(test_lines()) )-1]
    list= fillordi(lignechoisie)
    return list

def niv2(list):
    """  -Ordi bloque le joueur si celui peut gagner en un mouvement
         -ordi joue au hasard
        """
    try:
        lignechoisie = test_3util_align() [randint( 1 , len(test_3util_align()) )-1]
    except:
        lignechoisie = test_lines() [randint( 1 , len(test_lines()) )-1]
    list= fillordi(lignechoisie)
    return list

def niv3(list):
    """ -Ordi gagne s'il peut gagner en 1 coup
        -Ordi bloque le joueur si celui peut gagner en un mouvement
        -Ordi joue au hasard
        """
    try:
        lignechoisie = test_3ordi_align() [randint( 1 , len(test_3ordi_align()) )-1]
    except:
        try:
            lignechoisie = test_3util_align() [randint( 1 , len(test_3util_align()) )-1]
        except:
            lignechoisie = test_lines() [randint( 1 , len(test_lines()) )-1]
    list= fillordi(lignechoisie)
    return list

def niv4(list):
    """ -Ordi gagne s'il peut gagner en 1 coup
        -Ordi bloque le joueur si celui peut gagner en un mouvement
        -Ordi joue de manière à déposer un troisième jeton aligné
        -Ordi joue au hasard
    """
    try:
        lignechoisie = test_3ordi_align() [randint( 0 , len(test_3ordi_align()) )-1]
    except:
        try:
            lignechoisie = test_3util_align() [randint( 0 , len(test_3util_align()) )-1]
        except:
            try:
                lignechoisie = test_2ordi_align() [randint( 0 , len(test_2ordi_align()) )-1]
            except:
                lignechoisie = test_lines() [randint( 0 , len(test_lines()) )-1]
    list= fillordi(lignechoisie)
    return list


def test_3util_align():
    test_3util_align=[]
    for colonne in range(7):
        for i in range(3):
            if list[colonne][i:i+4]==[" ","X","X","X"]:                      # sur une verticale
                test_3util_align.append(colonne)
    Tlist= trans(list)
    for i in range(6):
        for colonne in range(5):
            if Tlist[i][colonne:colonne+4]==[" ","X","X","X"]:                #sur une horizontale
                test_3util_align.append(colonne)
            if Tlist[i][colonne:colonne+4]==["X","X","X"," "]:
                test_3util_align.append(colonne+3)
            if Tlist[i][colonne:colonne+4]==["X","X"," ","X"]:
                test_3util_align.append(colonne+2)
            if Tlist[i][colonne:colonne+4]==["X"," ","X","X"]:
                test_3util_align.append(colonne+1)
    
    for colonne in range(4):
        for i in range(3,6):
            listdiagonale4 = [list[colonne][i],list[colonne+1][i-1],list[colonne+2][i-2],list[colonne+3][i-3]]
            if listdiagonale4 == [" ","X","X","X"]:                # sur diagonale de en bas a gauche à en haut a droite              
                test_3util_align.append(colonne)
            if listdiagonale4 == ["X","X","X"," "]:            
                test_3util_align.append(colonne+3)
            if listdiagonale4 == ["X","X"," ","X"]:
                test_3util_align.append(colonne+2)
            if listdiagonale4 == ["X"," ","X","X"]:
                test_3util_align.append(colonne+1)
    for colonne in range(3,7):
        for i in range(3,6):
            listdiagonale4= [list[colonne][i],list[colonne-1][i-1],list[colonne-2][i-2],list[colonne-3][i-3]]
            if listdiagonale4 == [" ","X","X","X"]:
                test_3util_align.append(colonne)
            if listdiagonale4 == ["X","X","X"," "]:
                test_3util_align.append(colonne-3)
            if listdiagonale4 == ["X","X"," ","X"]:
                test_3util_align.append(colonne-2)
            if listdiagonale4 == ["X"," ","X","X"]:
                test_3util_align.append(colonne-1)
    return test_3util_align

def test_3ordi_align():
    test_align=[]
    for colonne in range(7):
        for i in range(3):
            if list[colonne][i:i+4]==[" ",0,0,0]:                      # sur une verticale
                test_align.append(colonne)
    Tlist= trans(list)
    for i in range(len(Tlist)):
        for colonne in range(5):
            if Tlist[i][colonne:colonne+4]==[" ",0,0,0]:                #sur une horizontale
                test_align.append(colonne)
            if Tlist[i][colonne:colonne+4]==[0,0,0," "]:                #sur une horizontale
                test_align.append(colonne+3)
            if Tlist[i][colonne:colonne+4]==[0,0," ",0]:
                test_align.append(colonne+2)
            if Tlist[i][colonne:colonne+4]==[0," ",0,0]:
                test_align.append(colonne+1)
    
    for colonne in range(4):
        for i in range(3,6):
            listdiagonale4 = [list[colonne][i],list[colonne+1][i-1],list[colonne+2][i-2],list[colonne+3][i-3]]
            if listdiagonale4 == [" ",0,0,0]:                # sur diagonale de en bas a gauche à en haut a droite              
                test_align.append(colonne)
            if listdiagonale4 == [0,0,0," "]:            
                test_align.append(colonne+3)
            if listdiagonale4 == [0,0," ",0]:
                test_align.append(colonne+2)
            if listdiagonale4 == [0," ",0,0]:
                test_align.append(colonne+1)
    for colonne in range(3,7):
        for i in range(3,6):
            listdiagonale4= [list[colonne][i],list[colonne-1][i-1],list[colonne-2][i-2],list[colonne-3][i-3]]
            if listdiagonale4 == [" ",0,0,0]:
                test_align.append(colonne)
            if listdiagonale4 == [0,0,0," "]:
                test_align.append(colonne-3)
            if listdiagonale4 == [0,0," ",0]:
                test_align.append(colonne-2)
            if listdiagonale4 == [0," ",0,0]:
                test_align.append(colonne-1)
    return test_align

def test_2ordi_align():
    test_align=[]
    for colonne in range(7):
        for i in range(5):
            vert= list[colonne][i:i+3]
            if vert==[" ",0,0]:                      # sur une verticale
                test_align.append(colonne)
    Tlist= trans(list)
    for i in range(len(Tlist)):
        for colonne in range(5):
            horiz= Tlist[i][colonne:colonne+3]    #sur une horizontale
            if horiz==[" ",0,0]:                
                test_align.append(colonne)
            if horiz==[0," ",0]:                
                test_align.append(colonne+1)
            if horiz==[0,0," "]:                
                test_align.append(colonne+2)
    for colonne in range(5):
        for i in range(2,6):
            diagonale= [list[colonne][i],list[colonne+1][i-1],list[colonne+2][i-2]]   # sur diagonale de en bas a gauche à en haut a droite
            if diagonale == [" ",0,0]:    
                test_align.append(colonne)
            if diagonale == [0," ",0]:    
                test_align.append(colonne+1)
            if diagonale == [0,0," "]:    
                test_align.append(colonne+2)
    for colonne in range(2,7):
        for i in range(2,6):
            diagonale= [list[colonne][i],list[colonne-1][i-1],list[colonne-2][i-2]]   # sur diagonale de en bas a doite à en haut a gauche 
            if diagonale == [" ",0,0]:     
                test_align.append(colonne)
            if diagonale == [0," ",0]:     
                test_align.append(colonne-1)
            if diagonale == [0,0," "]:     
                test_align.append(colonne-2)
    return test_align

def affichage(list):
    Tlist= trans(list)
    print("|" + " ".join(map(str,Tlist[0])) + "|",)
    print("|" + " ".join(map(str,Tlist[1])) + "|",)
    print("|" + " ".join(map(str,Tlist[2])) + "|",)
    print("|" + " ".join(map(str,Tlist[3])) + "|",)
    print("|" + " ".join(map(str,Tlist[4])) + "|",)
    print("|" + " ".join(map(str,Tlist[5])) + "|",)
    print("-1 2 3 4 5 6 7-")

def trans(list):
    Tlist= [ [0 for j in range(len(list))] for i in range(len(list[0])) ]
    for i in range(len(list)):
        for j in range(len(list[0])):
            Tlist[j][i]=list[i][j] 
    return Tlist

def fillordi(colonne):
    for i in range( len(list[colonne])-1,-1,-1 ):
        if list[colonne][i] == " ":
            list[colonne][i]= 0
            return list

def fillutil(colonne):
    for i in range(len(list[colonne])-1,-1,-1):
        if list[colonne][i] == " ":
            list[colonne][i]= "X"
            return list

def test_lines():
    testlines= []
    for colonne in range(len(list)):
        if " " in list[colonne]:
            testlines.append(colonne)
    return testlines

def read(nivf,list):
    affichage(list)                         #affichage du plateau
    choixjoueur= input(messtour)
    while choixjoueur not in "1234567"or choixjoueur=="" or int(choixjoueur)-1 not in test_lines() :      #test si ligne pas remplie
        print(messtriche)
        choixjoueur= input(messtour)
    
    list= fillutil( int(choixjoueur)-1 ) #joueur ajoute 
    
    list= nivf(list)#ordi ajoute
    
def test_fin(list):
    for colonne in range(7):
        for i in range(3):
            if list[colonne][i:i+4] == [0,0,0,0] :
                affichage(list)
                print(ordigagne)
                return True
            if list[colonne][i:i+4]==["X","X","X","X"]:                      #4 sur une verticale
                affichage(list)
                print(utilgagne)
                return True
            
    Tlist= trans(list)
    for i in range(len(Tlist)):
        for colonne in range(4):
            if Tlist[i][colonne:colonne+4] == [0,0,0,0] :
                affichage(list)
                print(ordigagne)                                    #4 sur l'horizontale
                return True
            if Tlist[i][colonne:colonne+4]==["X","X","X","X"]:
                affichage(list)
                print(utilgagne)
                return True
            
    for colonne in range(4):
        for i in range(3,6):
            if [list[colonne][i],list[colonne+1][i-1],list[colonne+2][i-2],list[colonne+3][i-3]] == [0,0,0,0]:
                affichage(list)
                print(ordigagne)
                return True
            if [list[colonne][i],list[colonne+1][i-1],list[colonne+2][i-2],list[colonne+3][i-3]] == ["X","X","X","X"]:     #4 sur diagonale de en bas a gauche à en haut a droite
                affichage(list)
                print(utilgagne)
                return True
    for colonne in range(3,7):
        for i in range(3,6):
            if [list[colonne][i],list[colonne-1][i-1],list[colonne-2][i-2],list[colonne-3][i-3]] == [0,0,0,0]:
                affichage(list)
                print(ordigagne)
                return True
            if [list[colonne][i],list[colonne-1][i-1],list[colonne-2][i-2],list[colonne-3][i-3]] == ["X","X","X","X"]:     #4 sur diagonale de en bas a doite à en haut a gauche 
                affichage(list)
                print(utilgagne)
                return True   
            
    if test_lines() == []:
        affichage(list)
        print(finégalité)        #board rempli égalité
        return True
    
    return False
    
    

#seed(int(input(messseed)))
inp= None
inputniv= None


print(bienvenue)
inputniv = int(input(niv))

while inp != "non":
    list= [ [" " for i in range(6)] for i in range(7)]
    while not test_fin(list) or str(inputniv) not in "1234":  
        try:
            if inputniv == 1:
                read(niv1,list)
            elif inputniv == 2:
                read(niv2,list)
            elif inputniv == 3:
                read(niv3,list)
            elif inputniv == 4:
                print(list)
                print(trans(list))
                read(niv4,list)
                
            else:
                raise ValueError
        except:
            print(messtriche)
            inputniv = int(input(niv))
    inp= input(requestion)
print(fermerprog)