



if(a > b and b > c) or (c >b and b>a):
    median = b
    
if (b>a and a>c) or (c>a and a>b):
    median = a
    
if (a>c and c>b) or (b>c and c>a):
    median = c
    
print(median)
    
    