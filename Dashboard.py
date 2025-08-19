import os
import sqlite3
import time
from tkinter import *
from tkinter import messagebox

from PIL import Image, ImageTk
from Employee import EmployeeClass
from Supplier import SupplierClass
from Category import CategoryClass
from Product import ProductClass
from Sales import SalesClass


class IMS:
    def __init__(self, root_window):
        self.root = root_window
        self.root.geometry("1350x710+0+0")
        self.root.title("Inventory Management System")
        self.root.config(bg="white")

        # ============================ Title ============================
        self.icon_title = PhotoImage(file="Images\\logo1.png")
        title = Label(self.root, text="Inventory Management System", font=("times new roman", 40, "bold"), bg="#010c48",
                      fg="white", image=self.icon_title, compound=LEFT, anchor="w", padx=20)
        title.place(x=0, y=0, relwidth=1, height=70)

        # ============================ Logout btn =======================
        btn_logout = Button(self.root, text="Logout", font=("times new roman", 15, "bold"), bg="yellow", cursor="hand2", command=self.logout)
        btn_logout.place(x=1150, y=10, height=50, width=150)

        # ============================= Clock Lbl =======================
        self.clock_lbl = Label(self.root, text="Welcome to Inventory Management System \t\t Date: DD-MM-YYYY \t\t Time : HH-MM-SS",
                               font=("times new roman", 15), bg="#4d636d", fg="white")
        self.clock_lbl.place(x=0, y=70, relwidth=1, height=30)

        # ============================= Left Menu =======================
        self.menu_logo = Image.open("Images\\menu_im.png")
        self.menu_logo = self.menu_logo.resize((200, 200))
        self.menu_logo = ImageTk.PhotoImage(self.menu_logo)

        left_menu = Frame(self.root, bd=2, relief=RIDGE, bg="white")
        left_menu.place(x=0, y=102, width=200, height=565)

        menu_logo_lbl = Label(left_menu, image=self.menu_logo)
        menu_logo_lbl.pack(side=TOP, fill=X)

        menu_lbl = Label(left_menu, text="Menu", font=("times new roman", 20), bg="#009688")
        menu_lbl.pack(side=TOP, fill=X)

        # ============================ Logout btn =======================
        self.side_arrow = PhotoImage(file="Images\\side.png")
        employee_btn = Button(left_menu, text="Employee", font=("times new roman", 20, "bold"), bg="white", cursor="hand2",
                              bd=3, image=self.side_arrow, compound=LEFT, padx=5, anchor="w", command=self.employee)
        employee_btn.pack(side=TOP, fill=X)

        supplier_btn = Button(left_menu, text="Supplier", font=("times new roman", 20, "bold"), bg="white", cursor="hand2",
                              bd=3, image=self.side_arrow, compound=LEFT, padx=5, anchor="w", command=self.supplier)
        supplier_btn.pack(side=TOP, fill=X)

        category_btn = Button(left_menu, text="Category", font=("times new roman", 20, "bold"), bg="white", cursor="hand2",
                              bd=3, image=self.side_arrow, compound=LEFT, padx=5, anchor="w", command=self.category)
        category_btn.pack(side=TOP, fill=X)

        product_btn = Button(left_menu, text="Product", font=("times new roman", 20, "bold"), bg="white", cursor="hand2",
                             bd=3, image=self.side_arrow, compound=LEFT, padx=5, anchor="w", command=self.product)
        product_btn.pack(side=TOP, fill=X)

        sales_btn = Button(left_menu, text="Sales", font=("times new roman", 20, "bold"), bg="white", cursor="hand2",
                           bd=3, image=self.side_arrow, compound=LEFT, padx=5, anchor="w", command=self.sales)
        sales_btn.pack(side=TOP, fill=X)

        exit_btn = Button(left_menu, text="Exit", font=("times new roman", 20, "bold"), bg="white", cursor="hand2",
                          bd=3, image=self.side_arrow, compound=LEFT, padx=5, anchor="w", command=exit)
        exit_btn.pack(side=TOP, fill=X)

        # ============================ Contents =========================
        self.employee_lbl = Label(self.root, text="Total Employee\n[0]", font=("goudy old style", 20, "bold"),
                                  bg="#33bbf9", fg="white", bd=5, relief=RIDGE)
        self.employee_lbl.place(x=300, y=120, height=150, width=300)

        self.supplier_lbl = Label(self.root, text="Total Supplier\n[0]", font=("goudy old style", 20, "bold"),
                                  bg="#ff5722", fg="white", bd=5, relief=RIDGE)
        self.supplier_lbl.place(x=650, y=120, height=150, width=300)

        self.category_lbl = Label(self.root, text="Total Category\n[0]", font=("goudy old style", 20, "bold"),
                                  bg="#009688", fg="white", bd=5, relief=RIDGE)
        self.category_lbl.place(x=1000, y=120, height=150, width=300)

        self.product_lbl = Label(self.root, text="Total Product\n[0]", font=("goudy old style", 20, "bold"),
                                 bg="#607d8d", fg="white", bd=5, relief=RIDGE)
        self.product_lbl.place(x=300, y=300, height=150, width=300)

        self.sales_lbl = Label(self.root, text="Total Sales\n[0]", font=("goudy old style", 20, "bold"),
                               bg="#ffc107", fg="white", bd=5, relief=RIDGE)
        self.sales_lbl.place(x=650, y=300, height=150, width=300)

        # ============================= footer Lbl =======================
        footer_lbl = Label(self.root, text="IMS - Inventory Management System\n"
                                           "For Any Technical Issue Contact : 9730122426", font=("times new roman", 12),
                           bg="#4d636d", fg="white")
        footer_lbl.pack(side=BOTTOM, fill=X)

        self.update_content()

    def employee(self):
        new_window = Toplevel(self.root)
        EmployeeClass(new_window)

    def supplier(self):
        new_window = Toplevel(self.root)
        SupplierClass(new_window)

    def category(self):
        new_window = Toplevel(self.root)
        CategoryClass(new_window)

    def product(self):
        new_window = Toplevel(self.root)
        ProductClass(new_window)

    def sales(self):
        new_window = Toplevel(self.root)
        SalesClass(new_window)

    def update_content(self):
        con = sqlite3.connect("ims.db")
        cur = con.cursor()
        try:
            cur.execute("select * from product")
            product = cur.fetchall()
            self.product_lbl.config(text=f"Total Product\n[ {str(len(product))} ]")

            cur.execute("select * from supplier")
            supplier = cur.fetchall()
            self.supplier_lbl.config(text=f"Total Supplier\n[ {str(len(supplier))} ]")

            cur.execute("select * from category")
            category = cur.fetchall()
            self.category_lbl.config(text=f"Total Category\n[ {str(len(category))} ]")

            cur.execute("select * from employee")
            employee = cur.fetchall()
            self.employee_lbl.config(text=f"Total Employee\n[ {str(len(employee))} ]")

            con.commit()
            con.close()

            bill = len(os.listdir('Bill\\'))
            self.sales_lbl.config(text=f"Total Sales\n[ {str(bill)} ]")

            curr_time = time.strftime("%I:%M:%S")
            curr_date = time.strftime("%d-%m-%Y")
            self.clock_lbl.config(text=f"Welcome to Inventory Management System \t\t Date: {curr_date} \t\t Time : {curr_time}",
                                  font=("times new roman", 15), bg="#4d636d", fg="white")
            self.clock_lbl.after(200, self.update_content)

        except Exception as error:
            messagebox.showerror("Error", f"Error Due To : {str(error)}", parent=self.root)

    def logout(self):
        self.root.destroy()
        os.system("python Login.py")


if __name__ == '__main__':
    root = Tk()
    obj = IMS(root)
    root.mainloop()
