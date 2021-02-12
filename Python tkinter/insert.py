import mysql.connector
from tkinter import *

win = Tk()
win.title("Insert Record")
win.geometry("700x400")

Acc_No_Ent = StringVar()
Acc_Name_Ent = StringVar()
Acc_Bal_Ent = StringVar()
dis = StringVar()


def submit():
    con = mysql.connector.connect(user='root', password='root',
                                  host='localhost', database='student')
    cur = con.cursor()
    query = "insert into account values('%s','%s','%s')" % (Acc_No_Ent.get(), Acc_Name_Ent.get(), Acc_Bal_Ent.get())
    cur.execute(query)
    con.commit()
    dis.set("data is sueccsfully submit")
    con.close()

    Acc_No_Ent.delete(0, END)
    Acc_Name_Ent.delete(0, END)
    Acc_Bal_Ent.delete(0, END)
    return


Enter_Details = Label(win, text="Enter Details :", font="times 25", fg='orange')
Conn_Details = Label(win, text="Connection successful :", font="times 10", fg='black')

Acc_No = Label(win, text="Account NO", font="times 20", fg='blue')
Acc_No_Ent = Entry(win, textvariable=Acc_No_Ent, font="times 20", width=25, borderwidth=9)

Acc_Name = Label(win, text="Name", font="times 20", fg='blue')
Acc_Name_Ent = Entry(win, textvariable=Acc_Name_Ent, font="times 20", width=25, borderwidth=9)

Acc_Bal = Label(win, text="Balance", font="times 20", fg='blue')
Acc_Bal_Ent = Entry(win, textvariable=Acc_Bal_Ent, font="times 20", width=25, borderwidth=9)

Submit = Button(win, text="Submit", font="times 20", borderwidth=5, fg='green', command=submit)
Exit = Button(win, text="Exit", font="times 20", borderwidth=5, fg='red', command=quit)

Dis_Details = Label(win, textvariable=dis, font="times 15", fg='green')

Enter_Details.grid(row=0, column=2)
Conn_Details.grid(row=0, column=1)

Acc_No.grid(row=1, column=1)
Acc_No_Ent.grid(row=1, column=2)
Acc_Name.grid(row=2, column=1)
Acc_Name_Ent.grid(row=2, column=2)
Acc_Bal.grid(row=3, column=1)
Acc_Bal_Ent.grid(row=3, column=2)
Submit.grid(row=5, column=2)
Exit.grid(row=5, column=3)
Dis_Details.grid(row=6, column=2)



