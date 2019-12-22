
Tlist= [[1,2," ",3]]

print("|" + "".join(map(str,Tlist[0])) + "|",)


list= [[1,2," ",3],[" ",4,7," "]]
Tlist= [ [0 for j in range(len(list))] for i in range(len(list[0])) ]

for i in range(len(list)):
    for j in range(len(list[0])):
        Tlist[j][i]=list[i][j] 

print(Tlist)



if 5 in 2343456:
    print("er")