# import the module
import tkinter
import webbrowser

from tkinter import *

win = Tk()
win.title('Smart Student')
win.configure(background="#2E86C1")

# create geometry
win.geometry("375x559")

# Heading
l = Label(win, text="Section O-9", pady="30", bg="#2E86C1", fg="#09FF00", font="Verdana 24 bold")
l.pack()

# Class Routine
def open_window():
    novi = Toplevel()
    novi.title('Class Routine')
    canvas = Canvas(novi, width=1050, height=380)
    canvas.pack(expand=YES, fill=BOTH)
    filename = PhotoImage(file='Capture.PNG')
    canvas.create_image(50, 10, image=filename, anchor=NW)
    # assigned the gif1 to the canvas object
    canvas.filename = filename


b1 = Button(win, text='Routine', width="20", activebackground="#09FF00", command=open_window)
b1.pack()
l1 = Label(win, bg="#2E86C1", pady="5")
l1.pack()

# Student Portal
new = 1
url1 = "http://studentportal.diu.edu.bd/#/login"


def student_portal():
    webbrowser.open(url1, new=new)


b2 = Button(win, text='Student Portal', width="20", activebackground="#09FF00", command=student_portal)
b2.pack()
l2 = Label(win, bg="#2E86C1", pady="5")
l2.pack()

# Notice Board
new = 1
url2 = "https://daffodilvarsity.edu.bd/department/cse"


def notice_board():
    webbrowser.open(url2, new=new)


b3 = Button(win, text='Notice Board', width="20", activebackground="#09FF00", command=notice_board)
b3.pack()
l3 = Label(win, bg="#2E86C1", pady="5")
l3.pack()


# Teacher Information
def Teacher():
    novi = Toplevel()
    novi.title('Teachers Information')
    canvas = Canvas(novi, width=1150, height=200)
    canvas.pack(expand=YES, fill=BOTH)
    filename = PhotoImage(file='Tinfo.PNG')
    canvas.create_image(50, 10, image=filename, anchor=NW)
    # assigned the gif1 to the canvas object
    canvas.filename = filename


b4 = Button(win, text='Teacher Info', width="20", activebackground="#09FF00", command=Teacher)
b4.pack()
l4 = Label(win, bg="#2E86C1", pady="5")
l4.pack()

# Student Information
new = 1
url5 = "https://docs.google.com/spreadsheets/d/13oUnqHcS1h1yciUTYbnDJscU16Dtz52vq5_cSpW0iIs/edit?usp=sharing"


def student_information():
    webbrowser.open(url5, new=new)


b5 = Button(win, text='Student Info', width="20", activebackground="#09FF00", command=student_information)
b5.pack()
l5 = Label(win, bg="#2E86C1", pady="5")
l5.pack()

# DIU Blended Learning Center
new = 1
url6 = "https://elearn.daffodilvarsity.edu.bd/"


def blc():
    webbrowser.open(url6, new=new)


b6 = Button(win, text='DIU BLC', width="20", activebackground="#09FF00", command=blc)
b6.pack()
l6 = Label(win, bg="#2E86C1", pady="5")
l6.pack()

# Section group
new = 1
url7 = "https://www.facebook.com/groups/1762603323856591/"


def section_group():
    webbrowser.open(url7, new=new)


b7 = Button(win, text='Section Group', width="20", activebackground="#09FF00", command=section_group)
b7.pack()
l7 = Label(win, bg="#2E86C1", pady="5")
l7.pack()

# Question bank

new = 1
url8 = "https://drive.google.com/drive/folders/1wOkEWsxkbmbarz_EkCvbxY-dwtZvRMuD?usp=sharing"


def qbank():
    webbrowser.open(url8, new=new)


b8 = Button(win, text='Question Bank', width="20", activebackground="#09FF00", command=qbank)
b8.pack()
l8 = Label(win, bg="#2E86C1", pady="5")
l8.pack()

win.mainloop()