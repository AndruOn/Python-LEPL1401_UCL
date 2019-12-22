from random import randint, seed

bienvenue= "Bienvenue au Puissance 4"
niv= "Veuillez choisir le niveau de l'IA (1-4) : "
messseed= "Veuillez entrer votre graine : "

messtour= "Dans quelle colonne souhaitez-vous jouer ? "
messtriche= "Pas possible, recommencez : "

utilgagne= "Félicitations, vous avez gagné la partie !"
ordigagne= "L'intelligence artificielle vous a battu."
finégalité= "Partie nulle"


def niv1(list):
    lignechoisie = test_lines() [randint( 1 , len(test_lines()) )-1]
    list= fillordi(lignechoisie)
    return list

def niv2(list):
    try:
        lignechoisie = test_3util_align() [randint( 1 , len(test_3util_align()) )-1]
    except:
        lignechoisie = test_lines() [randint( 1 , len(test_lines()) )-1]
    list= fillordi(lignechoisie)
    return list

def niv3(list):
    try:
        lignechoisie = test_3util_align() [randint( 1 , len(test_3util_align()) )-1]
    except:
        try:
            lignechoisie = test_3ordi_align() [randint( 1 , len(test_3ordi_align()) )-1]
        except:
            lignechoisie = test_lines() [randint( 1 , len(test_lines()) )-1]
    list= fillordi(lignechoisie)
    return list

def niv4(list):
    try:
        lignechoisie = test_3util_align() [randint( 1 , len(test_3util_align()) )-1]
    except:
        try:
            lignechoisie = test_3ordi_align() [randint( 1 , len(test_3ordi_align()) )-1]
        except:
            try:
                lignechoisie = test_2ordi_align() [randint( 1 , len(test_2ordi_align()) )-1]
            except:
                lignechoisie = test_lines() [randint( 1 , len(test_lines()) )-1]
    list= fillordi(lignechoisie)
    return list


def test_3util_align():
    test_3util_align=[]
    for colonne in range(7):
        for i in range(4):
            if list[colonne][i:i+3]==["X","X","X"]:                      # sur une verticale
                try:
                    if list[colonne][i-1]== " " :
                        test_3util_align.append(colonne)
                except:
                    continue
    Tlist= trans(list)
    for i in range(len(Tlist)):
        for colonne in range(5):
            if Tlist[i][colonne:colonne+3]==["X","X","X"]:
                try:
                    if Tlist[i][colonne-1]== " " :                 #sur une horizontale
                        test_3util_align.append(colonne-1)
                except:
                    continue
                try:
                    if Tlist[i][colonne+3]== " " :
                        test_3util_align.append(colonne+3)
                except:
                    continue
    for colonne in range(4):
        for i in range(3,6):
            if [list[colonne][i],list[colonne+1][i-1],list[colonne+2][i-2]] == ["X","X","X"]:     # sur diagonale de en bas a gauche à en haut a droite              
                try:
                    if list[colonne+3][i-3]== " " :
                        test_3util_align.append(colonne+3)
                except:
                    continue
                try:
                    if list[colonne-1][i+1]== " " :
                        test_3util_align.append(colonne-1)
                except:
                    continue
    for colonne in range(3,7):
        for i in range(3,6):
            if [list[colonne][i],list[colonne-1][i-1],list[colonne-2][i-2]] == ["X","X","X"]:     # sur diagonale de en bas a doite à en haut a gauche 
                try:
                    if list[colonne-3][i-3]== " " :
                        test_3util_align.append(colonne-3)
                except:
                    continue
                try:
                    if list[colonne+1][i+1]== " " :
                        test_3util_align.append(colonne+1)
                except:
                    continue
    return test_3util_align

