from PythonMagick import Image
photo=Image("9x9", "#0404B4")
x=y=0
photo.pixelColor(2,3,'#04B404' )
photo.pixelColor(3,2,'#04B404' )
photo.pixelColor(4,1,'#04B404' )
photo.pixelColor(5,2,'#04B404' )
photo.pixelColor(6,3,'#04B404' )
photo.pixelColor(2,5,'#04B404' )
photo.pixelColor(3,4,'#04B404' )
photo.pixelColor(4,3,'#04B404' )
photo.pixelColor(5,4,'#04B404' )
photo.pixelColor(6,5,'#04B404' )
for i in range(2,7):
    photo.pixelColor(i,0,'#04B404')
for i in range(3,6):
    photo.pixelColor(i,7,'#04B404')
for i in range(2,5):
    photo.pixelColor(8,i,'#04B404')
for i in range(2,5):
    photo.pixelColor(0,i,'#04B404')
for i in range(5,7):
    photo.pixelColor(i/3,i,'#04B404')
photo.pixelColor(1,1, '#04B404')
photo.pixelColor(7,1, '#04B404')
photo.pixelColor(7,5, '#04B404')
photo.pixelColor(6,6, '#04B404')

photo.scale("200x200")
photo.write("239.png")
