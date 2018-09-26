from tkinter import *
from tkinter import font
import socket
import threading
import time
import random

host = "127.0.0.1"
port = 9000
param = (host,port)
s = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
s.bind(param)
s.listen(1)

def pokreniServer():
    kon, adr = s.accept()
    prima = (kon.recv(1024)).decode()
    print(prima)

    while True:
        zahtev = (kon.recv(1024)).decode()
        zahtev = int(zahtev)

        if zahtev == 0:
                prihvati = (kon.recv(1024)).decode()
                vreme = random.randint(5, 10)
                while vreme > 0:
                    lb1.insert(0, prihvati + "," + str(vreme))
                    vreme = vreme - 1
                    time.sleep(1)
                    lb1.delete(0)

                    if vreme == 0:
                        lb2.insert(0, prihvati)

serverNit = threading.Thread(target=pokreniServer)
serverNit.start()

root = Tk()
frm = Frame(root, width=500, height=600)
frm.grid(row = 1, column = 0)

font = font.Font(family="Verdana", size=15)
label1 = Label(frm,text="NEISPORUČENO ",bg="crimson",font = font)
label1.grid(row = 2,column = 0)

label2 = Label(frm,text="ISPORUČENO ",bg="lime",font = font)
label2.grid(row = 2,column = 1)

lb1 = Listbox(frm,height = 20,width=60)
lb1.grid(row =3,column=0)

lb2 = Listbox(frm,height = 20,width=60)
lb2.grid(row =3,column=1)

root.mainloop()