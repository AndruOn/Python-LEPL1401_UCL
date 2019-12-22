import sys
import bioinfo

"""
  Placez vos methodes de tests ci-dessous.

  Pour vos tests, vous pouvez vous aider des exemples suivants:

  Une courte sequence d'ADN valide
"""
short_adn  = "gatcctccatatacaacggtatctccacctcaggtttagatctcaacaacggaaccattgccgacatgagac"


long_adn = """gatcctccatatacaacggtatctccacctcaggtttagatctcaacaacggaaccattgccgacatgagacagttaggtatcgtcgagagttacaagctaaaacgagcagt
agtcagctctgcatctgaagccgctgaagttctactaagggtggataacatcatccgtgcaagaccaagaaccgccaatagacaacatatgtaacatatttaggatatacctcgaaaataataaaccgcca
cactgtcattattataattagaaacagaacgcaaaaattatccactatataattcaaagacgcgaaaaaaaaagaacaacgcgtcatagaacttttggcaattcgcgtcacaaataaattttggcaactt
atgtttcctcttcgagcagtactcgagccctgtctcaagaatgtaataaatacccatcgtaggtatggttaaagatagcatctccacaacctcaaagctccttgccgagagtcgccctcctttgtcgagt
aattttcacttttcatatgagaacttattttcttattctttactctcacatcctgtagtgattgacactgcaacagccaccatcactagaagaacagaacaattacttaatagaaaaattatatcttcct
cgaaacgatttcctgcttccaacatctacgtatatcaagaagcattcacttaccatgacacagcttcagatttcattattgctgacagctactatatcactactccatctagtagtggccacgccctat
gaggcatatcctatcggaaaacaataccccccagtggcaagagtcaatgaatcgtttacatttcaaatttccaatgatacctataaatcgtctgtagacaagacagctcaaataacatacaattgctt
cgacttaccgagctggctttcgtttgactctagttctagaacgttctcaggtgaaccttcttctgacttactatctgatgcgaacaccacgttgtatttcaatgtaatactcgagggtacggactctg
ccgacagcacgtctttgaacaatacataccaatttgttgttacaaaccgtccatccatctcgctatcgtcagatttcaatctattggcgttgttaaaaaactatggttatactaacggcaaaaacgct
ctgaaactagatcctaatgaagtcttcaacgtgacttttgaccgttcaatgttcactaacgaagaatccattgtgtcgtattacggacgttctcagttgtataatgcgccgttacccaattggctgtt
cttcgattctggcgagttgaagtttactgggacggcaccggtgataaactcggcgattgctccagaaacaagctacagttttgtcatcatcgctacagacattgaaggattttctgccgttgaggtag
aattcgaattagtcatcggggctcaccagttaactacctctattcaaaatagtttgataatcaacgttactgacacaggtaacgtttcatatgacttacctctaaactatgtttatctcgatgacgat
cctatttcttctgataaattgggttctataaacttattggatgctccagactgggtggcattagataatgctaccatttccgggtctgtcccagatgaattactcggtaagaactccaatcctgccaa
tttttctgtgtccatttatgatacttatggtgatgtgatttatttcaacttcgaagttgtctccacaacggatttgtttgccattagttctcttcccaatattaacgctacaaggggtgaatggttctcc
tactattttttgccttctcagtttacagactacgtgaatacaaacgtttcattagagtttactaattcaagccaagaccatgactgggtgaaattccaatcatctaatttaacattagctggagaagtgccc
aagaatttcgacaagctttcattaggtttgaaagcgaaccaaggttcacaatctcaagagctatattttaacatcattggcatggattcaaagataactcactcaaaccacagtgcgaatgcaacgtccacaa
gaagttctcaccactccacctcaacaagttcttacacatcttctacttacactgcaaaaatttcttctacctccgctgctgctacttcttctgctccagcagcgctgccagcagccaataaaacttcatctca
caataaaaaagcagtagcaattgcgtgcggtgttgctatcccattaggcgttatcctagtagctctcatttgcttcctaatattctggagacgcagaagggaaaatccagacgatgaaaacttaccgcatgc
tattagtggacctgatttgaataatcctgcaaataaaccaaatcaagaaaacgctacacctttgaacaacccctttgatgatgatgcttcctcgtacgatgatacttcaatagcaagaagattggctgctt
tgaacactttgaaattggataaccactctgccactgaatctgatatttccagcgtggatgaaaagagagattctctatcaggtatgaatacatacaatgatcagttccaatcccaaagtaaagaagaatta
ttagcaaaacccccagtacagcctccagagagcccgttctttgacccacagaataggtcttcttctgtgtatatggatagtgaaccagcagtaaataaatcctggcgatatactggcaacctgtcaccagtct
ctgatattgtcagagacagttacggatcacaaaaaactgttgatacagaaaaacttttcgatttagaagcaccagagaaggaaaaacgtacgtcaagggatgtcactatgtcttcactggacccttggaacag
caatattagcccttctcccgtaagaaaatcagtaacaccatcaccatataacgtaacgaagcatcgtaaccgccacttacaaaatattcaagactctcaaagcggtaaaaacggaatcactcccacaacaatgt
caacttcatcttctgacgattttgttccggttaaagatggtgaaaatttttgctgggtccatagcatggaaccagacagaagaccaagtaagaaaaggttagtagatttttcaaataagagtaatgtcaatgtt
ggtcaagttaaggacattcacggacgcatcccagaaatgctgtgattatacgcaacgatattttgcttaattttattttcctgttttattttttattagtggtttacagataccctatattttatttagttttt
atacttagagacatttaattttaattccattcttcaaatttcatttttgcacttaaaacaaagatccaaaaatgctctcgccctcttcatattgagaatacactccattcaaaattttgtcgtcaccgctgat
taatttttcactaaactgatgaataatcaaaggccccacgtcagaaccgactaaagaagtgagttttattttaggaggttgaaaaccattattgtctggtaaattttcatcttcttgacatttaacccagtttg
aatccctttcaatttctgctttttcctccaaactatcgaccctcctgtttctgtccaacttatgtcctagttccaattcgatcgcattaataactgcttcaaatgttattgtgtcatcgttgactttaggtaatµ
ttctccaaatgcataatcaaactatttaaggaagatcggaattcgtcgaacacttcagtttccgtaatgatctgatcgtctttatccacatgttgtaattcactaaaatctaaaacgtatttttcaatgcataa
atcgttctttttattaataatgcagatggaaaatctgtaaacgtgcgttaatttagaaagaacatccagtataagttcttctatatagtcaattaaagcaggatgcctattaatgggaacgaactgcggcaagt
tgaatgactggtaagtagtgtagtcgaatgactgaggtgggtatacatttctataaaataaaatcaaattaatgtagcattttaagtataccctcagccacttctctacccatctattcataaagctgacgcaa
cgattactattttttttttcttcttggatctcagtcgtcgcaaaaacgtataccttctttttccgaccttttttttagctttctggaaaagtttatattagttaaacagggtctagtcttagtgtgaaagctag
tggtttcgattgactgatattaagaaagtggaaattaaattagtagtgtagacgtatatgcatatgtatttctcgcctgtttatgtttctacgtacttttgatttatagcaaggggaaaagaaatacatactat
tttttggtaaaggtgaaagcataatgtaaaagctagaataaaatggacgaaataaagagaggcttagttcatcttttttccaaaaagcacccaatgataataactaaaatgaaaaggatttgccatctgtcagc
aacatcagttgtgtgagcaataataaaatcatcacctccgttgcctttagcgcgtttgtcgtttgtatcttccgtaattttagtcttatcaatgggaatcataaattttccaatgaattagcaatttcgtccaa
ttctttttgagcttcttcatatttgctttggaattcttcgcacttcttttcccattcatctctttcttcttccaaagcaacgatccttctacccatttgctcagagttcaaatcggcctctttcagtttatcca
ttgcttccttcagtttggcttcactgtcttctagctgttgttctagatcctggtttttcttggtgtagttctcattattagatctcaagttattggagtcttcagccaattgctttgtatcagacaattgactc
tctaacttctccacttcactgtcgagttgctcgtttttagcggacaaagatttaatctcgttttctttttcagtgttagattgctctaattctttgagctgttctctcagctcctcatatttttcttgccatga
ctcagattctaattttaagctattcaatttctctttgat"""

