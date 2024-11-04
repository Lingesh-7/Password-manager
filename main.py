from tkinter import *
from tkinter import messagebox
import random as r
import pyperclip
# ---------------------------- PASSWORD GENERATOR ------------------------------- #
def password():
    al=['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z',
    'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z'] 
    num=['1','2','3','4','5','6','7','8','9','0']
    sy=[ '!', '"', '#', '$', '%', '&', "'", '(', ')', '*', '+', ',', '-', '.', '/', ':', ';', '<', '=', '>', '?', '@', '[', '\\', ']', '^', '_', '`', '{', '|', '}', '~']

    nr_letters=r.randint(8,10)
    nr_sys=r.randint(2,4)
    nr_num=r.randint(2,4)

    lett=[r.choice(al) for i in range(nr_letters)]

    number=[r.choice(num) for i in range(nr_num)]

    sys=[r.choice(sy) for i in range(nr_sys)]
    passw=lett+sys+number
    r.shuffle(passw)

    passwords="".join(passw)
    
    e3.insert(0,passwords)
    pyperclip.copy(passwords)
# print(password)yQ=V>IQ'q7jrx1Y8  5VQ+,vC0PZ8d7@T

# ---------------------------- SAVE PASSWORD ------------------------------- #
def data():
    if len(e1.get())==0 or len(e2.get())==0:
        messagebox.showinfo(title="Opps!!!!!!!",message="Heyy!! Don't leave any of the feild empty")
    else:
        isook=messagebox.askokcancel(title=e1.get(),message=f"These are the details entered:\nEmail: {e2.get()}\nPassword: {e3.get()}\n Is it okay to save?")
        if isook:
            with open("passdata.txt","a") as f:
                f.write(f"{e1.get()}|{e2.get()}|{e3.get()}\n")
            
            e1.delete(0,END)
            e2.delete(0,END)
            e2.insert(0,"lingesh.91918@gmail.com")
            e3.delete(0,END)

# ---------------------------- UI SETUP ------------------------------- #
win=Tk()
win.title("Password Manager🔒")
win.config(padx=50,pady=50,bg="white")
win.minsize(300,300)

canva=Canvas(width=200,height=200,bg="white",highlightthickness=0)
img=PhotoImage(file="logo.png")
canva.create_image(100,100,image=img)
canva.grid(column=1,row=0)

la1=Label(text="Website:",font=('courier',10,"bold"),bg="white")
la1.grid(column=0,row=1)

e1=Entry(width=35)
e1.grid(row=1,column=1,columnspan=2)
e1.focus()

la2=Label(text="Email/Username:",font=('courier',10,"bold"),bg="white")
la2.grid(column=0,row=2)

e2=Entry(width=35)
e2.insert(0,"lingesh.91918@gmail.com")
e2.grid(row=2,column=1,columnspan=2)

la3=Label(text="Password🔑:",font=('courier',10,'bold'),bg='white')
la3.grid(row=3,column=0)

e3=Entry(width=21)
e3.grid(row=3,column=1)

but1=Button(text="Generate Password",font=('courier',10,"bold"),bg="white",command=password)
but1.grid(row=3,column=2)


but2=Button(text="ADD",width=36,font=('courier',10,"bold"),bg="white",command=data)
but2.grid(row=4,column=1,columnspan=2)


win.mainloop()