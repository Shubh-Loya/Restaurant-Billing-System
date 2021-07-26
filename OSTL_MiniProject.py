from tkinter import*
import random
import time

root = Tk()
root.geometry("1100x700+150+5")
root.title("Restaurant Billing System")

Tops = Frame(root,width = 900,height=50)
Tops.pack(side=TOP)

f1 = Frame(root,width=1600,height=700)
f1.pack(side=LEFT)
#------------------TIME--------------
localtime=time.asctime(time.localtime(time.time()))
#-----------------INFO TOP------------
lblinfo = Label(Tops, font=( 'aria' ,30, 'bold' ),text="Restaurant Billing System",fg="steel blue",bd=45)
lblinfo.grid(row=0,column=0)
lblinfo = Label(Tops, font=( 'aria' ,20, ),text=localtime,fg="steel blue")
lblinfo.grid(row=1,column=0)
#---------------ALGEBRAIC CALCULATION------------------
text_Input=StringVar()
operator =""


def Ref():
    x=random.randint(1,100)
    randomRef = str(x)
    rand.set(randomRef)

    cof =float(Fries.get())
    colfries= float(Largefries.get())
    cob= float(Burger.get())
    cofi= float(Filet.get())
    cochee= float(Cheese_burger.get())
    codr= float(Drinks.get())

    costoffries = cof*25
    costoflargefries = colfries*40
    costofburger = cob*35
    costoffilet = cofi*50
    costofcheeseburger = cochee*50
    costofdrinks = codr*35

    costofmeal = str('%.2f'% (costoffries +  costoflargefries + costofburger + costoffilet + costofcheeseburger + costofdrinks))
   
    PayTax=((costoffries +  costoflargefries + costofburger + costoffilet +  costofcheeseburger + costofdrinks)*0.33)
    Totalcost=(costoffries +  costoflargefries + costofburger + costoffilet  + costofcheeseburger + costofdrinks)
    Ser_Charge=((costoffries +  costoflargefries + costofburger + costoffilet + costofcheeseburger + costofdrinks)/99)
    Service=str('%.2f'% Ser_Charge)
   
    OverAllCost= str('%.2f' % (PayTax + Totalcost + Ser_Charge))
   
    PaidTax= str('%.2f'% PayTax)

    Service_Charge.set(Service)
    cost.set(costofmeal)
    Tax.set(PaidTax)
    Subtotal.set(costofmeal)
    Total.set(OverAllCost)

def qexit():
    root.destroy()

def reset():
    rand.set("")
    Fries.set("")
    Largefries.set("")
    Burger.set("")
    Filet.set("")
    Subtotal.set("")
    Total.set("")
    Service_Charge.set("")
    Drinks.set("")
    Tax.set("")
    cost.set("")
    Cheese_burger.set("")
#---------------------------------------------------------------------------------------
rand = StringVar()
Fries = StringVar()
Largefries = StringVar()
Burger = StringVar()
Filet = StringVar()
Subtotal = StringVar()
Total = StringVar()
Service_Charge = StringVar()
Drinks = StringVar()
Tax = StringVar()
cost = StringVar()
Cheese_burger = StringVar()

lblreference = Label(f1, font=( 'aria' ,16, 'bold' ),text="Order No.",fg="steel blue",bd=10)
lblreference.grid(row=0,column=0)
lblreference = Label(f1,font=('ariel' ,16,'bold'), textvariable=rand ,width=12, bd=4,fg="black")
lblreference.grid(row=0,column=1)

lblfries = Label(f1, font=( 'aria' ,16, 'bold' ),text="Fries Meal",fg="steel blue",bd=10)
lblfries.grid(row=1,column=0)
txtfries = Entry(f1,font=('ariel' ,16,'bold'), textvariable=Fries ,width=12, bd=4,bg="powder blue" ,justify='right')
txtfries.grid(row=1,column=1)


lblLargefries = Label(f1, font=( 'aria' ,16, 'bold' ),text="Lunch Meal",fg="steel blue",bd=10)
lblLargefries.grid(row=2,column=0)
txtLargefries = Entry(f1,font=('ariel' ,16,'bold'), textvariable=Largefries ,width=12, bd=4,bg="powder blue" ,justify='right')
txtLargefries.grid(row=2,column=1)


