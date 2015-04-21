from PythonMagick import Image
bilde= Image("8x8","#33FFCC")
x=y=0
for i in range(0,4):
    bilde.pixelColor(i,1, "#993300")
for i in range(0,4):
    bilde.pixelColor(i,7, "#993300")
for i in range (2,4):
    bilde.pixelColor(i,3,"#993300")
for i in range (2,4):
    bilde.pixelColor(i,5,"#993300")
bilde.pixelColor(4,2, "#993300")
bilde.pixelColor(4,4, "#993300")
bilde.pixelColor(4,6, "#993300")
bilde.scale("200x200")
bilde.write("236.png")
