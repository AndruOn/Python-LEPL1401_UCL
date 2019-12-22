#un programme qui d onne une table des carrés et des sommes des carrés
#par andru onciul

a = 1
c = a * a   #la variable c sert a afficher la somme des carrés

while a <=10:    #une boucle while qui sera effectuée jusqu'a a=10 
    print(a,"\t",a*a,"\t",c)   #un tableau grace au \t
    a+=1      # a augmente de 1 à chaque tour de la bouvle
    c = c + a*a    #le carré de a est a chaque tour ajouté a la valeur de c