"Un petit palindrome"
palindrome1 = "ttaggatt";

"Un autre palindrome"
palindrome2 = "catggcactttgagcattttagccgattttacgagtttcacggtac"

"Une chaine qui n'est pas une chaine ADN"
invalid_adn = long_adn + "z" + short_adn



def test(did_pass):                                    #On définit d'abord une fonction "did_pass" que l'on va utiliser dans les autres fonctions test.
  
    """  Print the result of a test."""
    
    linenum = sys._getframe(1).f_lineno
    if did_pass:
        msg = "Test at line {0} ok.".format(linenum)
    else:
        msg = ("Test at line {0} FAILED.".format(linenum))
    print(msg)
    

def test_is_adn():
    
    """Run the sequence of DNA and returns true if it only contains "a,c,t,g" and false in any other case
    """
    test(bioinfo.is_adn(short_adn) == True)
    test(bioinfo.is_adn(invalid_adn) == False)
    test(bioinfo.is_adn("atcg") == True)
    test(bioinfo.is_adn("ttcg") == True)
    test(bioinfo.is_adn("atgg") == True)
    test(bioinfo.is_adn("atcc") == True)
    test(bioinfo.is_adn("ACTG") == True)
    test(bioinfo.is_adn("CCTG") == True)
    test(bioinfo.is_adn("ACCG") == True)
    test(bioinfo.is_adn("ACTT") == True)
    test(bioinfo.is_adn("xtcg") == False)
    test(bioinfo.is_adn("atxg") == False)
    test(bioinfo.is_adn("atcx") == False)
    test(bioinfo.is_adn("XTCG") == False)
    test(bioinfo.is_adn("ATXG") == False)
    test(bioinfo.is_adn("ATCX") == False)


def test_positions():
    test(bioinfo.positions("ACCG","t") == [])
    test(bioinfo.positions("ACCTG","t") == [3])
    test(bioinfo.positions("ACTCC","c") == [1, 3, 4])
    test(bioinfo.positions("ACTCCFDGCTCB","ctc") == [1, 8])   
    

def test_distance_h():
    test(bioinfo.distance_h("AA","AA") == 0)
    test(bioinfo.distance_h("ACTG","AATG") == 1)
    test(bioinfo.distance_h("ACTG","ACGD") == 2)
    test(bioinfo.distance_h("ATCG","ATTCG") == None)

def test_inverse():
    test(bioinfo.inverse("A") == "A")
    test(bioinfo.inverse("ATCG") == "GCTA")
        
def test_plus_long_palindrome():
    test(bioinfo.plus_long_palindrome("AXVG") == "A")
    test(bioinfo.plus_long_palindrome("ACCTGTTAGGATTC") == "TTAGGATT")
    test(bioinfo.plus_long_palindrome("") == None)
    test(bioinfo.plus_long_palindrome(palindrome1) == palindrome1)
    test(bioinfo.plus_long_palindrome("ACTGGTGC"+ palindrome2 +"TTGC") == palindrome2)
    


test_is_adn()
test_positions()
test_distance_h()
test_inverse()
test_plus_long_palindrome()

bioinfo.is_adn(long_adn)
    
    