from tkinter import *
import time
import ttkthemes
from tkinter import ttk,messagebox,filedialog
import pymysql
import pandas

#function
def iexit():
    result=messagebox.askyesno('Confirm','Do you want to exit')
    if result:
        root.destroy()
    else:
        pass    


def export_data():
    url=filedialog.asksaveasfilename(defaultextension='.csv')
    indexing=studentTable.get_children()
    newlist=[]
    for index in indexing:
        content=studentTable.item(index)
        datalist=content['values']
        newlist.append(datalist)

    table= pandas.DataFrame(newlist,columns=['Id','Name','Mobile','Email','Address','Gender','D.O.B','Added Date','Added Time'])
    table.to_csv(url ,index=False)
    messagebox.showinfo('Success','Data is saved')

def toplevel_data(title,button_text,command):
    global idEntry,nameEntry,emailEntry,phoneEntry,addressEntry,genderEntry,dobEntry,screen
    screen=Toplevel()
    screen.title(title)
    screen.grab_set()
    screen.resizable(False,False)
    idLabel=Label(screen,text='Id',font=('times new roman',20))
    idLabel.grid(padx=20,pady=15,sticky=W)
    idEntry=Entry(screen,font=('times new roman',20))
    idEntry.grid(row=0,column=1,padx=10,pady=15)
    
    nameLabel=Label(screen,text='Name',font=('times new roman',20))
    nameLabel.grid(row=1,column=0,padx=20,pady=15,sticky=W)
    nameEntry=Entry(screen,font=('times new roman',20))
    nameEntry.grid(row=1,column=1,padx=10,pady=15)
    
    phoneLabel=Label(screen,text='Phone',font=('times new roman',20))
    phoneLabel.grid(row=2,column=0,padx=20,pady=15,sticky=W)
    phoneEntry=Entry(screen,font=('times new roman',20))
    phoneEntry.grid(row=2,column=1,padx=10,pady=15)
    
    emailLabel=Label(screen,text='Email',font=('times new roman',20))
    emailLabel.grid(row=3,column=0,padx=20,pady=15,sticky=W)
    emailEntry=Entry(screen,font=('times new roman',20))
    emailEntry.grid(row=3,column=1,padx=10,pady=15)
    
    addressLabel=Label(screen,text='Address',font=('times new roman',20))
    addressLabel.grid(row=4,column=0,padx=20,pady=15,sticky=W)
    addressEntry=Entry(screen,font=('times new roman',20))
    addressEntry.grid(row=4,column=1,padx=10,pady=15)
    
    genderLabel=Label(screen,text='Gender',font=('times new roman',20))
    genderLabel.grid(row=5,column=0,padx=20,pady=15,sticky=W)
    genderEntry=Entry(screen,font=('times new roman',20))
    genderEntry.grid(row=5,column=1,padx=10,pady=15)
    
    dobLabel=Label(screen,text='D.O.B.',font=('times new roman',20))
    dobLabel.grid(row=6,column=0,padx=20,pady=15,sticky=W)
    dobEntry=Entry(screen,font=('times new roman',20))
    dobEntry.grid(row=6,column=1,padx=10,pady=15)

    student_Button=ttk.Button(screen,text=button_text,command=command)
    student_Button.grid(row=7,columnspan=2,pady=15)

    if title== 'Update Student':
        indexing= studentTable.focus()
        content=studentTable.item(indexing)
        listdata=content['values']
        idEntry.insert(0,listdata[0])
        nameEntry.insert(0,listdata[1])
        phoneEntry.insert(0,listdata[2])
        emailEntry.insert(0,listdata[3])
        addressEntry.insert(0,listdata[4])
        genderEntry.insert(0,listdata[5])
        dobEntry.insert(0,listdata[6])


def update_data():
    query='update student set name=%s,email=%s,mobile=%s,address=%s,gender=%s,dob=%s,date=%s,time=%s where id=%s'
    mycursor.execute(query,(nameEntry.get(),emailEntry.get(),phoneEntry.get(),addressEntry.get(),genderEntry.get(),dobEntry.get(),date,currentTime,idEntry.get()))
    con.commit()
    messagebox.showinfo('Success',f'Id {idEntry.get()} is updated',parent=screen)
    screen.destroy()
    show_student()



def show_student():
    query= 'select * from student'
    mycursor.execute(query)
    fetched_data=mycursor.fetchall()
    studentTable.delete(*studentTable.get_children())
    for data in fetched_data:
        studentTable.insert('',END,values=data)


