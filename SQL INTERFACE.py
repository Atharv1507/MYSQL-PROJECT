from tkinter import *
import mysql.connector as mc

y=mc.connect(host='localhost',user='root',password='Atharv123',database='hospital' )

global table
global Isrun
Isrun=True
tables=["emp","patients","stock"]
pkeys={'emp':'emp_no','patients':'pId','stock':'Icode'}
fkeys={'emp':'emp_no','patients':'doc','stock':'issued'}

def fetcher(wid):
    global data
    data=wid.get()

def searchKey():
    global sk_E
    Label(text="Enter "+pkeys[table]+":").pack()
    sk_E=Entry(Entry_Menu)
    sk_E.pack()

def fetchall(TbN):
    # shows all records
    global ids
    db = y.cursor()
    query=("select * from " +TbN)
    db.execute(query)
    actualrec=db.fetchall()
    count=db.rowcount
    ids=[]
    Label(Entry_Menu,text="total records are:"+str(count)).pack()
    for z in actualrec:
        ids.append(z[0])
        Label(text=z).pack()
    return ids

def fetchcol(TbN):
    global col
    # shows only column names
    db = y.cursor()
    query=("show columns from " +TbN)
    db.execute(query)
    col=[]
    actualrec=db.fetchall()
    print('available columns are')
    for z in actualrec:
        col.append(z[0])
        Label(text=z[0]).pack()
    return col

def Destroyer(window):
    window.destroy()

def entryMenu():
    global Entry_Menu
    Destroyer(Main_menu)
    Entry_Menu=Tk()

def goBackToMenu(win):
    Destroyer(win)
    main()


def check():
    global table
    table=tab.get().lower()
    while table in tables and Isrun==True:
        Destroyer(Table_Select) 
        main()
        break
    else:
        Label(text="No such table").pack()


global Table_Select,tab
Table_Select=Tk()
Table_Select.geometry("200x200")
Avail=Label(Table_Select,text=tables)
Table_Select.title("Table select")
tab=Entry(Table_Select,width=10)
Enter=Button(Table_Select,text="Submit",command=check)
tab.pack()
Avail.pack()
Enter.pack()

def main():
    global CurTab,Main_menu
    Main_menu=Tk()
    Main_menu.title("Main menu")
    CurTab=Label(Main_menu,text="Current working table:"+table,padx=10,pady=20)
    CurTab.pack()
    b1=Button(Main_menu,pady=10,padx=20,text="Add Data",command=addData)
    b2=Button(Main_menu,pady=10,padx=20,text="Delete Data",command=DelData)
    b3=Button(Main_menu,pady=10,padx=20,text="Alter Data",command=AlterData)
    b4=Button(Main_menu,pady=10,padx=20,text="Select Data",command=Select)
    b5=Button(Main_menu,pady=10,padx=20,text="Quit",command=Main_menu.destroy)
    b1.pack()
    b2.pack()
    b3.pack()
    b4.pack()
    b5.pack()

def Adder():
    y=mc.connect(host='localhost',user='root',password='Atharv123',database='hospital' )
    if table=='emp':
        empno=empno_E.get()
        sal=sal_E.get()
        spec=spec_E.get()
        name=name_E.get()
        db = y.cursor()
        q = "insert into "+table+" values('"+empno+"','"+name+"','"+spec+"',"+sal+");"
        try:
            db.execute(q)
            y.commit()
            Label(text="Record inserted").pack()        
            subButton.config(state=DISABLED)

        except:
            y.rollback()
            Label(text="Please check the data entered").pack()

      

    if table=='patients':
        pId=pId_E.get()
        doc=doc_E.get()
        doj=doj_E.get()
        room_no=room_no_E.get()
        Pname=Pname_E.get()
        db = y.cursor()
        q = "insert into "+table+" values('"+pId+"','"+Pname+"','"+doc+"',"+room_no+",'"+doj+"');"
        try:
            db.execute(q)
            y.commit()
            Label(text="Record inserted").pack()        
            subButton.config(state=DISABLED)

        except:
            y.rollback()
            Label(text="Please check the data entered").pack()

    if table=='stock':        
        Icode=Icode_E.get()
        Iname=Iname_E.get()
        exp=Expiration_E.get()
        issued=issued_E.get()
        
        db = y.cursor()
        q = "insert into "+table+" values('"+Icode+"','"+Iname+"','"+exp+"','"+issued+"');"
        try:
            db.execute(q)
            y.commit()
            subButton.config(state=DISABLED)
            Label(text="Record inserted").pack()        

        except:
            y.rollback()
            Label(text="Please check the data entered").pack()
