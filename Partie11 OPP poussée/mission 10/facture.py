"""
    Une facture, sous forme d'une liste d'articles.
   
    @author Kim Mens
    @version 18 novembre 2018
    (code adapté du code java de Charles Pecheur)
"""

class Facture :

    __numcls= 1
    
    def __init__(self, description, articles):
        """
        Crée une facture avec une description (titre) et un liste d'articles.
        """
        self.__num = Facture.__numcls
        Facture.__numcls +=1
        self.__reference = description
        self.__articles = articles

    def description(self):
        """
        Retourne la description de cette facture.
        """
        return self.__reference

    def articles(self):
        """
        Retourne la liste des articles de cette facture.
        """
        return self.__articles
        
    def __str__(self):
        """
        Retourne la représentation string d'une facture, à imprimer avec la méthode print().
        """
        s = self.entete_str()
        totalPrix = 0.0
        totalTVA = 0.0
        for art in self.articles() :
            s += self.article_str(art)
            totalPrix = totalPrix + art.prix()
            totalTVA = totalTVA + art.tva()
        s += self.totaux_str(totalPrix, totalTVA)
        return s

    def entete_str(self):
        """
        Imprime l'entête de la facture, comprenant le descriptif et les têtes de colonnes.
        """
        e = "Facture " +"No " + str(self.__num) + " : Fracture " +self.description() + "\n"
        e += self.barre_str()
        e += "| {0:<40} | {1:>10} | {2:>10} | {3:>10} |\n".format("Description","prix HTVA","TVA","prix TVAC")
        e += self.barre_str()
        return e

    def barre_str(self):
        """
        Retourne un string représentant une barre horizontale sur la largeur de la facture.
        """
        b = ""
        barre_longeur = 83
        for i in range(barre_longeur):
            b += "="
        return b + "\n"

    def article_str(self, art):
        """
        Retourne un string correspondant à une ligne de facture pour l'article art
        """
        return "| {0:40} | {1:10.2f} | {2:10.2f} | {3:10.2f} |\n".format(art.description(), art.prix(), art.tva(), art.prix_tvac())
    
    def totaux_str(self, prix, tva):
        """
        Retourne un string représentant une ligne de facture avec les totaux prix et tva, à imprimer en bas de la facture
        """
        b = self.barre_str()
        b += "| {0:40} | {1:10.2f} | {2:10.2f} | {3:10.2f} |\n".format("T O T A L", prix, tva, prix+tva)
        b += self.barre_str()
        return b
        
    # This method needs to be added during Etape 4 of the mission
    def nombre(self, pce) :
        """
        Retourne le nombre d'exemplaires de la pièce pce dans la facture, en totalisant sur tous les articles qui concernent cette pièce.
        """
        count=0
        for piece in self.articles:
            if pce == piece:
                count+=1
        return count

    # This method needs to be added during Etape 5 of the mission
    def livraison_str(self):
        """
        Cette méthode est une méthode auxiliaire pour la méthode printLivraison
        """
        en_tete = "Livraison - " + self.enteteliv
        totalnbre = 0.0
        totalprix = 0.0
        for art in self.list_articpiece() :
            s += self.article_str(art)
            totalPrix = totalPrix + art.prix()
            totalTVA = totalTVA + art.tva()
        s += self.totauxliv(totalnbre, totalprix)
        return s
    
    def enteteliv(self):
        """
        Imprime l'entête de la facture, comprenant le descriptif et les têtes de colonnes.
        """
        e = "Facture " +"No " + str(self.__num) + " : Fracture " +self.description() + "\n"
        e += self.barre_str()
        e += "| {0:<40} | {1:>10} | {2:>10} | {3:>10} |\n".format("Description","poids/pce","nombre","poids")
        e += self.barre_str()
        return e
    
    def list_articpiece(self):
        listart=self.articles.copy()
        list=[]
        for art in self.articles:
            nbre= self.nombre(art)
            for artpce in list:
                if artpce == art:
                    list.remove(art)
            list.append(ArticlePiece( nbre , art  ))
        return list
            
    def totauxliv(self,diffart,nbre,poids):
        b = self.barre_str()
        b += "| {0:31} articles | {1:10.2f} | {2:10.2f} | {3:10.2f} |\n".format(diffart, " ", nbre, poids)
        b += self.barre_str()
        
    
