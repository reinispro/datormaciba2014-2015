#Fails 231.py
#Autors Reinis Prockans

from PythonMagick import Image

#Izgatavojam jaunu objektu - bilde
#Objekta izmers 3x3 pixels
bilde = Image("32x32", "#22aaff")

#Izgatavojam mainigos x un y
x=y=0

#Uzstada objekta 'bilde' x,y pixela krasu
bilde.pixelColor (1, 13, "#eeff22")
bilde.pixelColor (1, 14, "#eeff22")
bilde.pixelColor (1, 15, "#eeff22")
bilde.pixelColor (1, 16, "#eeff22")
bilde.pixelColor (1, 17, "#eeff22")
bilde.pixelColor (1, 18, "#eeff22")
bilde.pixelColor (1, 19, "#eeff22")
bilde.pixelColor (1, 20, "#eeff22")
bilde.pixelColor (2, 13, "#eeff22")
bilde.pixelColor (3, 13, "#eeff22")
bilde.pixelColor (4, 13, "#eeff22")
bilde.pixelColor (5, 13, "#eeff22")
bilde.pixelColor (5, 14, "#eeff22")
bilde.pixelColor (5, 15, "#eeff22")
bilde.pixelColor (5, 16, "#eeff22")
bilde.pixelColor (4, 16, "#eeff22")
bilde.pixelColor (3, 16, "#eeff22")
bilde.pixelColor (2, 16, "#eeff22")
bilde.pixelColor (2, 17, "#eeff22")
bilde.pixelColor (3, 18, "#eeff22")
bilde.pixelColor (4, 19, "#eeff22")
bilde.pixelColor (5, 20, "#eeff22")


#3x3 pixels palielina lidz 200x200
bilde.scale("200x200")

#Objektu 'bilde' ieraksta faila
bilde.write("232.png")