def test_3ordi_align():
    test_align=[]
    for colonne in range(7):
        for i in range(4):
            if list[colonne][i:i+3]==[0,0,0]:                      # sur une verticale
                try:
                    if list[colonne][i-1]== " " :
                        test_align.append(colonne)
                except:
                    continue
    Tlist= trans(list)
    for i in range(len(Tlist)):
        for colonne in range(5):
            if Tlist[i][colonne:colonne+3]==[0,0,0]:            #sur une horizontale
                try:
                    if Tlist[i][colonne-1]== " " :
                        test_align.append(colonne-1)
                except:
                    continue
                try:
                    if Tlist[i][colonne+3]== " " :
                        test_align.append(colonne+3)
                except:
                    continue
    for colonne in range(4):
        for i in range(3,6):
            if [list[colonne][i],list[colonne+1][i-1],list[colonne+2][i-2]] == [0,0,0]:     # sur diagonale de en bas a gauche à en haut a droite
                try:
                    if list[colonne+3][i-3]== " " :
                        test_align.append(colonne+3)
                except:
                    continue
                try:
                    if list[colonne-1][i+1]== " " :
                        test_align.append(colonne-1)
                except:
                    continue
    for colonne in range(3,7):
        for i in range(3,6):
            if [list[colonne][i],list[colonne-1][i-1],list[colonne-2][i-2]] == [0,0,0]:     # sur diagonale de en bas a doite à en haut a gauche 
                try:
                    if list[colonne-3][i-3]== " " :
                        test_align.append(colonne-3)
                except:
                    continue
                try:
                    if list[colonne+1][i+1]== " " :
                        test_align.append(colonne+1)
                except:
                    continue
    return test_align

def test_2ordi_align():
    test_align=[]
    for colonne in range(7):
        for i in range(4):
            if list[colonne][i:i+3]==[0,0]:                      # sur une verticale
                try:
                    if list[colonne][i-1]== " " :
                        test_align.append(colonne)
                except:
                    continue
    Tlist= trans(list)
    for i in range(len(Tlist)):
        for colonne in range(5):
            if Tlist[i][colonne:colonne+3]==[0,0]:            #sur une horizontale
                try:
                    if Tlist[i][colonne-1]== " " :
                        test_align.append(colonne-1)
                except:
                    continue
                try:
                    if Tlist[i][colonne+3]== " " :
                        test_align.append(colonne+3)
                except:
                    continue
    for colonne in range(4):
        for i in range(3,6):
            if [list[colonne][i],list[colonne+1][i-1],list[colonne+2][i-2]] == [0,0]:     # sur diagonale de en bas a gauche à en haut a droite
                try:
                    if list[colonne+3][i-3]== " " :
                        test_align.append(colonne+3)
                except:
                    continue
                try:
                    if list[colonne-1][i+1]== " " :
                        test_align.append(colonne-1)
                except:
                    continue
    for colonne in range(3,7):
        for i in range(3,6):
            if [list[colonne][i],list[colonne-1][i-1],list[colonne-2][i-2]] == [0,0]:     # sur diagonale de en bas a doite à en haut a gauche 
                try:
                    if list[colonne-3][i-3]== " " :
                        test_align.append(colonne-3)
                except:
                    continue
                try:
                    if list[colonne+1][i+1]== " " :
                        test_align.append(colonne+1)
                except:
                    continue
    return test_align

def affichage(list):
    Tlist= trans(list)
    print("|" + "".join(map(str,Tlist[0])) + "|",)
    print("|" + "".join(map(str,Tlist[1])) + "|",)
    print("|" + "".join(map(str,Tlist[2])) + "|",)
    print("|" + "".join(map(str,Tlist[3])) + "|",)
    print("|" + "".join(map(str,Tlist[4])) + "|",)
    print("|" + "".join(map(str,Tlist[5])) + "|",)
    print("-1234567-")

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
    for i in range(len(list)):
        if " " in list[i]:
            testlines.append(i)
    return testlines

def read(nivf,list):
    affichage(list)                         #affichage du plateau
    choixjoueur= input(messtour)
    while choixjoueur not in "1234567"or int(choixjoueur)-1 not in test_lines() :#test si ligne pas remplie
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
    
    
    
list= [ [" " for i in range(6)] for i in range(7)]

print(bienvenue)
inputniv = int(input(niv))
#seed(int(input(messseed)))

if inputniv == 1:
    while not test_fin(list) :
        read(niv1,list)
if inputniv == 2:
    while not test_fin(list) :
        read(niv2,list)
if inputniv == 3:
    while not test_fin(list) :
        read(niv3,list)
if inputniv == 4:
    while not test_fin(list) :
        read(niv4,list)


