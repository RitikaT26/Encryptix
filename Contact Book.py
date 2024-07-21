from tkinter import *
from tkinter import messagebox,ttk
from PIL import Image, ImageTk
import mysql.connector as sq
import time
book= Tk()
book.geometry('1270x630')
book.config(background='#cbc3f5')
book.title('Contact Book|Developed By Ritika Talwar')

con= sq.connect(user='root',passwd='2115',host='localhost',database='test')
cursor= con.cursor()

#-------heading------
title= Label(book, text="Contact Book",
             font=("times new roman", 40, "bold"),
             bg="#744fdb", fg="white", anchor=W,
             padx=100).place(x=110,y=0, relwidth=1)

#--------logo---------
ima1= Image.open("D:\\PYTHON PROJECTS\\logo.jpg")
reima1= ima1.resize((120,65))
img1=ImageTk.PhotoImage(reima1)
panel1= Label(book, image= img1)
panel1.place(x=0, y=0)

#----footer courtesy----
label1= Label(book, text="Contact Book| Developed By Ritika Talwar",bg="#C5C6D0", font=("times new roman", 15))
label1.pack(side=BOTTOM, fill=X)

#---------clock---------
def display_date():
    d=time.strftime("%d.%m.%Y")
    label2= Label(book, text=d, bg='#ceb1fb', fg='white', font=('Times New Roman', 20, 'bold'))
    label2.place(x=570,y=20)
    label2.after(100,display_date)

def display_time():
    t=time.strftime("%I:%M:%S %p")
    label3= Label(book,text=t , bg='#ceb1fb', fg='white', font=('Times New Roman', 20, 'bold'))
    label3.place(x=720,y=20)
    label3.after(100,display_time)
    
display_date()
display_time()

#--number of contacts---
label4=Label(book)
label4.place(x=900,y=20)
def display_contactno():
    cursor.execute('select count(*) from contact')
    a=cursor.fetchall()
    for x in a:
        for j in x:
            k=j
    txt= 'Number of Saved Contacts: '+ str(k)
    label4.config(text=txt, bg='#ceb2fb', fg='white', font=('Times New Roman', 20, 'bold'))

display_contactno()

#----sql frame table----
frame= Frame(book, relief=RIDGE)
frame.place(x=250,y=80,width=1000,height=520)

contree=ttk.Treeview(frame, columns=('ContactID','Name','Phone Number','Email Address','Address'))
contree.pack(fill=BOTH, expand=True)

contree.heading('ContactID',text='Contact ID')
contree.heading('Name',text='Name')
contree.heading('Phone Number',text='Phone Number')
contree.heading('Email Address',text='Email Address')
contree.heading('Address', text='Address')

contree.column('ContactID',width=50, anchor='center')
contree.column('Name',width=150, anchor='center')
contree.column('Phone Number',width=100,anchor='center')
contree.column('Email Address',width=200,anchor='center')
contree.column('Address',width=200,anchor='center')

contree.config(show='headings', padding=(5,5,5,5))

cursor.execute('select * from contact')
row=cursor.fetchall()
for i in row:
    contree.insert('','end',values=i)

