from tkinter import *
from tkinter import messagebox
from PIL import ImageTk

def Login():
    if userNameEntry.get()=='' or passwordEntry.get()=='':
        messagebox.showerror('Error','Please enter username and password')
    elif userNameEntry.get()=='Sahil' or passwordEntry.get()=='1234':
        messagebox.showinfo('Sucess','Welcome')
        window.destroy()
        import sms 

    else:
        messagebox.showerror('Error','Incorrect credentials')     
    

window = Tk()

window.geometry('1280x720+0+0')
window.title('Login Student Mnagement System')

window.resizable(False,False)

backgroundimage = ImageTk.PhotoImage(file='bg.jpg')

bgLabel=Label(window,image= backgroundimage)
bgLabel.place(x=0,y=0)

loginframe = Frame(window,bg='white')
loginframe.place(x=400,y=150)

logoImage = PhotoImage(file='logo.png')
logoLabel = Label(loginframe,image=logoImage,bg='white')
logoLabel.grid(row=0,column=0,columnspan=2,pady=15)

usernameImage = PhotoImage(file='user.png')
usernameLable = Label(loginframe,image=usernameImage,text='Username',compound=LEFT,font=('times new roman',20,'bold'),bg='white' ) 
usernameLable.grid(row=1,column=0,pady=15,padx=10)

userNameEntry= Entry(loginframe,font=('times new roman',20,'bold'),bd=2)
userNameEntry.grid(row=1,column=1,pady=15,padx=10)

passwordImage = PhotoImage(file='password.png')
passwordLable = Label(loginframe,image=passwordImage,text='Password',compound=LEFT,font=('times new roman',20,'bold'),bg='white' ) 
passwordLable.grid(row=2,column=0,pady=15,padx=10)

passwordEntry= Entry(loginframe,font=('times new roman',20,'bold'),bd=2)
passwordEntry.grid(row=2,column=1,pady=15,padx=10)

loginbutton=Button(loginframe,text='Login',font=('times new roman',14,'bold'),width=10,fg='white',bg='cornflowerblue',
                   activebackground='cornflowerblue',cursor='hand2',command=Login)
loginbutton.grid(row=3,column=0,columnspan=2,pady=10) 

window.mainloop()