def delete_student():
    indexing= studentTable.focus()
    content= studentTable.item(indexing)
    content_id= content['values'][0]
    query = 'delete from student where id=%s'
    mycursor.execute(query,content_id)
    con.commit()
    messagebox.showinfo('Deleted',f'Id {content_id} is deleted')
    query= 'select * from student'
    mycursor.execute(query)
    fetched_data=mycursor.fetchall()
    studentTable.delete(*studentTable.get_children())
    for data in fetched_data:
        studentTable.insert('',END,values=data)

    

def search_data():
    query='select * from student where id=%s or name=%s or email=%s or mobile=%s or address=%s or gender=%s or dob=%s'
    mycursor.execute(query,(idEntry.get(),nameEntry.get(),emailEntry.get(),phoneEntry.get(),addressEntry.get(),genderEntry.get(),dobEntry.get()))
    studentTable.delete(*studentTable.get_children())
    fetched_data=mycursor.fetchall()
    for data in fetched_data:
        studentTable.insert('',END,values=data)



def add_data():
    if idEntry.get()==''or nameEntry.get()=='' or phoneEntry.get()=='' or emailEntry.get()=='' or addressEntry.get()=='' or genderEntry.get()=='' or dobEntry.get()=='':
        messagebox.showerror('Error','Enter all details',parent=screen)

    else :
        
        try:
            query='insert into student values(%s,%s,%s,%s,%s,%s,%s,%s,%s)'  
            mycursor.execute(query,(idEntry.get(),nameEntry.get(),phoneEntry.get(),emailEntry.get(),addressEntry.get(),genderEntry.get(),dobEntry.get(),date,currentTime))
            con.commit()
            result=messagebox.askyesno('Data added successfully', 'Do you want to clean the form',parent=screen)
            if result:
                idEntry.delete(0,END)
                nameEntry.delete(0,END)
                phoneEntry.delete(0,END)
                emailEntry.delete(0,END)
                addressEntry.delete(0,END)
                genderEntry.delete(0,END)
                dobEntry.delete(0,END)
            else:
                pass  
        except:
            messagebox.showerror('Error','Id alredy exist',parent=screen)
            return  


        query= 'select * from student'
        mycursor.execute(query)
        fetch_data=mycursor.fetchall()
        studentTable.delete(*studentTable.get_children())
        for data in fetch_data:
        
            studentTable.insert('',END,values=data)
    

def connect_database():
    def connect():
        global mycursor,con
        try:
          con=pymysql.connect(host=hostEntry.get(),user=userNameEntry.get(),password=passwordEntry.get())
          mycursor=con.cursor()
          
        except:
            messagebox.showerror("Error",'Invalid Details',parent=connectWindow)
            return
        
        try:
            query='create database studentmanagementsystem'
            mycursor.execute(query)  
            query='use studentmanagementsystem'
            mycursor.execute(query)
            query='''create table student(id int not null primary key, name varchar(30),mobile varchar(10),
                    email varchar(30),address varchar(100),gender varchar(10),dob varchar(20),date varchar(20),time varchar(20))'''
            mycursor.execute(query)
        except:
            query='use studentmanagementsystem'
            mycursor.execute(query)
        messagebox.showinfo('Success','Database Connection Successful',parent=connectWindow)
        connectWindow.destroy()
        addstudentbutton.config(state=NORMAL)
        searchstudentbutton.config(state=NORMAL)
        deletestudentbutton.config(state=NORMAL)
        updatestudentbutton.config(state=NORMAL)
        showstudentbutton.config(state=NORMAL)
        exportstudentbutton.config(state=NORMAL)
        exitstudentbutton.config(state=NORMAL)

    connectWindow=Toplevel()
    connectWindow.grab_set()
    connectWindow.geometry('470x250+730+230')
    connectWindow.title('Database Connection')
    connectWindow.resizable(0,0)

    hostnamelabel=Label(connectWindow,text='Host Name', font=('new times roman',18))
    hostnamelabel.grid(row=0,column=0,padx=20)

    hostEntry=Entry(connectWindow,font=('new times roman',15,'bold'))
    hostEntry.grid(row=0,column=1,padx=40,pady=20)
    
    userNamelabel=Label(connectWindow,text='User Name', font=('new times roman',18))
    userNamelabel.grid(row=1,column=0,padx=20)

    userNameEntry=Entry(connectWindow,font=('new times roman',15,'bold'))
    userNameEntry.grid(row=1,column=1,padx=40,pady=20)
   
    passwordlabel=Label(connectWindow,text='Password', font=('new times roman',18))
    passwordlabel.grid(row=2,column=0,padx=20)

    passwordEntry=Entry(connectWindow,font=('new times roman',15,'bold'))
    passwordEntry.grid(row=2,column=1,padx=40,pady=20)

    connectButton= ttk.Button(connectWindow,text='Connect',width=20,command=connect)
    connectButton.grid(row=3,columnspan=2)



