#!/usr/bin/env python
# -*- coding:utf-8 -*-

import Tkinter

class App:
    def __init__(self, master):
        frame = Tkinter.Frame(master)
        frame.pack()
        self.button = Tkinter.Button(frame, text="QUIT", command=frame.quit)
        self.button.pack(side=Tkinter.LEFT)
        self.buttons = Tkinter.Button(frame, text="button", command=self.say_hi)
        self.buttons.pack(side=Tkinter.LEFT)
    def say_hi(self):
        print "hello Tkinter widget"
        
root = Tkinter.Tk()
app = App(root)
root.mainloop()
root.destroy()
