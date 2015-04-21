#Autors: Reionis Prockāns
#Uzdevums 241.py
#Darba mērķis

from Tkinter import *
w=Tk()
uzr01=Label(w,bg="#28c", text='1. Datormācība, Lekc')
uzr02=Label(w,bg="#38c", text='Elektronikas Teorētiskie Pamati')
uzr03=Label(w,bg="#48c", text='Fizika')
uzr04=Label(w,bg="#58c", text='4. Datormācība, Pr.d')
uzr01.pack(side=LEFT)
uzr02.pack(side=LEFT)
uzr03.pack(side=LEFT)
uzr04.pack(side=LEFT)
w.geometry('800x600')
w.title('Stundu saraksts 18.02.2015')
w.mainloop()