#--------add Contacts subpage------------
def insertContact():
    addRec= Toplevel()
    addRec.geometry("600x300")
    addRec.resizable(False,False)
    addRec.title("Add Contacts")
    addRec.configure(background="#e6d8fd")

    l1= Label(addRec, text="INSERT CONTACT", width=37, font= ("tahoma", 20, "bold"),fg="white", bg="#BF00FF")
    l1.place(x=0,y=10)

    l2= Label(addRec, text="Name:", font= ("times new roman", 14))
    l2.place(x=10,y=60)
    l3= Label(addRec, text="Phone Number:", font= ("times new roman", 14))
    l3.place(x=10,y=100)
    l4= Label(addRec, text="Email Address:", font= ("times new roman", 14))
    l4.place(x=10,y=140)
    l5= Label(addRec, text="Address:", font= ("times new roman", 14))
    l5.place(x=10,y=180)

    tb1= Entry(addRec, width=25, font= ("times new roman", 14), fg="black")
    tb1.place(x=300,y=60)
    tb2= Entry(addRec, width=25, font= ("times new roman", 14), fg="black")
    tb2.place(x=300,y=100)
    tb3= Entry(addRec, width=25, font= ("times new roman", 14), fg="black")
    tb3.place(x=300,y=140)
    tb4= Entry(addRec, width=25, font= ("times new roman", 14), fg="black")
    tb4.place(x=300,y=180)
    
    def addContact():
        if tb1.get()=='' or tb2.get()=='' or tb3.get()=='' or tb4.get()=='':
           messagebox.showerror('ERROR', "All Fields are required.")
        else:
           cursor.execute("insert into contact(name,phone_number, email_address,address) values('{}','{}','{}','{}')".format(tb1.get(), tb2.get(), tb3.get(), tb4.get()))
           con.commit()
           cursor.execute("select * from contact")
           fetch=cursor.fetchall()
           contree.delete(*contree.get_children())
           for i in fetch:
               contree.insert('', END, values=i)

           def display_contactno():
               cursor.execute('select count(*) from contact')
               a=cursor.fetchall()
               for x in a:
                  for j in x:
                      k=j
               txt= 'Number of Saved Contacts: '+ str(k)
               label4.config(text=txt, bg='#ceb2fb', fg='white', font=('Times New Roman', 20, 'bold'))

           display_contactno()

           r= messagebox.askyesno('Insert Contact', "Contact Inserted. Would you like to insert more Contacts?")
           if r:
               tb1.delete(0,END)
               tb2.delete(0,END)
               tb3.delete(0,END)
               tb4.delete(0,END)
           else:
               addRec.destroy()
    b1= Button(addRec, text="INSERT CONTACT", width=20, command=addContact, font= ("times new roman", 16, "underline"), fg="black", bg="#e6d8fd")
    b1.place(x=175, y=250)

#---------delete Contact subpage---------
def deleteContact():
    delRec= Toplevel()
    delRec.geometry("600x300")
    delRec.resizable(False,False)
    delRec.title("Delete Contacts")
    delRec.configure(background="#e6d8fd")

    l5= Label(delRec, text="        DELETE CONTACT        ", width=37, font= ("tahoma", 20, "bold"),fg="white", bg="#bf00ff")
    l5.place(x=0,y=10)

    l6= Label(delRec, text="Contact ID:", font= ("times new roman", 14))
    l6.place(x=10,y=60)
    l7= Label(delRec, text="Name:", font= ("times new roman", 14))
    l7.place(x=10,y=100)
    l8= Label(delRec, text="Phone Number:", font= ("times new roman", 14))
    l8.place(x=10,y=140)
    l9= Label(delRec, text="Email Address:", font= ("times new roman", 14))
    l9.place(x=10,y=180)
    l10= Label(delRec, text="Address:", font= ("times new roman", 14))
    l10.place(x=10,y=220)

    tb6= Entry(delRec, width=25, font= ("times new roman", 14), fg="black")
    tb6.place(x=300,y=60)
    tb7= Entry(delRec, width=25, font= ("times new roman", 14), fg="black")
    tb7.place(x=300,y=100)
    tb8= Entry(delRec, width=25, font= ("times new roman", 14), fg="black")
    tb8.place(x=300,y=140)
    tb9= Entry(delRec, width=25, font= ("times new roman", 14), fg="black")
    tb9.place(x=300,y=180)
    tb10= Entry(delRec, width=25, font= ("times new roman", 14), fg="black")
    tb10.place(x=300,y=220)
    
    def delContact():
        if tb6.get()=='' and tb7.get()=='' and tb8.get()=='' and tb9.get()=='' and tb10.get()=='':
           messagebox.showerror('ERROR', "One of the Fields are required.")
        else:
           cursor.execute("delete from contact where id='{}' or name= '{}' or phone_number='{}' or email_address='{}' or address='{}'".format(tb6.get(),tb7.get(),tb8.get(),tb9.get(),tb10.get()))
           con.commit()
           cursor.execute("select * from contact")
           fetch=cursor.fetchall()
           contree.delete(*contree.get_children())
           for i in fetch:
               contree.insert('', END, values=i)

           def display_contactno():
               cursor.execute('select count(*) from contact')
               a=cursor.fetchall()
               for x in a:
                  for j in x:
                      k=j
               txt= 'Number of Saved Contacts: '+ str(k)
               label4.config(text=txt, bg='#ceb2fb', fg='white', font=('Times New Roman', 20, 'bold'))

           display_contactno()
           
           r= messagebox.askyesno('Delete Contact', "Contact Deleted. Would you like to delete more Contacts?")
           if r:
               tb6.delete(0,END)
               tb7.delete(0,END)
               tb8.delete(0,END)
               tb9.delete(0,END)
           else:
               delRec.destroy()

    b2= Button(delRec, text="DELETE CONTACT", width=20, command=delContact, font= ("times new roman", 16, "underline"), fg="black", bg="#e6d8fd")
    b2.place(x=150, y=250)

