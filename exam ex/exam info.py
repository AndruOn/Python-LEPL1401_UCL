

def addsort(l1,l2):
    
    list=[]
    a = 0
    b = 0
    while a < len(l1) :
        
        if l1[a] < l2[b] :
            list.append(l1[a])
            a += 1
            print("<")
            
        elif l1[a] > l2[b] :
            list.append(l2[b])
            b += 1
            print(">")
            
        elif l1[a] == l2[b] :
            list.append(l1[a])
            list.append(l2[b])
            a += 1
            b += 1
            print("==")
        print("a=",a)
        print("b=",b)
        
    a -= 1
    
    while b < len(l2) :
        
        if l1[a] < l2[b] :
                list.append(l2[b])
                b += 1
                print("<")
            
        elif l1[a] > l2[b] :
            b += 1
            print(">")
            
        elif l1[a] == l2[b] :
            list.append(l1[a])
            list.append(l2[b])
            b += 1
            print("==")
            
        print("a=",a)
        print("b=",b)
        

    print(list)
    
    
    
    

l1=[1,2,3,5,6]
l2=[3,7,8,8,9]


addsort(l1,l2)


