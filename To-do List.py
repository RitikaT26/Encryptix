from tkinter import *
from tkinter import messagebox,ttk
import mysql.connector as sq

todo= Tk()
todo.geometry('480x450')
todo.config(background='#b7f9cf')
todo.title('To-Do List| Developed By Ritika Talwar')
todo.resizable(False,False)

con= sq.connect(user='root',passwd='2115',host='localhost',database='test')
cursor= con.cursor()

#-------heading------
head= Label(todo, text='              TO DO LIST                   ',anchor='center', font=('times new roman',26,'bold'), fg='#065535')
head.place(x=0,y=10)

#------task list-----
frame= Frame(todo, relief=RIDGE)
frame.place(x=20,y=70,width=450,height=300)

todotree= ttk.Treeview(frame, columns=('Task ID','Task','Deadline'))
todotree.pack(fill=BOTH, expand=True)
todotree.heading('Task ID',text='Task ID')
todotree.heading('Task', text='Task')
todotree.heading('Deadline', text='Deadline')

todotree.column('Task ID',width=30, anchor='center')
todotree.column('Task',width=200, anchor='center')
todotree.column('Deadline',width=50, anchor='center')

todotree.config(show='headings', padding=(5,5,5,5))

cursor.execute('select * from todolist')
row=cursor.fetchall()
for d in row:
    todotree.insert('','end',values=d)

#-insert record subpage-
def insertRec():
    addRec=Toplevel()
    addRec.geometry('300x200')
    addRec.config(background='#b4eccf')
    addRec.title('Insert Tasks')
    addRec.resizable(False,False)

    headAdd= Label(addRec, text='INSERT TASKS', width=16,anchor='center', font=('times new roman',24,'bold'), fg='#3a8b63')
    headAdd.place(x=0,y=10)

    label1= Label(addRec, text='Enter Task:',font=('times new roman',12))
    label1.place(x=10,y=60)
    label2= Label(addRec, text='''Enter Deadline
(in YYYY/MM/DD Format):''',font=('times new roman',12))
    label2.place(x=10,y=100)

    text1= Entry(addRec, width=30)
    text1.place(x=110,y=60)
    text2= Entry(addRec, width=10)
    text2.place(x=210,y=100)

    def insert():
        if text1.get()=='' or text2.get()=='':
           messagebox.showerror('ERROR', "All Fields are required.")
        else:
            cursor.execute("insert into todolist(task,deadline) values('{}','{}')".format(text1.get(),text2.get()))
            con.commit()
            cursor.execute("select * from todolist")
            fetch=cursor.fetchall()
            todotree.delete(*todotree.get_children())
            for i in fetch:
                todotree.insert('',END, values=i)
            r= messagebox.askyesno('Insert Task', "Task Inserted. Would you like to insert more tasks?")
            if r:
               text1.delete(0,END)
               text2.delete(0,END)
            else:
               addRec.destroy()
    b1= Button(addRec, text='Insert Task', font=('times new roman',12), command=insert)
    b1.place(x=100,y=150)
    
#-delete record subpage-
def deleteRec():
    delRec=Toplevel()
    delRec.geometry('300x150')
    delRec.config(background='#b4eccf')
    delRec.title('Delete Tasks')
    delRec.resizable(False,False)

    headDel= Label(delRec, text='DELETE TASKS',width=16,anchor='center', font=('times new roman',24,'bold'), fg='#3a8b63')
    headDel.place(x=0,y=10)

    label3= Label(delRec, text='Enter Task ID:',font=('times new roman',12))
    label3.place(x=10,y=60)

    text3= Entry(delRec, width=10)
    text3.place(x=210,y=60)

    def delete():
        if text3.get()=='':
            messagebox.showerror('ERROR', "All Fields are required.")
        else:
            cursor.execute("delete from todolist where taskid='{}'".format(text3.get()))
            con.commit()
            cursor.execute("select * from todolist")
            fetch=cursor.fetchall()
            todotree.delete(*todotree.get_children())
            for i in fetch:
                todotree.insert('',END,values=i)
            r= messagebox.askyesno('Delete Task','Task Deleted, Would you like to delete more tasks?')
            if r:
                text3.delete(0,END)
            else:
                delRec.destroy()
            
    b2= Button(delRec, text='Delete Task', font=('times new roman',12), command=delete)
    b2.place(x=100,y=100)
    