lblburger = Label(f1, font=( 'aria' ,16, 'bold' ),text="Burger Meal",fg="steel blue",bd=10)
lblburger.grid(row=3,column=0)
txtburger = Entry(f1,font=('ariel' ,16,'bold'), textvariable=Burger ,width=12, bd=4,bg="Powder blue" ,justify='right')
txtburger.grid(row=3,column=1)


lblFilet = Label(f1, font=( 'aria' ,16, 'bold' ),text="Pizza Meal",fg="steel blue",bd=10)
lblFilet.grid(row=4,column=0)
txtFilet = Entry(f1,font=('ariel' ,16,'bold'), textvariable=Filet ,width=12, bd=4,bg="powder blue" ,justify='right')
txtFilet.grid(row=4,column=1)


lblCheese_burger = Label(f1, font=( 'aria' ,16, 'bold' ),text="Cheese burger",fg="steel blue",bd=10)
lblCheese_burger.grid(row=5,column=0)
txtCheese_burger = Entry(f1,font=('ariel' ,16,'bold'), textvariable=Cheese_burger ,width=12, bd=4,bg="powder blue" ,justify='right')
txtCheese_burger.grid(row=5,column=1)

lblDrinks = Label(f1, font=( 'aria' ,16, 'bold' ),text="Drinks",fg="steel blue",bd=10)
lblDrinks.grid(row=6,column=0)
txtDrinks = Entry(f1,font=('ariel' ,16,'bold'), textvariable=Drinks ,width=12, bd=4,bg="powder blue" ,justify='right')
txtDrinks.grid(row=6,column=1)

#-----------------------------------------------------------------------------------------------------------------------------

lblcost = Label(f1, font=( 'aria' ,16, 'bold' ),text="Cost",fg="steel blue",bd=10)
lblcost.grid(row=1,column=3)
lblcost = Label(f1,font=('ariel' ,16,'bold'), textvariable=cost , bd=6,fg="black")
lblcost.grid(row=1,column=4)

lblService_Charge = Label(f1, font=( 'aria' ,16, 'bold' ),text="Service Charge",fg="steel blue",bd=10)
lblService_Charge.grid(row=2,column=3)
lblreference = Label(f1,font=('ariel' ,16,'bold'), textvariable=Service_Charge , bd=6,fg="black")
lblreference.grid(row=2,column=4)

lblTax = Label(f1, font=( 'aria' ,16, 'bold' ),text="Tax",fg="steel blue",bd=10)
lblTax.grid(row=3,column=3)
lblreference = Label(f1,font=('ariel' ,16,'bold'), textvariable=Tax , bd=6,fg="black")
lblreference.grid(row=3,column=4)

lblSubtotal = Label(f1, font=( 'aria' ,16, 'bold' ),text="Subtotal",fg="steel blue",bd=10)
lblSubtotal.grid(row=4,column=3)
lblreference = Label(f1,font=('ariel' ,16,'bold'), textvariable=Subtotal , bd=6,fg="black")
lblreference.grid(row=4,column=4)

lblTotal = Label(f1, font=( 'aria' ,16, 'bold' ),text="Total",fg="steel blue",bd=10)
lblTotal.grid(row=5,column=3)
lblreference = Label(f1,font=('ariel' ,16,'bold'), textvariable=Total , bd=6,fg="black")
lblreference.grid(row=5,column=4)

#-----------------------------------------BUTTONS------------------------------------------

btnTotal=Button(f1,padx=16,pady=8, bd=10 ,fg="black",font=('ariel' ,16,'bold'),width=10, text="TOTAL", bg="powder blue",command=Ref)
btnTotal.grid(row=10, column=1)


btnreset=Button(f1,padx=16,pady=8, bd=10 ,fg="black",font=('ariel' ,16,'bold'),width=10, text="RESET", bg="powder blue",command=reset)
btnreset.grid(row=10, column=3)

btnexit=Button(f1,padx=16,pady=8, bd=10 ,fg="black",font=('ariel' ,16,'bold'),width=10, text="EXIT", bg="powder blue",command=qexit)
btnexit.grid(row=10, column=4)