def addData():
    
    entryMenu()
    Entry_Menu.title("Adding Data")
    
    if table=='emp':
        global empno_E, name_E,sal_E,spec_E,subButton

        Label(Entry_Menu,text="Enter EmpNo",padx=10,pady=10).pack()
        empno_E=Entry(Entry_Menu,text='enter emmployee no.:')
        empno_E.pack()

        Label(Entry_Menu,text="Enter Name",padx=10,pady=10).pack() 
        name_E=Entry(Entry_Menu,text='enter name:')
        name_E.pack()

        Label(Entry_Menu,text="Enter Speciality",padx=10,pady=10).pack()
        spec_E=Entry(Entry_Menu,text='enter spec')
        spec_E.pack()

        Label(Entry_Menu,text="Enter Salary",padx=10,pady=10).pack()
        sal_E=Entry(Entry_Menu,text="enter sal:")
        sal_E.pack()


    if table=="patients":
        global pId_E,Pname_E,doc_E,room_no_E,doj_E

        Label(Entry_Menu,text="Enter Patient Id",padx=10,pady=10).pack()
        pId_E=Entry(Entry_Menu,text="enter patient Id :")
        pId_E.pack()
        
        Label(Entry_Menu,text="Enter Patient name",padx=10,pady=10).pack()
        Pname_E=Entry(Entry_Menu,text="enter name:")
        Pname_E.pack()
        
        Label(Entry_Menu,text="Enter doctor Id",padx=10,pady=10).pack()
        doc_E=Entry(Entry_Menu,text="enter doc id")
        doc_E.pack()
        
        Label(Entry_Menu,text="Enter room Id",padx=10,pady=10).pack()
        room_no_E=Entry(Entry_Menu,text="enter room no")
        room_no_E.pack()
        
        Label(Entry_Menu,text="Enter date of addmision(DD/MM/YY)",padx=10,pady=10).pack()
        doj_E=Entry(Entry_Menu,text="enter date of addmision((DD/MM/YY))")
        doj_E.pack()
        
    if table=='stock':
        global Icode_E,Iname_E,Expiration_E,issued_E
        Label(Entry_Menu,text="Enter Item code",padx=10,pady=10).pack()
        Icode_E=Entry(Entry_Menu)
        Icode_E.pack()

        Label(Entry_Menu,text="Enter Item name",padx=10,pady=10).pack() 
        Iname_E=Entry(Entry_Menu)
        Iname_E.pack()

        Label(Entry_Menu,text="Enter Expiration",padx=10,pady=10).pack()
        Expiration_E=Entry(Entry_Menu)
        Expiration_E.pack()

        Label(Entry_Menu,text="Issued By",padx=10,pady=10).pack()
        issued_E=Entry(Entry_Menu)
        issued_E.pack()
    
        
        
    subButton=Button(Entry_Menu,padx=10,pady=10,text="Submit",command=Adder)
    subButton.pack()
    Button(text="BACK",command=lambda:goBackToMenu(Entry_Menu)).pack()

def Deleter(wid):
    global sk,match
    sk=wid.get()
    if sk in ids:
        Label(Entry_Menu,text="Data accessed").pack()
        match=True
    else:
        Label(Entry_Menu,text="Data not found").pack()
        match =False
    if match==True:
        subButton.config(state=DISABLED)
        y=mc.connect(host='localhost',user='root',password='Atharv123',database='hospital' )
        db=y.cursor()
        q="delete from "+table+" where "+pkeys[table]+"='"+sk+"';" 
        print(q)
        try:
            db.execute(q)     
            y.commit()
            Label(text="Data Deleted").pack()
            
        except:
            Label(Entry_Menu,text="Not Deleted").pack()
            y.rollback()
        y.close()

def DelData():
    global subButton
    entryMenu()
    Entry_Menu.title("Delete Data")
    fetchall(table)
    searchKey()
    subButton=Button(text="Submit",command=lambda:Deleter(sk_E))
    subButton.pack()
    Button(text="BACK",command=lambda:goBackToMenu(Entry_Menu)).pack()


