from tkinter import *
from tkinter import filedialog,simpledialog
from tkinter.scrolledtext import ScrolledText
from tkinter  import messagebox
from tkinter.ttk import *
import re

root = Tk()
root.title('Text Editor In Python')


textPad = ScrolledText(root, width="40", height="40")
filename = ''

def newFile():
    global filename
    if len(textPad.get('1.0',END+'-1c'))>0:
        if messagebox.askyesno("SAVE","Do you want to save?"):
            saveFile()
        else:
            textPad.delete(0.0,END)
    root.title("TEXT EDITOR")

def saveFile():
    f = filedialog.asksaveasfile(mode='w',defaultextension='.txt')
    if f!= None:
        data = textPad.get('1.0',END)
    try:
        f.write(data)
    except:
        messagebox.showerror(title="Oops!!",message="Unable to save file!")
     
def saveAs():
    f = filedialog.asksaveasfile(mode='w',defaultextension='.txt')
    t = textPad.get(0.0,END)
    try:
        f.write(t.rstrip())
    except:
        messagebox.showerror(title="Oops!!",message="Unable to save file!")

def openFile():
    f = filedialog.askopenfile(parent=root,mode='r')
    t = f.read()
    textPad.delete(0.0,END)
    textPad.insert(0.0,t)
    
def about_command():
    label = messagebox.showinfo("Text Editor ", "Done by using tkinter\nDone By Pranu Deepak")

def handle_click(event):
    textPad.tag_config('Found',background='Black',foreground='grey')
    

def find_pattern():
    textPad.tag_remove("Found",'1.0',END)
    find = simpledialog.askstring("Find....","Enter text:")
    if find:
        idx = '1.0'
    while 1:
        idx = textPad.search(find,idx,nocase=1,stopindex=END)
        if not idx:
            break
        lastidx = '%s+%dc' %(idx,len(find))
        textPad.tag_add('Found',idx,lastidx)
        idx = lastidx
    textPad.tag_config('Found',foreground='white',background='black')
    textPad.bind("<1>",handle_click)


def printme():
    label = messagebox.showinfo("Text","Welcome to text editor")

def exit_command():
    if messagebox.askyesno("Exit","Are you sure you want to exit?"):
        root.destroy()
menuM = Menu(root)
root.configure(menu=menuM)

fileM = Menu(menuM)
menuM.add_cascade(label='File',menu=fileM)
fileM.add_command(label='New',command=newFile)
fileM.add_command(label='Open',command=openFile)
fileM.add_command(label='Save',command=saveFile)
fileM.add_command(label='Save As...',command=saveAs)
fileM.add_separator()
fileM.add_command(label='Exit',command=exit_command)

editM = Menu(menuM)
menuM.add_cascade(label='Edit',menu=editM)
editM.add_command(label='Undo')
editM.add_command(label='Redo')
editM.add_command(label='Cut')
editM.add_command(label='Copy')
editM.add_command(label='Paste')

viewM = Menu(menuM)
menuM.add_cascade(label='View',menu=viewM)
viewM.add_command(label='Text',command=printme)

aboutM = Menu(menuM)
menuM.add_cascade(label='About',menu=aboutM)
aboutM.add_command(label='About',command = about_command)

findM = Menu(menuM)
menuM.add_cascade(label='Find',menu=findM)
findM.add_command(label='Find',command = find_pattern)

textPad.pack()

root.mainloop()




