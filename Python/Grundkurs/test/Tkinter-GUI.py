from Tkinter import *
import tkMessageBox

def hole():
	lab=Label(root,text="Hier nicht!")
	lab.pack()
	print textfenster.get('1.0',END)
	tkMessageBox.showinfo('Hier nicht!','Hier auch nicht!')
	
root=Tk()
#lab=Label(root,text=u"Viel Spa\xdf mit dem Tkinter-Tutorial")
#lab.pack()
#but=Button(root,text="Test?",command=hole)
#but.pack()
#eingabe=Entry(root)
#eingabe.pack()
#textfenster = Text(root)
#textfenster.pack()
#textfenster.insert(END,"Hallo G10b")

rows = []
for i in range(5):
    cols = []
    for j in range(4):
        e = Entry(relief=RIDGE)
        e.grid(row=i, column=j, sticky=NSEW)
        e.insert(END, '%d.%d' % (i, j))
        cols.append(e)
    rows.append(cols)

def onPress():
    for row in rows:
        for col in row:
            print col.get(),
        print

Button(text='Fetch', command=onPress).grid()

root.mainloop()
