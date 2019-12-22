import math

noma = 69721800
e = 0.8 + noma/(10**9) #excentricité

n = 37


print("e=",e)
def fact(k):
    if k == 0:
        return 1
    else:
        return k*fact(k-1)
        
def a(k):
    a = 1
    n = 0
    while n<k:
        a *= (1-2*n)/2
        n += 1
    return abs(a)/fact(k)


def w(k):   #k est pair!!!
    if k == 0:
        return (math.pi)/2
    else:
        return ((k-1)/k)*w(k-2)

def l(k):   # k = ordre du polynome de taylor
    def somme(k):
        s = 0
        n = 1
        while n <= k:
            s += (a(n))*(e**(2*n))*(w(2*n))
            n += 1
        return s
    l = (math.pi)/2 - somme(k)
    return l

print("l=",l(n))
        
a = 1/2   
count = 1

n1 = 2*n
for i in range(0, n):
    val = a - i
    count = count *val
value = count/math.factorial(n)
print("count=",count)
print("value=",value)
ans = 1
def calcul(n1):
    global ans
    if n1 == 0:
        ans = ans*(math.pi/2)
        return ans
    b = n1-1
    ans = ans * (b/n1)*calcul(n1-2)
    return ans
calcul(n1)
print("ans=",ans)
print("Nième terme=",abs(value)*(e**(2*n))*ans)