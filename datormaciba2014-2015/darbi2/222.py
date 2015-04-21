# -*- coding: utf-8 -*-
#Fails : 222.py
# Autors : Reinis Prockāns
#Apliecibas numurs : 141REB155
# Datums : 2015.02.11.
#Aprēķina ķēdes ar 2 virknē saslēgtiem rezistoriem izejas spriegumu un strāvu

Us = 15.5
R2 = 50
solis = input("Ievadiet soli: ")
diap0 = input("Ievadiet diapazona sākuma vērtību: ")
diap1 = input("Ievadiet diapazona beigu vērtību: ")
f=open('222.html',"w")
f.write("<html><pre>R1\tizeja.U\t   V1.I\n")
for x in range(diap0, diap1+1, solis):
    I1 = Us/(R2+x)
    Ur = Us-I1*x
    f.write("%d\t%5.2f\t   %.3f\n" % (x,Ur,I1))
f.write("</pre></html>")