def AlterData():
    global new_e,colName,choice_e,subButton
    entryMenu()
    Entry_Menu.title("Alter Data")
    fetchall(table)
    searchKey()
    colName=fetchcol(table)
    Label(Entry_Menu,text="enter the name of data you want to change:").pack()
    choice_e=Entry()
    choice_e.pack()
    Label(text="Enter new data").pack()
    new_e=Entry(Entry_Menu,text="enter new data:")
    new_e.pack()
    subButton=Button(text="Submit",command=lambda:Alter(sk_E))
    subButton.pack()
    Button(text="BACK",command=lambda:goBackToMenu(Entry_Menu)).pack()

def Alter(wid):
    global sk,match
    sk=wid.get()
    new=new_e.get()
    choice=choice_e.get()

    if sk in ids:
        Label(Entry_Menu,text="Data accessed").pack()
        match=True
    else:
        Label(Entry_Menu,text="Data not found").pack()
        match =False    
    if match==True:
        subButton.config(state=DISABLED)        
        if choice in colName:
            db=y.cursor()
            q="update "+table+" set "+choice+"='"+new+"' where "+pkeys[table]+"='"+sk+"';"
            try:
                db.execute(q)
                y.commit()
                Label(text="Data changed").pack()
            except:
                Label(text="Task failed:check the field entered").pack()
                y.rollback()
        else:
            pass
    else:
        Label(Entry_Menu,text="Invalid Data")

def joiner():
    refcol=col_E.get()
    db=y.cursor()
    subButton.config(state=DISABLED)
    join=join_E.get()
    Destroyer(Entry_Menu)
    Data=Tk()
    Data.title("Data")
    Button(text="BACK",command=lambda:goBackToMenu(Data)).pack()

    if join=="no" :
        if refcol in col:
            q="select "+ParentCol+","+refcol+" from "+table+","+reftable+";"
        else:
            Label(text="No such column").pack()
    elif join=="yes": 
        if refcol in col:
            #"select name, emp_no,Pname from emp,patients where emp.emp_no=patients.doc;"
            q="select "+refcol+","+ParentCol+" from "+table+","+reftable+" where "+table+"."+fkeys[table]+"="+reftable+"."+fkeys[reftable]+";"
        else:
            Label(text="No such column").pack()

    db.execute(q)
    rec=db.fetchall()
    for z in rec:
        Label(Data,text=z).pack() 



def refgetter():
    global reftable,refcol,join_E,subButton,col_E
    subButton.config(state=DISABLED)
    reftable=reftable_E.get()
    fetchcol(reftable)
    Label(text="Enter coloum to use:").pack()
    col_E=Entry()
    col_E.pack()
    Label(text="do you want to join data(yes/no)").pack()
    join_E=Entry()
    join_E.pack()
    subButton=Button(Entry_Menu,text='Submit',command=joiner)
    subButton.pack()

def reference():
    global reftable_E
    Label(text=tables).pack()
    Label(text='what table do you want to use:').pack()
    reftable_E=Entry()
    reftable_E.pack()
    subButton=Button(Entry_Menu,text='Submit',command=refgetter)
    subButton.pack()


def selecter():
    subButton.config(state=DISABLED)
    db=y.cursor()
    global ParentCol,ref
    ParentCol=ParentCol_E.get()
    ref=ref_E.get()
    if ref=='no':
        if ParentCol=="all":
            fetchall(table)
        else:
            if ParentCol in col:
                q="select "+ParentCol+" from "+table+";"
                db.execute(q)
                rec=db.fetchall()
                for z in rec:
                    Label(text=z).pack() 
            else:
                Label(text="No such column").pack()
    else:
        reference()

def Select():
    global ParentCol_E,ref_E,subButton
    entryMenu()
    Entry_Menu.title("Selecting Data")
    fetchcol(table)
    Button(text="BACK",command=lambda:goBackToMenu(Entry_Menu)).pack()
    Label(text="To print all the columns type 'All'").pack()
    Label(text="enter name of column to show").pack()
    ParentCol_E=Entry(Entry_Menu)
    ParentCol_E.pack()
    Label(text="do you want to refer data from another table(yes/no)").pack()
    ref_E=Entry()
    ref_E.pack()
    subButton=Button(Entry_Menu,text='Submit',command=selecter)
    subButton.pack()

        
mainloop()