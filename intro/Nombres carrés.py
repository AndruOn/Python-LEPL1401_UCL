#Nombres carrés et leurs sommes

a = 1
c = a*a
d = a


while a <= 10:
    print(a,"\t",a*a,"\t",c,"\t",((a+1)*(a+1-1)*(2*(a+1)-1))//6)
    a = a + 1
    c = c + a * a