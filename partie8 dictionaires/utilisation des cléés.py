
#question 6

def get_country(l,name):
    for i in range(len(l)):
        if l[i]["City"] == name:
            return l[i].get("Country",False)