import sqlite3
from tkinter import *
from tkinter import ttk, messagebox


class SupplierClass:
    def __init__(self, root_window):
        self.root = root_window
        self.root.geometry("1100x500+225+150")
        self.root.title("Inventory Management System")
        self.root.config(bg="white")
        self.root.focus_force()

        # ================================= Variables =============================
        self.search_by_var = StringVar()
        self.search_txt_var = StringVar()

        self.supplier_invoice_var = StringVar()
        self.supplier_name_var = StringVar()
        self.supplier_contact_var = StringVar()

        # ================================= Options ===============================
        search_lbl = Label(self.root, text="Invoice No.", font=("goudy old style", 15), bg="white")
        search_lbl.place(x=700, y=80)

        search_txt = Entry(self.root, font=("goudy old style", 15), bg="light yellow",
                           textvariable=self.search_txt_var)
        search_txt.place(x=810, y=80, width=160)

        search_btn = Button(self.root, text="Search", font=("goudy old style", 15), bg="#4caf50", fg="white",
                            cursor="hand2", command=self.search)
        search_btn.place(x=980, y=79, width=100, height=28)

        # =================================== Title ================================
        title = Label(self.root, text="Supplier Details", font=("goudy old style", 20, "bold"), bg="#0f4d7d",
                      fg="white")
        title.place(x=50, y=10, width=1000, height=40)

        # =================================== Content ==============================
        # =================================== Row 1 ==============================
        supp_invoice_lbl = Label(self.root, text="Invoice No", font=("goudy old style", 15, "bold"), bg="white")
        supp_invoice_lbl.place(x=50, y=80)
        supp_invoice_txt = Entry(self.root, textvariable=self.supplier_invoice_var,
                                 font=("goudy old style", 15, "bold"),
                                 bg="light yellow")
        supp_invoice_txt.place(x=180, y=80, width=180)

        # =================================== Row 2 ==============================
        supp_name_lbl = Label(self.root, text="Name", font=("goudy old style", 15, "bold"), bg="white")
        supp_name_lbl.place(x=50, y=120)
        supp_name_txt = Entry(self.root, textvariable=self.supplier_name_var, font=("goudy old style", 15, "bold"),
                              bg="light yellow")
        supp_name_txt.place(x=180, y=120, width=180)

        # =================================== Row 3 ==============================
        supp_contact_lbl = Label(self.root, text="Contact", font=("goudy old style", 15, "bold"), bg="white")
        supp_contact_lbl.place(x=50, y=160)
        supp_contact_txt = Entry(self.root, textvariable=self.supplier_contact_var,
                                 font=("goudy old style", 15, "bold"),
                                 bg="light yellow")
        supp_contact_txt.place(x=180, y=160, width=180)

        # =================================== Row 4 ==============================
        supp_description_lbl = Label(self.root, text="Description", font=("goudy old style", 15, "bold"), bg="white")
        supp_description_lbl.place(x=50, y=200)
        self.supp_description_txt = Text(self.root, font=("goudy old style", 15, "bold"), bg="light yellow")
        self.supp_description_txt.place(x=180, y=200, width=470, height=120)

        # =================================== Buttons =============================
        add_btn = Button(self.root, text="Save", font=("goudy old style", 15, "bold"), bg="#2196f3", fg="white",
                         cursor="hand2", command=self.add)
        add_btn.place(x=180, y=370, width=110, height=35)

        update_btn = Button(self.root, text="Update", font=("goudy old style", 15, "bold"), bg="#4caf50", fg="white",
                            cursor="hand2", command=self.update)
        update_btn.place(x=300, y=370, width=110, height=35)

        delete_btn = Button(self.root, text="Delete", font=("goudy old style", 15, "bold"), bg="#f44336", fg="white",
                            cursor="hand2", command=self.delete)
        delete_btn.place(x=420, y=370, width=110, height=35)

        clear_btn = Button(self.root, text="Clear", font=("goudy old style", 15, "bold"), bg="#607d8b", fg="white",
                           cursor="hand2", command=self.clear)
        clear_btn.place(x=540, y=370, width=110, height=35)

        # ================================= Supplier Details ==============================
        supplier_frame = Frame(self.root, bd=3, relief=RIDGE)
        supplier_frame.place(x=700, y=120, width=380, height=350)

        scroll_x = Scrollbar(supplier_frame, orient=HORIZONTAL)
        scroll_y = Scrollbar(supplier_frame, orient=VERTICAL)

        self.supplier_table = ttk.Treeview(supplier_frame, columns=("invoice", "name", "contact", "desc"),
                                           xscrollcommand=scroll_x.set, yscrollcommand=scroll_y.set)
        scroll_x.pack(side=BOTTOM, fill=X)
        scroll_y.pack(side=RIGHT, fill=Y)
        scroll_x.config(command=self.supplier_table.xview)
        scroll_y.config(command=self.supplier_table.yview)

        self.supplier_table.heading("invoice", text="Invoice No")
        self.supplier_table.heading("name", text="Name")
        self.supplier_table.heading("contact", text="Contact")
        self.supplier_table.heading("desc", text="Description")
        self.supplier_table["show"] = "headings"

        self.supplier_table.column("invoice", width=90)
        self.supplier_table.column("name", width=100)
        self.supplier_table.column("contact", width=100)
        self.supplier_table.column("desc", width=100)
        self.supplier_table.pack(fill=BOTH, expand=1)
        self.supplier_table.bind("<ButtonRelease-1>", self.get_data)

        self.show()

    def add(self):
        con = sqlite3.connect(database=r"ims.db")
        cur = con.cursor()
        try:
            if self.supplier_invoice_var.get() == "":
                messagebox.showerror("Error", "Invoice Must Be Required !", parent=self.root)

            elif self.supplier_name_var.get() == "" or self.supplier_contact_var.get() == "" or self.supplier_contact_var.get() == "" or self.supp_description_txt.get(
                    '1.0', END) == "":
                messagebox.showerror("Error", "All Fields Are Required !", parent=self.root)

            else:
                cur.execute("select * from supplier where invoice=?", (self.supplier_invoice_var.get(),))
                row = cur.fetchone()
                if row is not None:
                    messagebox.showerror("Error", "This Invoice No is Already Present, Try Different One.",
                                         parent=self.root)
                else:
                    cur.execute(
                        "Insert into supplier (invoice, name, contact, desc) values(?, ?, ?, ?)", (
                            self.supplier_invoice_var.get(),
                            self.supplier_name_var.get(),
                            self.supplier_contact_var.get(),
                            self.supp_description_txt.get('1.0', END),
                        ))
                    con.commit()
                    messagebox.showinfo("Success", "Supplier Added Successfully.", parent=self.root)
                    self.show()

        except Exception as ex:
            messagebox.showerror("Error", f"Error due to : {str(ex)}", parent=self.root)

    def show(self):
        con = sqlite3.connect(database=r"ims.db")
        cur = con.cursor()
        try:
            cur.execute("select * from supplier")
            rows = cur.fetchall()
            self.supplier_table.delete(*self.supplier_table.get_children())
            for row in rows:
                self.supplier_table.insert("", END, values=row)

        except Exception as ex:
            messagebox.showerror("Error", f"Error due to : {str(ex)}", parent=self.root)

    def get_data(self, ev):
        f = self.supplier_table.focus()
        content = (self.supplier_table.item(f))
        row = content['values']
        self.supplier_invoice_var.set(row[0]),
        self.supplier_name_var.set(row[1]),
        self.supplier_contact_var.set(row[2]),
        self.supp_description_txt.delete('1.0', END),
        self.supp_description_txt.insert(END, row[3]),

    def update(self):
        con = sqlite3.connect(database=r"ims.db")
        cur = con.cursor()
        try:
            if self.supplier_invoice_var.get() == "":
                messagebox.showerror("Error", "Invoice No Must Be Required !", parent=self.root)

            elif self.supplier_name_var.get() == "" or self.supplier_contact_var.get() == "" or self.supp_description_txt.get(
                    '1.0', END) == "":
                messagebox.showerror("Error", "All Fields Are Required !", parent=self.root)

            else:
                cur.execute("select * from supplier where invoice=?", (self.supplier_invoice_var.get(),))
                row = cur.fetchone()
                if row is None:
                    messagebox.showerror("Error", "Invalid Invoice No !", parent=self.root)

                else:
                    cur.execute(
                        "update supplier set name=?, contact=?, desc=? where invoice=?", (
                            self.supplier_name_var.get(),
                            self.supplier_contact_var.get(),
                            self.supp_description_txt.get('1.0', END),
                            self.supplier_invoice_var.get(),
                        ))
                    con.commit()
                    messagebox.showinfo("Success", "Supplier Updated Successfully.", parent=self.root)
                    self.clear()

        except Exception as ex:
            messagebox.showerror("Error", f"Error due to : {str(ex)}", parent=self.root)

    def delete(self):
        con = sqlite3.connect(database=r"ims.db")
        cur = con.cursor()
        try:
            if self.supplier_invoice_var.get() == "":
                messagebox.showerror("Error", "Invoice No. Must Be Required !", parent=self.root)

            elif self.supplier_name_var.get() == "" or self.supplier_contact_var.get() == "" or self.supp_description_txt.get(
                    '1.0', END) == "":
                messagebox.showerror("Error", "All Fields Are Required !", parent=self.root)

            else:
                cur.execute("select * from supplier where invoice=?", (self.supplier_invoice_var.get(),))
                row = cur.fetchone()
                if row is None:
                    messagebox.showerror("Error", "Invalid Invoice No. !", parent=self.root)
                else:
                    option = messagebox.askyesno("Confirm", "Do You Really Want to Delete ?", parent=self.root)
                    if option is True:
                        cur.execute("delete from supplier where invoice=?", (self.supplier_invoice_var.get(),))
                        con.commit()
                        messagebox.showinfo("Delete", "Supplier Deleted Successfully", parent=self.root)
                        self.clear()
                        self.show()

        except Exception as ex:
            messagebox.showerror("Error", f"Error due to : {str(ex)}", parent=self.root)

    def clear(self):
        self.supplier_invoice_var.set(""),
        self.supplier_name_var.set(""),
        self.supplier_contact_var.set(""),
        self.supp_description_txt.delete('1.0', END),
        self.search_txt_var.set("")
        self.show()

    def search(self):
        con = sqlite3.connect(database=r"ims.db")
        cur = con.cursor()
        try:
            if self.search_txt_var.get() == "":
                messagebox.showerror("Error", "Search Invoice No. is Required !", parent=self.root)
            else:
                cur.execute("select * from supplier where invoice=?", (self.search_txt_var.get(),))
                rows = cur.fetchall()
                if len(rows) != 0:
                    self.supplier_table.delete(*self.supplier_table.get_children())
                    for row in rows:
                        self.supplier_table.insert("", END, values=row)
                else:
                    messagebox.showerror("Error", "No Record Found !", parent=self.root)

        except Exception as ex:
            messagebox.showerror("Error", f"Error due to : {str(ex)}", parent=self.root)


if __name__ == '__main__':
    root = Tk()
    obj = SupplierClass(root)
    root.mainloop()
