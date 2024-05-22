import socket
import os
import tkinter
from tkinter import *
from PIL import Image, ImageTk

def clear():
    os.system("clear")
def start():
    target = t1.get(1.0,"end-1c")
    ip_address = socket.gethostbyname(target)

    global l2
    global l3
    global l4
    l2 = Label(program, text=f"Target IP: {ip_address}")
    l3 = Label(program, text=f"Target: {target}")

    l2.pack()
    l3.pack()

    t1.delete("1.0","end")

def print():
    f = open("targets.txt","a")
    target = t1.get(1.0, "end-1c")
    ip_address = socket.gethostbyname(target)
    f.write(f"Target IP: {ip_address}\n")
    f.write(f"Target: {target}\n")
    f.write("\n")
    f.close()
    t1.delete("1.0","end")

program = tkinter.Tk()
program.geometry('380x350')
program.title("IP Information Gathering")

img = Image.open("pictures/network_logo.png")
resize_img = img.resize((165,140))
img2 = ImageTk.PhotoImage(resize_img)
img_lbl = Label(image=img2)
img_lbl.image = img2
img_lbl.pack()

l1 = Label(program, text="IP Information Gathering")
l1.pack()
l4 = Label(program, text="Programming by cpu-astatine")
l4.pack()

t1 = Text(program, width=35, height=1)
t1.pack()

b1 = Button(program, text="Start", command=start)
b1.pack()
b2 = Button(program, text="Printing Targets", command=print)
b2.pack()
b3 = Button(program, text="Quit", command=program.destroy)
b3.pack()

program.mainloop()
