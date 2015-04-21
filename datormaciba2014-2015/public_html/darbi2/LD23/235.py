from PythonMagick import Image
bilde = Image("16x16", "#FFFF00")
x=y=0
for a in range(0,5):
    bilde.pixelColor(8,a,"#FFFF00")
for a in range(11,16):
    bilde.pixelColor(8,a,"#FFFF00")
for a in range(6,10):
    bilde.pixelColor(a,5,"#00FFFF")
for a in range(6,10):
    bilde.pixelColor(a,11,"#00FFFF")
for a in range(5,12):
    bilde.pixelColor(6,a,"#00FFFF")
for a in range(5,12):
    bilde.pixelColor(10,a,"#00FFFF")
bilde.scale("200x200")
bilde.write("235.png")
