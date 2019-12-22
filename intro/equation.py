 
 
solutions = 0   #permet de donner le nombre de solutions
a = int(input("Entrez la valeur du coefficient a : "))
b = int(input("Entrez la valeur du coefficient b : "))
c = int(input("Entrez la valeur du coefficient c : "))
max = int(input("Entrez la valeur maximale pour x et y : "))

for x in range(1,max):      #je test pour toutes les valeurs jusqu'au max
    for y in range(1,max):
        for z in range(1,max):
            if x**a + y**b == z**c:
                print("x =", x, " y =", y," z =",z)
                solutions += 1
                
if solutions == 0:
    print("Aucune solution trouvée")
elif solutions == 1:
    print(solutions," solution trouvée")
else:
    print(solutions," solutions trouvées")
                