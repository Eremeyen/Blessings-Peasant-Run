from PIL import Image
import os
from os import listdir
from random import random
import csv

#attribute folders:
backgrounds = r"Backgrounds"
tail = r"Tail"
bodies = r"Bodies"
eyes = r"Eye"
accessories = r"accessories"
hair = r"Hair"
horn = r"Horn"
sunglasses = r"sunglasses"

#final images destination
finalImages = r"Blessings"

#dictionaries
background_names = {
    "PEASANT COLOUR BACKGROUND 1.png":"Maximum Blue Purple",
    "PEASANT COLOUR BACKGROUND 2.png":"Picton Blue",
    "PEASANT COLOUR BACKGROUND 3.png":"Warm Orange",
    "PEASANT COLOUR BACKGROUND 4.png":"Lilac",
    "PEASANT COLOUR BACKGROUND 5.png":"Hot Pink",
    "PEASANT COLOUR BACKGROUND 6.png":"Vibrant Green",
    "PEASANT COLOUR BACKGROUND 8.png":"Orange",
    "PEASANT GRADIENT BACKGROUND 1.png":"Light Pink Gradient",
    "PEASANT GRADIENT BACKGROUND 2.png":"Purple Pink Gradient",
    "PEASANT GRADIENT BACKGROUND 3.png":"Lilac Gradient",
    "PEASANT GRADIENT BACKGROUND 4.png":"Blue Pink Gradient",
    "PEASANT GRADIENT BACKGROUND 5.png":"Green Gradient",
    "PEASANT GRADIENT BACKGROUND 6.png":"Red Blue Gradient",
    "PEASANT GRADIENT BACKGROUND 9.png":"Hot Pink Gradient",
    "PEASANT GRADIENT BACKGROUND 10.png":"Orange Gradient"
}
tail_names = {
    "PEASANT TAIL 1.png":"White tail",
    "PEASANT TAIL 2.png":"Blue tail",
    "PEASANT TAIL 5.png":"Pink tail",
    "PEASANT TAIL 6.png":"Brown tail",
    "PEASANT TAIL 3.png":"Purple curly tail",
    "PEASANT TAIL 4.png":"Blue curly tail"
}
body_names = {
    "PEASANT BODY 1.png":"Grace",
    "PEASANT BODY 3.png":"Fluffy Grace",
    "PEASANT BODY 8.png":"Mocha",
    "PEASANT BODY 6.png":"Stripes",
    "PEASANT BODY 4.png":"Purple Mint"
}
eye_names = {
    "PEASANT EYE 1.png":"Female blue eyes",
    "PEASANT EYE 2.png":"Female green eyes",
    "PEASANT EYE 3.png":"Female purple eyes",
    "PEASANT EYE 4.png":"Female aquamarine eyes",
    "PEASANT EYE M1.png":"Male blue eyes",
    "PEASANT EYE M2.png":"Male green eyes",
    "PEASANT EYE M3.png":"Male purple eyes",
    "PEASANT EYE M4.png":"Male aquamarine eyes"
}
accessory_names = {
    "220329-0959-BOS LAYER.png":"none",
    "PEASANT ACC 1.png":"Green pendant",
    "PEASANT ACC 6.png":"Red pendant",
    "PEASANT ACC 7.png":"Purple pendant",
    "PEASANT ACC 2.png":"Green tassel",
    "PEASANT ACC 4.png":"Orange tassel",
    "PEASANT ACC 8.png":"Blue tassel",
    "PEASANT ACC 9.png":"Purple bow",
    "PEASANT ACC 3.png":"Orange throw",
    "PEASANT ACC 5.png":"Black throw"
}
hair_names = {
    "PEASANT HAIR 1.png":"White hair",
    "PEASANT HAIR 2.png":"Blue hair",
    "PEASANT HAIR 5.png":"Pink hair",
    "PEASANT HAIR 6.png":"Brown hair",
    "PEASANT HAIR 3.png":"Purple curly hair",
    "PEASANT HAIR 4.png":"Blue curly hair"
}
horn_names = {
    "PEASANT HORN 2.png":"Pink spiral horn",
    "PEASANT HORN 3.png":"Purple spiral horn",
    "PEASANT HORN 4.png":"Gold spiral horn",
    "PEASANT HORN 1.png":"Blue sparkle horn",
    "PEASANT HORN 5.png":"Purple sparkle horn",
    "PEASANT HORN 6.png":"Gold sparkle horn"
}
sunglass_names = {
    "220329-0959-BOS LAYER.png":"None",
    "PEASANT SUNGLASSES 1.png":"Goggles",
    "PEASANT SUNGLASSES 2.png":"Black green gradient sunnies",
    "PEASANT SUNGLASSES 4.png":"Orange razor sunnies",
    "PEASANT SUNGLASSES 8.png":"Red razor sunnies",
    "PEASANT SUNGLASSES 9.png":"Pink razor sunnies",
    "PEASANT SUNGLASSES 10.png":"Purple razor sunnies",
    "PEASANT SUNGLASSES 3.png":"Purple large sunnies",
    "PEASANT SUNGLASSES 5.png":"Dawn large sunnies",
    "PEASANT SUNGLASSES 6.png":"Pink large sunnies",
    "PEASANT SUNGLASSES 7.png":"French tan"
}




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



