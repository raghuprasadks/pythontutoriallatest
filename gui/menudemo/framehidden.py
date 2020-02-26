import tkinter as tk
import glob
 
class App:
 
def __init__(self, root):
    self.root = root
    self.menu()
    self.text()
    self.root.bind("<Control-l>", lambda x: self.hide())
    self.hidden = 0
 
def menu(self):
    self.frame1 = tk.Frame(self.root)
    self.frame1.pack(side="left", fill=tk.BOTH, expand=1)
    self.lb = tk.Listbox(self.frame1)
    self.lb['bg'] = "black"
    self.lb['fg'] = "lime"
    self.lb.pack(side="left", fill=tk.BOTH, expand=1)

for file in glob.glob("*"):
    self.lb.insert(tk.END, file)
 
def text(self):
    self.frame2 = tk.Frame(self.root)
    self.frame2.pack(side="left", fill=tk.BOTH, expand=1)
    self.txt = tk.Text(self.frame2)
    self.txt['bg'] = 'gold'
    self.txt.pack(fill=tk.BOTH, expand=1)
 
def hide(self):
    if self.hidden == 0:
        self.frame1.destroy()
        self.hidden = 1
        print("Hidden", self.hidden)
    else:
        self.frame2.destroy()
        self.menu()
        self.text()
        self.hidden = 0
        print("Hidden", self.hidden)
     
 
 
root = tk.Tk()
app = App(root)
root.mainloop()