def price():
    roo = Tk()
    roo.geometry("600x220+0+0")
    roo.title("Price List")
    lblinfo = Label(roo, font=('aria', 15, 'bold'), text="ITEM", fg="black", bd=5)
    lblinfo.grid(row=0, column=0)
    lblinfo = Label(roo, font=('aria', 15, 'bold'), text="PRICE", fg="black")
    lblinfo.grid(row=0, column=3)
    lblinfo = Label(roo, font=('aria', 15, 'bold'), text="Fries Meal", fg="steel blue")
    lblinfo.grid(row=1, column=0)
    lblinfo = Label(roo, font=('aria', 15, 'bold'), text="25", fg="steel blue")
    lblinfo.grid(row=1, column=3)
    lblinfo = Label(roo, font=('aria', 15, 'bold'), text="Lunch Meal", fg="steel blue")
    lblinfo.grid(row=2, column=0)
    lblinfo = Label(roo, font=('aria', 15, 'bold'), text="40", fg="steel blue")
    lblinfo.grid(row=2, column=3)
    lblinfo = Label(roo, font=('aria', 15, 'bold'), text="Burger Meal", fg="steel blue")
    lblinfo.grid(row=3, column=0)
    lblinfo = Label(roo, font=('aria', 15, 'bold'), text="35", fg="steel blue")
    lblinfo.grid(row=3, column=3)
    lblinfo = Label(roo, font=('aria', 15, 'bold'), text="Pizza Meal", fg="steel blue")
    lblinfo.grid(row=4, column=0)
    lblinfo = Label(roo, font=('aria', 15, 'bold'), text="50", fg="steel blue")
    lblinfo.grid(row=4, column=3)
    lblinfo = Label(roo, font=('aria', 15, 'bold'), text="Cheese Burger", fg="steel blue")
    lblinfo.grid(row=5, column=0)
    lblinfo = Label(roo, font=('aria', 15, 'bold'), text="30", fg="steel blue")
    lblinfo.grid(row=5, column=3)
    lblinfo = Label(roo, font=('aria', 15, 'bold'), text="Drinks", fg="steel blue")
    lblinfo.grid(row=6, column=0)
    lblinfo = Label(roo, font=('aria', 15, 'bold'), text="35", fg="steel blue")
    lblinfo.grid(row=6, column=3)

    roo.mainloop()

btnprice=Button(f1,padx=16,pady=8, bd=10 ,fg="black",font=('ariel' ,16,'bold'),width=10, text="PRICE", bg="powder blue",command=price)
btnprice.grid(row=10, column=0)

def bill():
    ro=Tk()
    ro.geometry("700x500")
    ro.title("Bill")

    q1 =Fries.get()
    q2= Largefries.get()
    q3= Burger.get()
    q4= Filet.get()
    q5= Cheese_burger.get()
    q6= Drinks.get()
    q7=rand.get()
    t1=cost.get()
    t2=Service_Charge.get()
    t3=Tax.get()
    t4=Subtotal.get()
    t5=Total.get()

    lblinfo = Label(ro, font=( 'aria' ,15, 'bold' ),text=" ***ORDER",fg="steel blue",bd=5)
    lblinfo.grid(row=0,column=2)
    lblinfo = Label(ro, font=( 'aria' ,15, 'bold' ),text="NO.  {} ***".format(q7),fg="steel blue",bd=5)
    lblinfo.grid(row=0,column=3)
    lblinfo = Label(ro, font=('aria', 15, 'bold'), text="ITEM", fg="black", bd=5)
    lblinfo.grid(row=1, column=0)
    lblinfo = Label(ro, font=('aria', 15, 'bold'), text="QUANTITY", fg="black")
    lblinfo.grid(row=1, column=3)
    lblinfo = Label(ro, font=('aria', 15, 'bold'), text="AMOUNT", fg="black")
    lblinfo.grid(row=1, column=5)
    #-----------------------------------------------------------------------------------------
    #Item Column
    lblinfo = Label(ro, font=('aria', 15, 'bold'), text="Fries Meal", fg="black")
    lblinfo.grid(row=2, column=0)
    lblinfo = Label(ro, font=('aria', 15, 'bold'), text="Lunch Meal", fg="black")
    lblinfo.grid(row=3, column=0)
    lblinfo = Label(ro, font=('aria', 15, 'bold'), text="Burger Meal", fg="black")
    lblinfo.grid(row=4, column=0)
    lblinfo = Label(ro, font=('aria', 15, 'bold'), text="Pizza Meal", fg="black")
    lblinfo.grid(row=5, column=0)
    lblinfo = Label(ro, font=('aria', 15, 'bold'), text="Cheeseburger", fg="black")
    lblinfo.grid(row=6, column=0)
    lblinfo = Label(ro, font=('aria', 15, 'bold'), text="Drinks", fg="black")
    lblinfo.grid(row=7, column=0)
