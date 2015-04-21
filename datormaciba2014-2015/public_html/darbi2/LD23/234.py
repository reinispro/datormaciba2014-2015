from PythonMagick import Image
bilde = Image("16x16", "#00FFFF")
x=y=0
for a in range(0,5):
    bilde.pixelColor(a,8,"#FFFF00")
for a in range(11,16):
    bilde.pixelColor(a,8,"#FFFF00")
for a in range(6,11):
    bilde.pixelColor(5,a,"#FF0000")
for a in range(6,11):
    bilde.pixelColor(11,a,"#FF0000")
for a in range(5,12):
    bilde.pixelColor(a,6,"#FF0000")
for a in range(5,12):
    bilde.pixelColor(a,11,"#FF0000")
bilde.scale("200x200")
bilde.write("234.png")
