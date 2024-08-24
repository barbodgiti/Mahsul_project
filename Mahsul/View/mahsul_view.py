from tkinter import *
import tkinter.ttk as ttk
import tkinter.messagebox as msg
from Mahsul.Module.module_file import *
from Mahsul.Module.module_mahsul import *
from Mahsul.Validator.product_validator import *

def refresh_table():
    for item in table.get_children():
        table.delete(item)


    for doc in mahsul:
        p = tuple(doc)
        table.insert("",END, p, tags=p[4])

def save_click():
    try:
        if new_validator(prd.get()):
            doc = get_document(prd.get(), prc.get(), prsn.get(), ste.get(), cnt.get())
            new_count = mahsul_transaction(doc, total_count.get())
                if new_count:
                    total_count.set(new_count)
                    msg.showinfo("SAVE", f"DATAS ARE SAVED {doc}")
                    mahsul.append(doc)
                    save_data(mahsul)
                    refresh_table()
                    prd.set("")
                    prc.set(0)
                    prsn.set("")
                    ste.set("")
                elif cnt < table.heading(3, text="Count"):
                    msg.showerror("SAVE", "ERROR : NOT ENOUGH COUNT")
                else:
                    msg.showerror("SAVE", "ERROR : NOT ENOUGH COUNT")

        elif prdt = table.heading(3, text="Product")
            msg.showerror("SAVE", "ERROR}")

    except Exception as e:
            msg.showerror("SAVE", f"ERROR: {e}")

mahsul = load_data()
mahsul_count = 0

win = Tk()
win.title("Mahsul")
win.geometry("900x500")

# Product
Label(win, text="Product").place(x=20, y=10)
prd = StringVar()
Entry(win, width=14, font="Arial", textvariable=prd).place(x=140, y=20)

# Price
Label(win, text="Price").place(x=20, y=80)
prc = IntVar()
Entry(win, width=14, font="Arial", textvariable=prc).place(x=140, y=90)

# Count
Label(win, text="Count").place(x=20, y=150)
cnt = IntVar()
Entry(win, width=14, font="Arial", textvariable=cnt).place(x=140, y=160)

# Person
Label(win, text="Person").place(x=20, y=220)
prsn = StringVar()
Entry(win, width=14, font="Arial", textvariable=prsn).place(x=140, y=230)

# Store
Label(win, text="Store").place(x=20, y=290)
ste = StringVar()
ttk.Combobox(win,
             width=17,
             values=["In", "Out"],
             textvariable=ste).place(x=140, y=295)

#
table = ttk.Treeview(win, height=16, columns=(1, 2, 3, 4), show="headings")

table.heading(1, text="Product")
table.heading(2, text="Price")
table.heading(3, text="Count")
table.heading(4, text="Person")

table.column(1, width=110)
table.column(2, width=100)
table.column(3, width=100)
table.column(4, width=100)

table.tag_configure("In", background="lightgreen")
table.tag_configure("Out", background="pink")

table.place(x=400 , y=20)

Button(win, width=20, font=("Arial", 16),bg="lightblue", text="SAVE", ).place(x=80, y=400)


win.mainloop()
