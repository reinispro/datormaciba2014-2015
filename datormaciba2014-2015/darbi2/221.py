# -*- coding: utf-8 -*-
# Fails : 221.py
# Autors : Reinis Prockāns
# Apliecibas numurs : 141REB155
# Datums : 2015.02.11.
# Aprēķina ķēdes ar 2 virknē saslēgtiem rezistoriem izejas spriegumu un strāvu

Us = 15.5
R2 = 50
solis = input("Ievadiet soli: ")
diap0 = input("Ievadiet diapazona sākuma vērtību: ")
diap1 = input("Ievadiet diapazona beigu vērtību: ")
for x in range(diap0, diap1+1, solis):
    I1 = Us/(R2+x)
    Ur = Us-I1*x
    print "R1 = %d\t\t izeja.V = %5.2f\t V1.I = %.3f" % (x,Ur,I1)