#---------update Contact subpage---------
def updateContact():
    uptRec= Toplevel()
    uptRec.geometry("600x300")
    uptRec.resizable(False,False)
    uptRec.title("Update Contacts")
    uptRec.configure(background="#e6d8fd")

    l10= Label(uptRec, text="UPDATE CONTACT", width=37, font= ("tahoma", 20, "bold"),fg="white", bg="#bf00ff")
    l10.place(x=0,y=10)

    l11= Label(uptRec, text="Select Particular to Update: ", font= ("times new roman", 14))
    l11.place(x=10,y=100)
    opt=['Select Column','Name', 'Phone_Number','Email_Address','Address']
    drop_one=StringVar(uptRec)
    drop_one.set(opt[0])
    drop= OptionMenu(uptRec, drop_one, *opt)
    drop.place(x=270, y=100)

    l12= Label(uptRec, text="Enter Contact ID:", font= ("times new roman", 14))
    l12.place(x=10,y=60)
    l13= Label(uptRec, text="Enter Updated Credentials:", font= ("times new roman", 14))
    l13.place(x=10,y=200)

    tb12= Entry(uptRec, width=25, font= ("times new roman", 14), fg="black")
    tb12.place(x=270,y=60)
    tb13= Entry(uptRec, width=25, font= ("times new roman", 14), fg="black")
    tb13.place(x=270,y=200)
    
    def uptContact():
        if tb12.get()=='' and tb13.get()=='':
           messagebox.showerror('ERROR', "The fields are required.")
        elif drop_one=='Select Column':
           messagebox.showerror('ERROR', "Column Dropdown Details not selected.")
        else:
           query = "update contact set {}= '{}' where id='{}' ".format(drop_one.get(),tb13.get(), tb12.get())
           cursor.execute(query)
           con.commit()
           
           cursor.execute("select * from contact")
           fetch=cursor.fetchall()
           contree.delete(*contree.get_children())
           for i in fetch:
               data_list= list(i)
               contree.insert('', END, values=i)

           def display_contactno():
               cursor.execute('select count(*) from contact')
               a=cursor.fetchall()
               for x in a:
                  for j in x:
                      k=j
               txt= 'Number of Saved Contacts: '+ str(k)
               label4.config(text=txt, bg='#ceb2fb', fg='white', font=('Times New Roman', 20, 'bold'))

           display_contactno()
           
           r= messagebox.askyesno('Update Contact', "Contact Updated. Would you like to update more Contacts?")
           if r:
               tb12.delete(0,END)
               tb13.delete(0,END)
               drop_one.set(options[0])
           else:
               uptRec.destroy()

    b3= Button(uptRec, text="UPDATE CONTACT", width=20, command=uptContact, font= ("times new roman", 16, "underline"), fg="black", bg="#e6d8fd")
    b3.place(x=150, y=250)

