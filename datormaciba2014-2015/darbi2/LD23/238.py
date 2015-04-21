from PythonMagick import Image
photo=Image("9x9", "#E65C00")
x=y=0
for i in range(1,7):
    photo.pixelColor(4,i,'#0404B4')
for i in range(3,6):
    photo.pixelColor(i,2,'#0404B4')
for i in range(2,7):
    photo.pixelColor(i,3,'#0404B4')
for i in range(2,7):
    photo.pixelColor(i,0,'#0404B4')
for i in range(3,6):
    photo.pixelColor(i,7,'#0404B4')
for i in range(2,5):
    photo.pixelColor(8,i,'#0404B4')
for i in range(2,5):
    photo.pixelColor(0,i,'#0404B4')
for i in range(5,7):
    photo.pixelColor(i/3,i,'#0404B4')
photo.pixelColor(1,1, '#0404B4')
photo.pixelColor(7,1, '#0404B4')
photo.pixelColor(7,5, '#0404B4')
photo.pixelColor(6,6, '#0404B4')

photo.scale("200x200")
photo.write("238.png")
