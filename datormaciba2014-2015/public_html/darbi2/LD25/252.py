#Fails 252.py
#Autors Reinis Prockans

import Tkinter as tk

root=tk.Tk()
root.title("Televizijas krasu tabula")
w=tk.Canvas(root, width=800, height=450, bg="#abc")
w.pack()

w.create_line(50, 450, 50, 0, fill="white", width=100)
w.create_line(150, 450, 150, 0, fill="yellow", width=100)
w.create_line(250, 450, 250, 0, fill="Cyan", width=100)
w.create_line(350, 450, 350, 0, fill="green", width=100)
w.create_line(450, 450, 450, 0, fill="#66023C", width=100)
w.create_line(550, 450, 550, 0, fill="red", width=100)
w.create_line(650, 450, 650, 0, fill="blue", width=100)
w.create_line(750, 450, 750, 0, fill="black", width=100)

root.mainloop()