#---------search Contact subpage---------
def searchContact():
    seaRec= Toplevel()
    seaRec.geometry("600x300")
    seaRec.resizable(False,False)
    seaRec.title("Search Contacts")
    seaRec.configure(background="#e6d8fd")

    l15= Label(seaRec, text="SEARCH STOCK CONTACT", width=37, font= ("tahoma", 20, "bold"),fg="white", bg="#bf00ff")
    l15.place(x=0,y=10)

    l16= Label(seaRec, text="Name:", font= ("times new roman", 14))
    l16.place(x=10,y=60)
    l17= Label(seaRec, text="Phone Number:", font= ("times new roman", 14))
    l17.place(x=10,y=100)
    l18= Label(seaRec, text="Email Address:", font= ("times new roman", 14))
    l18.place(x=10,y=140)
    l19= Label(seaRec, text="Address:", font= ("times new roman", 14))
    l19.place(x=10,y=180)

    tb16= Entry(seaRec, width=25, font= ("times new roman", 14), fg="black")
    tb16.place(x=300,y=60)
    tb17= Entry(seaRec, width=25, font= ("times new roman", 14), fg="black")
    tb17.place(x=300,y=100)
    tb18= Entry(seaRec, width=25, font= ("times new roman", 14), fg="black")
    tb18.place(x=300,y=140)
    tb19= Entry(seaRec, width=25, font= ("times new roman", 14), fg="black")
    tb19.place(x=300,y=180)
    
    def seaContact():
        if tb16.get()=='' and tb17.get()=='' and tb18.get()=='' and tb19.get()=='':
           messagebox.showerror('ERROR', "Atleast One of the Fields is required.")
        else:
           if tb16.get():
                name_entry='%'+tb16.get()+'%'
                cursor.execute("select * from contact where name like '{}'".format(name_entry))
           elif tb17.get():
                phone_entry='%'+tb17.get()+'%'
                cursor.execute("select * from contact where phone_number like'{}'".format(phone_entry))
           elif tb18.get():
                email_entry='%'+tb18.get()+'%'
                cursor.execute("select * from contact where email_address like'{}'".format(email_entry))
           elif tb19.get():
                address_entry='%'+tb19.get()+'%'
                cursor.execute("select * from contact where address like'{}'".format(address_entry))
           fetched_data= cursor.fetchall()
           contree.delete(*contree.get_children())            
           for h in fetched_data:
                contree.insert('',"end", values=h)

           def display_contactno():
               cursor.execute('select count(*) from contact')
               a=cursor.fetchall()
               for x in a:
                  for j in x:
                      k=j
               txt= 'Number of Saved Contacts: '+ str(k)
               label4.config(text=txt, bg='#ceb2fb', fg='white', font=('Times New Roman', 20, 'bold'))

           display_contactno()
           
           r= messagebox.askyesno('Search Contact', "Contact Searched. Would you like to search more Contacts?")
           if r:
               tb16.delete(0,END)
               tb17.delete(0,END)
               tb18.delete(0,END)
               tb19.delete(0,END)
           else:
               seaRec.destroy()
    b4= Button(seaRec, text="SEARCH CONTACT", width=20, command=seaContact, font= ("times new roman", 16, "underline"), fg="black", bg="#e6d8fd")
    b4.place(x=150, y=250)
    
