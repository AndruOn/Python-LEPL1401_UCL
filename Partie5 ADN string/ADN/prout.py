s = "pute"
print(s[::-1])



def inverse(s):
    """ pré: s est un string ou une liste
        post: fonction rend le string ou la liste lu de droite à gauche"""
    return s[::-1]

def palindrome(s):
    for c in inverse(range(len(s))):
        for i in range(len(s)):
            if s[i:i+c] == inverse(s[i+c-1:i+2*c-1]):
                return s[i:i+c]
                

print(palindrome("putetupkayakayak"))
l=[]
help(l.append("3"))