count=0
text=''
def slider():
    global text,count
    text=text+s[count]
    sliderLabel.config(text=text)
    count+=1
    sliderLabel.after(30,slider)


def clock():
    global date,currentTime
    date=time.strftime('%d/%m/%Y')
    currentTime= time.strftime('%H:%M:%S')
    datetimeLabel.config(text=f'   Date :{date}\nTime :{currentTime}')
    datetimeLabel.after(1000,clock)

#GUI
root= ttkthemes.ThemedTk()
root.get_themes
root.set_theme('plastik')

root.geometry('1280x720+0+0')
root.resizable(0,0)
root.title('Student Mnagement System')

datetimeLabel=Label(root,text='',font=('times new roman',18,'bold'))
datetimeLabel.place(x=5,y=5)
clock()
s='Student Mangement System'
sliderLabel=Label(root,text=s,font=('times new roman',26,'bold'))
sliderLabel.place(x=450,y=0)
slider()

connectButton= ttk.Button(root,text='Connect to Database',width=25,command= connect_database )
connectButton.place(x=1000,y=5)

leftFrame= Frame(root)
leftFrame.place(x=80,y=80,width=400,height=600)

logo_Image=PhotoImage(file='logo.png')
logo_Lable=Label(leftFrame,image=logo_Image)
logo_Lable.grid(row=0,column=0)

addstudentbutton=ttk.Button(leftFrame,text='Add Student',width=25,state=DISABLED,command=lambda: toplevel_data('Add Student','Add Student',add_data))
addstudentbutton.grid(row=1,column=0,pady=20)

searchstudentbutton=ttk.Button(leftFrame,text='Search Student',width=25,state=DISABLED,command=lambda: toplevel_data('Search Student','Search',search_data))
searchstudentbutton.grid(row=2,column=0,pady=20)

deletestudentbutton=ttk.Button(leftFrame,text='Delete Student',width=25,state=DISABLED,command=delete_student)
deletestudentbutton.grid(row=3,column=0,pady=20)

updatestudentbutton=ttk.Button(leftFrame,text='Update Student',width=25,state=DISABLED,command=lambda: toplevel_data('Update Student','Update',update_data))
updatestudentbutton.grid(row=4,column=0,pady=20)

showstudentbutton=ttk.Button(leftFrame,text='Show Student',width=25,state=DISABLED,command=show_student)
showstudentbutton.grid(row=5,column=0,pady=20)

exportstudentbutton=ttk.Button(leftFrame,text='Export Data',width=25,state=DISABLED,command=export_data)
exportstudentbutton.grid(row=6,column=0,pady=20)

exitstudentbutton=ttk.Button(leftFrame,text='Exit',width=25,state=DISABLED,command=iexit)
exitstudentbutton.grid(row=7,column=0,pady=20)

rightFrame= Frame(root)
rightFrame.place(x=350,y=80,width=900,height=630)

scrollbarX=Scrollbar(rightFrame,orient=HORIZONTAL)
scrollbarY=Scrollbar(rightFrame,orient=VERTICAL)

studentTable=ttk.Treeview(rightFrame,columns=('Id','Name','Mobile','Email','Address','Gender','D.O.B','Added Date','Added Time'),
                          xscrollcommand=scrollbarX.set,yscrollcommand=scrollbarY.set)
scrollbarX.config(command=studentTable.xview)
scrollbarY.config(command=studentTable.yview)

scrollbarX.pack(side=BOTTOM,fill=X)
scrollbarY.pack(side=RIGHT,fill=Y)

studentTable.pack(fill=BOTH,expand=1)

studentTable.heading('Id',text='Id')
studentTable.heading('Name',text='Name')
studentTable.heading('Mobile',text='Mobile No.')
studentTable.heading('Email',text='Email')
studentTable.heading('Address',text='Address')
studentTable.heading('Gender',text='Gender')
studentTable.heading('D.O.B',text='D.O.B')
studentTable.heading('Added Date',text='Added Date')
studentTable.heading('Added Time',text='Added Time')

studentTable.column('Id',width=50,anchor=CENTER)
studentTable.column('Name',width=200,anchor=CENTER)
studentTable.column('Mobile',width=200,anchor=CENTER)
studentTable.column('Email',width=300,anchor=CENTER)
studentTable.column('Address',width=300,anchor=CENTER)
studentTable.column('Gender',width=100,anchor=CENTER)
studentTable.column('D.O.B',width=100,anchor=CENTER)
studentTable.column('Added Date',width=100,anchor=CENTER)
studentTable.column('Added Time',width=100,anchor=CENTER)

style=ttk.Style()
style.configure('Treeview',rowheight=35,font=('arial',12),background='white',fieldbackground='white')
style.configure('Treeview.Heading',font=('arial',12,'bold'))

studentTable.config(show='headings')

root.mainloop()