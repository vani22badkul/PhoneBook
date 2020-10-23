from Tkinter import *
from tkMessageBox import *
import sqlite3
con=sqlite3.Connection('My_DBMS')
cur=con.cursor()

##------ splash screen---------##

root2=Tk()
root2.geometry('800x500')
root2.configure(bg='light sky blue')
Label(root2,text="PROJECT TITLE: PHONEBOOK",font='arial 15 bold italic',bg='light sky blue').grid(row=0,column=0)
Label(root2,text="Project Of Python and DBMS",font='arial 15 bold italic',bg='light sky blue').grid(row=1,column=1)
Label(root2,text="Developed By : Vani Jain Badkul",font='arial 15 bold italic',bg='light sky blue',fg='midnight blue').grid(row=2,column=1)
Label(root2,text="---------------------------------",font='arial 15 bold',bg='light sky blue',fg='midnight blue').grid(row=3,column=1)
Label(root2,text="Make Mouse movement over this screen to close",font='arial 10 bold',bg='light sky blue',fg='maroon').grid(row=4,column=1)

def close1(c1=1):
    root2.destroy()
    root=Tk()
    root.configure(bg='lemon chiffon')
##------------------Image inserting------------##

    def close1():
        root.destroy()

    
    photo=PhotoImage(file="phonebook_v.gif")
    Label(root,image=photo).grid(row=0,column=1)

 ##-----------creating table--------------##   

    cur.execute("create table if not exists people(id INTEGER primary key AUTOINCREMENT ,fname varchar(20) ,mname varchar(15),lname varchar(20),company varchar(30),address varchar(20),city varchar(20),pin number,website varchar(50),dob date)")
    cur.execute("create table if not exists contact(id1 INTEGER ,cont_type varchar(20),p_no number(10),FOREIGN KEY(id1) REFERENCES people(id) on delete cascade)")
    cur.execute("create table if not exists email(id2 INTEGER ,id_type varchar(15), email_id varchar(20),FOREIGN KEY(id2) REFERENCES people(id) on delete cascade)")

    Label(root,text='PhoneBook',font='arial 12 bold',fg='midnight blue',bg='lemon chiffon').grid(row=0,column=0)

    
    Label(root,text="First Name",bg='lemon chiffon').grid(row=1,column=0)
    e=Entry(root)
    e.grid(row=1,column=1)

    Label(root,text="Middle Name",bg='lemon chiffon').grid(row=2,column=0)
    e1=Entry(root)
    e1.grid(row=2,column=1)


    Label(root,text="Last Name",bg='lemon chiffon').grid(row=3,column=0)
    e2=Entry(root)
    e2.grid(row=3,column=1)


    Label(root,text="Company Name",bg='lemon chiffon').grid(row=4,column=0)
    e3=Entry(root)
    e3.grid(row=4,column=1)



    Label(root,text="Address",bg='lemon chiffon').grid(row=5,column=0)
    e4=Entry(root)
    e4.grid(row=5,column=1)

    Label(root,text="City",bg='lemon chiffon').grid(row=6,column=0)
    e5=Entry(root)
    e5.grid(row=6,column=1)

    Label(root,text="Pin Code",bg='lemon chiffon').grid(row=7,column=0)
    e6=Entry(root)
    e6.grid(row=7,column=1)

    Label(root,text="Website URL",bg='lemon chiffon').grid(row=8,column=0)
    e7=Entry(root)
    e7.grid(row=8,column=1)

    Label(root,text="Date of Birth",bg='lemon chiffon').grid(row=9,column=0)
    e8=Entry(root)
    e8.grid(row=9,column=1)

    v=IntVar()
    Label(root,text="Select Phone Type",font='arial 22 bold italic',fg='midnight blue',bg='lemon chiffon').grid(row=10,column=0)
    r1=Radiobutton(root,text="Office",bg='lemon chiffon',variable=v,value=1).grid(row=10,column=1)
    r2=Radiobutton(root,text="Home",bg='lemon chiffon',variable=v,value=2).grid(row=10,column=2)
    r3=Radiobutton(root,text="Mobile",bg='lemon chiffon',variable=v,value=3).grid(row=10,column=3)
    if v.get()==1:
        z='office'
    elif  v.get()==2:
        z='home'
    else:
        z='mobile'

    Label(root,text="Phone Number",bg='lemon chiffon').grid(row=11,column=0)
    e11=Entry(root)
    e11.grid(row=11,column=1)
    def fun1():
        e9=Entry(root)
        e9.grid(row=11,column=3)
    Button(root,text='+',bg='lemon chiffon',command=fun1).grid(row=11,column=2)

    v1=IntVar()
    Label(root,text="Select Email Type",font='arial 22 bold italic',fg='midnight blue',bg='lemon chiffon').grid(row=12,column=0)
    p1=Radiobutton(root,text="Office",bg='lemon chiffon',variable=v1,value=1).grid(row=12,column=1)
    p2=Radiobutton(root,text="Personal",bg='lemon chiffon',variable=v1,value=2).grid(row=12,column=2)

    if v1.get()==1:
        d="Office"
    else:
        d="Personal"
        


    Label(root,text="Email Id",bg='lemon chiffon').grid(row=13,column=0)
    e10=Entry(root)
    e10.grid(row=13,column=1)
    def fun1():
        e10.grid(row=13,column=3)
    Button(root,text='+',bg='lemon chiffon',command=fun1).grid(row=13,column=2)


    def toinsert():
        showinfo('save','Record successfylly saved')
        
    
        cur.execute("insert into people(fname,mname,lname,company,address,city,pin,website,dob) values(?,?,?,?,?,?,?,?,?)",(str(e.get()),str(e1.get()),str(e2.get()),str(e3.get()),str(e4.get()),str(e5.get()),str(e6.get()),str(e7.get()),str(e8.get())))
        cur.execute("insert into contact(id1,cont_type,p_no) values((select max(id) from people),?,?)",(str(v.get()),str(e11.get())))
        cur.execute("insert into email(id2,id_type,email_id)values((select max(id) from people),?,?)",(str(v1.get()),str(e10.get())))

        print 'successfully saved'


        e.delete(0,END)
        e1.delete(0,END)
        e2.delete(0,END)
        e3.delete(0,END)
        e4.delete(0,END)
        e5.delete(0,END)
        e6.delete(0,END)
        e7.delete(0,END)
        e8.delete(0,END)
        e11.delete(0,END)
        e10.delete(0,END)

        con.commit()
