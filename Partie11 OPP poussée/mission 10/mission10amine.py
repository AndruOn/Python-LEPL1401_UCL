from article import Article



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
    
    def description(self):
        return self.__description
    def prix(self):
        return self.__prix
    def poids(self):
        return self.__poids
    def fragile(self):
        return self.__fragile
    def tva_reduit(self):
        return self.__tva
    
    def __eq__(self, P):
        if self.__description == P.__description and self.__prix == P.__prix:
            return True
        return False

        
    
class ArticlePiece(Article):
    
    
    def __init__(self,nbre,piece):
        super().__init__(piece.description(), piece.prix())
        self.__nbre = nbre
        self.__piece= piece
        
    def nbre(self):
        return self.__nbre
        
    def piece(self):
        return self.__piece
        
    def description(self):
        if self.nbre()==1:
            return ( "{0} @ {1} {2}".format(self.piece().description() ,self.piece().prix(),self.ifprint_frag() ))
        else:
            return ( "{0} * {1} @ {2} {3}".format(self.nbre() ,self.piece().description() ,self.piece().prix() ,self.ifprint_frag() ) )
        
    def poids(self):
        return self.__piece.poids()
    def fragile(self):
        return self.__piece.fragile()
    def tva_art(self):
        return self.piece().tva_reduit()
    def poids_tot(self):
        return self.__nbre * self.poids()
    def prix(self):
        return self.__nbre * self.piece().prix() 
    def tva(self):
        if self.__piece.tva_reduit():
            return self.prix() * 0.06
        return super().tva()
    def ifprint_frag(self):
        if self.fragile():
            return "(!)"
        return ""
        
    def __eq__(self,art):
        if self.__piece == art.piece():
            return True
        return False

class Facture :

    __numcls= 1
    
    def __init__(self, description, articles):
        """
        Crée une facture avec une description (titre) et un liste d'articles.
        """
        self.__num = Facture.__numcls
        Facture.__numcls +=1
        self.__reference = description
        artpce= []
        for art in articles:
            if type(art) == ArticlePiece:
                artpce.append(art)
            else:
                artpce.append(ArticlePiece(1,Piece(art.description(),art.prix())))
            
        self.__articles = artpce

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
        
    def fact_str(self):
        """
        Retourne la représentation string d'une facture, à imprimer avec la méthode print().
        """
        s = self.entete_str()
        totalPrix = 0.0
        totalTVA = 0.0
        liste= self.list_articpiece()
        for art in liste :
            s += self.article_str(art)
            totalPrix = totalPrix + art.prix()
            totalTVA = totalTVA + art.tva()
        s += self.totaux_str(totalPrix, totalTVA)
        return s

    def entete_str(self):
        """
        Imprime l'entête de la facture, comprenant le descriptif et les têtes de colonnes.
        """
        e = "Facture " +"No " + str(self.__num) + " : " +self.description() + "\n"
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
    def nombre(self,pce) :
        """
        Retourne le nombre d'exemplaires de la pièce pce dans la facture, en totalisant sur tous les articles qui concernent cette pièce.
        """
        count= 0
        for art in self.articles():
            if pce == art.piece():
                count+= art.nbre()
        return count

    # This method needs to be added during Etape 5 of the mission
    def livraison_str(self):
        """
        Cette méthode est une méthode auxiliaire pour la méthode printLivraison
        """
        s = "Livraison - " + self.enteteliv()
        totalnbre = 0
        totalpoids = 0.0
        nbre_dart=0
        liste_art= self.list_articpiece()
        for art in liste_art :
            s += self.articleliv_str(art)
            totalnbre += art.nbre()
            totalpoids += art.poids_tot()
            nbre_dart+=1
        s += self.totauxliv(nbre_dart,totalnbre, totalpoids)
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
        liste=[]
        for art in self.articles():
            nbre= self.nombre(art.piece())
            count = 0
            for art1 in liste:
                if art1 == art:
                    count = 1
            if count == 0:
                liste.append(ArticlePiece(nbre,Piece(art.piece().description(), art.piece().prix(), art.poids(), art.fragile(), art.tva_art())))
                    
        return liste

    def articleliv_str(self, art):
        """
        Retourne un string correspondant à une ligne de facture pour l'article art
        """
        return "| {0:40} | {1:10.2f} | {2:10} | {3:10.2f} |\n".format(art.description(), art.piece().poids(), int(art.nbre()), art.poids_tot())

    def totauxliv(self,diffart,nbre,poids):
        b = self.barre_str()
        txt= str(diffart)+ " articles"
        b += "| {0:40} |            | {1:10} | {2:10.2f} |\n".format(txt, nbre , poids)
        b += self.barre_str()
        return b

    def if_fragile(self):
        for art in self.articles():
            if art.piece().fragile():
                return "(!) *** livraison fragile ***"
        return ""

    def __str__(self):
        str=self.fact_str()
        str+= "\n"
        str+=self.livraison_str()
        str+= self.if_fragile()
        return str


articles = [ Article("laptop 15\" 8GB RAM", 743.79),
                 Article("installation windows", 66.11),
                 Article("installation wifi", 45.22),
                 Article("carte graphique", 119.49),
                 ArticlePiece(1, Piece("disque dur 350 GB", 49.99, 0.355, True)),
                 ArticlePiece(3, Piece("souris bluetooth", 15.99, 0.176)),
                 ArticlePiece(5, Piece("adaptateur DVI - VGA", 12.00)),
                 ArticlePiece(2, Piece("Java in Nutshell", 24.00, 0.00, False, True)),
                 ArticlePiece(5, Piece("souris bluetooth", 15.99, 0.176))]
    

fac = Facture("PC Store - 22 novembre", articles)
print(fac)
