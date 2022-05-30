from PIL import Image
import os
from os import listdir
from random import random

#attribute folders:
backgrounds = r"C:\Users\meren\OneDrive\Masaüstü\Blessings Peasant Run\Backgrounds"
tail = r"C:\Users\meren\OneDrive\Masaüstü\Blessings Peasant Run\Tail"
bodies = r"C:\Users\meren\OneDrive\Masaüstü\Blessings Peasant Run\Bodies"
eyes = r"C:\Users\meren\OneDrive\Masaüstü\Blessings Peasant Run\Eye"
accessories = r"C:\Users\meren\OneDrive\Masaüstü\Blessings Peasant Run\accessories"
hair = r"C:\Users\meren\OneDrive\Masaüstü\Blessings Peasant Run\Hair"
horn = r"C:\Users\meren\OneDrive\Masaüstü\Blessings Peasant Run\Horn"
sunglasses = r"C:\Users\meren\OneDrive\Masaüstü\Blessings Peasant Run\sunglasses"

#final images destination
finalImages = r"C:\Users\meren\OneDrive\Masaüstü\Blessings Peasant Run\Blessings"

#defining an empty images array which we'll use to come up with each final image
images = []
for i in range(len(os.listdir(r"C:\Users\meren\OneDrive\Masaüstü\Blessings Peasant Run"))-2):
    images.append("")




bCounter = 1

def whichBackground():
    n = random()
    if(n < 0.1):
        return "PEASANT COLOUR BACKGROUND 1.png"
    elif(n < 0.2):
        return "PEASANT COLOUR BACKGROUND 2.png"
    elif(n < 0.3):
        return "PEASANT COLOUR BACKGROUND 3.png"
    elif(n < 0.5):
        return "PEASANT COLOUR BACKGROUND 4.png"
    elif(n < 0.6):
        return "PEASANT COLOUR BACKGROUND 5.png"
    elif(n < 0.7):
        return "PEASANT COLOUR BACKGROUND 6.png"
    elif(n < 0.8):
        return "PEASANT COLOUR BACKGROUND 8.png"
    elif(n < 0.825):
        return "PEASANT GRADIENT BACKGROUND 1.png"
    elif(n < 0.85):
        return "PEASANT GRADIENT BACKGROUND 2.png"
    elif(n < 0.875):
        return "PEASANT GRADIENT BACKGROUND 3.png"
    elif(n < 0.9):
        return "PEASANT GRADIENT BACKGROUND 4.png"
    elif(n < 0.925):
        return "PEASANT GRADIENT BACKGROUND 5.png"
    elif(n < 0.95):
        return "PEASANT GRADIENT BACKGROUND 6.png"
    elif(n < 0.975):
        return "PEASANT GRADIENT BACKGROUND 9.png"
    else:
        return "PEASANT GRADIENT BACKGROUND 10.png"

    
def whichTail():
    n = random()
    if(n < 0.2):
        return "PEASANT TAIL 1.png"
    elif(n < 0.4):
        return "PEASANT TAIL 2.png"
    elif(n < 0.6):
        return "PEASANT TAIL 5.png"
    elif(n < 0.8):
        return "PEASANT TAIL 6.png"
    elif(n < 0.9):
        return "PEASANT TAIL 3.png"
    else:
        return "PEASANT TAIL 4.png"

def whichBody():
    n = random()
    if(n < 0.225):
        return "PEASANT BODY 1.png"
    elif(n < 0.45):
        return "PEASANT BODY 3.png"
    elif(n < 0.675):
        return "PEASANT BODY 8.png"
    elif(n < 0.875):
        return "PEASANT BODY 6.png"
    else:
        return "PEASANT BODY 4.png"

def whichEye():
    n = random()
    if(n < 0.075):
        return "PEASANT EYE 1.png"
    elif(n < 0.15):
        return "PEASANT EYE 2.png"
    elif(n < 0.225):
        return "PEASANT EYE 3.png"
    elif(n < 0.3):
        return "PEASANT EYE 4.png"
    elif(n < 0.475):
        return "PEASANT EYE M1.png"
    elif(n < 0.650):
        return "PEASANT EYE M2.png"
    elif(n < 0.825):
        return "PEASANT EYE M3.png"
    else:
        return "PEASANT EYE M4.png"


def whichHorn():
    n = random()
    if(n < 0.24):
        return "PEASANT HORN 2.png"
    elif(n < 0.47):
        return "PEASANT HORN 3.png"
    elif(n < 0.7):
        return "PEASANT HORN 4.png"
    elif(n < 0.8):
        return "PEASANT HORN 1.png"
    elif (n < 0.9):
        return "PEASANT HORN 5.png"
    else:
        return "PEASANT HORN 6.png"

def whichSunglasses():
    n = random()
    if(n < 0.1):
        return "PEASANT SUNGLASSES 1.png"
    elif(n < 0.14):
        return "PEASANT SUNGLASSES 2.png"
    elif(n < 0.18):
        return "PEASANT SUNGLASSES 4.png"
    elif(n < 0.22):
        return "PEASANT SUNGLASSES 8.png"
    elif(n < 0.26):
        return "PEASANT SUNGLASSES 9.png"
    elif(n < 0.3):
        return "PEASANT SUNGLASSES 10.png"
    elif(n < 0.325):
        return "PEASANT SUNGLASSES 3.png"
    elif(n < 0.35):
        return "PEASANT SUNGLASSES 5.png"
    elif(n < 0.375):
        return "PEASANT SUNGLASSES 6.png"
    elif(n < 0.4):
        return "PEASANT SUNGLASSES 7.png"
    else:
        return "220329-0959-BOS LAYER.png"


def whichAccessory():
    n = random()
    if(n < 0.07):
        return "PEASANT ACC 1.png"
    elif(n < 0.14):
        return "PEASANT ACC 6.png"
    elif(n < 0.21):
        return "PEASANT ACC 7.png"
    elif(n < 0.245):
        return "PEASANT ACC 2.png"
    elif(n < 0.28):
        return "PEASANT ACC 4.png"
    elif(n < 0.315):
        return "PEASANT ACC 8.png"
    elif(n < 0.35):
        return "PEASANT ACC 9.png"
    elif(n < 0.375):
        return "PEASANT ACC 3.png"
    elif(n < 0.4):
        return "PEASANT ACC 5.png"
    else:
        return "220329-0959-BOS LAYER.png"




while(bCounter < 501):
    images[0] = Image.open(backgrounds + "/" + whichBackground()).convert("RGBA")
    wTail = whichTail()
    images[1] = Image.open(tail + "/" + wTail).convert("RGBA")
    images[2] = Image.open(bodies + "/" + whichBody()).convert("RGBA")
    images[3] = Image.open(eyes + "/" + whichEye()).convert("RGBA")
    
    #determining which hair to use
    wHair = "PEASANT HAIR " + wTail[-5] + ".png"
    images[4] = Image.open(hair + "/" + wHair).convert("RGBA") #hair
    images[5] = Image.open(horn + "/" + whichHorn()).convert("RGBA")
    images[6] = Image.open(sunglasses + "/" + whichSunglasses()).convert("RGBA")
    images[7] = Image.open(accessories + "/" + whichAccessory()).convert("RGBA")
    final_image = images[0]

    #combining all layers
    for i in range(1,len(images)):
        final_image = Image.alpha_composite(final_image,images[i])
    #saving the image with the correct name and directory
    print(str(bCounter) + " images generated")
    final_image.save(finalImages+"/Blessings Peasant " +str(bCounter)+".png")
    bCounter += 1

    






