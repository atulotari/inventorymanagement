import sqlite3
import time
from tkinter import *
from tkinter import ttk
from tkinter import messagebox
import os
import tempfile


class Billing:
    def __init__(self, root_window):
        self.root = root_window
        self.root.geometry("1350x710+0+0")
        self.root.title("Inventory Management System")
        self.root.config(bg="white")

        self.cart_list = []
        self.chk_print = 0

        # ============================ Title ============================
        self.icon_title = PhotoImage(file="Images\\logo1.png")
        title = Label(self.root, text="Inventory Management System", font=("times new roman", 40, "bold"), bg="#010c48",
                      fg="white", image=self.icon_title, compound=LEFT, anchor="w", padx=20)
        title.place(x=0, y=0, relwidth=1, height=70)

        # ============================ Logout btn =======================
        btn_logout = Button(self.root, text="Logout", font=("times new roman", 15, "bold"), bg="yellow", cursor="hand2", command=self.logout)
        btn_logout.place(x=1150, y=10, height=50, width=150)

        # ============================= Clock Lbl =======================
        self.clock_lbl = Label(self.root,
                               text="Welcome to Inventory Management System \t\t Date: DD-MM-YYYY \t\t Time : HH-MM-SS",
                               font=("times new roman", 15), bg="#4d636d", fg="white")
        self.clock_lbl.place(x=0, y=70, relwidth=1, height=30)

        # ============================= Product Frame =======================
        product_frame_1 = Frame(self.root, bd=4, relief=RIDGE, bg="white")
        product_frame_1.place(x=6, y=110, width=410, height=550)

        product_title = Label(product_frame_1, text="All Products", font=("goudy old style", 20, "bold"), bg="#262626",
                              fg="white")
        product_title.pack(side=TOP, fill=X)

        # ============================= Product Frame =======================
        self.search_var = StringVar()

        product_frame_2 = Frame(product_frame_1, bd=2, relief=RIDGE, bg="white")
        product_frame_2.place(x=2, y=42, width=398, height=90)

        search_title_lbl = Label(product_frame_2, text="Search Product | By Name", font=("times new roman", 15, "bold"),
                                 bg="white", fg="green")
        search_title_lbl.place(x=2, y=5)

        search_p_name_lbl = Label(product_frame_2, text="Product Name", font=("times new roman", 15, "bold"),
                                  bg="white")
        search_p_name_lbl.place(x=2, y=45)
        search_p_name_txt = Entry(product_frame_2, textvariable=self.search_var, font=("times new roman", 15),
                                  bg="light yellow")
        search_p_name_txt.place(x=130, y=47, width=150, height=22)

        search_btn = Button(product_frame_2, text="Search", font=("goudy old style", 15, "bold"), bg="#2196f3",
                            fg="white", cursor="hand2", command=self.search)
        search_btn.place(x=285, y=45, width=100, height=25)

        show_all_btn = Button(product_frame_2, text="Show All", font=("goudy old style", 15, "bold"), bg="#083531",
                              fg="white", cursor="hand2", command=self.show)
        show_all_btn.place(x=285, y=10, width=100, height=25)

        # ================================= Cart Details ==============================
        product_frame_3 = Frame(product_frame_1, bd=3, relief=RIDGE)
        product_frame_3.place(x=2, y=140, width=398, height=375)

        scroll_x = Scrollbar(product_frame_3, orient=HORIZONTAL)
        scroll_y = Scrollbar(product_frame_3, orient=VERTICAL)

        self.product_table = ttk.Treeview(product_frame_3, columns=("p_id", "name", "price", "quantity", "status"),
                                          xscrollcommand=scroll_x.set, yscrollcommand=scroll_y.set)
        scroll_x.pack(side=BOTTOM, fill=X)
        scroll_y.pack(side=RIGHT, fill=Y)
        scroll_x.config(command=self.product_table.xview)
        scroll_y.config(command=self.product_table.yview)

        self.product_table.heading("p_id", text="P ID")
        self.product_table.heading("name", text="Name")
        self.product_table.heading("price", text="Price")
        self.product_table.heading("quantity", text="Qty")
        self.product_table.heading("status", text="Status")
        self.product_table["show"] = "headings"

        self.product_table.column("p_id", width=40)
        self.product_table.column("name", width=100)
        self.product_table.column("price", width=100)
        self.product_table.column("quantity", width=40)
        self.product_table.column("status", width=90)
        self.product_table.pack(fill=BOTH, expand=1)
        self.product_table.bind("<ButtonRelease-1>", self.get_data)

        note_lbl = Label(product_frame_1, text="Note: 'Enter 0 Quantity to Remove Product From Cart'",
                         font=("goudy old style", 12, "bold"), bg="white", fg="red", anchor="w")
        note_lbl.pack(side=BOTTOM, fill=X)

        # ================================= Customer Frame ==============================
        self.customer_name_var = StringVar()
        self.contact_var = StringVar()

        customer_frame = Frame(self.root, bd=4, relief=RIDGE, bg="white")
        customer_frame.place(x=420, y=110, width=530, height=70)

        customer_title = Label(customer_frame, text="Customer Details", font=("goudy old style", 15, "bold"),
                               bg="light gray")
        customer_title.pack(side=TOP, fill=X)

        customer_name_lbl = Label(customer_frame, text="Name", font=("times new roman", 15), bg="white")
        customer_name_lbl.place(x=5, y=33)
        customer_name_txt = Entry(customer_frame, textvariable=self.customer_name_var, font=("times new roman", 13),
                                  bg="light yellow")
        customer_name_txt.place(x=80, y=35, width=180)

        customer_contact_lbl = Label(customer_frame, text="Contact No.", font=("times new roman", 15), bg="white")
        customer_contact_lbl.place(x=270, y=33)
        customer_contact_txt = Entry(customer_frame, textvariable=self.contact_var, font=("times new roman", 13),
                                     bg="light yellow")
        customer_contact_txt.place(x=380, y=35, width=140)

        # ====================================== Calculator Frame =================================
        calculator_cart_frame = Frame(self.root, bd=2, relief=RIDGE, bg="white")
        calculator_cart_frame.place(x=420, y=190, width=530, height=360)

        # ================================= Calculator Frame ==============================
        self.cal_input_var = StringVar()

        calculator_frame = Frame(calculator_cart_frame, bd=9, relief=RIDGE, bg="white")
        calculator_frame.place(x=5, y=10, width=268, height=340)

        cal_input_txt = Entry(calculator_frame, textvariable=self.cal_input_var, font=("arial", 15, "bold"), width=21,
                              bd=10, relief=GROOVE, state="readonly", justify=RIGHT)
        cal_input_txt.grid(row=0, columnspan=4)

        btn_7 = Button(calculator_frame, text="7", font=("arial", 15, "bold"), bd=5, width=4, pady=11, cursor="hand2",
                       command=lambda: self.get_input(7))
        btn_7.grid(row=1, column=0)
        btn_8 = Button(calculator_frame, text="8", font=("arial", 15, "bold"), bd=5, width=4, pady=11, cursor="hand2",
                       command=lambda: self.get_input(8))
        btn_8.grid(row=1, column=1)
        btn_9 = Button(calculator_frame, text="9", font=("arial", 15, "bold"), bd=5, width=4, pady=11, cursor="hand2",
                       command=lambda: self.get_input(9))
        btn_9.grid(row=1, column=2)
        btn_c = Button(calculator_frame, text="C", font=("arial", 15, "bold"), bd=5, width=4, pady=11, cursor="hand2",
                       fg="red", command=self.clear_cal)
        btn_c.grid(row=1, column=3)

        btn_4 = Button(calculator_frame, text="4", font=("arial", 15, "bold"), bd=5, width=4, pady=11, cursor="hand2",
                       command=lambda: self.get_input(4))
        btn_4.grid(row=2, column=0)
        btn_5 = Button(calculator_frame, text="5", font=("arial", 15, "bold"), bd=5, width=4, pady=11, cursor="hand2",
                       command=lambda: self.get_input(5))
        btn_5.grid(row=2, column=1)
        btn_6 = Button(calculator_frame, text="6", font=("arial", 15, "bold"), bd=5, width=4, pady=11, cursor="hand2",
                       command=lambda: self.get_input(6))
        btn_6.grid(row=2, column=2)
        btn_plus = Button(calculator_frame, text="+", font=("arial", 15, "bold"), bd=5, width=4, pady=11,
                          cursor="hand2", command=lambda: self.get_input('+'))
        btn_plus.grid(row=2, column=3)

        btn_1 = Button(calculator_frame, text="1", font=("arial", 15, "bold"), bd=5, width=4, pady=11, cursor="hand2",
                       command=lambda: self.get_input(1))
        btn_1.grid(row=3, column=0)
        btn_2 = Button(calculator_frame, text="2", font=("arial", 15, "bold"), bd=5, width=4, pady=11, cursor="hand2",
                       command=lambda: self.get_input(2))
        btn_2.grid(row=3, column=1)
        btn_3 = Button(calculator_frame, text="3", font=("arial", 15, "bold"), bd=5, width=4, pady=11, cursor="hand2",
                       command=lambda: self.get_input(3))
        btn_3.grid(row=3, column=2)
        btn_minus = Button(calculator_frame, text="-", font=("arial", 15, "bold"), bd=5, width=4, pady=11,
                           cursor="hand2", command=lambda: self.get_input('-'))
        btn_minus.grid(row=3, column=3)

        btn_0 = Button(calculator_frame, text="0", font=("arial", 15, "bold"), bd=5, width=4, pady=12, cursor="hand2",
                       command=lambda: self.get_input(0))
        btn_0.grid(row=4, column=0)
        btn_equal = Button(calculator_frame, text="=", font=("arial", 15, "bold"), bd=5, width=4, pady=12,
                           cursor="hand2", command=self.perform_cal)
        btn_equal.grid(row=4, column=1)
        btn_div = Button(calculator_frame, text="/", font=("arial", 15, "bold"), bd=5, width=4, pady=12, cursor="hand2",
                         command=lambda: self.get_input('/'))
        btn_div.grid(row=4, column=2)
        btn_mul = Button(calculator_frame, text="*", font=("arial", 15, "bold"), bd=5, width=4, pady=12, cursor="hand2",
                         command=lambda: self.get_input('*'))
        btn_mul.grid(row=4, column=3)

        # ================================= Cart Frame ==============================
        cart_frame = Frame(calculator_cart_frame, bd=3, relief=RIDGE)
        cart_frame.place(x=280, y=8, width=245, height=342)

        self.cart_title = Label(cart_frame, text="Cart \t Total Product: [0]", font=("goudy old style", 15, "bold"),
                                bg="light gray")
        self.cart_title.pack(side=TOP, fill=X)

        scroll_x = Scrollbar(cart_frame, orient=HORIZONTAL)
        scroll_y = Scrollbar(cart_frame, orient=VERTICAL)

        self.cart_table = ttk.Treeview(cart_frame, columns=("p_id", "name", "price", "quantity"),
                                       xscrollcommand=scroll_x.set, yscrollcommand=scroll_y.set)
        scroll_x.pack(side=BOTTOM, fill=X)
        scroll_y.pack(side=RIGHT, fill=Y)
        scroll_x.config(command=self.cart_table.xview)
        scroll_y.config(command=self.cart_table.yview)

        self.cart_table.heading("p_id", text="P ID")
        self.cart_table.heading("name", text="Name")
        self.cart_table.heading("price", text="Price")
        self.cart_table.heading("quantity", text="Qty")
        self.cart_table["show"] = "headings"

        self.cart_table.column("p_id", width=40)
        self.cart_table.column("name", width=90)
        self.cart_table.column("price", width=90)
        self.cart_table.column("quantity", width=40)
        self.cart_table.pack(fill=BOTH, expand=1)
        self.cart_table.bind("<ButtonRelease-1>", self.get_data_cart)

        # ================================= Add Cart Widget Frames ==============================
        self.product_id = StringVar()
        self.product_name = StringVar()
        self.product_price = StringVar()
        self.product_quantity = StringVar()
        self.product_stock = StringVar()
        self.product_status = StringVar()

        add_cart_widgets_frame = Frame(self.root, bd=2, relief=RIDGE, bg="white")
        add_cart_widgets_frame.place(x=420, y=550, width=530, height=110)

        product_name_lbl = Label(add_cart_widgets_frame, text="Product Name", font=("times new roman", 15), bg="white")
        product_name_lbl.place(x=15, y=5)
        product_name_txt = Entry(add_cart_widgets_frame, textvariable=self.product_name, font=("times new roman", 15),
                                 bg="light yellow", state="readonly")
        product_name_txt.place(x=15, y=35, width=190, height=22)

        product_price_lbl = Label(add_cart_widgets_frame, text="Price Per Qty", font=("times new roman", 15),
                                  bg="white")
        product_price_lbl.place(x=220, y=5)
        product_price_txt = Entry(add_cart_widgets_frame, textvariable=self.product_price, font=("times new roman", 15),
                                  bg="light yellow", state="readonly")
        product_price_txt.place(x=220, y=35, width=150, height=22)

        product_qty_lbl = Label(add_cart_widgets_frame, text="Quantity", font=("times new roman", 15), bg="white")
        product_qty_lbl.place(x=390, y=5)
        product_qty_txt = Entry(add_cart_widgets_frame, textvariable=self.product_quantity,
                                font=("times new roman", 15), bg="light yellow")
        product_qty_txt.place(x=390, y=35, width=120, height=22)

        self.in_stock_lbl = Label(add_cart_widgets_frame, text="In Stock", font=("times new roman", 15), bg="white")
        self.in_stock_lbl.place(x=15, y=70)

        clear_cart_btn = Button(add_cart_widgets_frame, text="Clear", font=("times new roman", 15, "bold"),
                                bg="light gray", cursor="hand2", command=self.clear_cart)
        clear_cart_btn.place(x=180, y=70, width=150, height=30)

        add_cart_btn = Button(add_cart_widgets_frame, text="Add | Update Cart", font=("times new roman", 15, "bold"),
                              bg="orange", cursor="hand2", command=self.add_update_cart)
        add_cart_btn.place(x=340, y=70, width=180, height=30)

        # ================================= Billing Area ==============================
        bill_frame = Frame(self.root, bd=2, relief=RIDGE, bg="white")
        bill_frame.place(x=953, y=110, width=390, height=410)

        bill_title = Label(bill_frame, text="Customer Bill Area", font=("goudy old style", 20, "bold"), bg="#f44336",
                           fg="white")
        bill_title.pack(side=TOP, fill=X)

        scroll_y = Scrollbar(bill_frame, orient=VERTICAL)
        scroll_y.pack(side=RIGHT, fill=Y)
        self.bill_area_txt = Text(bill_frame, yscrollcommand=scroll_y.set)
        self.bill_area_txt.pack(fill=BOTH, expand=1)
        scroll_y.config(command=self.bill_area_txt.yview)

        # ================================= Billing Buttons ==============================
        bill_menu_frame = Frame(self.root, bd=2, relief=RIDGE, bg="white")
        bill_menu_frame.place(x=953, y=520, width=390, height=140)

        self.amt_lbl = Label(bill_menu_frame, text="Bill Amount\n[0]", font=("goudy old style", 15, "bold"),
                             bg="#3f51b5", fg="white")
        self.amt_lbl.place(x=2, y=5, width=122, height=70)

        self.discount_lbl = Label(bill_menu_frame, text="Discount\n[5%]", font=("goudy old style", 15, "bold"),
                                  bg="#8bc34a", fg="white")
        self.discount_lbl.place(x=130, y=5, width=128, height=70)

        self.net_pay_lbl = Label(bill_menu_frame, text="Net Pay\n[0]", font=("goudy old style", 15, "bold"),
                                 bg="#607d8b", fg="white")
        self.net_pay_lbl.place(x=264, y=5, width=120, height=70)

        print_btn = Button(bill_menu_frame, text="Print", font=("goudy old style", 15, "bold"), bg="light green",
                           fg="white", cursor="hand2", command=self.print_bill)
        print_btn.place(x=2, y=80, width=122, height=50)

        clear_all_btn = Button(bill_menu_frame, text="Clear All", font=("goudy old style", 15, "bold"), bg="gray",
                               fg="white", cursor="hand2", command=self.clear_all)
        clear_all_btn.place(x=130, y=80, width=128, height=50)

        generate_btn_btn = Button(bill_menu_frame, text="Generate Bill", font=("goudy old style", 15, "bold"),
                                  bg="#009688", fg="white", cursor="hand2", command=self.generate_bill)
        generate_btn_btn.place(x=264, y=80, width=120, height=50)

        # ============================= footer Lbl =======================
        footer_lbl = Label(self.root, text="IMS - Inventory Management System | Developed By Atul\n"
                                           "For Any Technical Issue Contact : 9730122426", font=("times new roman", 12),
                           bg="#4d636d", fg="white")
        footer_lbl.pack(side=BOTTOM, fill=X)

        self.show()
        self.update_date_time()

    def get_input(self, num):
        x_num = self.cal_input_var.get() + str(num)
        self.cal_input_var.set(x_num)

    def clear_cal(self):
        self.cal_input_var.set("")

    def perform_cal(self):
        result = self.cal_input_var.get()
        self.cal_input_var.set(eval(result))

    def show(self):
        con = sqlite3.connect(database=r"ims.db")
        cur = con.cursor()
        try:
            cur.execute("select p_id, name, price, quantity, status from product where status='Active'")
            rows = cur.fetchall()
            self.product_table.delete(*self.product_table.get_children())
            for row in rows:
                self.product_table.insert("", END, values=row)

        except Exception as ex:
            messagebox.showerror("Error", f"Error due to : {str(ex)}", parent=self.root)

    def search(self):
        con = sqlite3.connect(database=r"ims.db")
        cur = con.cursor()
        try:
            if self.search_var.get() == "":
                messagebox.showerror("Error", "Search Input is Required !", parent=self.root)
            else:
                cur.execute(
                    "select p_id, name, price, quantity, status from product where name LIKE '%" + self.search_var.get() + "%' and status='Active'")
                rows = cur.fetchall()
                if len(rows) != 0:
                    self.product_table.delete(*self.product_table.get_children())
                    for row in rows:
                        self.product_table.insert("", END, values=row)
                else:
                    messagebox.showerror("Error", "No Record Found !", parent=self.root)

        except Exception as ex:
            messagebox.showerror("Error", f"Error due to : {str(ex)}", parent=self.root)

    def get_data(self, ev):
        f = self.product_table.focus()
        content = (self.product_table.item(f))
        row = content['values']
        self.product_id.set(row[0])
        self.product_name.set(row[1])
        self.product_price.set(row[2])
        self.in_stock_lbl.config(text=f"In Stock [{str(row[3])}]")
        self.product_stock.set(row[3])
        self.product_quantity.set("1")

    def get_data_cart(self, ev):
        f = self.cart_table.focus()
        content = (self.cart_table.item(f))
        row = content['values']
        self.product_id.set(row[0])
        self.product_name.set(row[1])
        self.product_price.set(row[2])
        self.product_quantity.set(row[3])
        self.in_stock_lbl.config(text=f"In Stock [{str(row[4])}]")
        self.product_stock.set(row[4])

    def add_update_cart(self):
        if self.product_id.get() == "":
            messagebox.showerror("Error", "Please Select Product From The List !", parent=self.root)

        elif self.product_quantity.get() == "":
            messagebox.showerror("Error", "Quantity is Required !", parent=self.root)

        elif int(self.product_quantity.get()) > int(self.product_stock.get()):
            messagebox.showerror("Error", "Invalid Quantity !", parent=self.root)

        else:
            price_calculate = self.product_price.get()
            cart_data = [self.product_id.get(), self.product_name.get(), price_calculate, self.product_quantity.get(), self.product_stock.get()]

            # ====================================== Update Cart ======================================
            present = 'no'
            index_product = 0
            for row in self.cart_list:
                if self.product_id.get() == row[0]:
                    present = 'yes'
                    break
                index_product += 1
            if present == 'yes':
                op = messagebox.askyesno("Confirm", "Product is Already Present\nDo you want to Update | Remove it from the cart list ?", parent=self.root)
                if op is True:
                    if self.product_quantity.get() == "0":
                        self.cart_list.pop(index_product)
                    else:
                        self.cart_list[index_product][3] = self.product_quantity.get()
            else:
                self.cart_list.append(cart_data)
            self.show_cart()
            self.bill_updates()

    def bill_updates(self):
        self.bill_amt = 0
        for row in self.cart_list:
            self.bill_amt = self.bill_amt + (float(row[2]) * int(row[3]))

        self.discount = (self.bill_amt * 5) / 100
        self.net_pay = self.bill_amt - self.discount

        self.amt_lbl.config(text=f"Bill Amount\n{str(self.bill_amt)}")
        self.net_pay_lbl.config(text=f"Net Pay\n{str(self.net_pay)}")
        self.cart_title.config(text=f"Cart \t Total Product: [{str(len(self.cart_list))}]")

    def show_cart(self):
        try:
            self.cart_table.delete(*self.cart_table.get_children())
            for row in self.cart_list:
                self.cart_table.insert("", END, values=row)

        except Exception as ex:
            messagebox.showerror("Error", f"Error due to : {str(ex)}", parent=self.root)

    def generate_bill(self):
        if self.customer_name_var.get() == "" or self.contact_var.get() == "":
            messagebox.showerror("Error", "Customer Details are Required", parent=self.root)

        elif len(self.cart_list) == 0:
            messagebox.showerror("Error", "Please Add Product to The Cart", parent=self.root)

        else:
            # ====================================== Bill Top ==========================================
            self.bill_top()

            # ====================================== Bill Middle========================================
            self.bill_middle()
            # ====================================== Bill Bottom========================================
            self.bill_bottom()

            f = open(f"Bill\\{self.invoice}.txt", "w")
            f.write(self.bill_area_txt.get("1.0", END))
            f.close()
            messagebox.showinfo("Saved", "Bill Has Been Generated / Saved in Backend", parent=self.root)
            self.chk_print = 1

    def bill_top(self):
        self.invoice = int(time.strftime("%H%M%S")) + int(time.strftime("%d%m%Y"))
        bill_top_temp = f"""
\t\t Yuva Net Cafe - Inventory
     Phone No. 9730122426, Borgaon-415413
{str("="*45)}
 Customer Name: {self.customer_name_var.get()}
 Phone No: {self.contact_var.get()}
 Bill No.: {str(self.invoice)}\t\t\tDate: {str(time.strftime("%d/%m/%Y"))}
{str("="*45)}
 Product Name\t\t\tQty\tPrice
{str("="*45)}
        """
        self.bill_area_txt.delete("1.0", END)
        self.bill_area_txt.insert("1.0", bill_top_temp)

    def bill_middle(self):
        con = sqlite3.connect("ims.db")
        cur = con.cursor()
        try:
            for row in self.cart_list:
                p_id = row[0]
                name = row[1]
                qty = int(row[4]) - int(row[3])

                if int(row[3]) == int(row[4]):
                    status = "Inactive"

                if int(row[3]) != int(row[4]):
                    status = "Active"

                price = float(row[2]) * int(row[3])
                self.bill_area_txt.insert(END, f"\n {name}\t\t\t{row[3]}\tRs. {str(price)}")
                cur.execute("update product set quantity=?, status=? where p_id=?", (qty, status, p_id))
                con.commit()
            con.close()
            self.show()
        except Exception as error:
            messagebox.showerror("Error", f"Error Due To: {error}", parent=self.root)

    def bill_bottom(self):
        bill_bottom_temp = f"""\n
{str("="*45)}\n
 Bill Amount\t\t\t\tRs. {self.bill_amt}
 Discount\t\t\t\tRs. {self.discount}
 Net Pay\t\t\t\tRs. {self.net_pay}\n
{str("="*45)}\n
        """
        self.bill_area_txt.insert(END, bill_bottom_temp)
    
    def clear_cart(self):
        self.product_id.set("")
        self.product_name.set("")
        self.product_price.set("")
        self.product_quantity.set("")
        self.in_stock_lbl.config(text=f"In Stock")
        self.product_stock.set("")

    def clear_all(self):
        del self.cart_list[:]
        self.customer_name_var.set("")
        self.contact_var.set("")
        self.bill_area_txt.delete("1.0", END)
        self.cart_title.config(text="Cart \t Total Product: [0]")
        self.search_var.set("")
        self.clear_cart()
        self.show()
        self.show_cart()
        self.chk_print = 0

    def update_date_time(self):
        curr_time = time.strftime("%I:%M:%S")
        curr_date = time.strftime("%d-%m-%Y")
        self.clock_lbl.config(text=f"Welcome to Inventory Management System \t\t Date: {curr_date} \t\t Time : {curr_time}",
                              font=("times new roman", 15), bg="#4d636d", fg="white")
        self.clock_lbl.after(200, self.update_date_time)

    def print_bill(self):
        if self.chk_print == 1:
            messagebox.showinfo("Print", "Please Wait While Printing", parent=self.root)
            new_file = tempfile.mktemp(".txt")
            open(new_file, "w").write(self.bill_area_txt.get("1.0", END))
            os.startfile(new_file, "print")
        else:
            messagebox.showerror("Print", "Please Generate Bill to Print Receipt", parent=self.root)

    def logout(self):
        self.root.destroy()
        os.system("python Login.py")


if __name__ == '__main__':
    root = Tk()
    obj = Billing(root)
    root.mainloop()
