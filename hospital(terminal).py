from tkinter import*
import mysql.connector as mc


root=Tk()

y=mc.connect(host='localhost',user='root',password='Atharv123',database='hospital')
global table
tables=["emp","patients","stock"]
global Isrun
Isrun=True
valid=True
pkeys={'emp':'emp_no','patients':'pId','stock':'Icode'}
fkeys={'emp':'emp_no','patients':'doc'}
print("available tables are ",tables)
table=input("enter the name of the table to work with: ")

Welcome=Label(root,text="WELCOME TO THE HOSPITAL DBMS")
Welcome.pack()


def fetchall(TbN):
    global ids
    db = y.cursor()
    query=("select * from " +TbN)
    db.execute(query)
    actualrec=db.fetchall()
    count=db.rowcount
    ids=[]
    print("total records are:",count)
    for z in actualrec:
        ids.append(z[0])
        print(z)
    return ids

def fetchcol(TbN):
    global col
    db = y.cursor()
    query=("show columns from " +TbN)
    db.execute(query)
    col=[]
    actualrec=db.fetchall()
    print('available columns are')
    for z in actualrec:
        col.append(z[0])
        print(z[0])
    return col

def emp():
    
    global empno, name,sal,spec
    empno =input('enter emmployee no.:')
    name=input('enter name:')
    spec=input('enter spec')
    sal=input("enter sal:")

def patients():
    global pId,Pname,doc,room_no,doj
    pId=input("enter patient Id :")
    Pname=input("enter name:")
    doc=input("enter doc id")
    room_no=input("enter room no")
    doj=input("enter date of addmision((DD/MM/YY))")

def stock():
        global Icode,Iname,exp
        Icode=input("Enter item  code:")
        Iname=input("Enter name of item")
        exp=input("enter expiration date(DD/MM/YY):")

def addData():
    n=int(input('enter no. of enteries:'))
    if table=='emp':
        for i in range(n):
            emp()
            db = y.cursor()
            q = "insert into "+table+" values('"+empno+"','"+name+"','"+spec+"',"+sal+");"
            db.execute(q)
            y.commit()
            print("Record inserted")
    if table=='stock':
        for i in range(n):
            stock()
            db = y.cursor()
            q = "insert into "+table+" values('"+Icode+"','"+Iname+"','"+exp+"');"
            db.execute(q)
            y.commit()
            print("Record inserted")

    if table=="patients":
        for i in range(n):
            patients()
            db = y.cursor()
            q = "insert into "+table+" values('"+pId+"','"+Pname+"','"+doc+"',"+room_no+",'"+doj+"');"
            db.execute(q)
            y.commit()
            print("Record inserted")
            y.rollback()
           
                
def searchKey():
    global sk
    valid=True
    sk=input("Enter "+pkeys[table]+":")
    if sk in ids:
        print("data accessed")
        return True
    else:
        print("Data not found")
        return False


def reference():
    reftable=input('what table do you want to use:').lower()
    fetchcol(reftable)
    if reftable in tables:
        col=input("enter coloum to use:")
    else:
        print("no such table")
    return col,reftable



def select():
    fetchcol(table)
    print("To print all the colums type 'All'")
    ParentCol=input("enter name of coloum to show: ")
    global valid
    valid=True
    
    db=y.cursor()
    if ParentCol=="all":
        fetchall(table)
    else:
        while ParentCol in col and valid==True:
            ref=input("do you want to refer data from another table(yes/no):").lower()
            if ref=="yes":
                join=input("do you want to join data(yes/no):")
                if join=="no":
                    refcol,reftable=reference()
                    q="select "+ParentCol+","+refcol+" from "+table+","+reftable+";"
                elif join=="yes":
                    refcol,reftable=reference()
                    #"select name, emp_no,Pname from emp,patients where emp.emp_no=patients.doc;"
                    q="select "+refcol+","+ParentCol+" from "+table+","+reftable+" where "+table+"."+fkeys[table]+"="+reftable+"."+fkeys[reftable]+";"
            
            elif ref=='no':
                q="select "+ParentCol+" from "+table+";"
            
            db.execute(q)
            count=db.rowcount
            rec=db.fetchall()
            for z in rec:
                print (z) 
        
            break
        else:
            valid=False
            print("No such column")
        
   
def alterData():
        fetchall(table)
        val=searchKey()
        if val==True:
            colName=fetchcol(table)
            choice=(input("enter the name of data you want to change:"))
            if choice in colName:
                new=input("enter new data:")
                db=y.cursor()
                q="update "+table+" set "+choice+"='"+new+"' where "+pkeys[table]+"='"+sk+"';"

                try:
                    db.execute(q)
                    y.commit()
                    print("Data changed")
                except:
                    print("Task faileds:check the field entered")
                    y.rollback()

            else:
                print("invalid data")
                valid=False



def deleteData():
    fetchall(table)
    valid=searchKey()
    while valid==True:
        db=y.cursor()
        q="delete from "+table+" where emp_no='"+sk+"';" 
        try:
            db.execute(q)     
            y.commit()
            print("data deleted")
            valid=False
            
        except:

            y.rollback()
        
    

ShowT=Label(root,text="Current working table "+table)
ShowT.pack()

def main():
    root.mainloop()
    global table
    print("Current working table ",table)
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

while table in tables and Isrun==True:
    main()

else:
    print("No such table")
    y.close()

