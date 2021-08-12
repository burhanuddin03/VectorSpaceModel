import tkinter
from tkinter import *
import VSM as g



root=tkinter.Tk()
Query=tkinter.StringVar()
alpha=tkinter.StringVar()

tkinter.Label(root,text='Vector Space Model',font=('Helvetica',25,'bold'),fg='blue').pack(pady=5,padx=5)
note="You can enter any free text query(Default Alpha=0.005)\n\n"
tkinter.Label(root,text=note,font=('Helvetica',15,'bold')).pack()
tkinter.Label(root,text='Enter Query',font=('Helvetica',15,'bold')).pack()
queryset=tkinter.Entry(root,textvariable=Query,font=('Arial',10),width=50)
queryset.pack()
tkinter.Label(root,text='\nEnter Alpha(Threshold)',font=('Helvetica',15,'bold')).pack()
alpha=tkinter.Entry(root,textvariable=alpha,font=('Arial',10),width=30)
alpha.pack()
l1=Text(root,font=('Helvetica',25,'bold'),fg='black')

def ScrapeStart():
    l1.pack()
    g.main1(Query.get(),alpha.get(),root,l1)


def exitt():
    quit()

tkinter.Button(root,text='Search',font=('Helvetica',10,'bold'),fg='white',bg='green',command=ScrapeStart).pack(pady=10)
tkinter.Button(root,text='Exit',font=('Helvetica',10,'bold'),fg='white',bg='green',command=exitt).pack(pady=10)
root.title('Search engine')
root.attributes("-fullscreen",True)
root.geometry('500x300')
root.mainloop()
