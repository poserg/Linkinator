import tkinter as tk
from tkinter.filedialog import askdirectory
from tkinter import PanedWindow, BOTH

from os import path

class Application(tk.Frame):
    def __init__(self, create_links, master=None):
        tk.Frame.__init__(self, master)
        self.pack()
        self.createWidgets()
        self.create_links = create_links

        self.start_btn = tk.Button(self)
        self.start_btn["text"] = "Start"
        self.start_btn.pack(side="bottom")
        self.start_btn["command"] = self.start

    def createWidgets(self):
        from_panel = Item(self)
        from_panel.pack(fill=BOTH, expand=1)
        from_panel.createItem("Select source directory")
        self.from_panel = from_panel

        to_panel = Item(self)
        to_panel.pack(fill=BOTH, expand=1)
        to_panel.createItem("Select target directory")
        self.to_panel = to_panel

    def start(self):
        src = self.from_panel.lbl["text"]
        dst = self.to_panel.lbl["text"]
        if path.exists(src) and path.exists(dst):
            self.create_links(src, dst)

class Item(PanedWindow):
    def createItem(self, title):
        self.lbl = self.createLabel(title)
        self.btn = self.createButton()
        
    def createButton(self):
        btn = tk.Button(self)
        btn["text"] = "Select"
        btn["command"] = self.select_dir
        btn.pack(side="right")

        return btn

    def createLabel(self, title):
        lbl = tk.Label(self, text=title)
        lbl.pack(side="left")

        return lbl

    def select_dir(self):
        self.lbl["text"]=askdirectory(title="Please select a directory")


    

def run_gui(create_links):
    root = tk.Tk()
    app = Application(create_links, master=root)
    app.mainloop()