Metadata = []

while(bCounter < 501):
    blessing = {}

    if(bCounter < 10):
        id = "000" + str(bCounter)
    elif(bCounter < 100):
        id = "00" + str(bCounter)
    elif(bCounter < 1000):
        id = "0" + str(bCounter)
    else:
        id = str(bCounter)
    blessing["id"] = int(id)


    whichBackground = whichBackground()
    images[0] = Image.open(backgrounds + "/" + wBackground).convert("RGBA")
    blessing["Background"] = background_names[wBackground]

    wTail = whichTail()
    images[1] = Image.open(tail + "/" + wTail).convert("RGBA")
    blessing["Tail"] = tail_names[wTail]
    
    wBody = whichBody()
    images[2] = Image.open(bodies + "/" + wBody).convert("RGBA")
    blessing["Body"] = body_names[wBody]
    
    wEye = whichEye()
    images[3] = Image.open(eyes + "/" + wEye).convert("RGBA")
    blessing["Eye"] = eye_names[wEye]

    
    #determining which hair to use
    wHair = "PEASANT HAIR " + wTail[-5] + ".png"
    images[4] = Image.open(hair + "/" + wHair).convert("RGBA") #hair
    blessing["Hair"] = hair_names[wHair]

    wHorn = whichHorn()
    images[5] = Image.open(horn + "/" + wHorn).convert("RGBA")
    blessing["Horn"] = horn_names[wHorn]
    
    wSunglass = whichSunglasses()
    images[6] = Image.open(sunglasses + "/" + wSunglass).convert("RGBA")
    blessing["Sunglasses"] = sunglass_names[wSunglass]

    wAccessory = whichAccessory()
    images[7] = Image.open(accessories + "/" + wAccessory).convert("RGBA")
    blessing["Accessory"] = accessory_names[wAccessory]

    final_image = images[0]

    #combining all layers
    for i in range(1,len(images)):
        final_image = Image.alpha_composite(final_image,images[i])
    #saving the image with the correct name and directory
    print(str(bCounter) + " images generated")
    final_image.save(finalImages+"/Blessings Peasant " +str(bCounter)+".png")
    
    if(bCounter < 10):
        id = "Peasant " + "000" + str(bCounter)
    elif(bCounter < 100):
        id = "Peasant " + "00" + str(bCounter)
    elif(bCounter < 1000):
        id = "Peasant "+ "0" + str(bCounter)
    else:
        id = str(bCounter)
    Metadata.append(blessing)


    bCounter += 1

main_info = ["id","Background","Tail","Body","Eye","Hair","Horn","Sunglasses","Accessory"]

with open("metadata.csv", "w") as csvfile:
    writer = csv.DictWriter(csvfile,fieldnames= main_info)
    writer.writeHeader()
    writer.writerows(Metadata)
    






