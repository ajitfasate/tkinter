import mysql.connector
from tkinter import *
from tkinter import messagebox


def Search():
    try:
        con = mysql.connector.connect(user='root', password='root',
                                      host='localhost', database='student')
        cur = con.cursor()

        query = "select * from account where no='%s'" % no.get()
        cur.execute(query)
        result = cur.fetchone()
        name.set(result[1])
        bal.set(result[2])

        con.commit()
        Acc_No_Ent.configure(state='disabled')
        con.close()

    except:
        messagebox.showinfo('Error :', 'No such data available...')
        clear()

    return


def Clear():
    no.set('')
    name.set('')
    bal.set('')
    Acc_No_Ent.configure(state="normal")

    return


win = Tk()
win.title("Display Details")
win.geometry("700x300")

no = StringVar()
name = StringVar()
bal = StringVar()

Dis_Details = Label(win, text="Details...", font="times 25", fg='Orange')

Acc_No = Label(win, text="Enter Account No :", font="Times 20", fg="blue")
Acc_No_Ent = Entry(win, font="Times 15", width=20, borderwidth=9, textvariable=no)

Acc_Name = Label(win, text="Name : ", font="Times 20", fg="blue")
Acc_Name_Ent = Entry(win, font="Times 15", width=20, borderwidth=9, textvariable=name)

Acc_Bal = Label(win, text="Balance : ", font="Times 20", fg="blue")
Acc_Bal_Ent = Entry(win, font="Times 15", width=20, borderwidth=9, textvariable=bal)

Show = Button(win, text="Show", font="Times 15", fg="green", borderwidth=9, command=Search)
Clear = Button(win, text="Clear", font="Times 15", fg="Black", borderwidth=9, command=Clear)
Exit = Button(win, text='Exit', font="Times 15", fg='red', borderwidth=9, command=quit)

Dis_Details.grid(row=0, column=0)

Acc_No.grid(row=1, column=0)
Acc_No_Ent.grid(row=1, column=1)

Show.grid(row=2, column=2)

Acc_Name.grid(row=3, column=0)
Acc_Name_Ent.grid(row=3, column=1)

Acc_Bal.grid(row=4, column=0)
Acc_Bal_Ent.grid(row=4, column=1)

Clear.grid(row=5, column=1)
Exit.grid(row=5, column=2)
