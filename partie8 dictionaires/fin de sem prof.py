
    
    
def topk(tuples,k):
     """ 
      pre: tuples est une liste 
      post: retourne les top-k tuples de la liste. Si deux (ou plus) tuples ont la meme frequence, ils sont retournes egalement
  """ 
  sorted_tuples = sorted(tuples,reverse=True)
  result = sorted_tuples[0:k]
  
  # Il faut printer tous les mots de mm frequence, pas seulement k
  k2 = k                           
  while k2 < len(sorted_tuples) and sorted_tuples[k2][0] == sorted_tuples[k-1][0]:
    result.append ( sorted_tuples[k2] )
    k2 += 1
  
  return result


def topk_words ( words, k ):
  """
  pre:  words est une liste de mots, k est un nombre entier > 0
  post: Renvoie les k mots les plus fréquents dans la liste de mots, 
            en utilisant une liste de tuples (compte, mot) en ordre décroissant; 
            si plusieurs mots ont la même fréquence que le k^me mot, tous les mots 
            avec cette fréquence sont retournés.
  """ 
