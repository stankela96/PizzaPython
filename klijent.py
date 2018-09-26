from tkinter import *
from tkinter import font
import threading
import time
import socket

host = "127.0.0.1"
port = 9000
param = (host,port)
s = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
s.connect(param)
s.send("burek".encode())

root = Tk()
frm = Frame(root, width=500, height=600)
frm.grid(row = 1, column = 0)

velicina = StringVar()
vrsta = StringVar()
placanje = StringVar()
dod1 = IntVar()
dod2 = IntVar()
dod3 = IntVar()

def posalji():
    s.send("0".encode())
    sve = ""

    d1 = ""
    d2 = ""
    d3 = ""

    if dod1.get():
        d1 += "kečap"
    else:
        d1 = ""

    if dod2.get():
        d2 += "Majonez"
    else:
        d2 = ""

    if dod3.get():
        d3 += "Origano"
    else:
        d3 = ""

    box = ""
    box += str(tb1.get() + ",")
    box += str(tb2.get() + ",")
    box += str(tb3.get())

    sve += (velicina.get() + "," + vrsta.get() + "," + d1+"," + d2+"," + d3 + "," + placanje.get() + "," + box)
    s.send(sve.encode())


font = font.Font(family="Verdana", size=11)

labela1 = Label(frm,text="Veličina",bg = "crimson",font = font)
labela1.grid(row=0,column = 0,columnspan = 4)

rb1 = Radiobutton(frm,text="25 cm",value="25cm",variable = velicina)
rb1.grid(row =1,column = 0)

rb2 = Radiobutton(frm,text="32 cm",value="32cm",variable = velicina)
rb2.grid(row =1,column = 1)

rb3 = Radiobutton(frm,text="50 cm",value="50cm",variable = velicina)
rb3.grid(row =1,column = 2)

labela2 = Label(frm,text="Vrsta",bg = "lime",font = font)
labela2.grid(row=2,column = 0,columnspan = 4)

rb4 = Radiobutton(frm,text="Margarita",value="Margarita",var = vrsta)
rb4.grid(row =3,column = 0)

rb5 = Radiobutton(frm,text="Funghi",value="Funghi",var = vrsta)
rb5.grid(row =3,column = 1)

rb6 = Radiobutton(frm,text="Quatro Stagione",value="Quatro Stagione",var = vrsta)
rb6.grid(row =3,column = 2)

rb7 = Radiobutton(frm,text="Vegeteriana",value="Vegeteriana",var = vrsta)
rb7.grid(row =3,column = 3)

labela3 = Label(frm,text="Dodaci",bg = "aqua",font = font)
labela3.grid(row=4,column = 0,columnspan = 4)

cb1 = Checkbutton(frm,text="Kecap", variable=dod1,onvalue = 1,offvalue = 0,)
cb1.grid(row = 5,column = 0)

cb2 = Checkbutton(frm,text="Majonez", variable=dod2,onvalue = 1,offvalue = 0)
cb2.grid(row = 5,column = 1)

cb3 = Checkbutton(frm,text="Origano", variable=dod3 ,onvalue = 1,offvalue = 0)
cb3.grid(row = 5,column = 2)

labela4 = Label(frm,text="Način plaćanja",bg = "yellow",font = font)
labela4.grid(row=6,column = 0,columnspan = 4)

rb8 = Radiobutton(frm,text="Keš",var = placanje,value = "Kes")
rb8.grid(row =7,column = 1)

rb9 = Radiobutton(frm,text="Kartica",var = placanje,value = "Kartica")
rb9.grid(row =7,column = 2)

labela5 = Label(frm,text="Adresa:",font = font,bg="red")
labela5.grid(row=8,column = 1)
tb1 = Entry(frm)
tb1.grid(row = 8,column = 2)

labela6 = Label(frm,text="Broj telefona:",font = font,bg="pink")
labela6.grid(row=9,column = 1)
tb2 = Entry(frm)
tb2.grid(row = 9,column = 2)

labela7 = Label(frm,text="Napomena:",font = font,bg="silver")
labela7.grid(row=10,column = 1)
tb3 = Entry(frm)
tb3.grid(row = 10,column = 2)

dugme = Button(frm,text = "POŠALJI NARUDŽBINU",bg = "purple",font = font,command = posalji)
dugme.grid(row = 11,column = 0,columnspan = 6)

root.mainloop()
