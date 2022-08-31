import os
from PIL import Image 

def compres(file_p):
    picsize=os.stat(file_p).st_size
    picture = Image.open(file_p)
    w=picture.size[0]
    h=picture.size[1]


    if w>5000 or h>5000:
        w=int(w/4)
        h=int(h/4)
        newpic=picture.resize((w,h))



    elif w> 3000 or h>3000:
        w=int(w/3)
        h=int(h/3)
        newpic=picture.resize((w,h))

    elif w> 2000 or h>2000:
        w=int(w/2)
        h=int(h/2)
        newpic=picture.resize((w,h))

    elif w<1500 or h<1500:
        if w>1000 : w=int(w/1.5)
        if h> 1000 :h=int(h/1.5)
        newpic=picture.resize((w,h))

    if picsize <= 1000:
        picture.save("final"+file_p,optimize=True,quality=95)
    elif picsize <= 2000:
        picture.save("final"+file_p,optimize=True,quality=90)
    elif picsize <= 3000:
        picture.save("final"+file_p,optimize=True,quality=80)
    elif picsize <= 4000:
        newpic.save("final"+file_p,optimize=True,quality=80)
    elif picsize <= 5000:
        newpic.save("final"+file_p,optimize=True,quality=70)
    elif picsize <= 6000 :
        newpic.save("final"+file_p,optimize=True,quality=70)
    else:
        newpic.save("final_"+file_p,optimize=True,quality=70)
    
compres("7mb.jpg")