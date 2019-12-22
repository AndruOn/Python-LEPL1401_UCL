#Question 2

def equal(l,d):
    newd={}
    for i in range(len(l)):
        for j in range(len(l[i])):
            if l[i][j] != 0:
                newd [(i,j)] = l[i][j]            
    for i in newd:
        if i not in d:
            return False
        else:
            if newd[i] != d[i]:
                return False
    return True
    
    
l = [[0, 2, 4], [4, 1, 0]]
d = {(0,1): 2, (0,2): 4, (1,0): 4, (1,1): 1}
print(equal(l,d))