##-----------------searching------------##         

    def search():
        root1=Tk()
        root1.configure(bg='lemon chiffon')
        Label(root1,text="Searching phone Book",font='arial 17 bold',bg='lemon chiffon').grid(row=0,column=1)
        Label(root1,text="Enter Name",bg='lemon chiffon').grid(row=1,column=0)
        a=Entry(root1,width=50)
        a.grid(row=1,column=1)

        cur.execute("select fname,mname,lname from people order by fname asc,mname asc,lname asc")
        fetch1=cur.fetchall()
    
        list1=Listbox(root1,width=50,height=15)
        list1.grid(row=2,column=1)
        for i1 in fetch1:
            list1.insert(END,i1)

        def closescr():
            root1.destroy()
        Button(root1,text="Close",bg='lemon chiffon',command=closescr).grid(row=9,column=1)
##-----------------------------------------data searching ---------------##        
        def main_search(b=1):
            list2=Listbox(root1,width=50,height=15)
            list2.grid(row=2,column=1)

            cur.execute("select fname,lname from people where fname like(?) or lname like(?)",('%'+str(a.get())+'%','%'+str(a.get())+'%'))
            fetch2=cur.fetchall()
            
            for i2 in fetch2:
                list2.insert(END,i2)
###--------------------PRINTING DATA-----------------------###
            def printdata(b=1):
                list3=Listbox(root1,width=50,height=15)
                list3.grid(row=2,column=1)
                select=list2.curselection()
                for i3 in select:
                    text=list2.get(i3)
                    
                cur.execute("select id from people where fname=?",(str(text[0]),))
                fetch3=cur.fetchall()
                cur.execute("select fname from people where id=?",(str(fetch3[0][0]),))
                fetch4=cur.fetchall()
                for i4 in fetch4:
                    list3.insert(END,"First Name :-"+str(i4[0]))

                cur.execute("select mname from people where id=?",(str(fetch3[0][0]),))
                fetch5=cur.fetchall()
                for i5 in fetch5:
                    list3.insert(END,"Middle Name:-"+str(i5[0]))

                cur.execute("select lname from people where id=?",(str(fetch3[0][0]),))
                fetch6=cur.fetchall()
                for i6 in fetch6:
                    list3.insert(END,"Last Name :-"+str(i6[0]))

                cur.execute("select company from people where id=?",(str(fetch3[0][0]),))
                fetch7=cur.fetchall()
                for i7 in fetch7:
                    list3.insert(END,"Company :-"+str(i7[0]))

                cur.execute("select address from people where id=?",(str(fetch3[0][0]),))
                fetch8=cur.fetchall()
                for i8 in fetch8:
                    list3.insert(END,"Address :-"+str(i8[0]))

                cur.execute("select city from people where id=?",(str(fetch3[0][0]),))
                fetch9=cur.fetchall()
                for i9 in fetch9:
                    list3.insert(END,"City :-"+str(i9[0]))

                cur.execute("select pin from people where id=?",(str(fetch3[0][0]),))
                fetch10=cur.fetchall()
                for i10 in fetch10:
                    list3.insert(END,"Pin :-"+str(i10[0]))

                cur.execute("select website from people where id=?",(str(fetch3[0][0]),))
                fetch11=cur.fetchall()
                for i11 in fetch11:
                    list3.insert(END,"Website URL :-"+str(i11[0]))

                cur.execute("select dob from people where id=?",(str(fetch3[0][0]),))
                fetch12=cur.fetchall()
                for i12 in fetch12:
                    list3.insert(END,"Birth Date :-"+str(i12[0]))


                cur.execute("select cont_type from contact where id1=?",(str(fetch3[0][0]),))
                fetch13=cur.fetchall()
                
                list3.insert(END,"Contact Type :-"+str(z))

                    
                cur.execute("select p_no from contact where id1=?",(str(fetch3[0][0]),))
                fetch14=cur.fetchall()
                for i14 in fetch14:
                    list3.insert(END,"Phone Number :-"+str(i14[0]))

                cur.execute("select id_type from email where id2=?",(str(fetch3[0][0]),))
                fetch15=cur.fetchall()
                
                list3.insert(END,"ID Type :-"+str(d))

                cur.execute("select email_id from email where id2=?",(str(fetch3[0][0]),))
                fetch16=cur.fetchall()
                for i16 in fetch16:
                    list3.insert(END,"Email ID :-"+str(i16[0]))

                def delete(c=1):
                    showinfo('record','Record Deleted from PhoneBook ')
                    cur.execute("delete from people where id=?",(str(fetch3[0][0]),))
                    cur.execute("delete from contact where id1=?",(str(fetch3[0][0]),))
                    cur.execute("delete from email where id2=?",(str(fetch3[0][0]),))
                    root1.destroy()
                Button(root1,text="Delete",bg='lemon chiffon',command=delete).grid(row=9,column=2)

                con.commit()


            list2.bind('<ButtonRelease-1>',printdata)
                    
                
                
        root1.bind('<KeyPress>',main_search)
        con.commit()
        root1.mainloop()


    Button(root,text="Save",bg='lemon chiffon',command=toinsert).grid(row=14,column=0)
    Button(root,text="search",bg='lemon chiffon',command=search).grid(row=14,column=1)
    Button(root,text="Close",bg='lemon chiffon',command=close1).grid(row=14,column=2)
    Button(root,text="Edit",bg='lemon chiffon').grid(row=14,column=3)

    root.mainloop()
root2.bind('<Motion>',close1)
root2.mainloop()