#-update record subpage-
def updateRec():
    uptRec=Toplevel()
    uptRec.geometry('300x220')
    uptRec.config(background='#b4eccf')
    uptRec.title('Update Tasks')
    uptRec.resizable(False,False)

    headUpt= Label(uptRec, text='UPDATE TASKS',width=16,anchor='center', font=('times new roman',24,'bold'), fg='#3a8b63')
    headUpt.place(x=0,y=10)

    label4= Label(uptRec, text='Enter Task ID:',font=('times new roman',12))
    label4.place(x=10,y=60)
    label5= Label(uptRec, text='Enter Task:',font=('times new roman',12))
    label5.place(x=10,y=90)
    label6= Label(uptRec, text='''Enter Deadline
(in YYYY/MM/DD Format):''',font=('times new roman',12))
    label6.place(x=10,y=120)

    text4= Entry(uptRec, width=10)
    text4.place(x=110,y=60)
    text5= Entry(uptRec, width=30)
    text5.place(x=110,y=90)
    text6= Entry(uptRec, width=10)
    text6.place(x=210,y=120)

    def update():
        if text4.get()=='' or (text5.get()=='' and text6.get()==''):
            messagebox.showerror('ERROR', "All Fields are required.")
        else:
            if text5.get() !='' and text6.get()=='':
                cursor.execute("update todolist set task='{}' where taskid='{}'".format(text5.get(),text4.get()))
                con.commit()
            elif text5.get() =='' and text6.get()!='':
                cursor.execute("update todolist set deadline='{}' where taskid='{}'".format(text6.get(),text4.get()))
                con.commit()
            elif text5.get() !='' and text6.get()!='':
                cursor.execute("update todolist set task='{}', deadline='{}' where taskid='{}'".format(text5.get(),text6.get(),text4.get()))
                con.commit()
                
            children = todotree.get_children()
            if children:
                todotree.delete(*children)
            cursor.execute('SELECT * FROM todolist')
            row = cursor.fetchall()
            for d in row:
                todotree.insert('', 'end', values=d)
            r= messagebox.askyesno('Update Task','Task Updated. Would you like to update more tasks?')
            if r:
                text4.delete(0,END)
                text5.delete(0,END)
                text6.delete(0,END)
            else:
                uptRec.destroy()
    
    b3= Button(uptRec, text='Update Task', font=('times new roman',12), command=update)
    b3.place(x=100,y=180)

#-search record subpage-
def searchRec():
    seaRec=Toplevel()
    seaRec.geometry('300x220')
    seaRec.config(background='#b4eccf')
    seaRec.title('Search Tasks')
    seaRec.resizable(False,False)

    headSea= Label(seaRec, text='SEARCH TASKS',width=16,anchor='center', font=('times new roman',24,'bold'), fg='#3a8b63')
    headSea.place(x=0,y=10)

    label7= Label(seaRec, text='Enter Task ID:',font=('times new roman',12))
    label7.place(x=10,y=60)
    label8= Label(seaRec, text='Enter Task:',font=('times new roman',12))
    label8.place(x=10,y=90)
    label9= Label(seaRec, text='''Enter Deadline
(in YYYY/MM/DD Format):''',font=('times new roman',12))
    label9.place(x=10,y=120)

    text7= Entry(seaRec, width=10)
    text7.place(x=110,y=60)
    text8= Entry(seaRec, width=30)
    text8.place(x=110,y=90)
    text9= Entry(seaRec, width=10)
    text9.place(x=210,y=120)

     
    def search():
        if text7.get()=='' and text8.get()=='' and text9.get()=='':
            messagebox.showerror('ERROR', "One of the Fields is required.")
        else:
            if text7.get():
                id_entry='%'+text7.get()+'%'
                cursor.execute("select * from todolist where taskid like '{}'".format(id_entry))
            elif text8.get():
                task_entry='%'+text8.get()+'%'
                cursor.execute("select * from todolist where task like'{}'".format(task_entry))
            elif text9.get():
                deadline_entry='%'+text9.get()+'%'
                cursor.execute("select * from todolist where deadline like'{}'".format(deadline_entry))
            fetched_data= cursor.fetchall()
            todotree.delete(*todotree.get_children())            
            for h in fetched_data:
                todotree.insert('',"end", values=h)
            r= messagebox.askyesno('Search Contact', "Contact Searched. Would you like to search more Contacts?")
            if r:
               text7.delete(0,END)
               text8.delete(0,END)
               text9.delete(0,END)
            else:
               seaRec.destroy()
    
    b4= Button(seaRec, text='Search Task', font=('times new roman',12), command=search)
    b4.place(x=100,y=180)

#---------sort record subpage---------
def sortContact():
        cursor.execute("SELECT * FROM todolist ORDER BY deadline")
        data=cursor.fetchall()
        todotree.delete(*todotree.get_children())
        for p in data:
            todotree.insert('',"end", values=p)

        messagebox.showinfo('Prioritise Tasks', "Tasks are prioritised successfully.")
        
#--------exit-------
def exit():
    abc= messagebox.askyesno('Want to Exit?',"Are you sure you want to exit?")
    if abc:
        messagebox.showinfo('Thank You!','Thank You!')
        todo.destroy()


#-------buttons------
b5= Button(todo,text='Insert Task', font=('times new roman', 10), command=insertRec)
b5.place(x=20,y=400)
b6= Button(todo, text='Delete Task', font=('times new roman', 10), command=deleteRec)
b6.place(x=100,y=400)
b7= Button(todo, text='Update Task', font=('times new roman', 10), command=updateRec)
b7.place(x=180,y=400)
b8= Button(todo, text='Search Task', font=('times new roman', 10), command=searchRec)
b8.place(x=260,y=400)
b9= Button(todo, text='Prioritise Tasks', font=('times new roman', 10), command=sortContact)
b9.place(x=340,y=400)
b9= Button(todo, text='Exit', font=('times new roman', 10), command=exit)
b9.place(x=440,y=400)





todo.mainloop()
