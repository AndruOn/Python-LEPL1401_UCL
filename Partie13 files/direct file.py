import os
from PIL import Image 

"""
direct,file,subfile
"""


def files(path):
    l=[]
    with os.scandir(path) as n:
        for i in n :
            if not i.name.startswith('.') and i.is_file():
                l.apend(i.name)
        return l
    
def directories(path):
    lst=[]
    for sub in os.scandir(path):
        if sub.is_dir():
            lst.append(sub.name)
            lst.append(sousfichier)
            
    return lst
        
def subfiles(dir):
    list=[]
    for file in os.scandir(dir):
        if file.is_dir():
            for subfil in os.scandir(file):
                if not subfil.name.startswith('.') and subfil.is_file():
                    list.append(subfil.name)
    return list



"""
Pillow
"""


def deform_image(file,width,length):
    im = Image.open(file)
    size= (width,length)
    im.thumbnail(size)
    im.save(file)
    
def double_im(file):
    im= Image.open(file)
    width, heigth= im.size
    newim= Image.new("RGB",(2*width,heigth))
    newim.paste(im,(0,0))
    newim.paste(im,(width,0))
    newim.save(file)


"""
Counters
"""
class Counters:
    def __init__ ( self, number ):
        pass

    def next(self, number):
        pass



deform_image("1_200px-Smiley.svg.png",200,100)