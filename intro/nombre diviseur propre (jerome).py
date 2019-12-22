n=25
for i in range (1, n+1) :
    d=1
    s=0
    while d<i :
        if i%d == 0 :
            s=s+1
        d=d+1
    print (i,' /t',s)