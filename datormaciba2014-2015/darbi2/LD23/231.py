#Fails 231.py
#Autors Reinis Prockans

from PythonMagick import Image

#Izgatavojam jaunu objektu - bilde
#Objekta izmers 3x3 pixels
bilde = Image("3x3", "#22aaff")

#Izgatavojam mainigos x un y
x=y=0

#Uzstada objekta 'bilde' x,y pixela krasu
bilde.pixelColor (x, y, "#eeff22")

#3x3 pixels palielina lidz 200x200
bilde.scale("200x200")

#Objektu 'bilde' ieraksta faila
bilde.write("231.png")
