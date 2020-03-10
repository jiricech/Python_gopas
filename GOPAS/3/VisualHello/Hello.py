#! /usr/bin/env python
#  -*- coding: utf-8 -*-
#
# GUI module generated by PAGE version 4.21
#  in conjunction with Tcl version 8.6
#    Mar 28, 2019 01:33:05 PM CET  platform: Windows NT

import sys

try:
    import Tkinter as tk
except ImportError:
    import tkinter as tk

try:
    import ttk
    py3 = False
except ImportError:
    import tkinter.ttk as ttk
    py3 = True

import Hello_support

def vp_start_gui():
    '''Starting point when module is the main routine.'''
    global val, w, root
    root = tk.Tk()
    Hello_support.set_Tk_var()
    top = Toplevel1 (root)
    Hello_support.init(root, top)
    root.mainloop()

w = None
def create_Toplevel1(root, *args, **kwargs):
    '''Starting point when module is imported by another program.'''
    global w, w_win, rt
    rt = root
    w = tk.Toplevel (root)
    Hello_support.set_Tk_var()
    top = Toplevel1 (w)
    Hello_support.init(w, top, *args, **kwargs)
    return (w, top)

def destroy_Toplevel1():
    global w
    w.destroy()
    w = None

class Toplevel1:
    def __init__(self, top=None):
        '''This class configures and populates the toplevel window.
           top is the toplevel containing window.'''
        _bgcolor = '#d9d9d9'  # X11 color: 'gray85'
        _fgcolor = '#000000'  # X11 color: 'black'
        _compcolor = '#d9d9d9' # X11 color: 'gray85'
        _ana1color = '#d9d9d9' # X11 color: 'gray85'
        _ana2color = '#ececec' # Closest X11 color: 'gray92'

        top.geometry("286x94+397+141")
        top.title("Visual Hello")
        top.configure(background="#d9d9d9")

        self.txtHlaska = tk.Entry(top)
        self.txtHlaska.place(relx=0.07, rely=0.213,height=20, relwidth=0.573)
        self.txtHlaska.configure(background="white")
        self.txtHlaska.configure(disabledforeground="#a3a3a3")
        self.txtHlaska.configure(font="TkFixedFont")
        self.txtHlaska.configure(foreground="#000000")
        self.txtHlaska.configure(insertbackground="black")
        self.txtHlaska.configure(textvariable=Hello_support.txtHlaskaVar)

        self.txtCopy = tk.Entry(top)
        self.txtCopy.place(relx=0.07, rely=0.532,height=20, relwidth=0.573)
        self.txtCopy.configure(background="white")
        self.txtCopy.configure(disabledforeground="#a3a3a3")
        self.txtCopy.configure(font="TkFixedFont")
        self.txtCopy.configure(foreground="#000000")
        self.txtCopy.configure(insertbackground="black")
        self.txtCopy.configure(textvariable=Hello_support.txtCopyVar)

        self.btnPozdrav = tk.Button(top)
        self.btnPozdrav.place(relx=0.734, rely=0.213, height=24, width=55)
        self.btnPozdrav.configure(activebackground="#ececec")
        self.btnPozdrav.configure(activeforeground="#000000")
        self.btnPozdrav.configure(background="#d9d9d9")
        self.btnPozdrav.configure(disabledforeground="#a3a3a3")
        self.btnPozdrav.configure(foreground="#000000")
        self.btnPozdrav.configure(highlightbackground="#d9d9d9")
        self.btnPozdrav.configure(highlightcolor="black")
        self.btnPozdrav.configure(pady="0")
        self.btnPozdrav.configure(text='''Pozdrav''')
        self.btnPozdrav.bind('<Button-1>',lambda e:Hello_support.btnPozdrav_Click(e))

        self.btnCopy = tk.Button(top)
        self.btnCopy.place(relx=0.734, rely=0.532, height=24, width=55)
        self.btnCopy.configure(activebackground="#ececec")
        self.btnCopy.configure(activeforeground="#000000")
        self.btnCopy.configure(background="#d9d9d9")
        self.btnCopy.configure(disabledforeground="#a3a3a3")
        self.btnCopy.configure(foreground="#000000")
        self.btnCopy.configure(highlightbackground="#d9d9d9")
        self.btnCopy.configure(highlightcolor="black")
        self.btnCopy.configure(pady="0")
        self.btnCopy.configure(text='''Copy''')
        self.btnCopy.configure(width=49)
        self.btnCopy.bind('<Button-1>',lambda e:Hello_support.btnCopy_Click(e))

if __name__ == '__main__':
    vp_start_gui()





