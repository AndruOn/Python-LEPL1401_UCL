import os
from PIL import Image

class ImageFolder:
    def __init__(self, path):
        try:
            self.__path= path
            self.__d = {}
            for fichier in os.scandir(path):
                
                if fichier.is_dir():
                    self.__d[fichier.name]= [ 0,[] ]
                    
                    for subfile in os.scandir(fichier):
                        new_l= self.__d[fichier.name][1] + [fichier.name +"/"+ subfile.name]
                        self.__d[fichier.name][1] = new_l 
        except:
            print("No such directory")

    
    def next(self, name):
        try:
            count = self.__d[name][0] + 1
            self.__d[name][0]= count
            listdename = self.__d[name][1]
            return listdename[(count-1) % len(listdename)]
        except:
            return None
    
    def tolist(self,txt):
        l=[]
        linecount=-1
        with open(txt,"r") as texte:
            for line in texte.readlines():
                linecount+=1
                l.append([])
                for num in line:
                    if num is not "\n":
                        l[linecount].append(self.next(num))
        return l
                
    def dico(self):
        return self.__d


def collage(dim,txt,path,namecollage):
    im = ImageFolder(path)
    list= im.tolist(txt)
    for line in list:
        for image in line:
            if image is not None:
                image = Image.open(path+"/"+image).copy()
                image.thumbnail(dim)
                width,height= image.size
                break

    print(list)
    blankpage= Image.new("RGB",( len(list[0])*width , len(list)*height ))
    
    heightcount= -height
    widthcount= 0
    for line in list:
        heightcount+= height
        widthcount=0
        for nom_image in line:
            if nom_image is not None:
                image_a_coller = Image.open(path+"/"+nom_image).copy()
                image_a_coller.thumbnail((width,height))
                blankpage.paste( image_a_coller , (widthcount,heightcount) )
                widthcount += width
            else:
                widthcount += width
    blankpage.show()
    


if __name__ == '__main__':
    collage((100,50),"photos/smiley.txt","photos","pute")


