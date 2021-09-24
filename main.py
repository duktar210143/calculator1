from tkinter import*
root=Tk()
root.title("calculator")
root.iconbitmap('cal.ico')
root.configure(bg="grey")
root.geometry("290x490")
#abcdefg gandu

e=Entry(root, width=40, borderwidth=9,bg="light grey",fg="black")
e.grid(row=0, column=0, columnspan=3, padx=10, pady=10)
#function for arithmetic task
def button_click(number):
    current=e.get()
    e.delete(0,END)
    e.insert(0,str(current)+str(number))
def button_clear():
    e.delete(0,END)
def button_add():
    first_number=e.get()
    global f_num
    global math
    math="addition"
    f_num=int(first_number)
    e.delete(0,END)
def button_multiply():
    first_number = e.get()
    global f_num
    global math
    math = "multiplication"
    f_num = int(first_number)
    e.delete(0, END)
def button_subtract():
    first_number = e.get()
    global f_num
    global math
    math = "subtraction"
    f_num = int(first_number)
    e.delete(0, END)
def button_division():
    first_number = e.get()
    global f_num
    global math
    math = "division"
    f_num = int(first_number)
    e.delete(0, END)
def button_power2():
    first_number = e.get()
    global f_num
    global math
    math = "squaring"
    f_num = int(first_number)
    e.delete(0, END)
def button_squareroot():
    first_number=e.get()
    global f_num
    global math
    math = "2root"
    f_num = int(first_number)
    e.delete(0, END)
def button_cuberoot():
    first_number=e.get()
    global f_num
    global math
    math = "3root"
    f_num = int(first_number)
    e.delete(0, END)

def button_equal():
    second_number=e.get()
    e.delete(0,END)
    if math=="addittion":
        e.insert(0,f_num+int(second_number))
    elif math=="subtraction":
        e.insert(0,f_num-int(second_number))
    elif math=="multiplication":
        e.insert(0,f_num*int(second_number))
    elif math=="division":
        e.insert(0,f_num/int(second_number))
    elif math=="2root":
        e.insert(0,f_num**0.5)
    elif math=="3root":
        e.insert(0,f_num**(1/3))
    else :
        e.insert(0,f_num**int(second_number))


#Define Button size
button1=Button(root,text="1",padx=40,pady=20,bg="grey",fg="white",command=lambda:button_click(1))
button2=Button(root,text="2",padx=40,pady=20,bg="grey",fg="white",command=lambda:button_click(2))
button3=Button(root,text="3",padx=40,pady=20,bg="grey",fg="white",command=lambda:button_click(3))
button4=Button(root,text="4",padx=40,pady=20,bg="grey",fg="white",command=lambda:button_click(4))
button5=Button(root,text="5",padx=40,pady=20,bg="grey",fg="white",command=lambda:button_click(5))
button6=Button(root,text="6",padx=40,pady=20,bg="grey",fg="white",command=lambda:button_click(6))
button7=Button(root,text="7",padx=40,pady=20,bg="grey",fg="white",command=lambda:button_click(7))
button8=Button(root,text="8",padx=40,pady=20,bg="grey",fg="white",command=lambda:button_click(8))
button9=Button(root,text="9",padx=40,pady=20,bg="grey",fg="white",command=lambda:button_click(9))
button0=Button(root,text="0",padx=40,pady=20,bg="grey",fg="white",command=lambda:button_click(0))
button_add=Button(root,text="+",padx=39,pady=20,bg="grey",fg="white",command=button_add)
button_equal=Button(root,text="=",padx=88,pady=20,bg="blue",fg="white",command=button_equal)
button_clear=Button(root,text="clear",padx=79,pady=20,bg="blue",fg="white",command=button_clear)
button_subtract=Button(root,text="-",padx=40,pady=20,bg="grey",fg="white",command=button_subtract)
button_multipy=Button(root,text="*",padx=39,pady=20,bg="grey",fg="white",command=button_multiply)
button_division=Button(root,text="/",padx=42,pady=20,bg="grey",fg="white",command=button_division)
button_power2=Button(root,text="^",padx=39,pady=20,bg="grey",fg="white",command=button_power2)
button_squareroot=Button(root,text="sq_root",padx=21,pady=20,bg="grey",fg="white",command=button_squareroot)
button_cuberoot=Button(root,text="cub_root",padx=18,pady=20,bg="grey",fg="white",command=button_cuberoot)

#button postion on the screen
button1.grid(row=3,column=0)
button2.grid(row=3,column=1)
button3.grid(row=3,column=2)

button4.grid(row=2,column=0)
button5.grid(row=2,column=1)
button6.grid(row=2,column=2)

button7.grid(row=1,column=0)
button8.grid(row=1,column=1)
button9.grid(row=1,column=2)
button_squareroot.grid(row=6,column=0)
button_equal.grid(row=6,column=1,columnspan=2)
button_cuberoot.grid(row=7,column=0)
button_clear.grid(row=7,column=1,columnspan=2)


button0.grid(row=4,column=0)
button_add.grid(row=4,column=1)
button_subtract.grid(row=4,column=2)
button_multipy.grid(row=5,column=0)
button_division.grid(row=5,column=1)
button_power2.grid(row=5,column=2)
root.mainloop()