#------------------------------------------------------------------------------------------------
    #Quantity Column
    lblinfo = Label(ro, font=('aria', 15, 'bold'), text="{}".format(q1),fg="black")
    lblinfo.grid(row=2, column=3)
    lblinfo = Label(ro, font=('aria', 15, 'bold'), text="{}".format(q2),fg="black")
    lblinfo.grid(row=3, column=3)
    lblinfo = Label(ro, font=('aria', 15, 'bold'), text="{}".format(q3),fg="black")
    lblinfo.grid(row=4, column=3)
    lblinfo = Label(ro, font=('aria', 15, 'bold'), text="{}".format(q4),fg="black")
    lblinfo.grid(row=5, column=3)
    lblinfo = Label(ro, font=('aria', 15, 'bold'), text="{}".format(q5), fg="black")
    lblinfo.grid(row=6, column=3)
    lblinfo = Label(ro, font=('aria', 15, 'bold'), text="{}".format(q6), fg="black")
    lblinfo.grid(row=7, column=3)
#--------------------------------------------------------------------------------------------------
    #Amount List Column
    c1=int(q1)
    c2=int(q2)
    c3=int(q3)
    c4=int(q4)
    c5=int(q5)
    c6=int(q6)
    c1=c1*25
    c2=c2*40
    c3=c3*35
    c4=c4*50
    c5=c5*30
    c6=c6*35

    lblinfo = Label(ro, font=('aria', 15, 'bold'), text=c1, fg="black")
    lblinfo.grid(row=2, column=5)
    lblinfo = Label(ro, font=('aria', 15, 'bold'), text= c2, fg="black")
    lblinfo.grid(row=3, column=5)
    lblinfo = Label(ro, font=('aria', 15, 'bold'), text=c3, fg="black")
    lblinfo.grid(row=4, column=5)
    lblinfo = Label(ro, font=('aria', 15, 'bold'), text=c4, fg="black")
    lblinfo.grid(row=5, column=5)
    lblinfo = Label(ro, font=('aria', 15, 'bold'), text=c5, fg="black")
    lblinfo.grid(row=6, column=5)    
    lblinfo = Label(ro, font=('aria', 15, 'bold'), text=c6, fg="black")
    lblinfo.grid(row=7, column=5)
    lblinfo = Label(ro, font=('aria', 15, 'bold'), text="-----------------", fg="black")
    lblinfo.grid(row=8, column=5)
    lblinfo = Label(ro, font=('aria', 15, 'bold'), text="Cost: Rs {}".format(t1), fg="black")
    lblinfo.grid(row=9, column=5)
    lblinfo = Label(ro, font=('aria', 15, 'bold'), text="Service Charge: Rs {}".format(t2), fg="black")
    lblinfo.grid(row=10, column=5)
    lblinfo = Label(ro, font=('aria', 15, 'bold'), text="Tax: Rs {}".format(t3), fg="black")
    lblinfo.grid(row=11, column=5)
    lblinfo = Label(ro, font=('aria', 15, 'bold'), text="Subtotal: Rs {}".format(t4), fg="black")
    lblinfo.grid(row=12, column=5)
    lblinfo = Label(ro, font=('aria', 15, 'bold'), text="Total: Rs {}".format(t5), fg="black")
    lblinfo.grid(row=13, column=5)
    lblinfo = Label(ro, font=('italic', 15, 'bold'), text="THANK YOU!", fg="black")
    lblinfo.grid(row=16, column=3)
    ro.mainloop()

btnBill=Button(f1,padx=16,pady=8, bd=10 ,fg="black",font=('ariel' ,16,'bold'),width=10, text="BILL", bg="powder blue",command=bill)
btnBill.grid(row=10, column=2)

root.mainloop()
