#! /usr/bin/env python
#  -*- coding: utf-8 -*-
#
# Support module generated by PAGE version 4.21
#  in conjunction with Tcl version 8.6
#    Mar 29, 2019 11:41:21 AM CET  platform: Windows NT

import sys

import sqlite3   # pridano pro praci sDB SQLite

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

def set_Tk_var():
    global txtIDVar
    txtIDVar = tk.StringVar()
    global txtKrestniVar
    txtKrestniVar = tk.StringVar()
    global txtPrijmeniVar
    txtPrijmeniVar = tk.StringVar()
    global txtOsloveniVar
    txtOsloveniVar = tk.StringVar()
    global txtMestoVar
    txtMestoVar = tk.StringVar()

conn = None
cursor = None
records = None
recordCount = None
currentRecord = None

def readDB():
    global conn,cursor,records,recordCount,currentRecord

    conn = sqlite3.connect("nwe.sqlite")    # pripojeni k DB (v praxi try/except)
    conn.row_factory = sqlite3.Row          # abych mohl pouzivat nazvy sloupcu misto cisel
    cursor = conn.cursor()
    cursor.execute("Select EmployeeID,LastName,FirstName,TitleOfCourtesy,City From Employees")
    records = cursor.fetchall()             # v praxi cist po castech
    recordCount = len(records)              # pocet nactenych recordu (radku)
    currentRecord = 0                       # 1. record jako aktualni (predpoklad - nacten alespon 1 record)
    # conn.close()                          # odpojeni od DB

def fillForm(index):
    record = records[index]

    # txtIDVar.set(record[0])               # pristup ke "sloupci" pomoci indexu sloupce
    txtIDVar.set(record["EmployeeID"])
    txtKrestniVar.set(record["FirstName"])
    txtPrijmeniVar.set(record["LastName"])
    txtOsloveniVar.set(record["TitleOfCourtesy"])
    txtMestoVar.set(record["City"])

def initDB():
    readDB()
    fillForm(currentRecord)

def btnFirst_Click(p1):
    global currentRecord
    currentRecord = 0    # prvni
    fillForm(currentRecord)

def btnLast_Click(p1):
    global currentRecord
    currentRecord = recordCount - 1 # posledni
    fillForm(currentRecord)

def btnNext_Click(p1):
    global currentRecord
    if currentRecord < recordCount - 1: # jsem pred koncem?
        currentRecord += 1  # dalsi
        fillForm(currentRecord)

def btnPrev_Click(p1):
    global currentRecord
    if currentRecord > 0:   # jsem pred zacatkem?
        currentRecord -= 1
        fillForm(currentRecord)

def btnUpdate_Click(p1):
    print('DB_support.btnUpdate_Click')
    print('p1 = {0}'.format(p1))
    sys.stdout.flush()

def init(top, gui, *args, **kwargs):
    global w, top_level, root
    w = gui
    top_level = top
    root = top
    initDB()            # pripojeni k DB, nacteni dat a zobrazeni 1. recordu

def destroy_window():
    # Function which closes the window.
    global top_level
    top_level.destroy()
    top_level = None

if __name__ == '__main__':
    import DB
    DB.vp_start_gui()




