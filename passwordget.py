from tkinter import *
from tkinter import messagebox

def passsearch():
    searched=[]
    with open("passdata.txt","r") as f:
        read=f.read().split("\n")
        pee=[[i]for i in read]
        l=len(pee)
        for i in range(l):
            for j in pee[i]:
                h=j.split('|')
                searched.append(h)
    s=False
    for i in range(len(searched)):
        if searched[i][0]==e1.get():
            messagebox.showinfo(title=f"{e1.get()}",message=f"Your Email Id is:{searched[i][1]}\nYour Password Is:{searched[i][2]}")           
            break   
        else:
            s=True
    if s:
        messagebox.showerror(title="ERROR",message=f"NOT FOUND")

        
win =Tk()
win.title("Password Gettter🔓")
win.config(padx=50,pady=50)


canva=Canvas(height=200,width=200,highlightthickness=0)
img=PhotoImage(file="logo.png")
canva.create_image(100,100,image=img)
canva.grid(row=0,column=1)


la1=Label(text="Enter the Website:",font=("courier",15,"bold"))
la1.grid(row=1,column=1)

e1=Entry(width=20)
e1.grid(row=2, column=1)

but1=Button(text="Search",command=passsearch)
but1.grid(row=3,column=1)


win.mainloop()