#---------sort record subpage---------
def sortContact():
    sortRec= Toplevel()
    sortRec.geometry("600x300")
    sortRec.title("Sort Records")
    sortRec.configure(background="#e6d8fd")

    l28= Label(sortRec, text="SORT CONTACTS", width=37, font= ("tahoma", 20, "bold"),fg="white", bg="#bf00ff")
    l28.place(x=0,y=10)

    l29= Label(sortRec, text="Select Column to sort by: ", font= ("times new roman", 14))
    l29.place(x=10,y=100)
    options=['Select Column','ID','Name', 'Phone_Number','Email_Address','Address']
    drop_one1=StringVar(sortRec)
    drop_one1.set(options[0])
    drop= OptionMenu(sortRec, drop_one1, *options)
    drop.place(x=270, y=100)
    
    l30= Label(sortRec, text="Order: ", font= ("times new roman", 14), fg="black")
    l30.place(x=20, y=150)
    
    radio_one= StringVar()
    radio_one.set("Ascending")
    radio_button1= Radiobutton(sortRec, text="Ascending", value="Ascending", variable=radio_one) 
    radio_button1.place(x=250 ,y=150)
    radio_button2= Radiobutton(sortRec, text="Descending", value="Descending", variable=radio_one) 
    radio_button2.place(x=350 ,y=150)

    l31= Label(sortRec, font= ("times new roman", 14), fg="black")
    l31.place(x=100,y=200)
    def radio_select():
        select_option= radio_one.get()
        l31.config(text= select_option)
    radio_button1.config(command=radio_select)
    radio_button2.config(command=radio_select)
    
    def sortingContact():
        if drop_one1.get()=='Select Column':
           messagebox.showerror('ERROR', "Column to Update not selected.")
        else:
            if radio_one.get() == "Ascending":
                order_by = "ASC"
            else:
                order_by = "DESC"
            query = "SELECT * FROM contact ORDER BY `{}` {}".format(drop_one1.get(), order_by)
            cursor.execute(query)
            data=cursor.fetchall()
            contree.delete(*contree.get_children())
            for p in data:
               contree.insert('',"end", values=p)

        def display_contactno():
               cursor.execute('select count(*) from contact')
               a=cursor.fetchall()
               for x in a:
                  for j in x:
                      k=j
               txt= 'Number of Saved Contacts: '+ str(k)
               label4.config(text=txt, bg='#ceb2fb', fg='white', font=('Times New Roman', 20, 'bold'))

        display_contactno()
           
        messagebox.showinfo('Sort Records', "Records are sorted successfully")
        sortRec.destroy()
        
    b5= Button(sortRec, text="SORT RECORD", width=20, command=sortingContact, font= ("times new roman", 16, "underline"), fg="black", bg="#61b1f7")
    b5.place(x=150, y=250)

#-------------exit message-------------
def exit():
    abc= messagebox.askyesno('Want to Exit?',"Are you sure you want to exit?")
    if abc:
        messagebox.showinfo('Thank You!','Thank You!')
        book.destroy()

#-----------command menu-----------------
frame1= Frame(book, bd=2, relief=RIDGE)
frame1.place(x=20,y=80,width=200,height=520)
label2= Label(frame1, text="MENU", font=("times new roman", 24, "bold"),bg="#9f00ff", fg="white").pack(side=TOP, fill=X)    

ima2= Image.open("D:\\PYTHON PROJECTS\\8643765.png")
reima2= ima2.resize((200,115))
img2=ImageTk.PhotoImage(reima2)
panel2= Label(frame1, image= img2).pack(side=TOP, fill=X)
    
button2= Button(frame1, text='''ADD CONTACT''', command=insertContact, font=("times new roman", 16, "bold"), bg="#bf00ff", fg="white", bd=3, cursor="hand2").pack(side=TOP, fill=X)
button3= Button(frame1, text='''DELETE
CONTACT''', command=deleteContact, font= ("times new roman", 16, "bold"), bg="#bf00ff", fg="white", bd=3, cursor="hand2").pack(side=TOP, fill=X)
button4= Button(frame1, text='''UPDATE
CONTACT''', command=updateContact, font= ("times new roman", 16, "bold"), bg="#bf00ff", fg="white", bd=3, cursor="hand2").pack(side=TOP, fill=X)
button5= Button(frame1, text='''SEARCH
CONTACT''', command=searchContact, font= ("times new roman", 16, "bold"), bg="#bf00ff", fg="white", bd=3, cursor="hand2").pack(side=TOP, fill=X)
button6= Button(frame1, text='''SORT
CONTACT''', command=sortContact, font= ("times new roman", 16, "bold"), bg="#bf00ff", fg="white", bd=3, cursor="hand2").pack(side=TOP, fill=X)
button7= Button(frame1, text='''LOGOUT''', command=exit, font= ("times new roman", 16, "bold"), bg="#bf00ff", fg="white", bd=3, cursor="hand2").pack(side=TOP, fill=X)

    













book.mainloop()
