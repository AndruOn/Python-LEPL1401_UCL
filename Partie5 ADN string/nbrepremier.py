

def prime(max):
    l=[]
    for i in range(2,max+1):
        sum = 0
        for c in l:
            if i % c == 0:
                break
            else:
                sum += 1
        if sum == len(l):
            l.append(i)
                
    return(l)
    
    

            
