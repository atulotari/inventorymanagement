import sqlite3
from tkinter import *
from tkinter import ttk, messagebox


class EmployeeClass:
    def __init__(self, root_window):
        self.root = root_window
        self.root.geometry("1100x500+225+150")
        self.root.title("Inventory Management System")
        self.root.config(bg="white")
        self.root.focus_force()

        # ================================= Variables =============================
        self.search_by_var = StringVar()
        self.search_txt_var = StringVar()

        self.employee_id_var = StringVar()
        self.employee_gender_var = StringVar()
        self.employee_contact_var = StringVar()
        self.employee_name_var = StringVar()
        self.employee_dob_var = StringVar()
        self.employee_doj_var = StringVar()
        self.employee_email_var = StringVar()
        self.employee_password_var = StringVar()
        self.employee_user_type_var = StringVar()
        self.employee_salary_var = StringVar()

        # ================================= Search Frame ==========================
        search_frame = LabelFrame(self.root, text="Search Employee", font=("goudy old style", 12, "bold"), bd=2,
                                  relief=RIDGE, bg="white")
        search_frame.place(x=250, y=20, width=600, height=70)

        # ================================= Options ===============================
        search_cmb = ttk.Combobox(search_frame, values=("Search By", "E-mail", "Name", "Contact"), state="readonly",
                                  justify=CENTER, font=("goudy old style", 15), textvariable=self.search_by_var)
        search_cmb.place(x=10, y=10, width=180)
        search_cmb.current(0)

        search_txt = Entry(search_frame, font=("goudy old style", 15), bg="light yellow",
                           textvariable=self.search_txt_var)
        search_txt.place(x=200, y=10)

        search_btn = Button(search_frame, text="Search", font=("goudy old style", 15), bg="#4caf50", fg="white",
                            cursor="hand2", command=self.search)
        search_btn.place(x=420, y=9, width=150, height=30)

        # =================================== Title ================================
        title = Label(self.root, text="Employee Details", font=("goudy old style", 15, "bold"), bg="#0f4d7d",
                      fg="white")
        title.place(x=50, y=100, width=1000)

        # =================================== Content ==============================
        # =================================== Row 1 ==============================
        emp_id_lbl = Label(self.root, text="Emp ID", font=("goudy old style", 15, "bold"), bg="white")
        emp_id_lbl.place(x=50, y=150)
        emp_id_txt = Entry(self.root, textvariable=self.employee_id_var, font=("goudy old style", 15, "bold"),
                           bg="light yellow")
        emp_id_txt.place(x=150, y=150, width=180)

        emp_gender_lbl = Label(self.root, text="Gender", font=("goudy old style", 15, "bold"), bg="white")
        emp_gender_lbl.place(x=350, y=150)
        emp_gender_cmb = ttk.Combobox(self.root, values=("Select", "Male", "Female", "Other"), state="readonly",
                                      justify=CENTER, font=("goudy old style", 15),
                                      textvariable=self.employee_gender_var)
        emp_gender_cmb.place(x=500, y=150, width=180)
        emp_gender_cmb.current(0)

        emp_contact_lbl = Label(self.root, text="Contact", font=("goudy old style", 15, "bold"), bg="white")
        emp_contact_lbl.place(x=750, y=150)
        emp_contact_txt = Entry(self.root, textvariable=self.employee_contact_var, font=("goudy old style", 15, "bold"),
                                bg="light yellow")
        emp_contact_txt.place(x=850, y=150, width=180)

        # =================================== Row 2 ==============================
        emp_name_lbl = Label(self.root, text="Name", font=("goudy old style", 15, "bold"), bg="white")
        emp_name_lbl.place(x=50, y=190)
        emp_name_txt = Entry(self.root, textvariable=self.employee_name_var, font=("goudy old style", 15, "bold"),
                             bg="light yellow")
        emp_name_txt.place(x=150, y=190, width=180)

        emp_dob_lbl = Label(self.root, text="D.O.B.", font=("goudy old style", 15, "bold"), bg="white")
        emp_dob_lbl.place(x=350, y=190)
        emp_dob_txt = Entry(self.root, textvariable=self.employee_dob_var, font=("goudy old style", 15, "bold"),
                            bg="light yellow")
        emp_dob_txt.place(x=500, y=190, width=180)

        emp_doj_lbl = Label(self.root, text="D.O.J.", font=("goudy old style", 15, "bold"), bg="white")
        emp_doj_lbl.place(x=750, y=190)
        emp_doj_txt = Entry(self.root, textvariable=self.employee_doj_var, font=("goudy old style", 15, "bold"),
                            bg="light yellow")
        emp_doj_txt.place(x=850, y=190, width=180)

        # =================================== Row 3 ==============================
        emp_email_lbl = Label(self.root, text="E-mail", font=("goudy old style", 15, "bold"), bg="white")
        emp_email_lbl.place(x=50, y=230)
        emp_email_txt = Entry(self.root, textvariable=self.employee_email_var, font=("goudy old style", 15, "bold"),
                              bg="light yellow")
        emp_email_txt.place(x=150, y=230, width=180)

        emp_password_lbl = Label(self.root, text="Password", font=("goudy old style", 15, "bold"), bg="white")
        emp_password_lbl.place(x=350, y=230)
        emp_password_txt = Entry(self.root, textvariable=self.employee_password_var,
                                 font=("goudy old style", 15, "bold"), bg="light yellow")
        emp_password_txt.place(x=500, y=230, width=180)

        emp_user_type_lbl = Label(self.root, text="User Type", font=("goudy old style", 15, "bold"), bg="white")
        emp_user_type_lbl.place(x=750, y=230)
        emp_user_type_cmb = ttk.Combobox(self.root, values=("Admin", "Employee"), state="readonly",
                                         justify=CENTER, font=("goudy old style", 15),
                                         textvariable=self.employee_user_type_var)
        emp_user_type_cmb.place(x=850, y=230, width=180)
        emp_user_type_cmb.current(0)

        # =================================== Row 4 ==============================
        emp_address_lbl = Label(self.root, text="Address", font=("goudy old style", 15, "bold"), bg="white")
        emp_address_lbl.place(x=50, y=270)
        self.emp_address_txt = Text(self.root, font=("goudy old style", 15, "bold"), bg="light yellow")
        self.emp_address_txt.place(x=150, y=270, width=300, height=60)

        emp_salary_lbl = Label(self.root, text="Salary", font=("goudy old style", 15, "bold"), bg="white")
        emp_salary_lbl.place(x=500, y=270)
        emp_salary_txt = Entry(self.root, textvariable=self.employee_salary_var,
                               font=("goudy old style", 15, "bold"), bg="light yellow")
        emp_salary_txt.place(x=600, y=270, width=180)

        # =================================== Buttons =============================
        add_btn = Button(self.root, text="Save", font=("goudy old style", 15, "bold"), bg="#2196f3", fg="white",
                         cursor="hand2", command=self.add)
        add_btn.place(x=500, y=305, width=110, height=28)

        update_btn = Button(self.root, text="Update", font=("goudy old style", 15, "bold"), bg="#4caf50", fg="white",
                            cursor="hand2", command=self.update)
        update_btn.place(x=620, y=305, width=110, height=28)

        delete_btn = Button(self.root, text="Delete", font=("goudy old style", 15, "bold"), bg="#f44336", fg="white",
                            cursor="hand2", command=self.delete)
        delete_btn.place(x=740, y=305, width=110, height=28)

        clear_btn = Button(self.root, text="Clear", font=("goudy old style", 15, "bold"), bg="#607d8b", fg="white",
                           cursor="hand2", command=self.clear)
        clear_btn.place(x=860, y=305, width=110, height=28)

        # ================================= Employee Details ==============================
        emp_frame = Frame(self.root, bd=3, relief=RIDGE)
        emp_frame.place(x=0, y=350, relwidth=1, height=150)

        scroll_x = Scrollbar(emp_frame, orient=HORIZONTAL)
        scroll_y = Scrollbar(emp_frame, orient=VERTICAL)

        self.employee_table = ttk.Treeview(emp_frame, columns=(
            "e_id", "name", "email", "gender", "contact", "dob", "doj", "pass", "u_type", "address", "salary"),
                                           xscrollcommand=scroll_x.set, yscrollcommand=scroll_y.set)
        scroll_x.pack(side=BOTTOM, fill=X)
        scroll_y.pack(side=RIGHT, fill=Y)
        scroll_x.config(command=self.employee_table.xview)
        scroll_y.config(command=self.employee_table.yview)

        self.employee_table.heading("e_id", text="EMP ID")
        self.employee_table.heading("name", text="Name")
        self.employee_table.heading("email", text="E-mail")
        self.employee_table.heading("gender", text="Gender")
        self.employee_table.heading("contact", text="Contact")
        self.employee_table.heading("dob", text="D.O.B.")
        self.employee_table.heading("doj", text="D.O.J.")
        self.employee_table.heading("pass", text="Password")
        self.employee_table.heading("u_type", text="User Type")
        self.employee_table.heading("address", text="Address")
        self.employee_table.heading("salary", text="Salary")
        self.employee_table["show"] = "headings"

        self.employee_table.column("e_id", width=90)
        self.employee_table.column("name", width=100)
        self.employee_table.column("email", width=100)
        self.employee_table.column("gender", width=100)
        self.employee_table.column("contact", width=100)
        self.employee_table.column("dob", width=100)
        self.employee_table.column("doj", width=100)
        self.employee_table.column("pass", width=100)
        self.employee_table.column("u_type", width=100)
        self.employee_table.column("address", width=100)
        self.employee_table.column("salary", width=100)
        self.employee_table.pack(fill=BOTH, expand=1)
        self.employee_table.bind("<ButtonRelease-1>", self.get_data)

        self.show()

    def add(self):
        con = sqlite3.connect(database=r"ims.db")
        cur = con.cursor()
        try:
            cur.execute("select u_type from employee")
            users_data = cur.fetchall()
            all_users = []
            all_users.clear()
            for user in users_data:
                all_users.append(user[0])
            admin = all_users.count("Admin")

            if self.employee_user_type_var.get() == "Admin" and admin > 3:
                self.employee_salary_var.set("")
                self.employee_user_type_var.set("Employee")
                messagebox.showerror("Error", "Only 4 Admins are Valid !", parent=self.root)

            elif self.employee_id_var.get() == "":
                messagebox.showerror("Error", "Employee ID Must Be Required !", parent=self.root)

            elif self.employee_name_var.get() == "" or self.employee_email_var.get() == "" or self.employee_gender_var.get() == "" or self.employee_contact_var.get() == "" or self.employee_dob_var.get() == "" or self.employee_doj_var.get() == "" or self.employee_password_var.get() == "" or self.employee_user_type_var.get() == "" or self.emp_address_txt.get('1.0', END) == "" or self.employee_salary_var.get() == "":
                messagebox.showerror("Error", "All Fields Are Required !", parent=self.root)

            else:
                cur.execute("select * from employee where e_id=?", (self.employee_id_var.get(),))
                row = cur.fetchone()
                if row is not None:
                    messagebox.showerror("Error", "This Employee ID is Already Present, Try Different One.", parent=self.root)
                else:
                    cur.execute("Insert into employee (e_id, name, email, gender, contact, dob, doj, pass, u_type, address, salary) values(?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)", (
                            self.employee_id_var.get(),
                            self.employee_name_var.get(),
                            self.employee_email_var.get(),
                            self.employee_gender_var.get(),
                            self.employee_contact_var.get(),
                            self.employee_dob_var.get(),
                            self.employee_doj_var.get(),
                            self.employee_password_var.get(),
                            self.employee_user_type_var.get(),
                            self.emp_address_txt.get('1.0', END),
                            self.employee_salary_var.get()
                        ))
                    con.commit()
                    messagebox.showinfo("Success", "Employee Added Successfully.", parent=self.root)
                    self.show()

        except Exception as ex:
            messagebox.showerror("Error", f"Error due to : {str(ex)}", parent=self.root)

    def show(self):
        con = sqlite3.connect(database=r"ims.db")
        cur = con.cursor()
        try:
            cur.execute("select * from employee")
            rows = cur.fetchall()
            self.employee_table.delete(*self.employee_table.get_children())
            for row in rows:
                self.employee_table.insert("", END, values=row)

        except Exception as ex:
            messagebox.showerror("Error", f"Error due to : {str(ex)}", parent=self.root)

    def get_data(self, ev):
        f = self.employee_table.focus()
        content = (self.employee_table.item(f))
        row = content['values']
        self.employee_id_var.set(row[0]),
        self.employee_name_var.set(row[1]),
        self.employee_email_var.set(row[2]),
        self.employee_gender_var.set(row[3]),
        self.employee_contact_var.set(row[4]),
        self.employee_dob_var.set(row[5]),
        self.employee_doj_var.set(row[6]),
        self.employee_password_var.set(row[7]),
        self.employee_user_type_var.set(row[8]),
        self.emp_address_txt.delete('1.0', END),
        self.emp_address_txt.insert(END, row[9]),
        self.employee_salary_var.set(row[10])

    def update(self):
        con = sqlite3.connect(database=r"ims.db")
        cur = con.cursor()
        try:
            cur.execute("select u_type from employee")
            users_data = cur.fetchall()
            all_users = []
            all_users.clear()
            for user in users_data:
                all_users.append(user[0])
            admin = all_users.count("Admin")

            if self.employee_user_type_var.get() == "Admin" and admin > 3:
                self.employee_salary_var.set("")
                self.employee_user_type_var.set("Employee")
                messagebox.showerror("Error", "Only 4 Admins are Valid !", parent=self.root)

            elif self.employee_id_var.get() == "":
                messagebox.showerror("Error", "Employee ID Must Be Required !", parent=self.root)

            elif self.employee_name_var.get() == "" or self.employee_email_var.get() == "" or self.employee_gender_var.get() == "" or self.employee_contact_var.get() == "" or self.employee_dob_var.get() == "" or self.employee_doj_var.get() == "" or self.employee_password_var.get() == "" or self.employee_user_type_var.get() == "" or self.emp_address_txt.get('1.0', END) == "" or self.employee_salary_var.get() == "":
                messagebox.showerror("Error", "All Fields Are Required !", parent=self.root)

            else:
                cur.execute("select * from employee where e_id=?", (self.employee_id_var.get(),))
                row = cur.fetchone()
                if row is None:
                    messagebox.showerror("Error", "Invalid Employee ID !", parent=self.root)

                else:
                    cur.execute("update employee set name=?, email=?, gender=?, contact=?, dob=?, doj=?, pass=?, u_type=?, address=?, salary=? where e_id=?", (
                            self.employee_name_var.get(),
                            self.employee_email_var.get(),
                            self.employee_gender_var.get(),
                            self.employee_contact_var.get(),
                            self.employee_dob_var.get(),
                            self.employee_doj_var.get(),
                            self.employee_password_var.get(),
                            self.employee_user_type_var.get(),
                            self.emp_address_txt.get('1.0', END),
                            self.employee_salary_var.get(),
                            self.employee_id_var.get(),
                    ))
                    con.commit()
                    messagebox.showinfo("Success", "Employee Updated Successfully.", parent=self.root)
                    self.clear()

        except Exception as ex:
            messagebox.showerror("Error", f"Error due to : {str(ex)}", parent=self.root)
            
    def delete(self):
        con = sqlite3.connect(database=r"ims.db")
        cur = con.cursor()
        try:
            if self.employee_id_var.get() == "":
                messagebox.showerror("Error", "Employee ID Must Be Required !", parent=self.root)

            elif self.employee_name_var.get() == "" or self.employee_email_var.get() == "" or self.employee_gender_var.get() == "" or self.employee_contact_var.get() == "" or self.employee_dob_var.get() == "" or self.employee_doj_var.get() == "" or self.employee_password_var.get() == "" or self.employee_user_type_var.get() == "" or self.emp_address_txt.get(
                    '1.0', END) == "" or self.employee_salary_var.get() == "":
                messagebox.showerror("Error", "All Fields Are Required !", parent=self.root)

            else:
                cur.execute("select * from employee where e_id=?", (self.employee_id_var.get(),))
                row = cur.fetchone()
                if row is None:
                    messagebox.showerror("Error", "Invalid Employee ID !", parent=self.root)
                else:
                    option = messagebox.askyesno("Confirm", "Do You Really Want to Delete ?", parent=self.root)
                    if option is True:
                        cur.execute("delete from employee where e_id=?", (self.employee_id_var.get(),))
                        con.commit()
                        messagebox.showinfo("Delete", "Employee Deleted Successfully", parent=self.root)
                        self.clear()
                        self.show()

        except Exception as ex:
            messagebox.showerror("Error", f"Error due to : {str(ex)}", parent=self.root)

    def clear(self):
        self.employee_id_var.set(""),
        self.employee_name_var.set(""),
        self.employee_email_var.set(""),
        self.employee_gender_var.set("Select"),
        self.employee_contact_var.set(""),
        self.employee_dob_var.set(""),
        self.employee_doj_var.set(""),
        self.employee_password_var.set(""),
        self.employee_user_type_var.set("Admin"),
        self.emp_address_txt.delete('1.0', END),
        self.employee_salary_var.set("")
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
                cur.execute("select * from employee where "+self.search_by_var.get()+" LIKE '%"+self.search_txt_var.get()+"%'")
                rows = cur.fetchall()
                if len(rows) != 0:
                    self.employee_table.delete(*self.employee_table.get_children())
                    for row in rows:
                        self.employee_table.insert("", END, values=row)
                else:
                    messagebox.showerror("Error", "No Record Found !", parent=self.root)

        except Exception as ex:
            messagebox.showerror("Error", f"Error due to : {str(ex)}", parent=self.root)


if __name__ == '__main__':
    root = Tk()
    obj = EmployeeClass(root)
    root.mainloop()
