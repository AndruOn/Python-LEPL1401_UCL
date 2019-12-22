

import sys

def test(did_pass):                                    #On définit d'abord une fonction "did_pass" que l'on va utiliser dans les autres fonctions test.
  
    """  Print the result of a test."""
    
    linenum = sys._getframe(1).f_lineno
    if did_pass:
        msg = "Test at line {0} ok.".format(linenum)
    else:
        msg = ("Test at line {0} FAILED.".format(linenum))
    print(msg)



def count(n,l):
    cou=0
    for i in l:
        if isinstance(i,list):
            cou+=count(n,i)
        else:
            if i == n:
                cou += 1
    return cou
             
            
            
            
            
test(count(2, []) == 0)
test(count(2, [2, 9, [2, 1, 13, 2], 8, [2, 6]]) == 4)
test(count(7, [[9, [7, 1, 13, 2], 8], [7, 6]]) == 2)
test(count(15, [[9, [7, 1, 13, 2], 8], [2, 6]]) == 0)
test(count(5, [[5, [5, [1, 5], 5], 5], [5, 6]]) == 6)
test(count("a", [["this",["a",["thing","a"],"a"],"is"], ["a","easy"]]) == 4)