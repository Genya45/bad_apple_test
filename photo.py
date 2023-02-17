import numpy as np
from PIL import Image    #  pip install Pillow

img = np.asarray(Image.open('frame1.jpg').convert('RGB').resize((73, 45)))

#print(img)
#print((' '))



def getLine(line):
    lineStr = ''
    for pixel in line:
        if pixel.sum() < 100:
            lineStr += 'o'
        else:
            lineStr += ' '
    
    return lineStr

for line in img:
    print(getLine(line))