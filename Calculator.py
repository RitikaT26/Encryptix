from tkinter import *

cal= Tk()
cal.title('Calculator')
cal.geometry('260x280')
cal.resizable(False,False)
cal.config(background='grey')

#------commands-------
exp=' '
def press(no):
    global exp
    exp += str(no)
    eq.set(exp)
    
def equal():
    global exp
    tot= eval(exp)
    total= str(tot)
    eq.set(tot)

def clear():
    global exp
    exp=' '
    eq.set(exp)
    
#-------heading-------
head= Label(cal, text='    CALCULATOR     ',anchor='center', font=('times new roman',20,'bold'), fg='#230C98')
head.place(x=0,y=0)

#-------textbox-------
eq= StringVar()
text= Entry(cal,textvariable=eq, width=39)
text.place(x=10,y=50)

#-------buttons-------
b1= Button(cal, text='1',font=('times new roman', 14), fg='white', bg='blue', command=lambda:press(1), height=1, width=5)
b1.place(x=10,y=80)
b2= Button(cal, text='2',font=('times new roman', 14), fg='white', bg='blue', command=lambda:press(2), height=1, width=5)
b2.place(x=70,y=80)
b3= Button(cal, text='3',font=('times new roman', 14), fg='white', bg='blue', command=lambda:press(3), height=1, width=5)
b3.place(x=130,y=80)
b4= Button(cal, text='4',font=('times new roman', 14), fg='white', bg='blue', command=lambda:press(4), height=1, width=5)
b4.place(x=10,y=118)
b5= Button(cal, text='5',font=('times new roman', 14), fg='white', bg='blue', command=lambda:press(5), height=1, width=5)
b5.place(x=70,y=118)
b6= Button(cal, text='6',font=('times new roman', 14), fg='white', bg='blue', command=lambda:press(6), height=1, width=5)
b6.place(x=130,y=118)
b7= Button(cal, text='7',font=('times new roman', 14), fg='white', bg='blue', command=lambda:press(7), height=1, width=5)
b7.place(x=10,y=156)
b8= Button(cal, text='8',font=('times new roman', 14), fg='white', bg='blue', command=lambda:press(8), height=1, width=5)
b8.place(x=70,y=156)
b9= Button(cal, text='9',font=('times new roman', 14), fg='white', bg='blue', command=lambda:press(9), height=1, width=5)
b9.place(x=130,y=156)
b0= Button(cal, text='0',font=('times new roman', 14), fg='white', bg='blue', command=lambda:press(0), height=1, width=5)
b0.place(x=10,y=194)
bplus= Button(cal, text='+',font=('times new roman', 14), fg='white', bg='blue', command=lambda:press('+'), height=1, width=5)
bplus.place(x=190,y=194)
bminus= Button(cal, text='-',font=('times new roman', 14), fg='white', bg='blue', command=lambda:press('-'), height=1, width=5)
bminus.place(x=190,y=156)
bmultiply= Button(cal, text='*',font=('times new roman', 14), fg='white', bg='blue', command=lambda:press('*'), height=1, width=5)
bmultiply.place(x=190,y=118)
bdivide= Button(cal, text='/',font=('times new roman', 14), fg='white', bg='blue', command=lambda:press('/'), height=1, width=5)
bdivide.place(x=190,y=80)
bequal= Button(cal, text='=',font=('times new roman', 14), fg='white', bg='blue', command=equal, height=1, width=5)
bequal.place(x=190,y=232)
bdecimal= Button(cal, text='.',font=('times new roman', 14), fg='white', bg='blue', command=lambda:press('.'), height=1, width=5)
bdecimal.place(x=70,y=194)
bopen= Button(cal, text='(',font=('times new roman', 14), fg='white', bg='blue', command=lambda:press('('), height=1, width=5)
bopen.place(x=130,y=194)
bclose= Button(cal, text=')',font=('times new roman', 14), fg='white', bg='blue', command=lambda:press(')'), height=1, width=5)
bclose.place(x=130,y=232)
bclear= Button(cal, text='CLEAR',font=('times new roman', 14), fg='white', bg='blue', command=clear, height=1, width=7)
bclear.place(x=10,y=232)


cal.mainloop()
