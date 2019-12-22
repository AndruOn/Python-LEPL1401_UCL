import sys

def test(did_pass):                                    #On définit d'abord une fonction "did_pass" que l'on va utiliser dans les autres fonctions test.
  
    """  Print the result of a test."""
    
    linenum = sys._getframe(1).f_lineno
    if did_pass:
        msg = "Test at line {0} ok.".format(linenum)
    else:
        msg = ("Test at line {0} FAILED.".format(linenum))
    print(msg)