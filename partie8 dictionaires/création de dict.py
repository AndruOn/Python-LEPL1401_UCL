#Questuion 3
l = [(7.0,10.0), (2.0, 5.0), (8.0, 12.0), (10.0, 40.0), (8.0, 50.0), (8.0, 50.0)]

def create_dict(l):
    d= {}
    for x,y in l:
        if x not in d:
            d[x] = [y]
        else:
            d[x].append(y)
    return d      

    

def create_dict_max(l):
    d = create_dict(l)
    for x in d:
        d[x] = max(d[x])
    return d

print(create_dict(l))