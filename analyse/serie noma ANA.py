a= int(input("a="))
n=1
sum=1

while n < a:
    if "6" in str(n):
        n+=1
    
    elif n%10000000==0:
        sum += 1/n
        print(sum)
        n+=1
        
    else :
        sum += 1/n
        n+=1
        

    