from PythonMagick import Image
bilde = Image("16x16", "#00FF33")
x=y=0
for a in range(0,7):
    bilde.pixelColor(a,8,"#FFFF66")
for a in range(9,16):
    bilde.pixelColor(a,8,"#FFFF66")
for a in range(6,11):
    bilde.pixelColor(9,a,"#000066")
for a in range(6,11):
    bilde.pixelColor(7,a,"#000066")
bilde.scale("200x200")
bilde.write("237.png")
