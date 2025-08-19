import sqlite3
from tkinter import *
# from PIL import Image, ImageTk
from tkinter import ttk, messagebox


class ProductClass:
    def __init__(self, root_window):
        self.root = root_window
        self.root.geometry("1100x500+225+150")
        self.root.title("Inventory Management System")
        self.root.config(bg="white")
        self.root.focus_force()

        # ========================= Variables ========================
        self.search_by_var = StringVar()
        self.search_txt_var = StringVar()

        self.p_id_var = StringVar()
        self.category_var = StringVar()
        self.supplier_var = StringVar()
        self.product_name_var = StringVar()
        self.price_var = StringVar()
        self.quantity_var = StringVar()
        self.status_var = StringVar()
        self.cat_list = []
        self.sup_list = []
        self.fetch_cat_sup()

        # ========================= Product Frame ========================
        product_frame = Frame(self.root, bd=2, relief=RIDGE, bg="white")
        product_frame.place(x=10, y=10, width=450, height=480)

        # =================================== Title ================================
        title = Label(product_frame, text="Manage Products Details", font=("goudy old style", 18, "bold"), bg="#0f4d7d",
                      fg="white")
        title.pack(side=TOP, fil=X)

        category_lbl = Label(product_frame, text="Category", font=("goudy old style", 18),
                             bg="white")
        category_lbl.place(x=30, y=60)
        category_cmb = ttk.Combobox(product_frame, values=self.cat_list, state="readonly",
                                    justify=CENTER, font=("goudy old style", 15), textvariable=self.category_var)
        category_cmb.place(x=150, y=60, width=200)
        category_cmb.current(0)

        supplier_lbl = Label(product_frame, text="Supplier", font=("goudy old style", 18),
                             bg="white")
        supplier_lbl.place(x=30, y=110)
        supplier_cmb = ttk.Combobox(product_frame, values=self.sup_list, state="readonly",
                                    justify=CENTER, font=("goudy old style", 15), textvariable=self.supplier_var)
        supplier_cmb.place(x=150, y=110, width=200)
        supplier_cmb.current(0)

        product_name_lbl = Label(product_frame, text="Name", font=("goudy old style", 18),
                                 bg="white")
        product_name_lbl.place(x=30, y=160)
        product_name_txt = Entry(product_frame, font=("goudy old style", 15), textvariable=self.product_name_var, bg="light yellow")
        product_name_txt.place(x=150, y=160, width=200)

        price_lbl = Label(product_frame, text="Price", font=("goudy old style", 18),
                          bg="white")
        price_lbl.place(x=30, y=210)
        price_txt = Entry(product_frame, font=("goudy old style", 15), textvariable=self.price_var, bg="light yellow")
        price_txt.place(x=150, y=210, width=200)

        quantity_lbl = Label(product_frame, text="Quantity", font=("goudy old style", 18),
                             bg="white")
        quantity_lbl.place(x=30, y=260)
        quantity_txt = Entry(product_frame, font=("goudy old style", 15), textvariable=self.quantity_var, bg="light yellow")
        quantity_txt.place(x=150, y=260, width=200)

        status_lbl = Label(product_frame, text="Status", font=("goudy old style", 18), bg="white")
        status_lbl.place(x=30, y=310)
        status_cmb = ttk.Combobox(product_frame, values=("Active", "Inactive"), state="readonly",
                                  justify=CENTER, font=("goudy old style", 15), textvariable=self.status_var)
        status_cmb.place(x=150, y=310, width=200)
        status_cmb.current(0)

        # =================================== Buttons =============================
        add_btn = Button(product_frame, text="Save", font=("goudy old style", 15, "bold"), bg="#2196f3", fg="white",
                         cursor="hand2", command=self.add)
        add_btn.place(x=10, y=400, width=100, height=40)

        update_btn = Button(product_frame, text="Update", font=("goudy old style", 15, "bold"), bg="#4caf50", fg="white",
                            cursor="hand2", command=self.update)
        update_btn.place(x=120, y=400, width=100, height=40)

        delete_btn = Button(product_frame, text="Delete", font=("goudy old style", 15, "bold"), bg="#f44336", fg="white",
                            cursor="hand2", command=self.delete)
        delete_btn.place(x=230, y=400, width=100, height=40)

        clear_btn = Button(product_frame, text="Clear", font=("goudy old style", 15, "bold"), bg="#607d8b", fg="white",
                           cursor="hand2", command=self.clear)
        clear_btn.place(x=340, y=400, width=100, height=40)

        # ================================= Search Frame ==========================
        search_frame = LabelFrame(self.root, text="Search Product", font=("goudy old style", 12, "bold"), bd=2,
                                  relief=RIDGE, bg="white")
        search_frame.place(x=480, y=10, width=600, height=80)

        # ================================= Options ===============================
        search_cmb = ttk.Combobox(search_frame, values=("Search By", "Category", "Supplier", "Name"), state="readonly",
                                  justify=CENTER, font=("goudy old style", 15), textvariable=self.search_by_var)
        search_cmb.place(x=10, y=10, width=180)
        search_cmb.current(0)

        search_txt = Entry(search_frame, font=("goudy old style", 15), bg="light yellow",
                           textvariable=self.search_txt_var)
        search_txt.place(x=200, y=10)

        search_btn = Button(search_frame, text="Search", font=("goudy old style", 15), bg="#4caf50", fg="white",
                            cursor="hand2", command=self.search)
        search_btn.place(x=420, y=9, width=150, height=30)

        # ================================= Product Details ==============================
        p_frame = Frame(self.root, bd=3, relief=RIDGE)
        p_frame.place(x=480, y=100, width=600, height=390)

        scroll_x = Scrollbar(p_frame, orient=HORIZONTAL)
        scroll_y = Scrollbar(p_frame, orient=VERTICAL)

        self.product_table = ttk.Treeview(p_frame, columns=(
            "p_id", "Category", "Supplier", "name", "price", "quantity", "status"),
                                           xscrollcommand=scroll_x.set, yscrollcommand=scroll_y.set)
        scroll_x.pack(side=BOTTOM, fill=X)
        scroll_y.pack(side=RIGHT, fill=Y)
        scroll_x.config(command=self.product_table.xview)
        scroll_y.config(command=self.product_table.yview)

        self.product_table.heading("p_id", text="P ID")
        self.product_table.heading("Category", text="Category")
        self.product_table.heading("Supplier", text="Supplier")
        self.product_table.heading("name", text="Name")
        self.product_table.heading("price", text="Price")
        self.product_table.heading("quantity", text="Quantity")
        self.product_table.heading("status", text="Status")
        self.product_table["show"] = "headings"

        self.product_table.column("p_id", width=90)
        self.product_table.column("Category", width=100)
        self.product_table.column("Supplier", width=100)
        self.product_table.column("name", width=100)
        self.product_table.column("price", width=100)
        self.product_table.column("quantity", width=100)
        self.product_table.column("status", width=100)
        self.product_table.pack(fill=BOTH, expand=1)
        self.product_table.bind("<ButtonRelease-1>", self.get_data)

        self.show()

    def fetch_cat_sup(self):
        self.cat_list.append("Empty")
        self.sup_list.append("Empty")
        con = sqlite3.connect(database=r"ims.db")
        cur = con.cursor()
        try:
            cur.execute("select name from category")
            cat = cur.fetchall()
            if len(cat) > 0:
                del self.cat_list[:]
                self.cat_list.append("Select")
                for i in cat:
                    self.cat_list.append(i[0])

            cur.execute("select name from supplier")
            sup = cur.fetchall()
            if len(sup) > 0:
                del self.sup_list[:]
                self.sup_list.append("Select")
                for i in sup:
                    self.sup_list.append(i[0])

        except Exception as ex:
            messagebox.showerror("Error", f"Error due to : {str(ex)}", parent=self.root)

    def add(self):
        con = sqlite3.connect(database=r"ims.db")
        cur = con.cursor()
        try:
            if self.category_var.get() == "Select" or self.category_var.get() == "Empty" or self.supplier_var.get() == "Select" or self.supplier_var.get() == "Empty" or self.product_name_var.get() == "" or self.price_var.get() == "" or self.status_var.get() == "":
                messagebox.showerror("Error", "All Fields Are Required !", parent=self.root)

            else:
                cur.execute("select * from product where name=?", (self.product_name_var.get(),))
                row = cur.fetchone()
                if row is not None:
                    messagebox.showerror("Error", "Product is Already Present, Try Different One.", parent=self.root)

                else:
                    cur.execute(
                        "Insert into product (Category, Supplier, name, price, quantity, status) values(?, ?, ?, ?, ?, ?)",
                        (
                            self.category_var.get(),
                            self.supplier_var.get(),
                            self.product_name_var.get(),
                            self.price_var.get(),
                            self.quantity_var.get(),
                            self.status_var.get()
                        ))
                    con.commit()
                    messagebox.showinfo("Success", "Product Added Successfully.", parent=self.root)
                    self.show()

        except Exception as ex:
            messagebox.showerror("Error", f"Error due to : {str(ex)}", parent=self.root)

    def show(self):
        con = sqlite3.connect(database=r"ims.db")
        cur = con.cursor()
        try:
            cur.execute("select * from product")
            rows = cur.fetchall()
            self.product_table.delete(*self.product_table.get_children())
            for row in rows:
                self.product_table.insert("", END, values=row)

        except Exception as ex:
            messagebox.showerror("Error", f"Error due to : {str(ex)}", parent=self.root)

    def get_data(self, ev):
        f = self.product_table.focus()
        content = (self.product_table.item(f))
        row = content['values']
        self.p_id_var.set(row[0])
        self.category_var.set(row[1])
        self.supplier_var.set(row[2])
        self.product_name_var.set(row[3])
        self.price_var.set(row[4])
        self.quantity_var.set(row[5])
        self.status_var.set(row[6])

    def update(self):
        con = sqlite3.connect(database=r"ims.db")
        cur = con.cursor()
        try:
            if self.p_id_var.get() == "":
                messagebox.showerror("Error", "Please Select Product From List !", parent=self.root)

            elif self.product_name_var.get() == "" or self.price_var.get() == "" or self.quantity_var.get() == "":
                messagebox.showerror("Error", "All Fields Are Required !", parent=self.root)

            else:
                cur.execute("select * from product where p_id=?", (self.p_id_var.get(),))
                row = cur.fetchone()
                if row is None:
                    messagebox.showerror("Error", "Invalid Product !", parent=self.root)

                else:
                    cur.execute(
                        "update product set Category=?, Supplier=?, name=?, price=?, quantity=?, status=? where p_id=?",
                        (
                            self.category_var.get(),
                            self.supplier_var.get(),
                            self.product_name_var.get(),
                            self.price_var.get(),
                            self.quantity_var.get(),
                            self.status_var.get(),
                            self.p_id_var.get()
                        ))
                    con.commit()
                    messagebox.showinfo("Success", "Product Updated Successfully.", parent=self.root)
                    self.show()
                    # self.clear()

        except Exception as ex:
            messagebox.showerror("Error", f"Error due to : {str(ex)}", parent=self.root)

    def delete(self):
        con = sqlite3.connect(database=r"ims.db")
        cur = con.cursor()
        try:
            if self.p_id_var.get() == "":
                messagebox.showerror("Error", "Please Select Product From List !", parent=self.root)

            elif self.product_name_var.get() == "" or self.price_var.get() == "" or self.quantity_var.get() == "":
                messagebox.showerror("Error", "All Fields Are Required !", parent=self.root)

            else:
                cur.execute("select * from product where p_id=?", (self.p_id_var.get(),))
                row = cur.fetchone()
                if row is None:
                    messagebox.showerror("Error", "Invalid Product !", parent=self.root)
                else:
                    option = messagebox.askyesno("Confirm", "Do You Really Want to Delete ?", parent=self.root)
                    if option is True:
                        cur.execute("delete from product where p_id=?", (self.p_id_var.get(),))
                        con.commit()
                        messagebox.showinfo("Delete", "Product Deleted Successfully", parent=self.root)
                        self.clear()
                        self.show()

        except Exception as ex:
            messagebox.showerror("Error", f"Error due to : {str(ex)}", parent=self.root)

    def clear(self):
        self.category_var.set("Select")
        self.supplier_var.set("Select")
        self.product_name_var.set("")
        self.price_var.set("")
        self.quantity_var.set("")
        self.status_var.set("Active")
        self.p_id_var.set("")
        self.search_txt_var.set("")
        self.search_by_var.set("Search By")
        self.show()

    def search(self):
        con = sqlite3.connect(database=r"ims.db")
        cur = con.cursor()
        try:
            if self.search_by_var.get() == "Select":
                messagebox.showerror("Error", "Select Search By Option.", parent=self.root)
            elif self.search_txt_var.get() == "":
                messagebox.showerror("Error", "Search Input is Required !", parent=self.root)
            else:
                cur.execute(
                    "select * from product where " + self.search_by_var.get() + " LIKE '%" + self.search_txt_var.get() + "%'")
                rows = cur.fetchall()
                if len(rows) != 0:
                    self.product_table.delete(*self.product_table.get_children())
                    for row in rows:
                        self.product_table.insert("", END, values=row)
                else:
                    messagebox.showerror("Error", "No Record Found !", parent=self.root)

        except Exception as ex:
            messagebox.showerror("Error", f"Error due to : {str(ex)}", parent=self.root)


if __name__ == '__main__':
    root = Tk()
    obj = ProductClass(root)
    root.mainloop()
