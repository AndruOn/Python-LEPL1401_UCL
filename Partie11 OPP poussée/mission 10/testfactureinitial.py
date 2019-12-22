from article import Article

from mission10amine import ArticlePiece, Facture, Piece



class TestFactureInitial :

    articles = [ Article("laptop 15\" 8GB RAM", 743.79),
                 Article("installation windows", 66.11),
                 Article("installation wifi", 45.22),
                 Article("carte graphique", 119.49),
                 ArticlePiece(1, Piece("disque dur 350 GB", 49.99, 0.355, True)),
                 ArticlePiece(3, Piece("souris bluetooth", 15.99, 0.176)),
                 ArticlePiece(5, Piece("adaptateur DVI - VGA", 12.00)),
                 ArticlePiece(2, Piece("Java in Nutshell", 24.00, 0.00, False, True)),
                 ArticlePiece(5, Piece("souris bluetooth", 15.99, 0.176))]
    
    @classmethod
    def run(cls) :
        fac = Facture("PC Store - 22 novembre", cls.articles)
        print(fac)

if __name__ == "__main__":
    TestFactureInitial.run()


        