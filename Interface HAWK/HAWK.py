import Tkinter as tk
from PIL import Image, ImageTk
from itertools import count
from Tkinter import*
import Tkinter
from PIL import Image
import glob, os


class ImageLabel(tk.Label):
    
    def load(self, im):
        if isinstance(im, str):
            im = Image.open(im)
        self.loc = 0
        self.frames = []

        try:
            for i in count(1):
                self.frames.append(ImageTk.PhotoImage(im.copy()))
                im.seek(i)
        except EOFError:
            pass

        try:
            self.delay = im.info['duration']
        except:
            self.delay = 100

        if len(self.frames) == 1:
            self.config(image=self.frames[0])
        else:
            self.next_frame()

    def unload(self):
        self.config(image=None)
        self.frames = None

    def next_frame(self):
        if self.frames:
            self.loc += 1
            self.loc %= len(self.frames)
            self.config(image=self.frames[self.loc])
            self.after(self.delay, self.next_frame)


root = tk.Tk()
root.title("HAWK")
root.iconbitmap('ico.ico')
root["background"] = "#00030b"
#LxA+E+T
#300x300+100+100
root.geometry("500x500+500+100")


lb1 = Label(root, text="BEM VINDO AO HAWK!", font = "Helvetica 18 bold", bg="#F5F5F5")
lb2 = ImageLabel(root,bg="#00030b")
lb2.load('jarvis.gif')
lb3 = tk.Label(root, text="AGUARDANDO COMANDO DE VOZ...",font = "Helvetica 18 bold", bg="#F5F5F5")


lb1.pack(side=TOP, fill=BOTH, expand=1)
lb2.pack()
lb3.pack(side=TOP, fill=BOTH, expand=1)




root.mainloop()
