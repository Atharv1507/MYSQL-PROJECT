from tkinter import *
import mysql.connector as mc

y=mc.connect(host='localhost',user='root',password='Atharv123',database='hospital' )

global table
global Isrun

Isrun=True
valid=True

tables=["emp","patients","stock"]
pkeys={'emp':'emp_no','patients':'pId','stock':'Icode'}
fkeys={'emp':'emp_no','patients':'doc'}



def check():
    global tab,table
    table=tab.get().lower()
    print(table)
    while table in tables and Isrun==True:
        Table_Select.destroy() 
        main()
        break

    else:
        print("No such table")
        y.close()
    
Table_Select=Tk()
Table_Select.geometry("200x200")
Avail=Label(text=tables)
Table_Select.title("Table select")
tab=Entry(Table_Select,width=10)
Enter=Button(Table_Select,text="Submit",command=check)
tab.pack()
Avail.pack()
Enter.pack()
def addData():
    pass
def DelData():
    pass
def AlterData():
    pass
def Select():
    pass
def main():
    global CurTab
    Main_menu=Tk()
    Main_menu.title("Main menu")
    CurTab=Label(Main_menu,text="Current working table:"+table,padx=10,pady=20)
    CurTab.pack()
    b1=Button(Main_menu,pady=10,padx=20,text="Add data",command=addData)
    b2=Button(Main_menu,pady=10,padx=20,text="Delete data",command=DelData)
    b3=Button(Main_menu,pady=10,padx=20,text="Alter Data",command=AlterData)
    b4=Button(Main_menu,pady=10,padx=20,text="Select Data",command=Select)
    b5=Button(Main_menu,pady=10,padx=20,text="Quit",command=Main_menu.destroy)
    b1.pack()
    b2.pack()
    b3.pack()
    b4.pack()
    b5.pack()
    '''
    CurTab.grid(row=0,column=0,columnspan=3)
    b1.grid(column=0,row=1)
    b2.grid(column=1,row=1)
    b3.grid(column=2,row=1)
    b4.grid(column=0,row=2)
    b5.grid(column=1,row=2) 
    '''
    
    '''
    print('Available function are:\n 1.Add\n 2.Delete\n 3.alter data\n 4.Select\n 5.Quit\n 6.Change Table')
    ch=int(input('enter function to perform:'))
    if ch==1:
        addData()

    if ch==2:
        deleteData()
    if ch==3:
        alterData()
    if ch==4:
        select()
    if ch==5:
        global Isrun
        Isrun=False
    if ch==6:
        print("available tables are ",tables)
        table=input('Enter name of the table:').lower()


'''
mainloop()