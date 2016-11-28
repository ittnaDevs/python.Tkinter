from Tkinter import *
import tkFileDialog
from PIL import Image, ImageDraw
# from tkinter import ttk
from shutil import copyfile
import os


def openFile(event):
    root.filename = tkFileDialog.askopenfilename(initialdir = "/",title = "Select file",filetypes = (("jpeg files","*.jpg"),("png files","*.png")))
    root.title = root.filename
    print root.filename
    tmp = root.filename.split('/')
    fname = root.filename.split('/')[-1]
    fname = fname.split('.')
    s = ""
    a = 0
    while a < len(fname)-1:
        s += fname[a] + '.'
        a += 1
    s += 'copy.'+fname[-1]
    tmp[-1]=s
    img_file = '/'.join(tmp)
    print s, img_file
    copyfile(root.filename, img_file)

    img = Image.open(img_file)
    pix = img.load()
    # width, height = img.size
    canvas.create_image((0,0), image=img)


def colorRGBA(event):
    s1 = str(colorEntry1.get())
    s2 = str(colorEntry2.get())
    flasher.delete(0,"end")
    flasher.insert(0,"{} - {}".format(s1,s2))

root = Tk()
# frame = Frame(root)
colorEntry1 = Entry(root)
colorEntry1.pack(side=LEFT)
colorEntry2 = Entry(root)
colorEntry2.pack(side=LEFT)

flasher = Entry(root)
flasher.pack(side=LEFT)

fileButton =  Button(root, text="Image File")
fileButton.bind("<Button-1>",openFile)
fileButton.pack()
colorButton = Button(root, text="submit RGBA values")
colorButton.bind("<Button-1>",colorRGBA)
colorButton.pack(side=LEFT)

canvas = Canvas(root, width=400, height=400)
canvas.pack()


root.mainloop()
# root.destroy()
