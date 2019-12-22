import random

print("C'est parti pour un Yahtzee !")
print("Pour rappel, voici un résumé du jeu (modifié).")
print("Le principe de ce jeu est de réussir a obtenir 5 dés de même valeur.")
print("Pour vous faciliter la vie, je vais vous faire le premier lancé.")
print("Mais par la suite, vous allez devoir choisir quel dé relancé ou non")
print("pour arriver au yahtzee avec le moins de coup possible!")
print("A vous de créer les technique les plus farfelues pour être le plus efficace")
print("Voyons en combien de coup vous allez réussir ...")
print()
ready= input(print("Si vous étes prêt, appuyez sur enter"))
n = 5
l = 1
print()
print()
print()
print()

def verify():
    k = 0
    for i in range (n-1):
        if dés[1][i] == dés [1][i+1]:
            k += 1
    if k == n-1:
        return True
    else:
        return False
    
def change():
    print()
    print("Dommage! Il faut relancer. Les dés vont maintenant être énumérés.")
    print("Si vous voulez relancer le dé cité, écrivez O ou 0, dans le cas contraire, écrivez N, 1 ou rien.")
    print()
    for j in range (n):
        rep = input(print("Voulez-vous remplacer le dé numéro ", j+1, " ?"))
        if rep == "0" or rep == "o" or rep == "O":
            dés[1][j] = (random.randint(1,6))
    print()
    
#initialisation lancé de dés
dés = []
numéro = []
résultat = []

for i in range(n):
    numéro.append(i+1)
dés.append(numéro)
    
for j in range(n):
    dé = (random.randint(1,6))
    résultat.append(dé)
dés.append(résultat)
    
print("La première ligne représente le numéro du dé, la deuxième représente le chiffre obtenu sur ce dé")
print(dés[0])
print(dés[1])

for w in range (500000):
    if verify() == False:
        change()
        l += 1
        print("Voici votre ", l, "ième lancé")
        print(dés[0])
        print(dés[1])
    else:
        break
    
if l <= 5:
    print("Félicitations! Vous avez réussi en ", l, "coups!")
if 5 < l <= 10:
    print("Pas mal, vous avez réussi en ", l, " coups.")
if 10 < l <= 20:
    print("T'as réussi mais c'est pas bon, t'as réussi en ", l, " coups.")
if 20 < l:
    print("Wah t'es nul c'est chaud gro ... je vais pas te dire ton score pour pas que tu tombe en dépression mais ...")
    print("T'as déjà pensé au suicide ?")
    print("PS: t'as fait ", l)