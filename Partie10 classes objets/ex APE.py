
class Student :

    def __init__(self,n) :
        """
        Initialise un nouvel objet de type Student avec un nom n donné.
        @pre:  -
        @post: Un objet de type Student a été créé avec comme 'name' n,
               et un score None pour chacun des trois tests 'test1', 'test2' et 'test3'
        """
        # nom de l'étudiant
        self.name = n
        # score reçu par l'étudiant sur trois tests
        # (initialement None car l'étudiant n'a pas encore passé les tests)
        self.test1 = None
        self.test2 = None
        self.test3 = None

    def average_score(self) :
        """"
        Calcul du score moyen que l'étudiant a obtenu sur les 3 tests.
        @pre: les variables d'instance test1, test2 et test3
              contiennent des valeurs de type int
        @post: retourne la valeur moyenne de ces trois valeurs
        """
        return (self.test1 + self.test2 + self.test3) / 3
    
    def __str__(self):
       return ( "Bonjour,"+ self.name+ ". Vos scores sont:\n"+ str(self.test1)+ "\n" + str(self.test2) +"\n"+ str(self.test3) + "\nVotre score moyenne est "+ str(self.average_score()) )
    
student = Student("Kim")
student.test1 = 14.0
student.test2 = 10.5
student.test3 = 12.0
print(student)
        