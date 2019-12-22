from article import Article
from facture import Facture


class ArticleReparation(Article):
    
    def __init__(self,d,p,temps):
        super.__init__(d,p)
        self.__temps= temps
        
    def description():
        return ("Reparation ({0:.2f} heures)".format(self.__temps) )
    
    def prix():
        return (self.__temps * 35 + 20)
    
    
class Piece:
    def __init__(self, description, prix, poids=0, fragile=False, tva=False):
        self.__description = description
        self.__prix = prix
        self.__poids = poids
        self.__fragile = fragile
        self.__tva = tva
    
    def description():
        return self.__description
    def prix():
        return self.__prix
    def poids():
        return self.__poids
    def fragile():
        return self.__fragile
    def tva_reduit():
        return self.__tva
    
    def __eq__(self, P):
        if self.__description == P.__description and self.__prix == P.__prix:
            return True
        return False
    def __str__(self):
        pass
    
    
class ArticlePiece(Article):
    
    
    def __init__(self,nbre,piece):
        super().__init__(piece.description(),piece.prix())
        self.__nbre = nbre
        self.__piece= piece
        
    def nbre(self):
        return self.__nbre
        
    def piece(self):
        return self.__piece
        
    def definition(self):
        return ( "{0} * {1} @ {2}".format(self.nbre() ,self.piece().description() ,self.piece().prix()) )
    
    def prix(self):
        return self.__nbre * self.__piece
    
    def tva(self):
        if self.__piece.tva_reduit():
            return self.prix() * 0.06
        return super().tva()
            
    

    
    
    
    