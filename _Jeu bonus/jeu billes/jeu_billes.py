# Auteur : Dang Pham/Andru Onciul
# Date : 11/10/18
# But du programme : Projet 1 Billes

from random import randint, seed
import messages

def anti_triche1(bi_enlev):
    while bi_enlev > 4 or bi_enlev < 1:
        print(messages.message_10)                    #Vérifie si utilisateur respecte 0 < bi_enlev < 5
        print(messages.message_4.format(bi_tot))
        bi_enlev = int(input(messages.entree_3))
    return bi_enlev
    
def anti_triche2(bi_tot):
    while bi_tot > 40 or bi_tot < 7:
        print(messages.message_10)                    #Vérifie si utilisateur respecte 7 < bi_tot < 41
        bi_tot = int(input(messages.entree_2))
    return bi_tot
        

print(messages.message_1)
#seed(int(input(messages.entree_1)))                  #Rendre le randit non aléatoire pour débuguer plus facilement
envie_de_jouer = "oui"

while envie_de_jouer == "oui":
    print(messages.message_2)
    bi_tot = int(input(messages.entree_2))
    bi_tot = anti_triche2(bi_tot)
    print(messages.message_3)
    
    
    print(messages.message_4.format(bi_tot))
    bi_enlev = int(input(messages.entree_3))
    anti_triche1(bi_enlev)
    bi_tot -= bi_enlev
    
    while 40 > bi_tot > 5:
        
        print(messages.message_5.format(bi_tot))
        print(messages.message_6)

        if (bi_tot - 1) % 5 == 0:
            nb_ale = randint(1, 100)
            if nb_ale <= 70:
                print(messages.message_7.format(1))
                bi_tot -= 1
            else:
                print(messages.message_7.format(2))
                bi_tot -= 2

        else:
            bi_enlev = (bi_tot - 1) % 5
            print(messages.message_7.format(bi_enlev))
            bi_tot -= bi_enlev
       
        print(messages.message_4.format(bi_tot))
        bi_enlev = int(input(messages.entree_3))
        anti_triche1(bi_enlev)
        bi_tot -= bi_enlev
    
    if bi_tot == 1 :
        print(messages.message_8)

    else:
        print(messages.message_5.format(bi_tot))
        print(messages.message_6)

        a = (bi_tot - 1) % 5
        print(messages.message_7.format(a))
        bi_tot -= a
        print(messages.message_9)
        
    envie_de_jouer = str(input(messages.entree_4))

if messages.entree_4 != "oui":
    print("T'as le seum de perdre c'est pour ça ?")